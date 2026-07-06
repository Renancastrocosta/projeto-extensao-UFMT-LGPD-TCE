"""Verificação de permissões via robots.txt."""

from __future__ import annotations

from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import httpx


class RobotsChecker:
    """Consulta robots.txt e valida permissão de acesso por URL."""

    def __init__(self, user_agent: str, timeout_segundos: int = 30) -> None:
        self._user_agent = user_agent
        self._timeout = timeout_segundos
        self._parsers_por_dominio: dict[str, RobotFileParser] = {}
        self._urls_bloqueadas: set[str] = set()

    @property
    def urls_bloqueadas(self) -> set[str]:
        return set(self._urls_bloqueadas)

    def _obter_parser(self, url: str) -> RobotFileParser:
        parsed = urlparse(url)
        dominio_chave = parsed.netloc.lower()

        if dominio_chave not in self._parsers_por_dominio:
            robots_url = urljoin(f"{parsed.scheme}://{parsed.netloc}", "/robots.txt")
            parser = RobotFileParser()
            parser.set_url(robots_url)

            try:
                with httpx.Client(timeout=self._timeout) as client:
                    resposta = client.get(robots_url, headers={"User-Agent": self._user_agent})
                    if resposta.status_code == 200:
                        parser.parse(resposta.text.splitlines())
                    else:
                        parser.parse([])
            except httpx.HTTPError:
                parser.parse([])

            self._parsers_por_dominio[dominio_chave] = parser

        return self._parsers_por_dominio[dominio_chave]

    def pode_acessar(self, url: str) -> bool:
        parser = self._obter_parser(url)
        permitido = parser.can_fetch(self._user_agent, url)
        if not permitido:
            self._urls_bloqueadas.add(url)
        return permitido
