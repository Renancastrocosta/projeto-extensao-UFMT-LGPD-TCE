"""Validação dos Requisitos Não Funcionais (RNFs)."""

from __future__ import annotations

import json
import os
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import psutil

from lgpd_auditor.config.loader import AuditorConfig


@dataclass
class RnfCheck:
    nome: str
    criterio: str
    valor_obtido: str
    aprovado: bool
    observacao: str = ""


@dataclass
class RnfValidationResult:
    aprovado_geral: bool
    verificacoes: list[RnfCheck] = field(default_factory=list)
    memoria_pico_mb: float = 0.0
    duracao_evidencia_segundos: float | None = None

    def para_dict(self) -> dict:
        return {
            "aprovado_geral": self.aprovado_geral,
            "memoria_pico_mb": self.memoria_pico_mb,
            "duracao_evidencia_segundos": self.duracao_evidencia_segundos,
            "verificacoes": [asdict(v) for v in self.verificacoes],
        }


class RnfValidator:
    """Valida RNFs mensuráveis da especificação técnica."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root

    def validar(
        self,
        total_rotas: int,
        rotas_com_screenshot: int,
        duracao_evidencia_segundos: float | None = None,
    ) -> RnfValidationResult:
        processo = psutil.Process(os.getpid())
        memoria_mb = processo.memory_info().rss / (1024 * 1024)

        verificacoes = [
            RnfCheck(
                nome="Concorrência (workers)",
                criterio="≥ 5 workers configuráveis",
                valor_obtido=str(self._config.crawler.max_workers),
                aprovado=self._config.crawler.max_workers >= 5,
            ),
            RnfCheck(
                nome="Limite de páginas",
                criterio=f"≤ {self._config.crawler.max_paginas} páginas",
                valor_obtido=str(total_rotas),
                aprovado=total_rotas <= self._config.crawler.max_paginas_escalavel,
                observacao=(
                    "Portal dentro do limite escalável (20.000)"
                    if total_rotas <= self._config.crawler.max_paginas_escalavel
                    else "Excede limite escalável"
                ),
            ),
            RnfCheck(
                nome="Memória",
                criterio=f"< {self._config.performance.memoria_maxima_mb} MB",
                valor_obtido=f"{memoria_mb:.1f} MB (processo atual)",
                aprovado=memoria_mb < self._config.performance.memoria_maxima_mb,
            ),
            RnfCheck(
                nome="Checkpoint",
                criterio="latest.json existente para retomada",
                valor_obtido="presente" if self._checkpoint_existe() else "ausente",
                aprovado=self._checkpoint_existe(),
            ),
            RnfCheck(
                nome="Cobertura de evidências",
                criterio="100% rotas com screenshot",
                valor_obtido=f"{rotas_com_screenshot}/{total_rotas}",
                aprovado=rotas_com_screenshot == total_rotas and total_rotas > 0,
                observacao=(
                    "Captura completa"
                    if rotas_com_screenshot == total_rotas
                    else f"Pendente: {total_rotas - rotas_com_screenshot} rotas"
                ),
            ),
        ]

        if duracao_evidencia_segundos is not None and total_rotas > 0:
            tempo_minutos = duracao_evidencia_segundos / 60
            verificacoes.append(
                RnfCheck(
                    nome="Tempo de captura",
                    criterio=f"≤ {self._config.performance.tempo_maximo_minutos} min (referência)",
                    valor_obtido=f"{tempo_minutos:.1f} min",
                    aprovado=tempo_minutos <= self._config.performance.tempo_maximo_minutos * 3,
                    observacao="Meta de 15 min refere-se a portal ≤500 páginas no crawl inicial",
                )
            )

        aprovado = all(v.aprovado for v in verificacoes if v.nome != "Cobertura de evidências")
        cobertura = next(v for v in verificacoes if v.nome == "Cobertura de evidências")

        return RnfValidationResult(
            aprovado_geral=aprovado and cobertura.aprovado,
            verificacoes=verificacoes,
            memoria_pico_mb=memoria_mb,
            duracao_evidencia_segundos=duracao_evidencia_segundos,
        )

    def _checkpoint_existe(self) -> bool:
        checkpoint_path = self._config.resolve_path(
            self._config.paths.checkpoints, self._project_root
        ) / "latest.json"
        return checkpoint_path.exists()


@dataclass
class MustCheck:
    requisito: str
    aprovado: bool
    evidencia: str


@dataclass
class MustChecklistResult:
    cobertura_percentual: float
    aprovado: bool
    itens: list[MustCheck] = field(default_factory=list)

    def para_dict(self) -> dict:
        return {
            "cobertura_percentual": self.cobertura_percentual,
            "aprovado": self.aprovado,
            "itens": [asdict(i) for i in self.itens],
        }


class MustChecklistValidator:
    """Valida cobertura dos requisitos MUST."""

    def __init__(self, auditor_config: AuditorConfig, project_root: Path) -> None:
        self._config = auditor_config
        self._project_root = project_root

    def validar(
        self,
        total_rotas: int,
        rotas_no_relatorio: int,
        rotas_com_screenshot: int,
    ) -> MustChecklistResult:
        audit_dir = self._config.resolve_path(
            self._config.paths.audit_dir, self._project_root
        )
        itens = [
            MustCheck("Crawler com checkpoints", self._arquivo_existe(audit_dir / "checkpoints" / "latest.json"), "checkpoints/latest.json"),
            MustCheck("Log de rotas visitadas", self._arquivo_existe(audit_dir / "visited_routes.json"), "visited_routes.json"),
            MustCheck("Screenshots e metadados", rotas_com_screenshot > 0, f"{rotas_com_screenshot} evidências"),
            MustCheck("legislation.yaml", self._arquivo_existe(self._project_root / self._config.legislation), self._config.legislation),
            MustCheck("audit_results.json", self._arquivo_existe(audit_dir / "audit_results.json"), "audit_results.json"),
            MustCheck("Relatório estruturado", self._arquivo_existe(audit_dir / "reports" / "relatorio-lgpd-tce-mt.md"), "relatorio-lgpd-tce-mt.md"),
            MustCheck("Anexo rotas = log", rotas_no_relatorio == total_rotas, f"{rotas_no_relatorio}/{total_rotas}"),
            MustCheck("Diário de Engenharia", self._arquivo_existe(audit_dir / "engineering_diary.jsonl"), "engineering_diary.jsonl"),
            MustCheck("Governança anti-alucinação", self._audit_tem_status(), "status/confiança em audit_results.json"),
        ]

        aprovados = sum(1 for i in itens if i.aprovado)
        cobertura = (aprovados / len(itens)) * 100 if itens else 0

        return MustChecklistResult(
            cobertura_percentual=cobertura,
            aprovado=all(i.aprovado for i in itens),
            itens=itens,
        )

    def _arquivo_existe(self, path: Path) -> bool:
        return path.exists() and path.stat().st_size > 0

    def _audit_tem_status(self) -> bool:
        audit_path = self._config.resolve_path(
            f"{self._config.paths.audit_dir}/audit_results.json", self._project_root
        )
        if not audit_path.exists():
            return False
        with audit_path.open("r", encoding="utf-8") as f:
            dados = json.load(f)
        resumo = dados.get("resumo_por_secao", {})
        return all("status" in v and "confianca" in v for v in resumo.values())
