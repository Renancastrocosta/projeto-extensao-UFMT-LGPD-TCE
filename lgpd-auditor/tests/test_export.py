"""Testes da Fase 5 — exportação, dashboard e síntese."""

import json
from pathlib import Path

import pytest

from lgpd_auditor.ai_synthesis.synthesizer import EvidenceSynthesizer
from lgpd_auditor.config import load_auditor_config
from lgpd_auditor.export_service import ExportService
from lgpd_auditor.report.dashboard import DashboardGenerator

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def audit_setup(tmp_path: Path):
    audit_dir = tmp_path / "audits" / "tce-mt"
    reports_dir = audit_dir / "reports"
    evidence_dir = audit_dir / "evidence"
    reports_dir.mkdir(parents=True)
    evidence_dir.mkdir(parents=True)

    audit_results = {
        "audit_id": "tce-mt",
        "gerado_em": "2026-07-06T00:00:00Z",
        "total_paginas_analisadas": 2,
        "resumo_por_secao": {
            "4.1": {
                "secao_id": "4.1",
                "titulo": "Transparência",
                "status": "Confirmado",
                "confianca": "Alta",
                "percentual": 85,
                "evidence_ids": ["ev-001"],
                "fundamentacao_legal": ["art. 9 LGPD"],
                "total_achados": 1,
                "mensagem": "",
            },
            "4.4": {
                "secao_id": "4.4",
                "titulo": "Direitos do titular",
                "status": "Não Localizado",
                "confianca": "Muito Baixa",
                "percentual": 15,
                "evidence_ids": [],
                "fundamentacao_legal": ["art. 18 LGPD"],
                "total_achados": 0,
                "mensagem": "Não foi localizada evidência suficiente durante a auditoria.",
            },
        },
        "achados": [{
            "secao_id": "4.1",
            "regra": "transparencia",
            "descricao": "Política de privacidade",
            "status": "Confirmado",
            "confianca": "Alta",
            "percentual": 85,
            "evidence_ids": ["ev-001"],
            "fundamentacao_legal": ["art. 9 LGPD"],
            "url": "https://www.tce.mt.gov.br/",
            "detalhes": "Política identificada.",
            "termos_encontrados": ["privacidade"],
        }],
        "achados_por_pagina": [],
    }
    (audit_dir / "audit_results.json").write_text(
        json.dumps(audit_results), encoding="utf-8"
    )

    visited = {
        "audit_id": "tce-mt",
        "total_rotas": 1,
        "rotas": [{
            "ordem": 1,
            "url": "https://www.tce.mt.gov.br/",
            "status_http": 200,
            "visitada_em": "2026-07-06T00:00:00Z",
            "evidence_id": "ev-001",
            "screenshot": "evidence/ev-001/screenshot.png",
            "origem": "seed",
            "content_hash": "abc",
        }],
    }
    (audit_dir / "visited_routes.json").write_text(json.dumps(visited), encoding="utf-8")

    ev_dir = evidence_dir / "ev-001"
    ev_dir.mkdir()
    (ev_dir / "screenshot.png").write_bytes(b"png")
    (ev_dir / "metadata.json").write_text("{}", encoding="utf-8")
    (ev_dir / "page_summary.txt").write_text("privacidade", encoding="utf-8")

    (reports_dir / "relatorio-lgpd-tce-mt.html").write_text(
        "<html><body><h1>Teste</h1></body></html>", encoding="utf-8"
    )

    config = load_auditor_config(PROJECT_ROOT / "config" / "tce-mt.yaml")
    config.paths.audit_dir = "audits/tce-mt"
    config.paths.reports = "audits/tce-mt/reports"
    config.paths.evidence = "audits/tce-mt/evidence"
    config.paths.visited_routes = "audits/tce-mt/visited_routes.json"

    return tmp_path, config


def test_synthesizer_cita_evidence_ids(audit_setup):
    tmp_path, _ = audit_setup
    audit_path = tmp_path / "audits" / "tce-mt" / "audit_results.json"
    synthesizer = EvidenceSynthesizer(audit_path)
    resultado = synthesizer.gerar(tmp_path / "sintese.md")

    assert "ev-001" in resultado.texto
    assert "ev-001" in resultado.evidence_ids_citados
    assert "Não foi localizada evidência" in resultado.texto


def test_dashboard_generator(audit_setup):
    tmp_path, _ = audit_setup
    audit_path = tmp_path / "audits" / "tce-mt" / "audit_results.json"
    with audit_path.open("r", encoding="utf-8") as f:
        audit_data = json.load(f)

    generator = DashboardGenerator(tmp_path)
    output = generator.gerar(
        audit_data=audit_data,
        total_rotas=1,
        total_evidencias=1,
        output_path=tmp_path / "dashboard.html",
        portal_nome="TCE-MT",
        url_base="https://www.tce.mt.gov.br/",
    )

    html = output.read_text(encoding="utf-8")
    assert "Dashboard LGPD" in html
    assert "4.1" in html
    assert "Confirmado" in html


def test_export_service_sem_pdf(audit_setup):
    tmp_path, config = audit_setup
    servico = ExportService(config, tmp_path)
    resultado = servico.executar(
        gerar_pdf=False,
        gerar_dashboard=True,
        gerar_sintese=True,
        executar_ocr=False,
    )

    assert resultado.dashboard is not None
    assert resultado.sintese is not None
    assert resultado.dashboard.exists()
    assert resultado.sintese.exists()
