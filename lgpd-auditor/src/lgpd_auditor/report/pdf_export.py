"""Exportação do relatório HTML para PDF."""

from __future__ import annotations

from pathlib import Path


def exportar_pdf(html_path: Path, pdf_path: Path) -> Path:
    """Converte relatório HTML em PDF via WeasyPrint."""
    if not html_path.exists():
        raise FileNotFoundError(f"HTML não encontrado: {html_path}")

    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise RuntimeError(
            "PDF requer dependência opcional: pip install -e '.[pdf]'"
        ) from exc

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))
    return pdf_path
