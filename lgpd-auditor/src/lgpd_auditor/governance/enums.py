"""Enums de governança para classificação de evidências e requisitos."""

from enum import Enum


class EvidenceStatus(str, Enum):
    """Status de uma conclusão de auditoria conforme política anti-alucinação."""

    CONFIRMADO = "Confirmado"
    INFERENCIA = "Inferência"
    HIPOTESE = "Hipótese"
    NAO_LOCALIZADO = "Não Localizado"

    @property
    def mensagem_ausencia(self) -> str:
        if self == EvidenceStatus.NAO_LOCALIZADO:
            return "Não foi localizada evidência suficiente durante a auditoria."
        if self == EvidenceStatus.HIPOTESE:
            return "Não há evidências suficientes para confirmar esta conclusão."
        return ""


class ConfidenceLevel(str, Enum):
    """Nível de confiança de uma conclusão."""

    MUITO_ALTA = "Muito Alta"
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"
    MUITO_BAIXA = "Muito Baixa"

    @classmethod
    def from_evidence_count(cls, count: int) -> "ConfidenceLevel":
        if count >= 2:
            return cls.ALTA
        if count == 1:
            return cls.MEDIA
        return cls.MUITO_BAIXA

    def to_percentual(self) -> int:
        mapping = {
            ConfidenceLevel.MUITO_ALTA: 95,
            ConfidenceLevel.ALTA: 85,
            ConfidenceLevel.MEDIA: 65,
            ConfidenceLevel.BAIXA: 40,
            ConfidenceLevel.MUITO_BAIXA: 15,
        }
        return mapping[self]


class RequirementPriority(str, Enum):
    """Hierarquia de prioridade dos requisitos (P0–P8)."""

    P0_LEGISLACAO = "P0"
    P1_SEGURANCA = "P1"
    P2_INTEGRIDADE = "P2"
    P3_PRECISAO = "P3"
    P4_ACEITACAO = "P4"
    P5_FUNCIONAL = "P5"
    P6_NAO_FUNCIONAL = "P6"
    P7_RECOMENDADO = "P7"
    P8_OPCIONAL = "P8"

    @property
    def rank(self) -> int:
        return int(self.value[1])

    def dominates(self, other: "RequirementPriority") -> bool:
        return self.rank < other.rank
