"""Serviço de crawler com Playwright, BFS e pool de workers."""

from __future__ import annotations

import asyncio
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

from playwright.async_api import Browser, async_playwright

from lgpd_auditor.checkpoint.manager import CheckpointManager, UrlStatus
from lgpd_auditor.config.loader import AuditorConfig
from lgpd_auditor.crawler.robots import RobotsChecker
from lgpd_auditor.crawler.url_utils import (
    calcular_hash_conteudo,
    extrair_links,
    normalize_url,
    pertence_ao_dominio,
)
from lgpd_auditor.crawler.visited_routes import VisitedRoute, VisitedRoutesLog
from lgpd_auditor.evidence.store import EvidenceStore


@dataclass
class CrawlResult:
    paginas_visitadas: int = 0
    paginas_com_erro: int = 0
    paginas_bloqueadas: int = 0
    paginas_ignoradas: int = 0
    urls_descobertas: int = 0
    rotas_registradas: int = 0
    erros: list[str] = field(default_factory=list)


class CrawlerService:
    """Crawler BFS com workers concorrentes, checkpoints e log de rotas."""

    def __init__(
        self,
        auditor_config: AuditorConfig,
        project_root: Path,
    ) -> None:
        self._config = auditor_config
        self._project_root = project_root
        self._dominio = auditor_config.audit.dominio_permitido
        self._url_base = str(auditor_config.audit.url_base)

        checkpoints_dir = auditor_config.resolve_path(
            auditor_config.paths.checkpoints, project_root
        )
        visited_routes_path = auditor_config.resolve_path(
            auditor_config.paths.visited_routes, project_root
        )
        evidence_dir = auditor_config.resolve_path(
            auditor_config.paths.evidence, project_root
        )
        self._html_dir = checkpoints_dir / "html_resumo"
        self._html_dir.mkdir(parents=True, exist_ok=True)

        self._checkpoint = CheckpointManager(checkpoints_dir, auditor_config.audit.id)
        self._routes_log = VisitedRoutesLog(visited_routes_path, auditor_config.audit.id)
        self._evidence_store = EvidenceStore(evidence_dir, auditor_config.audit.id)
        self._robots = RobotsChecker(
            user_agent=auditor_config.crawler.user_agent,
            timeout_segundos=auditor_config.crawler.timeout_segundos,
        )

        self._fila: deque[str] = deque()
        self._urls_vistas: set[str] = set()
        self._lock = asyncio.Lock()
        self._resultado = CrawlResult()
        self._tarefas_ativas = 0

    async def executar(self) -> CrawlResult:
        self._inicializar_fila()

        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            try:
                semaforo = asyncio.Semaphore(self._config.crawler.max_workers)
                workers = [
                    asyncio.create_task(self._worker(browser, semaforo, worker_id))
                    for worker_id in range(self._config.crawler.max_workers)
                ]
                await asyncio.gather(*workers)
            finally:
                await browser.close()

        self._resultado.rotas_registradas = len(self._routes_log.rotas)
        self._resultado.paginas_visitadas = self._checkpoint.contar_por_status().get("done", 0)
        return self._resultado

    def _inicializar_fila(self) -> None:
        for url, checkpoint in self._checkpoint.state.urls.items():
            self._urls_vistas.add(url)

        fila_salva = self._checkpoint.state.fila_pendente
        if fila_salva:
            for url in fila_salva:
                if not self._checkpoint.ja_processada(url):
                    self._urls_vistas.add(url)
                    self._fila.append(url)
            return

        if self._atingiu_limite_paginas():
            return

        url_seed = normalize_url(self._url_base) or self._url_base
        if not self._checkpoint.ja_processada(url_seed):
            self._urls_vistas.add(url_seed)
            self._fila.append(url_seed)

    def _atingiu_limite_paginas(self) -> bool:
        return self._contar_paginas_concluidas() >= self._config.crawler.max_paginas

    def _contar_paginas_concluidas(self) -> int:
        return self._checkpoint.contar_por_status().get("done", 0)

    def _adicionar_a_fila(self, url: str) -> bool:
        if url in self._urls_vistas:
            return False
        if self._checkpoint.ja_processada(url):
            self._urls_vistas.add(url)
            return False
        if not pertence_ao_dominio(url, self._dominio):
            return False
        if self._atingiu_limite_paginas():
            return False

        self._urls_vistas.add(url)
        self._fila.append(url)
        self._resultado.urls_descobertas += 1
        return True

    async def _worker(self, browser: Browser, semaforo: asyncio.Semaphore, worker_id: int) -> None:
        while True:
            url = await self._obter_proxima_url()
            if url is None:
                async with self._lock:
                    if self._tarefas_ativas == 0 and not self._fila:
                        return
                await asyncio.sleep(0.2)
                continue

            async with semaforo:
                async with self._lock:
                    self._tarefas_ativas += 1
                try:
                    await self._processar_url(browser, url, worker_id)
                finally:
                    async with self._lock:
                        self._tarefas_ativas -= 1
                await asyncio.sleep(self._config.crawler.rate_limit_segundos)

    async def _obter_proxima_url(self) -> str | None:
        async with self._lock:
            if self._atingiu_limite_paginas():
                return None

            while self._fila:
                url = self._fila.popleft()
                if not self._checkpoint.ja_processada(url):
                    self._persistir_fila()
                    return url

            return None

    def _persistir_fila(self) -> None:
        self._checkpoint.atualizar_fila(list(self._fila))

    async def _processar_url(self, browser: Browser, url: str, worker_id: int) -> None:
        if self._config.crawler.respeitar_robots_txt and not self._robots.pode_acessar(url):
            self._checkpoint.registrar(url, UrlStatus.BLOCKED, origem="robots.txt")
            self._resultado.paginas_bloqueadas += 1
            return

        context = await browser.new_context(user_agent=self._config.crawler.user_agent)
        page = await context.new_page()
        html = ""

        try:
            resposta = await page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=self._config.crawler.timeout_segundos * 1000,
            )
            status_http = resposta.status if resposta else None
            html = await page.content()
            content_hash = calcular_hash_conteudo(html)

            ordem = self._routes_log.proxima_ordem()
            evidence_id = f"ev-{ordem:03d}"

            await self._evidence_store.capturar_da_pagina(
                page=page,
                evidence_id=evidence_id,
                url=url,
                status_http=status_http,
                html=html,
            )
            screenshot_path = self._evidence_store.obter_caminho_screenshot_relativo(
                evidence_id
            )

            self._checkpoint.registrar(
                url=url,
                status=UrlStatus.DONE,
                content_hash=content_hash,
                status_http=status_http,
                origem="crawl",
            )

            self._routes_log.registrar(
                VisitedRoute.criar(
                    ordem=ordem,
                    url=url,
                    status_http=status_http,
                    origem="seed" if ordem == 1 else "crawl",
                    content_hash=content_hash,
                    screenshot=screenshot_path,
                )
            )

        except Exception as exc:
            mensagem_erro = f"Worker {worker_id} — {url}: {exc}"
            self._checkpoint.registrar(
                url=url,
                status=UrlStatus.ERROR,
                origem="crawl",
                erro=str(exc),
            )
            self._resultado.paginas_com_erro += 1
            self._resultado.erros.append(mensagem_erro)
        finally:
            await context.close()

        if html:
            async with self._lock:
                if not self._atingiu_limite_paginas():
                    for link in extrair_links(html, url, self._dominio):
                        self._adicionar_a_fila(link)
