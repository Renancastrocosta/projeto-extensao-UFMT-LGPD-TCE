"""Classificadores heurísticos para auditoria LGPD."""

from __future__ import annotations

import re
from dataclasses import dataclass

from lgpd_auditor.audit.models import AuditFinding, ConformityRule
from lgpd_auditor.governance.enums import ConfidenceLevel, EvidenceStatus


@dataclass
class PageContext:
    evidence_id: str
    url: str
    texto: str
    page_title: str


class HeuristicClassifier:
    """Aplica heurísticas por seção LGPD sobre o conteúdo de uma página."""

    PRIVACIDADE_LINK = re.compile(
        r"(pol[ií]tica\s+de\s+privacidade|aviso\s+de\s+privacidade|prote[cç][aã]o\s+de\s+dados)",
        re.IGNORECASE,
    )
    EMAIL_LGPD = re.compile(r"[\w.+-]+@(?:[\w-]+\.)*[\w-]+\.(?:gov\.br|mt\.gov\.br)", re.IGNORECASE)
    FORMULARIO = re.compile(r"<form\b|type=[\"']email[\"']|name=[\"']cpf[\"']", re.IGNORECASE)
    COOKIE_BANNER = re.compile(
        r"(cookie[s]?\s+(policy|pol[ií]tica)|uso\s+de\s+cookie|banner.*cookie)",
        re.IGNORECASE,
    )
    CONSENTIMENTO_EXPLICITO = re.compile(
        r"(consentimento|li\s+e\s+concordo|aceito\s+os\s+termos|opt-?in)",
        re.IGNORECASE,
    )

    def analisar_pagina(
        self, contexto: PageContext, regras: list[ConformityRule]
    ) -> list[AuditFinding]:
        achados: list[AuditFinding] = []
        texto_minusculo = contexto.texto.lower()

        for regra in regras:
            classificador = self._obter_classificador(regra.chave)
            if classificador is None:
                continue
            achado = classificador(contexto, regra, texto_minusculo)
            if achado is not None:
                achados.append(achado)

        return achados

    def _obter_classificador(self, chave: str):
        mapa = {
            "transparencia": self._classificar_transparencia,
            "coleta_dados": self._classificar_coleta_dados,
            "consentimento": self._classificar_consentimento,
            "direitos_titular": self._classificar_direitos_titular,
            "seguranca": self._classificar_seguranca,
            "cookies": self._classificar_cookies,
        }
        return mapa.get(chave)

    def _buscar_keywords(
        self, texto: str, keywords: list[str]
    ) -> list[str]:
        return [kw for kw in keywords if kw in texto]

    def _criar_achado(
        self,
        contexto: PageContext,
        regra: ConformityRule,
        status: EvidenceStatus,
        confianca: ConfidenceLevel,
        detalhes: str,
        termos: list[str],
    ) -> AuditFinding:
        return AuditFinding(
            secao_id=regra.secao_id,
            regra=regra.chave,
            descricao=regra.descricao,
            status=status,
            confianca=confianca,
            percentual=confianca.to_percentual(),
            evidence_ids=[contexto.evidence_id],
            fundamentacao_legal=regra.fundamentacao_legal,
            url=contexto.url,
            detalhes=detalhes,
            termos_encontrados=termos,
        )

    def _classificar_transparencia(
        self, contexto: PageContext, regra: ConformityRule, texto: str
    ) -> AuditFinding | None:
        termos = self._buscar_keywords(texto, regra.keywords)
        link_privacidade = bool(self.PRIVACIDADE_LINK.search(contexto.texto))

        if link_privacidade and termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.MUITO_ALTA,
                "Referência explícita a política de privacidade identificada no conteúdo.",
                termos,
            )
        if link_privacidade or "privacidade" in contexto.url.lower():
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.ALTA,
                "Página ou URL com indicação de política de privacidade.",
                termos or ["privacidade"],
            )
        if termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.MEDIA,
                "Termos relacionados à transparência encontrados sem confirmação explícita de política.",
                termos,
            )
        return None

    def _classificar_coleta_dados(
        self, contexto: PageContext, regra: ConformityRule, texto: str
    ) -> AuditFinding | None:
        termos = self._buscar_keywords(texto, regra.keywords)
        tem_formulario = bool(self.FORMULARIO.search(contexto.texto))

        if tem_formulario and termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.MUITO_ALTA,
                "Formulário com campos de coleta de dados identificado.",
                termos,
            )
        if tem_formulario or len(termos) >= 2:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.ALTA,
                "Indícios de coleta de dados pessoais na página.",
                termos,
            )
        if termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.MEDIA,
                "Termo relacionado à coleta encontrado.",
                termos,
            )
        return None

    def _classificar_consentimento(
        self, contexto: PageContext, regra: ConformityRule, texto: str
    ) -> AuditFinding | None:
        termos = self._buscar_keywords(texto, regra.keywords)
        consentimento_explicito = bool(self.CONSENTIMENTO_EXPLICITO.search(contexto.texto))

        if consentimento_explicito:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.ALTA,
                "Mecanismo de consentimento identificado no conteúdo.",
                termos or ["consentimento"],
            )
        if termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.MEDIA,
                "Termos de consentimento encontrados sem confirmação de mecanismo explícito.",
                termos,
            )
        return None

    def _classificar_direitos_titular(
        self, contexto: PageContext, regra: ConformityRule, texto: str
    ) -> AuditFinding | None:
        termos = self._buscar_keywords(texto, regra.keywords)
        email_encontrado = bool(self.EMAIL_LGPD.search(contexto.texto))

        if email_encontrado and termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.MUITO_ALTA,
                "Canal de contato institucional identificado para exercício de direitos.",
                termos,
            )
        if "encarregado" in texto or "dpo" in texto:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.ALTA,
                "Referência ao encarregado/DPO identificada.",
                termos or ["encarregado"],
            )
        if termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.MEDIA,
                "Termos sobre direitos do titular encontrados.",
                termos,
            )
        return None

    def _classificar_seguranca(
        self, contexto: PageContext, regra: ConformityRule, texto: str
    ) -> AuditFinding | None:
        termos = self._buscar_keywords(texto, regra.keywords)
        usa_https = contexto.url.lower().startswith("https://")

        if usa_https and termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.ALTA,
                "Página servida via HTTPS com referências a segurança.",
                termos + ["https"],
            )
        if usa_https:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.MEDIA,
                "Página servida via HTTPS.",
                ["https"],
            )
        if termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.BAIXA,
                "Referências a segurança sem HTTPS confirmado.",
                termos,
            )
        return None

    def _classificar_cookies(
        self, contexto: PageContext, regra: ConformityRule, texto: str
    ) -> AuditFinding | None:
        termos = self._buscar_keywords(texto, regra.keywords)
        banner_cookie = bool(self.COOKIE_BANNER.search(contexto.texto))

        if banner_cookie:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.CONFIRMADO, ConfidenceLevel.ALTA,
                "Política ou banner de cookies identificado.",
                termos or ["cookies"],
            )
        if termos:
            return self._criar_achado(
                contexto, regra, EvidenceStatus.INFERENCIA, ConfidenceLevel.MEDIA,
                "Referência a cookies encontrada sem banner confirmado.",
                termos,
            )
        return None


