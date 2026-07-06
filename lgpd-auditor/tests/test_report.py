"""Testes da Fase 4 — geração de relatório."""

import json
from pathlib import Path

import pytest

from lgpd_auditor.config import load_auditor_config
from lgpd_auditor.crawler.visited_routes import VisitedRoute, VisitedRoutesLog
from lgpd_auditor.report.generator import ReportGenerator
from lgpd_auditor.report.routes_export import exportar_rotas_csv

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_exportar_rotas_csv(tmp_path: Path):
    log_path = tmp_path / "visited_routes.json"
    routes_log = VisitedRoutesLog(log_path, "tce-mt")
    routes_log.registrar(
        VisitedRoute.criar(
            1, "https://www.tce.mt.gov.br/", 200,
            screenshot="evidence/ev-001/screenshot.png",
        )
    )

    csv_path = tmp_path / "visited_routes.csv"
    exportar_rotas_csv(routes_log, csv_path)

    conteudo = csv_path.read_text(encoding="utf-8")
    assert "evidence_id" in conteudo
    assert "ev-001" in conteudo
    assert "https://www.tce.mt.gov.br/" in conteudo


def test_report_generator(tmp_path: Path):
    config = load_auditor_config(PROJECT_ROOT / "config" / "tce-mt.yaml")

    audit_dir = tmp_path / "audits" / "tce-mt"
    reports_dir = audit_dir / "reports"
    audit_dir.mkdir(parents=True)

    audit_results = {
        "audit_id": "tce-mt",
        "gerado_em": "2026-07-06T00:00:00Z",
        "total_paginas_analisadas": 1,
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
    (audit_dir / "visited_routes.json").write_text(
        json.dumps(visited), encoding="utf-8"
    )

    (audit_dir / "checkpoints").mkdir()
    (audit_dir / "checkpoints" / "latest.json").write_text(
        json.dumps({"audit_id": "tce-mt", "urls": {}, "fila_pendente": []}),
        encoding="utf-8",
    )
    (audit_dir / "engineering_diary.jsonl").write_text("", encoding="utf-8")

    (tmp_path / "templates" / "report").mkdir(parents=True)
    for template in ("relatorio.md.j2", "relatorio.html.j2"):
        origem = PROJECT_ROOT / "templates" / "report" / template
        (tmp_path / "templates" / "report" / template).write_text(
            origem.read_text(encoding="utf-8"), encoding="utf-8"
        )

    config.paths.audit_dir = "audits/tce-mt"
    config.paths.reports = "audits/tce-mt/reports"
    config.paths.visited_routes = "audits/tce-mt/visited_routes.json"
    config.paths.checkpoints = "audits/tce-mt/checkpoints"
    config.paths.engineering_diary = "audits/tce-mt/engineering_diary.jsonl"

    generator = ReportGenerator(config, tmp_path)
    paths = generator.gerar()

    assert paths.markdown.exists()
    assert paths.html.exists()
    assert paths.csv.exists()

    markdown = paths.markdown.read_text(encoding="utf-8")
    assert "Anexo A" in markdown
    assert "Diário de Engenharia" in markdown or "4.1" in markdown
    assert "ev-001" in markdown
    assert "503" not in markdown  # apenas 1 rota no teste
