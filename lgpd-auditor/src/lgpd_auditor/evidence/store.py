"""Armazenamento de evidências com screenshots, HTML resumido e metadados."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from playwright.async_api import Page

from lgpd_auditor.crawler.url_utils import calcular_hash_conteudo, resumir_html
from lgpd_auditor.evidence.models import EvidenceMetadata


class EvidenceStore:
    """Persiste evidências rastreáveis por evidence_id."""

    def __init__(self, evidence_dir: Path, audit_id: str) -> None:
        self._evidence_dir = evidence_dir
        self._evidence_dir.mkdir(parents=True, exist_ok=True)
        self._audit_id = audit_id
        self._indice_path = evidence_dir / "index.json"
        self._indice = self._carregar_indice()

    @property
    def evidence_dir(self) -> Path:
        return self._evidence_dir

    @property
    def indice_path(self) -> Path:
        return self._indice_path

    def _carregar_indice(self) -> dict[str, dict]:
        if not self._indice_path.exists():
            return {}
        with self._indice_path.open("r", encoding="utf-8") as indice_file:
            dados = json.load(indice_file)
        return dados.get("evidencias", {})

    def _salvar_indice(self) -> None:
        with self._indice_path.open("w", encoding="utf-8") as indice_file:
            json.dump(
                {
                    "audit_id": self._audit_id,
                    "total": len(self._indice),
                    "evidencias": self._indice,
                },
                indice_file,
                ensure_ascii=False,
                indent=2,
            )

    def _diretorio_evidencia(self, evidence_id: str) -> Path:
        diretorio = self._evidence_dir / evidence_id
        diretorio.mkdir(parents=True, exist_ok=True)
        return diretorio

    @staticmethod
    def _calcular_hash_arquivo(caminho: Path) -> str:
        return sha256(caminho.read_bytes()).hexdigest()

    def ja_capturada(self, evidence_id: str) -> bool:
        metadata_path = self._evidence_dir / evidence_id / "metadata.json"
        screenshot_path = self._evidence_dir / evidence_id / "screenshot.png"
        return metadata_path.exists() and screenshot_path.exists()

    def obter_caminho_screenshot_relativo(self, evidence_id: str) -> str:
        return f"evidence/{evidence_id}/screenshot.png"

    async def capturar_da_pagina(
        self,
        page: Page,
        evidence_id: str,
        url: str,
        status_http: int | None,
        html: str | None = None,
    ) -> EvidenceMetadata:
        """Captura screenshot e metadados a partir de uma página Playwright aberta."""
        if html is None:
            html = await page.content()

        page_title = await page.title()
        content_hash = calcular_hash_conteudo(html)
        diretorio = self._diretorio_evidencia(evidence_id)

        screenshot_path = diretorio / "screenshot.png"
        await page.screenshot(path=str(screenshot_path), full_page=True)

        html_summary_path = diretorio / "page_summary.txt"
        html_summary_path.write_text(resumir_html(html), encoding="utf-8")

        screenshot_hash = self._calcular_hash_arquivo(screenshot_path)
        screenshot_relativo = self.obter_caminho_screenshot_relativo(evidence_id)

        metadata = EvidenceMetadata.criar(
            evidence_id=evidence_id,
            url=url,
            status_http=status_http,
            content_hash=content_hash,
            screenshot_hash=screenshot_hash,
            screenshot_path=screenshot_relativo,
            html_summary_path=f"evidence/{evidence_id}/page_summary.txt",
            page_title=page_title,
            audit_id=self._audit_id,
        )

        metadata_path = diretorio / "metadata.json"
        metadata_path.write_text(
            json.dumps(metadata.para_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        self._indice[evidence_id] = metadata.para_dict()
        self._salvar_indice()
        return metadata

    def listar_evidencias(self) -> list[EvidenceMetadata]:
        return [EvidenceMetadata(**dados) for dados in self._indice.values()]

    def obter_metadata(self, evidence_id: str) -> EvidenceMetadata | None:
        dados = self._indice.get(evidence_id)
        if dados is None:
            metadata_path = self._evidence_dir / evidence_id / "metadata.json"
            if not metadata_path.exists():
                return None
            with metadata_path.open("r", encoding="utf-8") as metadata_file:
                dados = json.load(metadata_file)
        return EvidenceMetadata(**dados)
