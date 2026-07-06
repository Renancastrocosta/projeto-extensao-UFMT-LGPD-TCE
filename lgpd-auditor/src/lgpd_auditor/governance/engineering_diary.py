"""Diário de Engenharia — registro append-only de decisões técnicas."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class EngineeringDecision:
    """Registro de uma decisão técnica tomada durante a auditoria."""

    data: str
    modulo: str
    problema: str
    solucao_adotada: str
    justificativa: str
    impacto: str
    alternativas_descartadas: list[str] = field(default_factory=list)

    @classmethod
    def create(
        cls,
        modulo: str,
        problema: str,
        solucao_adotada: str,
        justificativa: str,
        impacto: str,
        alternativas_descartadas: list[str] | None = None,
    ) -> "EngineeringDecision":
        return cls(
            data=datetime.now(timezone.utc).isoformat(),
            modulo=modulo,
            problema=problema,
            solucao_adotada=solucao_adotada,
            justificativa=justificativa,
            impacto=impacto,
            alternativas_descartadas=alternativas_descartadas or [],
        )


class EngineeringDiary:
    """Persistência append-only de decisões em formato JSONL."""

    def __init__(self, diary_path: Path) -> None:
        self._diary_path = diary_path
        self._diary_path.parent.mkdir(parents=True, exist_ok=True)

    @property
    def path(self) -> Path:
        return self._diary_path

    def register(self, decision: EngineeringDecision) -> None:
        with self._diary_path.open("a", encoding="utf-8") as diary_file:
            diary_file.write(json.dumps(asdict(decision), ensure_ascii=False) + "\n")

    def register_decision(
        self,
        modulo: str,
        problema: str,
        solucao_adotada: str,
        justificativa: str,
        impacto: str,
        alternativas_descartadas: list[str] | None = None,
    ) -> EngineeringDecision:
        decision = EngineeringDecision.create(
            modulo=modulo,
            problema=problema,
            solucao_adotada=solucao_adotada,
            justificativa=justificativa,
            impacto=impacto,
            alternativas_descartadas=alternativas_descartadas,
        )
        self.register(decision)
        return decision

    def read_all(self) -> list[dict[str, Any]]:
        if not self._diary_path.exists():
            return []

        decisions: list[dict[str, Any]] = []
        with self._diary_path.open("r", encoding="utf-8") as diary_file:
            for line in diary_file:
                line = line.strip()
                if line:
                    decisions.append(json.loads(line))
        return decisions

    def to_markdown_section(self) -> str:
        decisions = self.read_all()
        if not decisions:
            return "## Diário de Engenharia\n\n_Nenhuma decisão registrada._\n"

        lines = ["## Diário de Engenharia", ""]
        for index, decision in enumerate(decisions, start=1):
            lines.append(f"### Decisão {index} — {decision['modulo']}")
            lines.append(f"- **Data:** {decision['data']}")
            lines.append(f"- **Problema:** {decision['problema']}")
            lines.append(f"- **Solução adotada:** {decision['solucao_adotada']}")
            lines.append(f"- **Justificativa:** {decision['justificativa']}")
            lines.append(f"- **Impacto:** {decision['impacto']}")
            if decision.get("alternativas_descartadas"):
                alternativas = ", ".join(decision["alternativas_descartadas"])
                lines.append(f"- **Alternativas descartadas:** {alternativas}")
            lines.append("")

        return "\n".join(lines)
