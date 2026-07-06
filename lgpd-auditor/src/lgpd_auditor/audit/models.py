"""Modelos de achados da auditoria LGPD."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

from lgpd_auditor.governance.enums import ConfidenceLevel, EvidenceStatus


@dataclass
class ConformityRule:
    chave: str
    secao_id: str
    descricao: str
    prioridade: str
    keywords: list[str]
    fundamentacao_legal: list[str]


@dataclass
class AuditFinding:
    secao_id: str
    regra: str
    descricao: str
    status: EvidenceStatus
    confianca: ConfidenceLevel
    percentual: int
    evidence_ids: list[str]
    fundamentacao_legal: list[str]
    url: str = ""
    detalhes: str = ""
    termos_encontrados: list[str] = field(default_factory=list)

    def para_dict(self) -> dict[str, Any]:
        dados = asdict(self)
        dados["status"] = self.status.value
        dados["confianca"] = self.confianca.value
        return dados


@dataclass
class SectionSummary:
    secao_id: str
    titulo: str
    status: EvidenceStatus
    confianca: ConfidenceLevel
    percentual: int
    evidence_ids: list[str]
    fundamentacao_legal: list[str]
    total_achados: int
    mensagem: str = ""

    def para_dict(self) -> dict[str, Any]:
        dados = asdict(self)
        dados["status"] = self.status.value
        dados["confianca"] = self.confianca.value
        return dados


@dataclass
class AuditResult:
    audit_id: str
    gerado_em: str
    total_paginas_analisadas: int
    resumo_por_secao: dict[str, SectionSummary]
    achados: list[AuditFinding]
    achados_por_pagina: list[dict[str, Any]]

    def para_dict(self) -> dict[str, Any]:
        return {
            "audit_id": self.audit_id,
            "gerado_em": self.gerado_em,
            "total_paginas_analisadas": self.total_paginas_analisadas,
            "resumo_por_secao": {
                chave: resumo.para_dict()
                for chave, resumo in self.resumo_por_secao.items()
            },
            "achados": [achado.para_dict() for achado in self.achados],
            "achados_por_pagina": self.achados_por_pagina,
        }

    @classmethod
    def criar_vazio(cls, audit_id: str) -> "AuditResult":
        return cls(
            audit_id=audit_id,
            gerado_em=datetime.now(timezone.utc).isoformat(),
            total_paginas_analisadas=0,
            resumo_por_secao={},
            achados=[],
            achados_por_pagina=[],
        )
