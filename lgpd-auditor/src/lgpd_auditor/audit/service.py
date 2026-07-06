"""Serviço de auditoria LGPD sobre evidências coletadas."""

from __future__ import annotations

import json
from pathlib import Path

from lgpd_auditor.audit.classifiers.heuristics import (
    HeuristicClassifier,
    PageContext,
    sintetizar_secao,
)
from lgpd_auditor.audit.models import AuditFinding, AuditResult
from lgpd_auditor.audit.rules.engine import LGPDRulesEngine
from lgpd_auditor.config.loader import AuditorConfig
from lgpd_auditor.evidence.store import EvidenceStore
from lgpd_auditor.governance import EngineeringDiary


class AuditService:
    """Executa auditoria heurística LGPD sobre evidências do portal."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root

        evidence_dir = auditor_config.resolve_path(
            auditor_config.paths.evidence, project_root
        )
        legislation_path = auditor_config.resolve_path(
            auditor_config.legislation, project_root
        )

        self._evidence_store = EvidenceStore(evidence_dir, auditor_config.audit.id)
        self._rules_engine = LGPDRulesEngine(legislation_path)
        self._classifier = HeuristicClassifier()
        self._resultado_path = auditor_config.resolve_path(
            f"{auditor_config.paths.audit_dir}/audit_results.json", project_root
        )

    @property
    def resultado_path(self) -> Path:
        return self._resultado_path

    def executar(self) -> AuditResult:
        regras = self._rules_engine.regras
        todos_achados: list[AuditFinding] = []
        achados_por_pagina: list[dict] = []

        for metadata in self._evidence_store.listar_evidencias():
            texto = self._carregar_texto_pagina(metadata.evidence_id)
            contexto = PageContext(
                evidence_id=metadata.evidence_id,
                url=metadata.url,
                texto=texto,
                page_title=metadata.page_title,
            )
            achados_pagina = self._classifier.analisar_pagina(contexto, regras)
            if achados_pagina:
                todos_achados.extend(achados_pagina)
                achados_por_pagina.append({
                    "evidence_id": metadata.evidence_id,
                    "url": metadata.url,
                    "achados": [a.para_dict() for a in achados_pagina],
                })

        resumo_por_secao = {}
        for regra in regras:
            resumo_por_secao[regra.secao_id] = sintetizar_secao(
                secao_id=regra.secao_id,
                titulo=self._rules_engine.titulo_secao(regra.secao_id),
                achados=todos_achados,
                fundamentacao_padrao=regra.fundamentacao_legal,
            )

        resultado = AuditResult(
            audit_id=self._config.audit.id,
            gerado_em=AuditResult.criar_vazio(self._config.audit.id).gerado_em,
            total_paginas_analisadas=len(self._evidence_store.listar_evidencias()),
            resumo_por_secao=resumo_por_secao,
            achados=todos_achados,
            achados_por_pagina=achados_por_pagina,
        )

        self._salvar_resultado(resultado)
        return resultado

    def _carregar_texto_pagina(self, evidence_id: str) -> str:
        summary_path = (
            self._evidence_store.evidence_dir / evidence_id / "page_summary.txt"
        )
        if summary_path.exists():
            return summary_path.read_text(encoding="utf-8")

        metadata = self._evidence_store.obter_metadata(evidence_id)
        return metadata.page_title if metadata else ""

    def _salvar_resultado(self, resultado: AuditResult) -> None:
        self._resultado_path.parent.mkdir(parents=True, exist_ok=True)
        dados = resultado.para_dict()
        dados["legislacao"] = self._rules_engine.versao_legislacao()
        with self._resultado_path.open("w", encoding="utf-8") as resultado_file:
            json.dump(dados, resultado_file, ensure_ascii=False, indent=2)


def registrar_decisao_fase3(
    auditor_config: AuditorConfig, project_root: Path
) -> None:
    diary_path = auditor_config.resolve_path(
        auditor_config.paths.engineering_diary, project_root
    )
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="fase-3",
        problema="Necessidade de avaliar conformidade LGPD com evidências rastreáveis",
        solucao_adotada="LGPDRulesEngine + classificadores heurísticos com status e confiança",
        justificativa="Atende MUST de auditoria LGPD sem alucinação — achados ancorados em evidence_id",
        impacto="audit_results.json pronto para geração de relatório na Fase 4",
        alternativas_descartadas=[
            "IA generativa sem evidências",
            "Checklist manual sem automação",
        ],
    )
