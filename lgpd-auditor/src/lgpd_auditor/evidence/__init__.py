"""Módulo de evidências."""

from lgpd_auditor.evidence.capture_service import (
    EvidenceCaptureResult,
    EvidenceCaptureService,
    registrar_decisao_fase2,
)
from lgpd_auditor.evidence.models import EvidenceMetadata
from lgpd_auditor.evidence.store import EvidenceStore

__all__ = [
    "EvidenceCaptureResult",
    "EvidenceCaptureService",
    "EvidenceMetadata",
    "EvidenceStore",
    "registrar_decisao_fase2",
]
