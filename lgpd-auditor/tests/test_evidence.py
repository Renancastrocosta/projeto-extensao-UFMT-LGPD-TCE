"""Testes da Fase 2 — EvidenceStore e captura de evidências."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

from lgpd_auditor.crawler.visited_routes import VisitedRoute, VisitedRoutesLog
from lgpd_auditor.evidence.models import EvidenceMetadata
from lgpd_auditor.evidence.store import EvidenceStore


@pytest.mark.asyncio
async def test_evidence_store_captura_da_pagina(tmp_path: Path):
    store = EvidenceStore(tmp_path, "tce-mt")

    page = AsyncMock()
    page.content = AsyncMock(return_value="<html><head><title>Teste</title></head><body>LGPD</body></html>")
    page.title = AsyncMock(return_value="Teste")
    page.screenshot = AsyncMock()

    def fake_screenshot(path: str, full_page: bool = True) -> None:
        Path(path).write_bytes(b"png-fake-content")

    page.screenshot.side_effect = fake_screenshot

    metadata = await store.capturar_da_pagina(
        page=page,
        evidence_id="ev-001",
        url="https://www.tce.mt.gov.br/",
        status_http=200,
    )

    assert metadata.evidence_id == "ev-001"
    assert metadata.url == "https://www.tce.mt.gov.br/"
    assert metadata.page_title == "Teste"
    assert (tmp_path / "ev-001" / "screenshot.png").exists()
    assert (tmp_path / "ev-001" / "metadata.json").exists()
    assert (tmp_path / "ev-001" / "page_summary.txt").exists()
    assert store.ja_capturada("ev-001")


def test_evidence_store_indice(tmp_path: Path):
    store = EvidenceStore(tmp_path, "tce-mt")
    diretorio = tmp_path / "ev-002"
    diretorio.mkdir()
    (diretorio / "screenshot.png").write_bytes(b"img")
    metadata = EvidenceMetadata.criar(
        evidence_id="ev-002",
        url="https://www.tce.mt.gov.br/sobre",
        status_http=200,
        content_hash="hash",
        screenshot_hash="shash",
        screenshot_path="evidence/ev-002/screenshot.png",
        html_summary_path="evidence/ev-002/page_summary.txt",
        audit_id="tce-mt",
    )
    (diretorio / "metadata.json").write_text(
        json.dumps(metadata.para_dict()), encoding="utf-8"
    )

    store_reloaded = EvidenceStore(tmp_path, "tce-mt")
    assert store_reloaded.ja_capturada("ev-002")
    obtido = store_reloaded.obter_metadata("ev-002")
    assert obtido is not None
    assert obtido.url == "https://www.tce.mt.gov.br/sobre"


def test_visited_routes_atualizar_screenshot(tmp_path: Path):
    log_path = tmp_path / "visited_routes.json"
    routes_log = VisitedRoutesLog(log_path, "tce-mt")
    rota = VisitedRoute.criar(1, "https://www.tce.mt.gov.br/", 200)
    routes_log.registrar(rota)

    assert routes_log.atualizar_screenshot("ev-001", "evidence/ev-001/screenshot.png")
    assert routes_log.rotas[0].screenshot == "evidence/ev-001/screenshot.png"


def test_visited_routes_sem_screenshot(tmp_path: Path):
    log_path = tmp_path / "visited_routes.json"
    routes_log = VisitedRoutesLog(log_path, "tce-mt")
    routes_log.registrar(VisitedRoute.criar(1, "https://www.tce.mt.gov.br/", 200))
    routes_log.registrar(
        VisitedRoute.criar(
            2, "https://www.tce.mt.gov.br/sobre", 200,
            screenshot="evidence/ev-002/screenshot.png",
        )
    )

    sem_screenshot = routes_log.rotas_sem_screenshot()
    assert len(sem_screenshot) == 1
    assert sem_screenshot[0].evidence_id == "ev-001"
