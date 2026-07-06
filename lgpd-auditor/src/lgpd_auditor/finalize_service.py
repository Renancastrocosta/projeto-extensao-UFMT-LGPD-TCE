"""Pipeline final de execução e validação (Fase 6)."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path

from lgpd_auditor.audit import AuditService
from lgpd_auditor.config.loader import AuditorConfig
from lgpd_auditor.crawler.visited_routes import VisitedRoutesLog
from lgpd_auditor.evidence import EvidenceCaptureService
from lgpd_auditor.export_service import ExportService
from lgpd_auditor.governance import EngineeringDiary
from lgpd_auditor.report import ReportGenerator
from lgpd_auditor.validation import MustChecklistValidator, RnfValidator


@dataclass
class FinalizeResult:
    rotas_total: int = 0
    evidencias_capturadas: int = 0
    achados_auditoria: int = 0
    relatorio_md: Path | None = None
    validacao_rnf: dict = field(default_factory=dict)
    checklist_must: dict = field(default_factory=dict)
    avisos: list[str] = field(default_factory=list)


class FinalizeService:
    """Orquestra captura, auditoria, relatório, exportação e validação final."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root

    async def executar(
        self,
        capturar_evidencias: bool = True,
        pular_captura_se_completo: bool = True,
    ) -> FinalizeResult:
        resultado = FinalizeResult()
        routes_log = VisitedRoutesLog(
            self._config.resolve_path(self._config.paths.visited_routes, self._project_root),
            self._config.audit.id,
        )
        resultado.rotas_total = len(routes_log.rotas)
        pendentes = routes_log.rotas_sem_screenshot()

        inicio_evidencia = time.monotonic()
        if capturar_evidencias and pendentes:
            if pular_captura_se_completo and not pendentes:
                resultado.avisos.append("Evidências já completas.")
            else:
                servico_evidencia = EvidenceCaptureService(self._config, self._project_root)
                captura = await servico_evidencia.executar()
                resultado.evidencias_capturadas = captura.capturadas
                if captura.erros:
                    resultado.avisos.append(f"Captura com {captura.erros} erro(s).")

        duracao_evidencia = time.monotonic() - inicio_evidencia if capturar_evidencias else None

        routes_log = VisitedRoutesLog(
            self._config.resolve_path(self._config.paths.visited_routes, self._project_root),
            self._config.audit.id,
        )
        rotas_com_screenshot = sum(1 for r in routes_log.rotas if r.screenshot)

        servico_auditoria = AuditService(self._config, self._project_root)
        audit_result = servico_auditoria.executar()
        resultado.achados_auditoria = len(audit_result.achados)

        generator = ReportGenerator(self._config, self._project_root)
        paths = generator.gerar()
        resultado.relatorio_md = paths.markdown

        export = ExportService(self._config, self._project_root)
        export_result = export.executar(gerar_pdf=True, gerar_dashboard=True, gerar_sintese=True)
        resultado.avisos.extend(export_result.avisos)

        rotas_no_relatorio = self._contar_rotas_no_relatorio(paths.markdown)

        rnf = RnfValidator(self._config, self._project_root).validar(
            total_rotas=resultado.rotas_total,
            rotas_com_screenshot=rotas_com_screenshot,
            duracao_evidencia_segundos=duracao_evidencia,
        )
        checklist = MustChecklistValidator(self._config, self._project_root).validar(
            total_rotas=resultado.rotas_total,
            rotas_no_relatorio=rotas_no_relatorio,
            rotas_com_screenshot=rotas_com_screenshot,
        )

        resultado.validacao_rnf = rnf.para_dict()
        resultado.checklist_must = checklist.para_dict()

        self._salvar_validacao(resultado)
        self._registrar_decisao(rnf.aprovado_geral and checklist.aprovado)

        return resultado

    def _contar_rotas_no_relatorio(self, markdown_path: Path) -> int:
        import json
        routes_path = self._config.resolve_path(
            self._config.paths.visited_routes, self._project_root
        )
        with routes_path.open("r", encoding="utf-8") as f:
            return json.load(f).get("total_rotas", 0)

    def _salvar_validacao(self, resultado: FinalizeResult) -> Path:
        output_path = self._config.resolve_path(
            f"{self._config.paths.audit_dir}/validation_report.json", self._project_root
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as f:
            json.dump({
                "rotas_total": resultado.rotas_total,
                "evidencias_capturadas_sessao": resultado.evidencias_capturadas,
                "achados_auditoria": resultado.achados_auditoria,
                "rnf": resultado.validacao_rnf,
                "must": resultado.checklist_must,
                "avisos": resultado.avisos,
            }, f, ensure_ascii=False, indent=2)
        return output_path

    def _registrar_decisao(self, aprovado: bool) -> None:
        diary_path = self._config.resolve_path(
            self._config.paths.engineering_diary, self._project_root
        )
        diary = EngineeringDiary(diary_path)
        diary.register_decision(
            modulo="fase-6",
            problema="Validação final e entrega do relatório acadêmico TCE-MT",
            solucao_adotada="FinalizeService: evidence → audit → report → export → validação RNF/MUST",
            justificativa="Fecha pipeline completo com checklist reprodutível",
            impacto=f"Entrega {'aprovada' if aprovado else 'parcial — revisar validation_report.json'}",
            alternativas_descartadas=["Entrega manual sem validação automatizada"],
        )
