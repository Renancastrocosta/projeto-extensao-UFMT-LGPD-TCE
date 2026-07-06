"""Carregamento de configurações YAML da auditoria."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field, HttpUrl


class AuditConfig(BaseModel):
    id: str
    nome: str
    url_base: HttpUrl
    dominio_permitido: str


class CrawlerConfig(BaseModel):
    max_workers: int = 5
    max_paginas: int = 500
    max_paginas_escalavel: int = 20000
    rate_limit_segundos: float = 0.5
    timeout_segundos: int = 30
    respeitar_robots_txt: bool = True
    user_agent: str = "LGPD-Auditor/0.1.0"


class PerformanceConfig(BaseModel):
    tempo_maximo_minutos: int = 15
    memoria_maxima_mb: int = 2048


class PathsConfig(BaseModel):
    audit_dir: str
    checkpoints: str
    evidence: str
    visited_routes: str
    reports: str
    engineering_diary: str


class AuditorConfig(BaseModel):
    audit: AuditConfig
    crawler: CrawlerConfig = Field(default_factory=CrawlerConfig)
    performance: PerformanceConfig = Field(default_factory=PerformanceConfig)
    paths: PathsConfig
    legislation: str = "legislation.yaml"

    def resolve_path(self, relative_path: str, base_dir: Path) -> Path:
        return (base_dir / relative_path).resolve()

    def ensure_directories(self, base_dir: Path) -> None:
        for path_attr in (
            self.paths.audit_dir,
            self.paths.checkpoints,
            self.paths.evidence,
            self.paths.reports,
        ):
            self.resolve_path(path_attr, base_dir).mkdir(parents=True, exist_ok=True)


def load_yaml_file(file_path: Path) -> dict[str, Any]:
    with file_path.open("r", encoding="utf-8") as yaml_file:
        content = yaml.safe_load(yaml_file)
    if not isinstance(content, dict):
        raise ValueError(f"Arquivo YAML inválido: {file_path}")
    return content


def load_auditor_config(config_path: Path) -> AuditorConfig:
    raw_config = load_yaml_file(config_path)
    return AuditorConfig.model_validate(raw_config)


def load_legislation(legislation_path: Path) -> dict[str, Any]:
    return load_yaml_file(legislation_path)
