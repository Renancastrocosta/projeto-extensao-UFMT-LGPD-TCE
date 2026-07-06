"""Utilitários de normalização e extração de URLs."""

from __future__ import annotations

import hashlib
import re
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse

from bs4 import BeautifulSoup

IGNORAR_EXTENSOES = {
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip", ".rar",
    ".jpg", ".jpeg", ".png", ".gif", ".svg", ".mp4", ".mp3",
    ".xml", ".json", ".css", ".js",
}


def normalize_url(url: str, base_url: str | None = None) -> str | None:
    """Normaliza URL removendo fragmentos e parâmetros de rastreamento comuns."""
    if not url or url.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None

    url_completa = urljoin(base_url, url) if base_url else url
    url_sem_fragmento, _ = urldefrag(url_completa)

    parsed = urlparse(url_sem_fragmento)
    if parsed.scheme not in ("http", "https"):
        return None

    caminho = parsed.path or "/"
    if caminho != "/" and caminho.endswith("/"):
        caminho = caminho.rstrip("/")

    return urlunparse((parsed.scheme, parsed.netloc.lower(), caminho, "", parsed.query, ""))


def pertence_ao_dominio(url: str, dominio_permitido: str) -> bool:
    """Verifica se a URL pertence ao domínio permitido (inclui subdomínios)."""
    hostname = urlparse(url).netloc.lower()
    dominio = dominio_permitido.lower()
    return hostname == dominio or hostname.endswith(f".{dominio}")


def deve_ignorar_url(url: str) -> bool:
    """Ignora recursos estáticos e URLs não HTML."""
    caminho = urlparse(url).path.lower()
    return any(caminho.endswith(extensao) for extensao in IGNORAR_EXTENSOES)


def calcular_hash_conteudo(conteudo: str) -> str:
    return hashlib.sha256(conteudo.encode("utf-8")).hexdigest()


def extrair_links(html: str, url_base: str, dominio_permitido: str) -> list[str]:
    """Extrai links internos válidos a partir do HTML da página."""
    soup = BeautifulSoup(html, "html.parser")
    links_encontrados: list[str] = []

    for tag_anchor in soup.find_all("a", href=True):
        href = tag_anchor.get("href", "").strip()
        url_normalizada = normalize_url(href, url_base)
        if not url_normalizada:
            continue
        if not pertence_ao_dominio(url_normalizada, dominio_permitido):
            continue
        if deve_ignorar_url(url_normalizada):
            continue
        links_encontrados.append(url_normalizada)

    return list(dict.fromkeys(links_encontrados))


def resumir_html(html: str, limite_caracteres: int = 5000) -> str:
    """Gera resumo textual do HTML para armazenamento leve."""
    texto = BeautifulSoup(html, "html.parser").get_text(separator=" ", strip=True)
    texto = re.sub(r"\s+", " ", texto)
    return texto[:limite_caracteres]
