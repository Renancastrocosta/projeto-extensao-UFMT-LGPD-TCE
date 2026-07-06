"""Motor de regras LGPD baseado em legislation.yaml."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from lgpd_auditor.audit.models import ConformityRule
from lgpd_auditor.config.loader import load_legislation


TITULOS_SECAO = {
    "4.1": "Transparência e política de privacidade",
    "4.2": "Coleta de dados",
    "4.3": "Consentimento",
    "4.4": "Direitos do titular",
    "4.5": "Segurança da informação",
    "4.6": "Cookies",
}


class LGPDRulesEngine:
    """Carrega e expõe regras de conformidade versionadas."""

    def __init__(self, legislation_path: Path) -> None:
        self._legislation_path = legislation_path
        self._legislation = load_legislation(legislation_path)
        self._regras = self._carregar_regras()

    @property
    def legislation(self) -> dict[str, Any]:
        return self._legislation

    @property
    def regras(self) -> list[ConformityRule]:
        return list(self._regras.values())

    def obter_regra(self, chave: str) -> ConformityRule | None:
        return self._regras.get(chave)

    def titulo_secao(self, secao_id: str) -> str:
        return TITULOS_SECAO.get(secao_id, secao_id)

    def _carregar_regras(self) -> dict[str, ConformityRule]:
        regras_brutas = self._legislation.get("regras_conformidade", {})
        regras: dict[str, ConformityRule] = {}

        for chave, dados in regras_brutas.items():
            regras[chave] = ConformityRule(
                chave=chave,
                secao_id=str(dados.get("id", "")),
                descricao=str(dados.get("descricao", "")),
                prioridade=str(dados.get("prioridade", "P5")),
                keywords=[kw.lower() for kw in dados.get("keywords", [])],
                fundamentacao_legal=list(dados.get("fundamentacao", [])),
            )

        return regras

    def versao_legislacao(self) -> dict[str, Any]:
        return {
            "lgpd": self._legislation.get("lgpd", {}),
            "anpd": self._legislation.get("anpd", {}),
            "arquivo": str(self._legislation_path),
        }
