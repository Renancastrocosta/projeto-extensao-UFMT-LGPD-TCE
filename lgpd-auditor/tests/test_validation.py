"""Testes da Fase 6 — validação RNF e checklist MUST."""

from pathlib import Path

import pytest

from lgpd_auditor.config import load_auditor_config
from lgpd_auditor.validation import MustChecklistValidator, RnfValidator

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_rnf_validator_workers():
    config = load_auditor_config(PROJECT_ROOT / "config" / "tce-mt.yaml")
    validator = RnfValidator(config, PROJECT_ROOT)
    resultado = validator.validar(total_rotas=503, rotas_com_screenshot=7)

    workers_check = next(v for v in resultado.verificacoes if v.nome == "Concorrência (workers)")
    assert workers_check.aprovado
    assert workers_check.valor_obtido == "5"


def test_must_checklist_com_projeto_real():
    config = load_auditor_config(PROJECT_ROOT / "config" / "tce-mt.yaml")
    validator = MustChecklistValidator(config, PROJECT_ROOT)
    resultado = validator.validar(
        total_rotas=503,
        rotas_no_relatorio=503,
        rotas_com_screenshot=7,
    )

    assert resultado.cobertura_percentual > 0
    crawler_item = next(i for i in resultado.itens if i.requisito == "Crawler com checkpoints")
    assert crawler_item.aprovado
