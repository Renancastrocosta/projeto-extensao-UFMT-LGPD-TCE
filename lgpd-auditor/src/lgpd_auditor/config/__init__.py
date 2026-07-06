"""Módulo de configuração."""

from lgpd_auditor.config.loader import (
    AuditorConfig,
    load_auditor_config,
    load_legislation,
    load_yaml_file,
)

__all__ = [
    "AuditorConfig",
    "load_auditor_config",
    "load_legislation",
    "load_yaml_file",
]
