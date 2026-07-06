"""Log append-only de rotas visitadas como evidência de cobertura."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class VisitedRoute:
    ordem: int
    url: str
    status_http: int | None
    visitada_em: str
    evidence_id: str
    screenshot: str | None = None
    origem: str = "crawl"
    content_hash: str | None = None

    @classmethod
    def criar(
        cls,
        ordem: int,
        url: str,
        status_http: int | None,
        origem: str = "crawl",
        content_hash: str | None = None,
        screenshot: str | None = None,
    ) -> "VisitedRoute":
        return cls(
            ordem=ordem,
            url=url,
            status_http=status_http,
            visitada_em=datetime.now(timezone.utc).isoformat(),
            evidence_id=f"ev-{ordem:03d}",
            screenshot=screenshot,
            origem=origem,
            content_hash=content_hash,
        )


class VisitedRoutesLog:
    """Persistência do log de rotas visitadas em JSON."""

    def __init__(self, log_path: Path, audit_id: str) -> None:
        self._log_path = log_path
        self._log_path.parent.mkdir(parents=True, exist_ok=True)
        self._audit_id = audit_id
        self._dados = self._carregar_ou_criar()

    @property
    def path(self) -> Path:
        return self._log_path

    @property
    def rotas(self) -> list[VisitedRoute]:
        return [
            VisitedRoute(**registro)
            for registro in self._dados.get("rotas", [])
        ]

    def _carregar_ou_criar(self) -> dict[str, Any]:
        if not self._log_path.exists():
            return {"audit_id": self._audit_id, "total_rotas": 0, "rotas": []}

        with self._log_path.open("r", encoding="utf-8") as log_file:
            return json.load(log_file)

    def _salvar(self) -> None:
        self._dados["total_rotas"] = len(self._dados["rotas"])
        with self._log_path.open("w", encoding="utf-8") as log_file:
            json.dump(self._dados, log_file, ensure_ascii=False, indent=2)

    def url_ja_registrada(self, url: str) -> bool:
        return any(registro["url"] == url for registro in self._dados["rotas"])

    def registrar(self, rota: VisitedRoute) -> VisitedRoute:
        if self.url_ja_registrada(rota.url):
            return rota

        self._dados["rotas"].append(asdict(rota))
        self._salvar()
        return rota

    def proxima_ordem(self) -> int:
        return len(self._dados["rotas"]) + 1

    def atualizar_screenshot(self, evidence_id: str, screenshot_path: str) -> bool:
        for registro in self._dados["rotas"]:
            if registro["evidence_id"] == evidence_id:
                registro["screenshot"] = screenshot_path
                self._salvar()
                return True
        return False

    def rotas_sem_screenshot(self) -> list[VisitedRoute]:
        return [
            VisitedRoute(**registro)
            for registro in self._dados["rotas"]
            if not registro.get("screenshot")
        ]
