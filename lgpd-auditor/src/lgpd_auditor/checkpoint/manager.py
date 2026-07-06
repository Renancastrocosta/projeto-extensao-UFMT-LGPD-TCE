"""Gerenciamento de checkpoints para retomada de auditoria."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any


class UrlStatus(str, Enum):
    PENDING = "pending"
    DONE = "done"
    ERROR = "error"
    BLOCKED = "blocked"


@dataclass
class UrlCheckpoint:
    url: str
    status: UrlStatus
    content_hash: str | None = None
    timestamp: str = ""
    status_http: int | None = None
    origem: str = "crawl"
    erro: str | None = None

    def __post_init__(self) -> None:
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()


@dataclass
class CheckpointState:
    audit_id: str
    updated_at: str = ""
    urls: dict[str, UrlCheckpoint] = field(default_factory=dict)
    fila_pendente: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.updated_at:
            self.updated_at = datetime.now(timezone.utc).isoformat()


class CheckpointManager:
    """Persiste estado da auditoria para reprocessamento incremental."""

    def __init__(self, checkpoints_dir: Path, audit_id: str) -> None:
        self._checkpoints_dir = checkpoints_dir
        self._checkpoints_dir.mkdir(parents=True, exist_ok=True)
        self._latest_path = checkpoints_dir / "latest.json"
        self._audit_id = audit_id
        self._state = self._carregar_ou_criar()

    @property
    def state(self) -> CheckpointState:
        return self._state

    @property
    def latest_path(self) -> Path:
        return self._latest_path

    def _carregar_ou_criar(self) -> CheckpointState:
        if not self._latest_path.exists():
            return CheckpointState(audit_id=self._audit_id)

        with self._latest_path.open("r", encoding="utf-8") as checkpoint_file:
            dados = json.load(checkpoint_file)

        urls: dict[str, UrlCheckpoint] = {}
        for url, registro in dados.get("urls", {}).items():
            urls[url] = UrlCheckpoint(
                url=url,
                status=UrlStatus(registro["status"]),
                content_hash=registro.get("content_hash"),
                timestamp=registro.get("timestamp", ""),
                status_http=registro.get("status_http"),
                origem=registro.get("origem", "crawl"),
                erro=registro.get("erro"),
            )

        return CheckpointState(
            audit_id=dados.get("audit_id", self._audit_id),
            updated_at=dados.get("updated_at", ""),
            urls=urls,
            fila_pendente=dados.get("fila_pendente", []),
        )

    def salvar(self) -> None:
        self._state.updated_at = datetime.now(timezone.utc).isoformat()
        dados: dict[str, Any] = {
            "audit_id": self._state.audit_id,
            "updated_at": self._state.updated_at,
            "urls": {
                url: {
                    **asdict(checkpoint),
                    "status": checkpoint.status.value,
                }
                for url, checkpoint in self._state.urls.items()
            },
            "fila_pendente": self._state.fila_pendente,
        }
        with self._latest_path.open("w", encoding="utf-8") as checkpoint_file:
            json.dump(dados, checkpoint_file, ensure_ascii=False, indent=2)

    def ja_processada(self, url: str) -> bool:
        registro = self._state.urls.get(url)
        return registro is not None and registro.status == UrlStatus.DONE

    def registrar(
        self,
        url: str,
        status: UrlStatus,
        content_hash: str | None = None,
        status_http: int | None = None,
        origem: str = "crawl",
        erro: str | None = None,
    ) -> UrlCheckpoint:
        checkpoint = UrlCheckpoint(
            url=url,
            status=status,
            content_hash=content_hash,
            status_http=status_http,
            origem=origem,
            erro=erro,
        )
        self._state.urls[url] = checkpoint
        self.salvar()
        return checkpoint

    def atualizar_fila(self, fila: list[str]) -> None:
        self._state.fila_pendente = fila
        self.salvar()

    def contar_por_status(self) -> dict[str, int]:
        contagem: dict[str, int] = {}
        for checkpoint in self._state.urls.values():
            chave = checkpoint.status.value
            contagem[chave] = contagem.get(chave, 0) + 1
        return contagem
