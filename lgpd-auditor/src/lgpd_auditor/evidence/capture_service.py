"""Serviço de captura de evidências para rotas já visitadas."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from pathlib import Path

from playwright.async_api import async_playwright

from lgpd_auditor.config.loader import AuditorConfig
from lgpd_auditor.crawler.visited_routes import VisitedRoutesLog
from lgpd_auditor.evidence.store import EvidenceStore
from lgpd_auditor.governance import EngineeringDiary


@dataclass
class EvidenceCaptureResult:
    total_rotas: int = 0
    capturadas: int = 0
    ja_existentes: int = 0
    pendentes: int = 0
    erros: int = 0
    mensagens_erro: list[str] = field(default_factory=list)


class EvidenceCaptureService:
    """Captura screenshots e metadados para rotas do visited_routes.json."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root

        evidence_dir = auditor_config.resolve_path(
            auditor_config.paths.evidence, project_root
        )
        visited_routes_path = auditor_config.resolve_path(
            auditor_config.paths.visited_routes, project_root
        )

        self._evidence_store = EvidenceStore(evidence_dir, auditor_config.audit.id)
        self._routes_log = VisitedRoutesLog(visited_routes_path, auditor_config.audit.id)

    async def executar(self, limite: int | None = None) -> EvidenceCaptureResult:
        resultado = EvidenceCaptureResult()
        rotas = self._routes_log.rotas
        resultado.total_rotas = len(rotas)
        lock = asyncio.Lock()

        rotas_pendentes = [
            rota for rota in rotas
            if not self._evidence_store.ja_capturada(rota.evidence_id)
            and not rota.screenshot
        ]

        resultado.ja_existentes = resultado.total_rotas - len(rotas_pendentes)
        resultado.pendentes = len(rotas_pendentes)

        if limite is not None:
            rotas_pendentes = rotas_pendentes[:limite]

        if not rotas_pendentes:
            return resultado

        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            semaforo = asyncio.Semaphore(self._config.crawler.max_workers)

            async def capturar_rota(rota) -> None:
                async with semaforo:
                    context = await browser.new_context(
                        user_agent=self._config.crawler.user_agent
                    )
                    page = await context.new_page()
                    try:
                        resposta = await page.goto(
                            rota.url,
                            wait_until="domcontentloaded",
                            timeout=self._config.crawler.timeout_segundos * 1000,
                        )
                        status_http = resposta.status if resposta else rota.status_http
                        await self._evidence_store.capturar_da_pagina(
                            page=page,
                            evidence_id=rota.evidence_id,
                            url=rota.url,
                            status_http=status_http,
                        )
                        screenshot_path = (
                            self._evidence_store.obter_caminho_screenshot_relativo(
                                rota.evidence_id
                            )
                        )
                        self._routes_log.atualizar_screenshot(
                            rota.evidence_id, screenshot_path
                        )
                        async with lock:
                            resultado.capturadas += 1
                    except Exception as exc:
                        async with lock:
                            resultado.erros += 1
                            resultado.mensagens_erro.append(
                                f"{rota.evidence_id} — {rota.url}: {exc}"
                            )
                    finally:
                        await context.close()
                    await asyncio.sleep(self._config.crawler.rate_limit_segundos)

            await asyncio.gather(*[capturar_rota(rota) for rota in rotas_pendentes])
            await browser.close()

        return resultado


def registrar_decisao_fase2(
    auditor_config: AuditorConfig, project_root: Path
) -> None:
    diary_path = auditor_config.resolve_path(
        auditor_config.paths.engineering_diary, project_root
    )
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="fase-2",
        problema="Rotas visitadas sem screenshots rastreáveis (screenshot: null)",
        solucao_adotada="EvidenceStore com PNG full-page, metadata.json e index.json por evidence_id",
        justificativa="Atende MUST de evidências verificáveis e rastreabilidade 100%",
        impacto="Screenshots vinculados ao visited_routes.json para relatório e auditoria LGPD",
        alternativas_descartadas=[
            "Screenshots apenas em memória",
            "Um único arquivo ZIP sem metadados",
        ],
    )
