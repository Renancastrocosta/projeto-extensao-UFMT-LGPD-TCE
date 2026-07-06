"""Testes da Fase 3 — motor de auditoria LGPD."""

import json
from pathlib import Path

import pytest

from lgpd_auditor.audit.classifiers.heuristics import (
    HeuristicClassifier,
    PageContext,
    sintetizar_secao,
)
from lgpd_auditor.audit.models import AuditFinding
from lgpd_auditor.audit.rules.engine import LGPDRulesEngine
from lgpd_auditor.audit.service import AuditService
from lgpd_auditor.config import load_auditor_config
from lgpd_auditor.evidence.models import EvidenceMetadata
from lgpd_auditor.evidence.store import EvidenceStore
from lgpd_auditor.governance.enums import ConfidenceLevel, EvidenceStatus

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_rules_engine_carrega_legislacao():
    engine = LGPDRulesEngine(PROJECT_ROOT / "legislation.yaml")
    regras = engine.regras
    assert len(regras) == 6
    assert engine.obter_regra("transparencia") is not None
    assert engine.obter_regra("transparencia").secao_id == "4.1"


def test_classificador_transparencia_confirmado():
    engine = LGPDRulesEngine(PROJECT_ROOT / "legislation.yaml")
    regra = engine.obter_regra("transparencia")
    classifier = HeuristicClassifier()

    contexto = PageContext(
        evidence_id="ev-001",
        url="https://www.tce.mt.gov.br/privacidade",
        texto="Política de privacidade e proteção de dados pessoais.",
        page_title="Privacidade",
    )
    achados = classifier.analisar_pagina(contexto, [regra])
    assert len(achados) == 1
    assert achados[0].status == EvidenceStatus.CONFIRMADO
    assert achados[0].evidence_ids == ["ev-001"]


def test_classificador_sem_evidencia_retorna_none():
    engine = LGPDRulesEngine(PROJECT_ROOT / "legislation.yaml")
    regra = engine.obter_regra("consentimento")
    classifier = HeuristicClassifier()

    contexto = PageContext(
        evidence_id="ev-099",
        url="https://www.tce.mt.gov.br/noticias",
        texto="Notícia institucional sem termos relevantes.",
        page_title="Notícias",
    )
    achados = classifier.analisar_pagina(contexto, [regra])
    assert achados == []


def test_sintetizar_secao_nao_localizado():
    resumo = sintetizar_secao("4.3", "Consentimento", [], ["art. 8 LGPD"])
    assert resumo.status == EvidenceStatus.NAO_LOCALIZADO
    assert "evidência suficiente" in resumo.mensagem


def test_sintetizar_secao_com_achados():
    achado = AuditFinding(
        secao_id="4.5",
        regra="seguranca",
        descricao="Segurança",
        status=EvidenceStatus.CONFIRMADO,
        confianca=ConfidenceLevel.ALTA,
        percentual=85,
        evidence_ids=["ev-001", "ev-002"],
        fundamentacao_legal=["art. 46 LGPD"],
        url="https://www.tce.mt.gov.br/",
    )
    resumo = sintetizar_secao("4.5", "Segurança", [achado], ["art. 46 LGPD"])
    assert resumo.status == EvidenceStatus.CONFIRMADO
    assert len(resumo.evidence_ids) == 2


def test_audit_service_executa(tmp_path: Path):
    config = load_auditor_config(PROJECT_ROOT / "config" / "tce-mt.yaml")

    evidence_dir = tmp_path / "evidence"
    store = EvidenceStore(evidence_dir, "teste")

    diretorio = evidence_dir / "ev-001"
    diretorio.mkdir(parents=True)
    (diretorio / "page_summary.txt").write_text(
        "Política de privacidade. Formulário de cadastro com CPF e e-mail. "
        "Consentimento. Encarregado de dados. Cookies.",
        encoding="utf-8",
    )
    metadata = EvidenceMetadata.criar(
        evidence_id="ev-001",
        url="https://www.tce.mt.gov.br/",
        status_http=200,
        content_hash="hash",
        screenshot_hash="shash",
        screenshot_path="evidence/ev-001/screenshot.png",
        html_summary_path="evidence/ev-001/page_summary.txt",
        page_title="Portal",
        audit_id="teste",
    )
    (diretorio / "screenshot.png").write_bytes(b"img")
    (diretorio / "metadata.json").write_text(
        json.dumps(metadata.para_dict()), encoding="utf-8"
    )
    store._indice["ev-001"] = metadata.para_dict()
    store._salvar_indice()

    (tmp_path / "legislation.yaml").write_text(
        (PROJECT_ROOT / "legislation.yaml").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    config.paths.evidence = str(evidence_dir.relative_to(tmp_path))
    config.paths.audit_dir = "audits"
    config.legislation = "legislation.yaml"

    servico = AuditService(config, tmp_path)
    resultado = servico.executar()

    assert resultado.total_paginas_analisadas == 1
    assert len(resultado.achados) > 0
    assert servico.resultado_path.exists()
    assert resultado.resumo_por_secao["4.1"].status != EvidenceStatus.NAO_LOCALIZADO
