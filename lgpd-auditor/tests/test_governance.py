"""Testes da Fase 0 — governança e configuração."""

from pathlib import Path

import pytest

from lgpd_auditor import __version__
from lgpd_auditor.config import load_auditor_config, load_legislation
from lgpd_auditor.governance import (
    ConfidenceLevel,
    EngineeringDiary,
    EvidenceStatus,
    RequirementPriority,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_version():
    assert __version__ == "0.1.0"


def test_evidence_status_mensagem_ausencia():
    assert "evidência suficiente" in EvidenceStatus.NAO_LOCALIZADO.mensagem_ausencia


def test_confidence_from_evidence_count():
    assert ConfidenceLevel.from_evidence_count(2) == ConfidenceLevel.ALTA
    assert ConfidenceLevel.from_evidence_count(0) == ConfidenceLevel.MUITO_BAIXA


def test_requirement_priority_dominates():
    assert RequirementPriority.P0_LEGISLACAO.dominates(RequirementPriority.P5_FUNCIONAL)


def test_load_auditor_config():
    config = load_auditor_config(PROJECT_ROOT / "config" / "tce-mt.yaml")
    assert config.audit.id == "tce-mt"
    assert config.crawler.max_workers == 5


def test_load_legislation():
    legislation = load_legislation(PROJECT_ROOT / "legislation.yaml")
    assert legislation["lgpd"]["lei"] == 13709
    assert "transparencia" in legislation["regras_conformidade"]


def test_engineering_diary_append(tmp_path: Path):
    diary_path = tmp_path / "engineering_diary.jsonl"
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="teste",
        problema="problema",
        solucao_adotada="solução",
        justificativa="justificativa",
        impacto="impacto",
    )
    decisions = diary.read_all()
    assert len(decisions) == 1
    assert decisions[0]["modulo"] == "teste"
