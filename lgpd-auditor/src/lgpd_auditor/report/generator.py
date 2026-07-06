"""Gerador de relatório LGPD em Markdown e HTML."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from lgpd_auditor import __version__
from lgpd_auditor.checkpoint.manager import CheckpointManager
from lgpd_auditor.config.loader import AuditorConfig
from lgpd_auditor.crawler.visited_routes import VisitedRoutesLog
from lgpd_auditor.governance import EngineeringDiary
from lgpd_auditor.report.routes_export import exportar_rotas_csv


@dataclass
class ReportPaths:
    markdown: Path
    html: Path
    csv: Path


class ReportGenerator:
    """Gera relatório estruturado a partir de audit_results.json e visited_routes.json."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root

        self._reports_dir = auditor_config.resolve_path(
            auditor_config.paths.reports, project_root
        )
        self._audit_results_path = auditor_config.resolve_path(
            f"{auditor_config.paths.audit_dir}/audit_results.json", project_root
        )
        self._visited_routes_path = auditor_config.resolve_path(
            auditor_config.paths.visited_routes, project_root
        )
        self._checkpoints_dir = auditor_config.resolve_path(
            auditor_config.paths.checkpoints, project_root
        )
        self._diary_path = auditor_config.resolve_path(
            auditor_config.paths.engineering_diary, project_root
        )
        self._templates_dir = project_root / "templates" / "report"

    def gerar(self) -> ReportPaths:
        if not self._audit_results_path.exists():
            raise FileNotFoundError(
                f"Resultado de auditoria não encontrado: {self._audit_results_path}. "
                "Execute 'lgpd-auditor audit' primeiro."
            )

        audit_data = self._carregar_json(self._audit_results_path)
        routes_log = VisitedRoutesLog(self._visited_routes_path, self._config.audit.id)
        checkpoint = CheckpointManager(self._checkpoints_dir, self._config.audit.id)
        diary = EngineeringDiary(self._diary_path)

        contexto = self._montar_contexto(audit_data, routes_log, checkpoint, diary)

        self._reports_dir.mkdir(parents=True, exist_ok=True)
        markdown_path = self._reports_dir / "relatorio-lgpd-tce-mt.md"
        html_path = self._reports_dir / "relatorio-lgpd-tce-mt.html"
        csv_path = self._reports_dir / "visited_routes.csv"

        env = Environment(
            loader=FileSystemLoader(str(self._templates_dir)),
            autoescape=select_autoescape(["html"]),
        )

        template_md = env.get_template("relatorio.md.j2")
        markdown_path.write_text(
            template_md.render(**contexto), encoding="utf-8"
        )

        contexto_html = {
            **contexto,
            "diario_engenharia_html": self._markdown_para_html_basico(
                contexto["diario_engenharia"]
            ),
        }
        template_html = env.get_template("relatorio.html.j2")
        html_path.write_text(
            template_html.render(**contexto_html), encoding="utf-8"
        )

        exportar_rotas_csv(routes_log, csv_path)

        return ReportPaths(markdown=markdown_path, html=html_path, csv=csv_path)

    def _carregar_json(self, path: Path) -> dict:
        with path.open("r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def _montar_contexto(
        self,
        audit_data: dict,
        routes_log: VisitedRoutesLog,
        checkpoint: CheckpointManager,
        diary: EngineeringDiary,
    ) -> dict:
        rotas = [asdict(rota) for rota in routes_log.rotas]

        resumo_por_secao = audit_data.get("resumo_por_secao", {})
        secoes_ordenadas = sorted(resumo_por_secao.items(), key=lambda x: x[0])

        achados = audit_data.get("achados", [])
        achados_por_secao: dict[str, list] = {}
        for achado in achados:
            secao = achado.get("secao_id", "")
            achados_por_secao.setdefault(secao, []).append(achado)

        contagem_checkpoint = checkpoint.contar_por_status()
        rotas_com_erro_http = sum(
            1 for rota in routes_log.rotas
            if rota.status_http and rota.status_http >= 400
        )

        return {
            "audit_id": audit_data.get("audit_id", self._config.audit.id),
            "portal_nome": self._config.audit.nome,
            "url_base": str(self._config.audit.url_base),
            "dominio": self._config.audit.dominio_permitido,
            "gerado_em": audit_data.get("gerado_em", ""),
            "versao_ferramenta": __version__,
            "max_workers": self._config.crawler.max_workers,
            "rate_limit": self._config.crawler.rate_limit_segundos,
            "total_rotas": len(rotas),
            "rotas_com_screenshot": sum(1 for r in routes_log.rotas if r.screenshot),
            "rotas_com_erro_http": rotas_com_erro_http,
            "rotas_bloqueadas": contagem_checkpoint.get("blocked", 0),
            "total_paginas_analisadas": audit_data.get("total_paginas_analisadas", 0),
            "total_achados": len(achados),
            "secoes_ordenadas": secoes_ordenadas,
            "achados_por_secao": achados_por_secao,
            "recomendacoes": self._gerar_recomendacoes(resumo_por_secao),
            "rotas": rotas,
            "diario_engenharia": diary.to_markdown_section(),
        }

    def _gerar_recomendacoes(self, resumo_por_secao: dict) -> list[str]:
        recomendacoes: list[str] = []

        mapeamento = {
            "4.1": "Publicar e destacar política de privacidade acessível no rodapé e menu principal.",
            "4.2": "Documentar finalidade e base legal em todos os formulários de coleta de dados pessoais.",
            "4.3": "Implementar mecanismos de consentimento explícito (opt-in) onde aplicável.",
            "4.4": "Disponibilizar canal visível para exercício de direitos do titular e contato do encarregado.",
            "4.5": "Garantir HTTPS em todas as páginas e revisar configurações de segurança.",
            "4.6": "Implementar banner de cookies com opção de consentimento granular.",
        }

        for secao_id, texto in mapeamento.items():
            resumo = resumo_por_secao.get(secao_id, {})
            status = resumo.get("status", "")
            if status in ("Não Localizado", "Inferência", "Hipótese"):
                recomendacoes.append(f"[{secao_id}] {texto}")

        if not recomendacoes:
            recomendacoes.append(
                "Manter monitoramento contínuo de conformidade e revisão periódica das políticas."
            )

        return recomendacoes

    @staticmethod
    def _markdown_para_html_basico(markdown: str) -> str:
        html = markdown
        html = re.sub(r"^### (.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
        html = re.sub(r"^## (.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
        html = re.sub(r"^- \*\*(.+?)\*\*: (.+)$", r"<p><strong>\1:</strong> \2</p>", html, flags=re.MULTILINE)
        html = re.sub(r"\n\n", "<br><br>", html)
        return f"<section>{html}</section>"


def registrar_decisao_fase4(
    auditor_config: AuditorConfig, project_root: Path
) -> None:
    diary_path = auditor_config.resolve_path(
        auditor_config.paths.engineering_diary, project_root
    )
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="fase-4",
        problema="Necessidade de relatório estruturado para entrega acadêmica",
        solucao_adotada="ReportGenerator com templates Jinja2, Markdown, HTML e CSV de rotas",
        justificativa="Atende MUST de relatório, anexo de rotas e Diário de Engenharia",
        impacto="relatorio-lgpd-tce-mt.md pronto para revisão e entrega no AVA",
        alternativas_descartadas=[
            "Relatório manual sem reprodutibilidade",
            "Apenas JSON sem formato legível",
        ],
    )
