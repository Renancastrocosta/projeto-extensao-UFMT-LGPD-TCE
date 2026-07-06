"""Orquestra exportações da Fase 5 (OCR, PDF, dashboard, síntese)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from lgpd_auditor.ai_synthesis.synthesizer import EvidenceSynthesizer
from lgpd_auditor.config.loader import AuditorConfig
from lgpd_auditor.crawler.visited_routes import VisitedRoutesLog
from lgpd_auditor.evidence.ocr_service import OcrBatchResult, OcrService
from lgpd_auditor.evidence.store import EvidenceStore
from lgpd_auditor.governance import EngineeringDiary
from lgpd_auditor.report.dashboard import DashboardGenerator
from lgpd_auditor.report.pdf_export import exportar_pdf


@dataclass
class ExportResult:
    pdf: Path | None = None
    dashboard: Path | None = None
    sintese: Path | None = None
    ocr: OcrBatchResult | None = None
    avisos: list[str] = field(default_factory=list)


class ExportService:
    """Executa funcionalidades SHOULD da Fase 5."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root
        self._reports_dir = auditor_config.resolve_path(
            auditor_config.paths.reports, project_root
        )
        self._evidence_dir = auditor_config.resolve_path(
            auditor_config.paths.evidence, project_root
        )
        self._audit_results_path = auditor_config.resolve_path(
            f"{auditor_config.paths.audit_dir}/audit_results.json", project_root
        )
        self._visited_routes_path = auditor_config.resolve_path(
            auditor_config.paths.visited_routes, project_root
        )

    def executar(
        self,
        gerar_pdf: bool = True,
        gerar_dashboard: bool = True,
        gerar_sintese: bool = True,
        executar_ocr: bool = False,
        ocr_limite: int | None = None,
    ) -> ExportResult:
        resultado = ExportResult()

        if not self._audit_results_path.exists():
            raise FileNotFoundError(
                f"audit_results.json não encontrado: {self._audit_results_path}"
            )

        html_relatorio = self._reports_dir / "relatorio-lgpd-tce-mt.html"
        if gerar_pdf:
            resultado.pdf = self._gerar_pdf(html_relatorio, resultado.avisos)

        if gerar_dashboard:
            resultado.dashboard = self._gerar_dashboard(resultado.avisos)

        if gerar_sintese:
            resultado.sintese = self._gerar_sintese()

        if executar_ocr:
            resultado.ocr = self._executar_ocr(ocr_limite, resultado.avisos)

        return resultado

    def _gerar_pdf(self, html_path: Path, avisos: list[str]) -> Path | None:
        pdf_path = self._reports_dir / "relatorio-lgpd-tce-mt.pdf"
        try:
            return exportar_pdf(html_path, pdf_path)
        except (RuntimeError, ImportError, OSError) as exc:
            avisos.append(f"PDF não gerado: {exc}")
            return None

    def _gerar_dashboard(self, avisos: list[str]) -> Path | None:
        try:
            import json
            with self._audit_results_path.open("r", encoding="utf-8") as f:
                audit_data = json.load(f)

            routes_log = VisitedRoutesLog(self._visited_routes_path, self._config.audit.id)
            evidence_store = EvidenceStore(self._evidence_dir, self._config.audit.id)

            generator = DashboardGenerator(self._project_root)
            return generator.gerar(
                audit_data=audit_data,
                total_rotas=len(routes_log.rotas),
                total_evidencias=len(evidence_store.listar_evidencias()),
                output_path=self._reports_dir / "dashboard.html",
                portal_nome=self._config.audit.nome,
                url_base=str(self._config.audit.url_base),
            )
        except Exception as exc:
            avisos.append(f"Dashboard não gerado: {exc}")
            return None

    def _gerar_sintese(self) -> Path:
        sintese_path = self._reports_dir / "sintese-executiva.md"
        synthesizer = EvidenceSynthesizer(self._audit_results_path)
        resultado = synthesizer.gerar(sintese_path)
        return resultado.caminho_saida

    def _executar_ocr(
        self, limite: int | None, avisos: list[str]
    ) -> OcrBatchResult | None:
        try:
            ocr_service = OcrService(self._evidence_dir)
            return ocr_service.processar_todas(limite=limite)
        except RuntimeError as exc:
            avisos.append(f"OCR não executado: {exc}")
            return None


def registrar_decisao_fase5(
    auditor_config: AuditorConfig, project_root: Path
) -> None:
    diary_path = auditor_config.resolve_path(
        auditor_config.paths.engineering_diary, project_root
    )
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="fase-5",
        problema="Necessidade de PDF, dashboard e síntese para entrega acadêmica",
        solucao_adotada="ExportService com PDF (WeasyPrint), dashboard HTML, síntese restrita e OCR opcional",
        justificativa="Atende requisitos SHOULD sem violar política anti-alucinação",
        impacto="Artefatos complementares prontos para anexar ao relatório",
        alternativas_descartadas=[
            "IA generativa sem ancoragem em evidence_id",
            "PDF via captura de tela",
        ],
    )
