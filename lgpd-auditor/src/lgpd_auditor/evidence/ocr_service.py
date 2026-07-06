"""OCR opcional para extração de texto em screenshots."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class OcrResult:
    evidence_id: str
    texto_extraido: str
    sucesso: bool
    erro: str | None = None


@dataclass
class OcrBatchResult:
    processados: int = 0
    sucessos: int = 0
    erros: int = 0
    resultados: list[OcrResult] = field(default_factory=list)


class OcrService:
    """Extrai texto de screenshots via Tesseract (opcional)."""

    def __init__(self, evidence_dir: Path) -> None:
        self._evidence_dir = evidence_dir

    def _importar_pytesseract(self):
        try:
            import pytesseract
            from PIL import Image
        except ImportError as exc:
            raise RuntimeError(
                "OCR requer dependências opcionais: pip install -e '.[ocr]' "
                "e binário tesseract instalado no sistema."
            ) from exc
        return pytesseract, Image

    def processar_evidencia(self, evidence_id: str) -> OcrResult:
        screenshot_path = self._evidence_dir / evidence_id / "screenshot.png"
        ocr_path = self._evidence_dir / evidence_id / "ocr_text.txt"

        if not screenshot_path.exists():
            return OcrResult(
                evidence_id=evidence_id,
                texto_extraido="",
                sucesso=False,
                erro="Screenshot não encontrado.",
            )

        if ocr_path.exists():
            return OcrResult(
                evidence_id=evidence_id,
                texto_extraido=ocr_path.read_text(encoding="utf-8"),
                sucesso=True,
            )

        try:
            pytesseract, Image = self._importar_pytesseract()
            imagem = Image.open(screenshot_path)
            texto = pytesseract.image_to_string(imagem, lang="por+eng")
            ocr_path.write_text(texto.strip(), encoding="utf-8")
            return OcrResult(
                evidence_id=evidence_id,
                texto_extraido=texto.strip(),
                sucesso=True,
            )
        except Exception as exc:
            return OcrResult(
                evidence_id=evidence_id,
                texto_extraido="",
                sucesso=False,
                erro=str(exc),
            )

    def processar_todas(self, limite: int | None = None) -> OcrBatchResult:
        resultado = OcrBatchResult()
        diretorios = sorted(
            d for d in self._evidence_dir.iterdir()
            if d.is_dir() and (d / "screenshot.png").exists()
        )

        if limite is not None:
            diretorios = diretorios[:limite]

        for diretorio in diretorios:
            resultado.processados += 1
            ocr_result = self.processar_evidencia(diretorio.name)
            resultado.resultados.append(ocr_result)
            if ocr_result.sucesso:
                resultado.sucessos += 1
            else:
                resultado.erros += 1

        return resultado
