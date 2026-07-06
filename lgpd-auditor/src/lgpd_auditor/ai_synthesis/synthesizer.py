"""Síntese restrita a evidências — sem inferência de fatos não coletados."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SynthesisResult:
    texto: str
    evidence_ids_citados: list[str]
    caminho_saida: Path


class EvidenceSynthesizer:
    """
    Gera síntese executiva exclusivamente a partir de audit_results.json.
    Proibido inferir fatos não presentes nas evidências.
    """

    def __init__(self, audit_results_path: Path) -> None:
        self._audit_results_path = audit_results_path
        with audit_results_path.open("r", encoding="utf-8") as f:
            self._dados = json.load(f)

    def gerar(self, output_path: Path) -> SynthesisResult:
        resumo = self._dados.get("resumo_por_secao", {})
        achados = self._dados.get("achados", [])
        evidence_ids = list(dict.fromkeys(
            eid for achado in achados for eid in achado.get("evidence_ids", [])
        ))

        linhas = [
            "## Síntese Executiva (baseada exclusivamente em evidências coletadas)",
            "",
            f"**Auditoria:** {self._dados.get('audit_id', '')}  ",
            f"**Páginas analisadas:** {self._dados.get('total_paginas_analisadas', 0)}  ",
            f"**Evidências referenciadas:** {', '.join(evidence_ids) if evidence_ids else 'Nenhuma'}",
            "",
            "> Esta síntese foi gerada automaticamente a partir de `audit_results.json`. "
            "Cada afirmação abaixo possui ancoragem em `evidence_id`. "
            "Não foram inferidos fatos ausentes das evidências.",
            "",
            "### Resumo por seção LGPD",
            "",
        ]

        for secao_id in sorted(resumo.keys()):
            secao = resumo[secao_id]
            eids = secao.get("evidence_ids", [])
            citacao = f" [evidências: {', '.join(eids)}]" if eids else ""
            mensagem = secao.get("mensagem", "")
            linha = (
                f"- **{secao_id} {secao.get('titulo', '')}**: "
                f"Status `{secao.get('status', '')}` | "
                f"Confiança `{secao.get('confianca', '')}` ({secao.get('percentual', 0)}%)"
                f"{citacao}"
            )
            linhas.append(linha)
            if mensagem:
                linhas.append(f"  - {mensagem}")

        linhas.extend(["", "### Principais achados documentados", ""])

        achados_por_evidencia: dict[str, list] = {}
        for achado in achados:
            for eid in achado.get("evidence_ids", []):
                achados_por_evidencia.setdefault(eid, []).append(achado)

        for eid in sorted(achados_por_evidencia.keys()):
            linhas.append(f"**{eid}:**")
            for achado in achados_por_evidencia[eid]:
                linhas.append(
                    f"- [{achado.get('secao_id')}] {achado.get('detalhes', '')} "
                    f"(`{achado.get('status')}`, {achado.get('url', '')})"
                )
            linhas.append("")

        if not achados:
            linhas.append(
                "Não foi localizada evidência suficiente durante a auditoria "
                "para elaborar achados detalhados."
            )

        texto = "\n".join(linhas)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(texto, encoding="utf-8")

        return SynthesisResult(
            texto=texto,
            evidence_ids_citados=evidence_ids,
            caminho_saida=output_path,
        )
