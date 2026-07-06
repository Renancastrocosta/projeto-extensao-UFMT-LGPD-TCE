"""Testes da Fase 1 — crawler, checkpoints e rotas visitadas."""

from pathlib import Path

import pytest

from lgpd_auditor.checkpoint import CheckpointManager, UrlStatus
from lgpd_auditor.crawler.url_utils import (
    calcular_hash_conteudo,
    extrair_links,
    normalize_url,
    pertence_ao_dominio,
)
from lgpd_auditor.crawler.visited_routes import VisitedRoute, VisitedRoutesLog


def test_normalize_url_remove_fragmento():
    url = normalize_url("https://www.tce.mt.gov.br/pagina#secao", "https://www.tce.mt.gov.br/")
    assert url == "https://www.tce.mt.gov.br/pagina"


def test_pertence_ao_dominio():
    assert pertence_ao_dominio("https://www.tce.mt.gov.br/", "tce.mt.gov.br")
    assert not pertence_ao_dominio("https://google.com/", "tce.mt.gov.br")


def test_extrair_links_internos():
    html = """
    <html><body>
      <a href="/sobre">Sobre</a>
      <a href="https://google.com">Externo</a>
      <a href="/doc.pdf">PDF</a>
    </body></html>
    """
    links = extrair_links(html, "https://www.tce.mt.gov.br/", "tce.mt.gov.br")
    assert "https://www.tce.mt.gov.br/sobre" in links
    assert len(links) == 1


def test_calcular_hash_conteudo():
    hash1 = calcular_hash_conteudo("conteudo")
    hash2 = calcular_hash_conteudo("conteudo")
    assert hash1 == hash2


def test_checkpoint_manager_persistencia(tmp_path: Path):
    manager = CheckpointManager(tmp_path, "teste")
    manager.registrar(
        url="https://www.tce.mt.gov.br/",
        status=UrlStatus.DONE,
        content_hash="abc123",
        status_http=200,
    )
    assert manager.ja_processada("https://www.tce.mt.gov.br/")

    manager2 = CheckpointManager(tmp_path, "teste")
    assert manager2.ja_processada("https://www.tce.mt.gov.br/")
    assert manager2.state.urls["https://www.tce.mt.gov.br/"].content_hash == "abc123"


def test_checkpoint_nao_reprocessa_done(tmp_path: Path):
    manager = CheckpointManager(tmp_path, "teste")
    manager.registrar("https://www.tce.mt.gov.br/", UrlStatus.DONE, content_hash="hash")
    manager.registrar("https://www.tce.mt.gov.br/contato", UrlStatus.PENDING)

    assert manager.ja_processada("https://www.tce.mt.gov.br/")
    assert not manager.ja_processada("https://www.tce.mt.gov.br/contato")


def test_visited_routes_log(tmp_path: Path):
    log_path = tmp_path / "visited_routes.json"
    routes_log = VisitedRoutesLog(log_path, "tce-mt")

    rota = VisitedRoute.criar(
        ordem=1,
        url="https://www.tce.mt.gov.br/",
        status_http=200,
        origem="seed",
        content_hash="hash",
    )
    routes_log.registrar(rota)

    assert routes_log.rotas[0].evidence_id == "ev-001"
    assert routes_log.url_ja_registrada("https://www.tce.mt.gov.br/")

    routes_log2 = VisitedRoutesLog(log_path, "tce-mt")
    assert len(routes_log2.rotas) == 1


def test_visited_routes_nao_duplica(tmp_path: Path):
    log_path = tmp_path / "visited_routes.json"
    routes_log = VisitedRoutesLog(log_path, "tce-mt")
    rota = VisitedRoute.criar(1, "https://www.tce.mt.gov.br/", 200)
    routes_log.registrar(rota)
    routes_log.registrar(rota)
    assert len(routes_log.rotas) == 1
