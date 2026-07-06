"""Modelos de evidência auditável."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class EvidenceMetadata:
    evidence_id: str
    url: str
    captured_at: str
    status_http: int | None
    content_hash: str
    screenshot_hash: str
    screenshot_path: str
    html_summary_path: str
    page_title: str = ""
    audit_id: str = ""

    @classmethod
    def criar(
        cls,
        evidence_id: str,
        url: str,
        status_http: int | None,
        content_hash: str,
        screenshot_hash: str,
        screenshot_path: str,
        html_summary_path: str,
        page_title: str = "",
        audit_id: str = "",
    ) -> "EvidenceMetadata":
        return cls(
            evidence_id=evidence_id,
            url=url,
            captured_at=datetime.now(timezone.utc).isoformat(),
            status_http=status_http,
            content_hash=content_hash,
            screenshot_hash=screenshot_hash,
            screenshot_path=screenshot_path,
            html_summary_path=html_summary_path,
            page_title=page_title,
            audit_id=audit_id,
        )

    def para_dict(self) -> dict[str, Any]:
        return asdict(self)
