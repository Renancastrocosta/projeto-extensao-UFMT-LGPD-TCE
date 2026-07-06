"""Exportação de rotas visitadas para CSV."""

from __future__ import annotations

import csv
from pathlib import Path

from lgpd_auditor.crawler.visited_routes import VisitedRoutesLog


def exportar_rotas_csv(routes_log: VisitedRoutesLog, csv_path: Path) -> Path:
    """Exporta rotas visitadas para CSV anexável ao relatório acadêmico."""
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "ordem",
                "url",
                "status_http",
                "evidence_id",
                "screenshot",
                "visitada_em",
                "origem",
                "content_hash",
            ],
        )
        writer.writeheader()
        for rota in routes_log.rotas:
            writer.writerow({
                "ordem": rota.ordem,
                "url": rota.url,
                "status_http": rota.status_http or "",
                "evidence_id": rota.evidence_id,
                "screenshot": rota.screenshot or "",
                "visitada_em": rota.visitada_em,
                "origem": rota.origem,
                "content_hash": rota.content_hash or "",
            })

    return csv_path