def sintetizar_secao(
    secao_id: str,
    titulo: str,
    achados: list[AuditFinding],
    fundamentacao_padrao: list[str],
) -> "SectionSummary":
    """Agrega achados de página em resumo por seção LGPD."""
    from lgpd_auditor.audit.models import SectionSummary

    achados_secao = [a for a in achados if a.secao_id == secao_id]

    if not achados_secao:
        return SectionSummary(
            secao_id=secao_id,
            titulo=titulo,
            status=EvidenceStatus.NAO_LOCALIZADO,
            confianca=ConfidenceLevel.MUITO_BAIXA,
            percentual=ConfidenceLevel.MUITO_BAIXA.to_percentual(),
            evidence_ids=[],
            fundamentacao_legal=fundamentacao_padrao,
            total_achados=0,
            mensagem=EvidenceStatus.NAO_LOCALIZADO.mensagem_ausencia,
        )

    prioridade_status = [
        EvidenceStatus.CONFIRMADO,
        EvidenceStatus.INFERENCIA,
        EvidenceStatus.HIPOTESE,
    ]
    status_final = EvidenceStatus.HIPOTESE
    for status_candidato in prioridade_status:
        if any(a.status == status_candidato for a in achados_secao):
            status_final = status_candidato
            break

    confiancas = [a.confianca for a in achados_secao]
    confianca_final = max(confiancas, key=lambda c: c.to_percentual())

    evidence_ids = list(dict.fromkeys(
        eid for achado in achados_secao for eid in achado.evidence_ids
    ))

    return SectionSummary(
        secao_id=secao_id,
        titulo=titulo,
        status=status_final,
        confianca=confianca_final,
        percentual=confianca_final.to_percentual(),
        evidence_ids=evidence_ids,
        fundamentacao_legal=fundamentacao_padrao,
        total_achados=len(achados_secao),
        mensagem="",
    )
