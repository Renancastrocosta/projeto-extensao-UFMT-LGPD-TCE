"""Interface de linha de comando do LGPD Auditor."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from lgpd_auditor import __version__
from lgpd_auditor.audit import AuditService, registrar_decisao_fase3
from lgpd_auditor.config import load_auditor_config
from lgpd_auditor.crawler import CrawlerService
from lgpd_auditor.evidence import EvidenceCaptureService, registrar_decisao_fase2
from lgpd_auditor.export_service import ExportService, registrar_decisao_fase5
from lgpd_auditor.finalize_service import FinalizeService
from lgpd_auditor.governance import EngineeringDiary
from lgpd_auditor.report import ReportGenerator, registrar_decisao_fase4


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lgpd-auditor",
        description="Auditor de conformidade LGPD para portais institucionais",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"lgpd-auditor {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser(
        "init",
        help="Inicializa diretórios e registra decisão de fundação no Diário de Engenharia",
    )
    init_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )

    run_parser = subparsers.add_parser(
        "run",
        help="Executa o crawler com checkpoints e log de rotas visitadas",
    )
    run_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )

    evidence_parser = subparsers.add_parser(
        "evidence",
        help="Captura screenshots e metadados das rotas visitadas",
    )
    evidence_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )
    evidence_parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limita quantidade de rotas a capturar (útil para testes)",
    )

    audit_parser = subparsers.add_parser(
        "audit",
        help="Executa auditoria LGPD heurística sobre as evidências coletadas",
    )
    audit_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )

    report_parser = subparsers.add_parser(
        "report",
        help="Gera relatório LGPD em Markdown, HTML e CSV de rotas",
    )
    report_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )

    export_parser = subparsers.add_parser(
        "export",
        help="Exporta PDF, dashboard HTML, síntese executiva e OCR opcional",
    )
    export_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )
    export_parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Não gera PDF",
    )
    export_parser.add_argument(
        "--no-dashboard",
        action="store_true",
        help="Não gera dashboard HTML",
    )
    export_parser.add_argument(
        "--no-synthesis",
        action="store_true",
        help="Não gera síntese executiva",
    )
    export_parser.add_argument(
        "--ocr",
        action="store_true",
        help="Executa OCR nos screenshots (requer tesseract)",
    )
    export_parser.add_argument(
        "--ocr-limit",
        type=int,
        default=None,
        help="Limita quantidade de screenshots para OCR",
    )

    finalize_parser = subparsers.add_parser(
        "finalize",
        help="Pipeline final: evidências → auditoria → relatório → export → validação",
    )
    finalize_parser.add_argument(
        "--config",
        default="config/tce-mt.yaml",
        help="Caminho para o arquivo de configuração YAML",
    )
    finalize_parser.add_argument(
        "--skip-evidence",
        action="store_true",
        help="Pula captura de evidências (usa existentes)",
    )

    return parser


def cmd_init(config_path: Path, project_root: Path) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)

    diary_path = auditor_config.resolve_path(
        auditor_config.paths.engineering_diary, project_root
    )
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="fase-0",
        problema="Projeto iniciado do zero sem código existente",
        solucao_adotada="Estrutura modular Python com Playwright, governança P0-P8 e legislation.yaml",
        justificativa="Atende requisitos MUST da especificação técnica e atividade acadêmica TCE-MT",
        impacto="Base para crawler, evidências, auditoria e relatório nas fases seguintes",
        alternativas_descartadas=[
            "Node.js/Puppeteer",
            "Auditoria manual sem automação",
        ],
    )

    print(f"Auditoria '{auditor_config.audit.id}' inicializada em {project_root}")
    print(f"Diário de Engenharia: {diary_path}")
    return 0


async def cmd_run_async(config_path: Path, project_root: Path) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)

    diary_path = auditor_config.resolve_path(
        auditor_config.paths.engineering_diary, project_root
    )
    diary = EngineeringDiary(diary_path)
    diary.register_decision(
        modulo="fase-1",
        problema="Necessidade de navegar o portal TCE-MT com retomada e rastreabilidade",
        solucao_adotada="CrawlerService BFS com Playwright, 5 workers, robots.txt e checkpoints",
        justificativa="Atende MUST de crawler, rotas visitadas e reprocessamento incremental",
        impacto="Base de URLs e HTML resumido para evidências (Fase 2) e auditoria LGPD (Fase 3)",
        alternativas_descartadas=[
            "httpx sem renderização JS",
            "Crawler sequencial sem workers",
        ],
    )

    print(f"Iniciando crawler — {auditor_config.audit.nome}")
    print(f"URL base: {auditor_config.audit.url_base}")
    print(f"Workers: {auditor_config.crawler.max_workers}")
    print(f"Máx. páginas: {auditor_config.crawler.max_paginas}")

    crawler = CrawlerService(auditor_config, project_root)
    resultado = await crawler.executar()

    print("\n--- Resumo do Crawler ---")
    print(f"Páginas visitadas: {resultado.paginas_visitadas}")
    print(f"Rotas registradas: {resultado.rotas_registradas}")
    print(f"URLs descobertas: {resultado.urls_descobertas}")
    print(f"Bloqueadas (robots.txt): {resultado.paginas_bloqueadas}")
    print(f"Erros: {resultado.paginas_com_erro}")

    if resultado.erros:
        print("\nPrimeiros erros:")
        for erro in resultado.erros[:5]:
            print(f"  - {erro}")

    visited_routes_path = auditor_config.resolve_path(
        auditor_config.paths.visited_routes, project_root
    )
    print(f"\nLog de rotas: {visited_routes_path}")
    return 0


def cmd_run(config_path: Path, project_root: Path) -> int:
    return asyncio.run(cmd_run_async(config_path, project_root))


async def cmd_evidence_async(
    config_path: Path, project_root: Path, limite: int | None
) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)
    registrar_decisao_fase2(auditor_config, project_root)

    print(f"Capturando evidências — {auditor_config.audit.nome}")
    print(f"Workers: {auditor_config.crawler.max_workers}")
    if limite:
        print(f"Limite: {limite} rotas")

    servico = EvidenceCaptureService(auditor_config, project_root)
    resultado = await servico.executar(limite=limite)

    print("\n--- Resumo da Captura de Evidências ---")
    print(f"Total de rotas: {resultado.total_rotas}")
    print(f"Já existentes: {resultado.ja_existentes}")
    print(f"Pendentes: {resultado.pendentes}")
    print(f"Capturadas agora: {resultado.capturadas}")
    print(f"Erros: {resultado.erros}")

    if resultado.mensagens_erro:
        print("\nPrimeiros erros:")
        for erro in resultado.mensagens_erro[:5]:
            print(f"  - {erro}")

    evidence_dir = auditor_config.resolve_path(
        auditor_config.paths.evidence, project_root
    )
    print(f"\nEvidências em: {evidence_dir}")
    return 0


def cmd_evidence(config_path: Path, project_root: Path, limite: int | None) -> int:
    return asyncio.run(cmd_evidence_async(config_path, project_root, limite))


def cmd_audit(config_path: Path, project_root: Path) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)
    registrar_decisao_fase3(auditor_config, project_root)

    print(f"Executando auditoria LGPD — {auditor_config.audit.nome}")

    servico = AuditService(auditor_config, project_root)
    resultado = servico.executar()

    print("\n--- Resumo da Auditoria LGPD ---")
    print(f"Páginas analisadas: {resultado.total_paginas_analisadas}")
    print(f"Total de achados: {len(resultado.achados)}")
    print("\nResumo por seção:")
    for secao_id, resumo in sorted(resultado.resumo_por_secao.items()):
        print(
            f"  {secao_id} {resumo.titulo}: "
            f"{resumo.status.value} | Confiança: {resumo.confianca.value} ({resumo.percentual}%) "
            f"| Evidências: {len(resumo.evidence_ids)}"
        )

    print(f"\nResultado salvo em: {servico.resultado_path}")
    return 0


def cmd_report(config_path: Path, project_root: Path) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)
    registrar_decisao_fase4(auditor_config, project_root)

    print(f"Gerando relatório LGPD — {auditor_config.audit.nome}")

    try:
        generator = ReportGenerator(auditor_config, project_root)
        paths = generator.gerar()
    except FileNotFoundError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1

    print("\n--- Relatório Gerado ---")
    print(f"Markdown: {paths.markdown}")
    print(f"HTML:     {paths.html}")
    print(f"CSV:      {paths.csv}")
    return 0


def cmd_export(
    config_path: Path,
    project_root: Path,
    gerar_pdf: bool,
    gerar_dashboard: bool,
    gerar_sintese: bool,
    executar_ocr: bool,
    ocr_limite: int | None,
) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)
    registrar_decisao_fase5(auditor_config, project_root)

    print(f"Exportando artefatos — {auditor_config.audit.nome}")

    try:
        servico = ExportService(auditor_config, project_root)
        resultado = servico.executar(
            gerar_pdf=gerar_pdf,
            gerar_dashboard=gerar_dashboard,
            gerar_sintese=gerar_sintese,
            executar_ocr=executar_ocr,
            ocr_limite=ocr_limite,
        )
    except FileNotFoundError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1

    print("\n--- Exportação Concluída ---")
    if resultado.pdf:
        print(f"PDF:       {resultado.pdf}")
    if resultado.dashboard:
        print(f"Dashboard: {resultado.dashboard}")
    if resultado.sintese:
        print(f"Síntese:   {resultado.sintese}")
    if resultado.ocr:
        print(
            f"OCR:       {resultado.ocr.sucessos}/{resultado.ocr.processados} sucesso(s)"
        )

    if resultado.avisos:
        print("\nAvisos:")
        for aviso in resultado.avisos:
            print(f"  - {aviso}")

    return 0


async def cmd_finalize_async(
    config_path: Path, project_root: Path, skip_evidence: bool
) -> int:
    auditor_config = load_auditor_config(config_path)
    auditor_config.ensure_directories(project_root)

    print(f"Pipeline final — {auditor_config.audit.nome}")
    print("Etapas: evidências → auditoria → relatório → export → validação")

    servico = FinalizeService(auditor_config, project_root)
    resultado = await servico.executar(capturar_evidencias=not skip_evidence)

    print("\n=== PIPELINE FINAL CONCLUÍDO ===")
    print(f"Rotas visitadas:        {resultado.rotas_total}")
    print(f"Evidências capturadas:  {resultado.evidencias_capturadas} (nesta sessão)")
    print(f"Achados de auditoria:   {resultado.achados_auditoria}")
    print(f"Relatório:              {resultado.relatorio_md}")

    print("\n--- Validação RNF ---")
    for verificacao in resultado.validacao_rnf.get("verificacoes", []):
        status = "OK" if verificacao["aprovado"] else "FALHA"
        print(f"  [{status}] {verificacao['nome']}: {verificacao['valor_obtido']}")

    print("\n--- Checklist MUST ---")
    must = resultado.checklist_must
    print(f"  Cobertura: {must.get('cobertura_percentual', 0):.0f}%")
    for item in must.get("itens", []):
        status = "OK" if item["aprovado"] else "FALHA"
        print(f"  [{status}] {item['requisito']}: {item['evidencia']}")

    if resultado.avisos:
        print("\nAvisos:")
        for aviso in resultado.avisos:
            print(f"  - {aviso}")

    validation_path = auditor_config.resolve_path(
        f"{auditor_config.paths.audit_dir}/validation_report.json", project_root
    )
    print(f"\nValidação salva em: {validation_path}")

    aprovado = (
        resultado.validacao_rnf.get("aprovado_geral", False)
        and resultado.checklist_must.get("aprovado", False)
    )
    if aprovado:
        print("\nEntrega APROVADA para submissão acadêmica.")
    else:
        print("\nEntrega PARCIAL — complete captura de evidências e reexecute 'finalize'.")

    return 0 if aprovado else 2


def cmd_finalize(config_path: Path, project_root: Path, skip_evidence: bool) -> int:
    return asyncio.run(cmd_finalize_async(config_path, project_root, skip_evidence))


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    project_root = Path.cwd()

    if args.command == "init":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_init(config_path, project_root)

    if args.command == "run":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_run(config_path, project_root)

    if args.command == "evidence":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_evidence(config_path, project_root, args.limit)

    if args.command == "audit":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_audit(config_path, project_root)

    if args.command == "report":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_report(config_path, project_root)

    if args.command == "export":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_export(
            config_path,
            project_root,
            gerar_pdf=not args.no_pdf,
            gerar_dashboard=not args.no_dashboard,
            gerar_sintese=not args.no_synthesis,
            executar_ocr=args.ocr,
            ocr_limite=args.ocr_limit,
        )

    if args.command == "finalize":
        config_path = project_root / args.config
        if not config_path.exists():
            print(f"Erro: configuração não encontrada: {config_path}", file=sys.stderr)
            return 1
        return cmd_finalize(config_path, project_root, skip_evidence=args.skip_evidence)

    if args.command is None:
        parser.print_help()
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

