# Relatório de Conformidade LGPD — Tribunal de Contas do Estado de Mato Grosso

**Auditoria:** tce-mt  
**Portal:** https://www.tce.mt.gov.br/  
**Gerado em:** 2026-07-06T13:53:41.266721+00:00  
**Ferramenta:** LGPD Auditor v0.1.0

---

## 1. Introdução

Este relatório apresenta a análise de conformidade com a Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 — LGPD) do portal institucional do **Tribunal de Contas do Estado de Mato Grosso**, disponível em https://www.tce.mt.gov.br/.

A análise foi conduzida com apoio da ferramenta automatizada LGPD Auditor, seguindo governança anti-alucinação: toda conclusão possui status (`Confirmado`, `Inferência`, `Hipótese` ou `Não Localizado`), nível de confiança e referência a `evidence_id`.

---

## 2. Metodologia

### 2.1 Abordagem

1. **Crawler BFS** com Playwright (5 workers) limitado ao domínio `tce.mt.gov.br`
2. **Respeito a robots.txt** e rate limiting de 0.5s entre requisições
3. **Captura de evidências**: screenshot full-page, resumo HTML e metadados com hash SHA-256
4. **Auditoria heurística LGPD** baseada em `legislation.yaml` (regras 4.1–4.6)
5. **Classificação** com status e confiança por achado

### 2.2 Cobertura da navegação

| Métrica | Valor |
|---------|-------|
| Total de rotas visitadas | 503 |
| Rotas com screenshot | 503 |
| Rotas com erro HTTP (4xx/5xx) | 1 |
| Rotas bloqueadas (robots.txt) | 6 |
| Páginas analisadas (auditoria) | 503 |
| Total de achados | 764 |

---

## 3. Ambiente Analisado

- **Instituição:** Tribunal de Contas do Estado de Mato Grosso
- **URL base:** https://www.tce.mt.gov.br/
- **Domínio:** tce.mt.gov.br
- **Legislação de referência:** Lei 13.709/2018 (LGPD), orientações ANPD, ISO 27001/27701, OWASP

---

## 4. Análise de Conformidade LGPD


### 4.1 Transparência e política de privacidade

| Campo | Valor |
|-------|-------|
| **Status** | Confirmado |
| **Confiança** | Muito Alta (95%) |
| **Achados** | 66 |
| **Evidências** | ev-002, ev-007, ev-009, ev-017, ev-016, ev-014, ev-028, ev-029, ev-034, ev-038, ev-044, ev-046, ev-050, ev-060, ev-066, ev-074, ev-075, ev-080, ev-079, ev-081, ev-082, ev-092, ev-093, ev-094, ev-091, ev-145, ev-147, ev-146, ev-148, ev-149, ev-150, ev-151, ev-153, ev-152, ev-154, ev-156, ev-158, ev-157, ev-159, ev-160, ev-155, ev-161, ev-162, ev-163, ev-164, ev-168, ev-170, ev-167, ev-172, ev-173, ev-176, ev-175, ev-177, ev-171, ev-178, ev-179, ev-174, ev-180, ev-182, ev-181, ev-184, ev-183, ev-185, ev-186, ev-193, ev-312 |
| **Fundamentação** | art. 9 LGPD |




**Detalhes dos achados:**


- **ev-002** — [https://www.tce.mt.gov.br/corpo-deliberativo/15](https://www.tce.mt.gov.br/corpo-deliberativo/15)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-007** — [https://www.tce.mt.gov.br/tribunal-pleno/609](https://www.tce.mt.gov.br/tribunal-pleno/609)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-009** — [https://www.tce.mt.gov.br/instituto-memoria](https://www.tce.mt.gov.br/instituto-memoria)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-017** — [https://www.tce.mt.gov.br/planejamento-estrategico/704](https://www.tce.mt.gov.br/planejamento-estrategico/704)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-016** — [https://www.tce.mt.gov.br/lgpd](https://www.tce.mt.gov.br/lgpd)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, proteção de dados, dados pessoais


- **ev-014** — [https://escolasuperiordecontas.tce.mt.gov.br/](https://escolasuperiordecontas.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-028** — [https://www.tce.mt.gov.br/assinatura](https://www.tce.mt.gov.br/assinatura)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-029** — [https://servicos.tce.mt.gov.br/aplic/remessa](https://servicos.tce.mt.gov.br/aplic/remessa)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-034** — [https://www.tce.mt.gov.br/geo-obras/486](https://www.tce.mt.gov.br/geo-obras/486)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-038** — [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-044** — [https://www.tce.mt.gov.br/documentos](https://www.tce.mt.gov.br/documentos)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-046** — [https://www.tce.mt.gov.br/processos](https://www.tce.mt.gov.br/processos)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-050** — [https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-060** — [https://www.tce.mt.gov.br/legislacoes/prejulgados](https://www.tce.mt.gov.br/legislacoes/prejulgados)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-066** — [https://www.tce.mt.gov.br/tvcontas](https://www.tce.mt.gov.br/tvcontas)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-074** — [https://www.tce.mt.gov.br/legislacao/148](https://www.tce.mt.gov.br/legislacao/148)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-075** — [https://www.tce.mt.gov.br/mapa-da-transparencia/731](https://www.tce.mt.gov.br/mapa-da-transparencia/731)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-080** — [https://www.tce.mt.gov.br/plano-de-acao/984](https://www.tce.mt.gov.br/plano-de-acao/984)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-079** — [https://www.tce.mt.gov.br/quadrimestral/949](https://www.tce.mt.gov.br/quadrimestral/949)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-081** — [https://www.tce.mt.gov.br/ouvidoria-organizacional](https://www.tce.mt.gov.br/ouvidoria-organizacional)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-082** — [https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-092** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-093** — [https://www.tce.mt.gov.br/agenda](https://www.tce.mt.gov.br/agenda)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-094** — [https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797](https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-091** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, política de privacidade, proteção de dados


- **ev-145** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia](https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-147** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-146** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade](https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-148** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma](https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-149** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica](https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-150** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos](https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-151** — [https://escolasuperiordecontas.tce.mt.gov.br/calendario](https://escolasuperiordecontas.tce.mt.gov.br/calendario)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-153** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-152** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro](https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-154** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho](https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-156** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-158** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados, dados pessoais


- **ev-157** — [https://escolasuperiordecontas.tce.mt.gov.br/noticias](https://escolasuperiordecontas.tce.mt.gov.br/noticias)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-159** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados, dados pessoais


- **ev-160** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire](https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-155** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites](https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-161** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos](https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-162** — [https://escolasuperiordecontas.tce.mt.gov.br/acervo](https://escolasuperiordecontas.tce.mt.gov.br/acervo)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-163** — [https://escolasuperiordecontas.tce.mt.gov.br/contato](https://escolasuperiordecontas.tce.mt.gov.br/contato)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-164** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao](https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-168** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-170** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-167** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades](https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-172** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-173** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-176** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-175** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao](https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-177** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-171** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-178** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-179** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841](https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-174** — [https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais](https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-180** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801](https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-182** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783](https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-181** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821](https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-184** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741](https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-183** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782](https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-185** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias](https://escolasuperiordecontas.tce.mt.gov.br/galerias)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-186** — [https://escolasuperiordecontas.tce.mt.gov.br/mapa](https://escolasuperiordecontas.tce.mt.gov.br/mapa)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: proteção de dados


- **ev-193** — [https://www.tce.mt.gov.br/lgpd-programa-de-governanca-de-privacidade-de-dados/1086](https://www.tce.mt.gov.br/lgpd-programa-de-governanca-de-privacidade-de-dados/1086)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página ou URL com indicação de política de privacidade.
  - Termos: privacidade


- **ev-312** — [https://limesurvey.tce.mt.gov.br/index.php/425193](https://limesurvey.tce.mt.gov.br/index.php/425193)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Referência explícita a política de privacidade identificada no conteúdo.
  - Termos: privacidade, dados pessoais





### 4.2 Coleta de dados

| Campo | Valor |
|-------|-------|
| **Status** | Inferência |
| **Confiança** | Alta (85%) |
| **Achados** | 123 |
| **Evidências** | ev-002, ev-001, ev-007, ev-004, ev-005, ev-009, ev-010, ev-008, ev-012, ev-011, ev-013, ev-015, ev-017, ev-016, ev-014, ev-019, ev-018, ev-020, ev-021, ev-022, ev-023, ev-026, ev-027, ev-028, ev-030, ev-031, ev-033, ev-034, ev-035, ev-036, ev-038, ev-040, ev-044, ev-045, ev-046, ev-047, ev-049, ev-048, ev-050, ev-051, ev-054, ev-053, ev-055, ev-052, ev-056, ev-057, ev-060, ev-058, ev-059, ev-061, ev-062, ev-063, ev-066, ev-064, ev-067, ev-065, ev-068, ev-071, ev-070, ev-072, ev-073, ev-074, ev-075, ev-077, ev-078, ev-080, ev-079, ev-081, ev-082, ev-084, ev-085, ev-087, ev-088, ev-086, ev-090, ev-092, ev-093, ev-094, ev-091, ev-095, ev-145, ev-147, ev-146, ev-148, ev-149, ev-150, ev-151, ev-153, ev-154, ev-156, ev-158, ev-157, ev-159, ev-160, ev-155, ev-161, ev-162, ev-165, ev-163, ev-168, ev-170, ev-167, ev-172, ev-173, ev-175, ev-171, ev-178, ev-179, ev-174, ev-180, ev-182, ev-181, ev-184, ev-183, ev-185, ev-186, ev-271, ev-273, ev-272, ev-294, ev-305, ev-308, ev-367 |
| **Fundamentação** | art. 7 LGPD, art. 9 LGPD |




**Detalhes dos achados:**


- **ev-002** — [https://www.tce.mt.gov.br/corpo-deliberativo/15](https://www.tce.mt.gov.br/corpo-deliberativo/15)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-001** — [https://www.tce.mt.gov.br/](https://www.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-007** — [https://www.tce.mt.gov.br/tribunal-pleno/609](https://www.tce.mt.gov.br/tribunal-pleno/609)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-004** — [https://www.tce.mt.gov.br/historia/12](https://www.tce.mt.gov.br/historia/12)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-005** — [https://www.tce.mt.gov.br/acessibilidade-do-portal/1067](https://www.tce.mt.gov.br/acessibilidade-do-portal/1067)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-009** — [https://www.tce.mt.gov.br/instituto-memoria](https://www.tce.mt.gov.br/instituto-memoria)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-010** — [https://www.tce.mt.gov.br/conheca-o-tribunal/10](https://www.tce.mt.gov.br/conheca-o-tribunal/10)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-008** — [https://www.tce.mt.gov.br/identidade/767](https://www.tce.mt.gov.br/identidade/767)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-012** — [https://www.tce.mt.gov.br/institucional/303](https://www.tce.mt.gov.br/institucional/303)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-011** — [https://www.tce.mt.gov.br/publico-de-relacionamento/878](https://www.tce.mt.gov.br/publico-de-relacionamento/878)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-013** — [https://www.tce.mt.gov.br/competencias-do-tribunal/876](https://www.tce.mt.gov.br/competencias-do-tribunal/876)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-015** — [https://www.tce.mt.gov.br/produtos-e-processos/877](https://www.tce.mt.gov.br/produtos-e-processos/877)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-017** — [https://www.tce.mt.gov.br/planejamento-estrategico/704](https://www.tce.mt.gov.br/planejamento-estrategico/704)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-016** — [https://www.tce.mt.gov.br/lgpd](https://www.tce.mt.gov.br/lgpd)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-014** — [https://escolasuperiordecontas.tce.mt.gov.br/](https://escolasuperiordecontas.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-019** — [https://servicos.tce.mt.gov.br/](https://servicos.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-018** — [http://www.tce.mt.gov.br/conteudo/index/sid/939](http://www.tce.mt.gov.br/conteudo/index/sid/939)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-020** — [https://conta.tce.mt.gov.br/](https://conta.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-021** — [https://conta.tce.mt.gov.br/conta](https://conta.tce.mt.gov.br/conta)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cpf, telefone


- **ev-022** — [https://conta.tce.mt.gov.br/conta/recupera-senha](https://conta.tce.mt.gov.br/conta/recupera-senha)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, e-mail, cpf


- **ev-023** — [https://servicos.tce.mt.gov.br/fiscalizado/arp](https://servicos.tce.mt.gov.br/fiscalizado/arp)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-026** — [https://www.tce.mt.gov.br/aplic/485](https://www.tce.mt.gov.br/aplic/485)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-027** — [https://servicos.tce.mt.gov.br/fiscalizado/aplic/envio-carga](https://servicos.tce.mt.gov.br/fiscalizado/aplic/envio-carga)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-028** — [https://www.tce.mt.gov.br/assinatura](https://www.tce.mt.gov.br/assinatura)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-030** — [https://www.tce.mt.gov.br/distribuicao](https://www.tce.mt.gov.br/distribuicao)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-031** — [https://servicos.tce.mt.gov.br/certidao](https://servicos.tce.mt.gov.br/certidao)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-033** — [https://www.tce.mt.gov.br/contas](https://www.tce.mt.gov.br/contas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-034** — [https://www.tce.mt.gov.br/geo-obras/486](https://www.tce.mt.gov.br/geo-obras/486)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-035** — [https://servicos.tce.mt.gov.br/consulta-debitos](https://servicos.tce.mt.gov.br/consulta-debitos)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-036** — [https://servicos.tce.mt.gov.br/fiscalizado/conta/cadastro](https://servicos.tce.mt.gov.br/fiscalizado/conta/cadastro)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-038** — [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-040** — [https://servicos.tce.mt.gov.br/sessao-virtual/sustentacao-oral](https://servicos.tce.mt.gov.br/sessao-virtual/sustentacao-oral)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-044** — [https://www.tce.mt.gov.br/documentos](https://www.tce.mt.gov.br/documentos)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-045** — [https://www.tce.mt.gov.br/julgamento/presencial](https://www.tce.mt.gov.br/julgamento/presencial)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-046** — [https://www.tce.mt.gov.br/processos](https://www.tce.mt.gov.br/processos)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf, telefone


- **ev-047** — [https://www.tce.mt.gov.br/julgamento/virtual](https://www.tce.mt.gov.br/julgamento/virtual)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-049** — [https://www.tce.mt.gov.br/legislacoes/resolucao-normativa](https://www.tce.mt.gov.br/legislacoes/resolucao-normativa)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-048** — [https://www.tce.mt.gov.br/legislacoes/lei-organica](https://www.tce.mt.gov.br/legislacoes/lei-organica)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-050** — [https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-051** — [https://www.tce.mt.gov.br/legislacoes/regimento-interno](https://www.tce.mt.gov.br/legislacoes/regimento-interno)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-054** — [https://www.tce.mt.gov.br/legislacoes/portarias](https://www.tce.mt.gov.br/legislacoes/portarias)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-053** — [https://www.tce.mt.gov.br/legislacoes/decisoes-administrativas](https://www.tce.mt.gov.br/legislacoes/decisoes-administrativas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-055** — [https://www.tce.mt.gov.br/legislacoes](https://www.tce.mt.gov.br/legislacoes)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-052** — [https://www.tce.mt.gov.br/legislacoes/decisoes-normativas](https://www.tce.mt.gov.br/legislacoes/decisoes-normativas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-056** — [https://www.tce.mt.gov.br/legislacoes/instrucoes-normativas](https://www.tce.mt.gov.br/legislacoes/instrucoes-normativas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-057** — [https://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32](https://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-060** — [https://www.tce.mt.gov.br/legislacoes/prejulgados](https://www.tce.mt.gov.br/legislacoes/prejulgados)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-058** — [https://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta](https://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-059** — [https://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21](https://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-061** — [https://www.tce.mt.gov.br/legislacoes/sumulas](https://www.tce.mt.gov.br/legislacoes/sumulas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-062** — [https://www.tce.mt.gov.br/noticias](https://www.tce.mt.gov.br/noticias)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-063** — [https://www.tce.mt.gov.br/publicacao](https://www.tce.mt.gov.br/publicacao)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-066** — [https://www.tce.mt.gov.br/tvcontas](https://www.tce.mt.gov.br/tvcontas)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-064** — [https://www.tce.mt.gov.br/galeria](https://www.tce.mt.gov.br/galeria)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-067** — [https://www.tce.mt.gov.br/artigos](https://www.tce.mt.gov.br/artigos)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-065** — [https://sistema7.tce.mt.gov.br/jusconex-externo/tese](https://sistema7.tce.mt.gov.br/jusconex-externo/tese)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: e-mail


- **ev-068** — [https://www.tce.mt.gov.br/radio-tce/169](https://www.tce.mt.gov.br/radio-tce/169)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-071** — [https://hotsites.tce.mt.gov.br/](https://hotsites.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-070** — [https://servicos.tce.mt.gov.br/sic/minhas-solicitacoes](https://servicos.tce.mt.gov.br/sic/minhas-solicitacoes)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-072** — [https://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149](https://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, e-mail, telefone


- **ev-073** — [https://www.tce.mt.gov.br/tipos-de-manifestacoes/724](https://www.tce.mt.gov.br/tipos-de-manifestacoes/724)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-074** — [https://www.tce.mt.gov.br/legislacao/148](https://www.tce.mt.gov.br/legislacao/148)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-075** — [https://www.tce.mt.gov.br/mapa-da-transparencia/731](https://www.tce.mt.gov.br/mapa-da-transparencia/731)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-077** — [https://www.tce.mt.gov.br/fiscalize-corretamente/155](https://www.tce.mt.gov.br/fiscalize-corretamente/155)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, e-mail, cpf


- **ev-078** — [https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes](https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, e-mail, telefone


- **ev-080** — [https://www.tce.mt.gov.br/plano-de-acao/984](https://www.tce.mt.gov.br/plano-de-acao/984)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-079** — [https://www.tce.mt.gov.br/quadrimestral/949](https://www.tce.mt.gov.br/quadrimestral/949)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-081** — [https://www.tce.mt.gov.br/ouvidoria-organizacional](https://www.tce.mt.gov.br/ouvidoria-organizacional)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-082** — [https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-084** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=GzNkLvzXaYEqSCRZGVU7YRDKWet6Fg6bgFCkfF55](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=GzNkLvzXaYEqSCRZGVU7YRDKWet6Fg6bgFCkfF55)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-085** — [https://www.tce.mt.gov.br/noticias/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas/62637](https://www.tce.mt.gov.br/noticias/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas/62637)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-087** — [https://www.tce.mt.gov.br/noticias/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt/62635](https://www.tce.mt.gov.br/noticias/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt/62635)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-088** — [https://www.tce.mt.gov.br/noticias/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao/62633](https://www.tce.mt.gov.br/noticias/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao/62633)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-086** — [https://www.tce.mt.gov.br/noticias/sergio-ricardo-determina-abertura-de-mesa-tecnica-para-destravar-regularizacao-ambiental-da-agricultura-familiar/62636](https://www.tce.mt.gov.br/noticias/sergio-ricardo-determina-abertura-de-mesa-tecnica-para-destravar-regularizacao-ambiental-da-agricultura-familiar/62636)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-090** — [https://geoobras.tce.mt.gov.br/cidadao](https://geoobras.tce.mt.gov.br/cidadao)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, cpf


- **ev-092** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-093** — [https://www.tce.mt.gov.br/agenda](https://www.tce.mt.gov.br/agenda)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-094** — [https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797](https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-091** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cadastro, telefone


- **ev-095** — [https://www.tce.mt.gov.br/artigos/fortalecimento-do-controle-social-do-sus-em-mato-grosso/625](https://www.tce.mt.gov.br/artigos/fortalecimento-do-controle-social-do-sus-em-mato-grosso/625)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-145** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia](https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-147** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-146** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade](https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-148** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma](https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-149** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica](https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-150** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos](https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-151** — [https://escolasuperiordecontas.tce.mt.gov.br/calendario](https://escolasuperiordecontas.tce.mt.gov.br/calendario)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-153** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-154** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho](https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-156** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-158** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: e-mail


- **ev-157** — [https://escolasuperiordecontas.tce.mt.gov.br/noticias](https://escolasuperiordecontas.tce.mt.gov.br/noticias)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-159** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: e-mail, telefone


- **ev-160** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire](https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-155** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites](https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-161** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos](https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-162** — [https://escolasuperiordecontas.tce.mt.gov.br/acervo](https://escolasuperiordecontas.tce.mt.gov.br/acervo)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-165** — [https://ead.tce.mt.gov.br/ava](https://ead.tce.mt.gov.br/ava)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cpf


- **ev-163** — [https://escolasuperiordecontas.tce.mt.gov.br/contato](https://escolasuperiordecontas.tce.mt.gov.br/contato)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: e-mail, telefone


- **ev-168** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: e-mail, telefone


- **ev-170** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-167** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades](https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-172** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-173** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-175** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao](https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-171** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-178** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-179** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841](https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-174** — [https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais](https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-180** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801](https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-182** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783](https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-181** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821](https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-184** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741](https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-183** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782](https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-185** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias](https://escolasuperiordecontas.tce.mt.gov.br/galerias)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-186** — [https://escolasuperiordecontas.tce.mt.gov.br/mapa](https://escolasuperiordecontas.tce.mt.gov.br/mapa)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-271** — [https://servicos.tce.mt.gov.br/empresas-inidoneas](https://servicos.tce.mt.gov.br/empresas-inidoneas)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro


- **ev-273** — [https://servicos.tce.mt.gov.br/ouvidoria](https://servicos.tce.mt.gov.br/ouvidoria)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: e-mail, telefone


- **ev-272** — [https://servicos.tce.mt.gov.br/inabilitacao-exercicio](https://servicos.tce.mt.gov.br/inabilitacao-exercicio)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cpf


- **ev-294** — [https://servicos.tce.mt.gov.br/log](https://servicos.tce.mt.gov.br/log)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-305** — [https://servicos.tce.mt.gov.br/certidao/emissao](https://servicos.tce.mt.gov.br/certidao/emissao)
  - Status: Inferência | Confiança: Alta (85%)
  - Indícios de coleta de dados pessoais na página.
  - Termos: cpf, telefone


- **ev-308** — [https://servicos.tce.mt.gov.br/certidao/pedido-acompanhamento](https://servicos.tce.mt.gov.br/certidao/pedido-acompanhamento)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: telefone


- **ev-367** — [https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026](https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Termo relacionado à coleta encontrado.
  - Termos: cadastro





### 4.3 Consentimento

| Campo | Valor |
|-------|-------|
| **Status** | Confirmado |
| **Confiança** | Alta (85%) |
| **Achados** | 62 |
| **Evidências** | ev-002, ev-007, ev-009, ev-017, ev-014, ev-028, ev-029, ev-034, ev-038, ev-044, ev-046, ev-050, ev-060, ev-066, ev-075, ev-080, ev-079, ev-081, ev-082, ev-092, ev-093, ev-094, ev-091, ev-145, ev-147, ev-146, ev-148, ev-149, ev-150, ev-151, ev-153, ev-152, ev-154, ev-156, ev-158, ev-157, ev-159, ev-160, ev-155, ev-161, ev-162, ev-163, ev-164, ev-168, ev-170, ev-167, ev-172, ev-173, ev-176, ev-175, ev-177, ev-171, ev-178, ev-179, ev-174, ev-180, ev-182, ev-181, ev-184, ev-183, ev-185, ev-186 |
| **Fundamentação** | art. 8 LGPD |




**Detalhes dos achados:**


- **ev-002** — [https://www.tce.mt.gov.br/corpo-deliberativo/15](https://www.tce.mt.gov.br/corpo-deliberativo/15)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-007** — [https://www.tce.mt.gov.br/tribunal-pleno/609](https://www.tce.mt.gov.br/tribunal-pleno/609)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-009** — [https://www.tce.mt.gov.br/instituto-memoria](https://www.tce.mt.gov.br/instituto-memoria)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-017** — [https://www.tce.mt.gov.br/planejamento-estrategico/704](https://www.tce.mt.gov.br/planejamento-estrategico/704)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-014** — [https://escolasuperiordecontas.tce.mt.gov.br/](https://escolasuperiordecontas.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-028** — [https://www.tce.mt.gov.br/assinatura](https://www.tce.mt.gov.br/assinatura)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-029** — [https://servicos.tce.mt.gov.br/aplic/remessa](https://servicos.tce.mt.gov.br/aplic/remessa)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-034** — [https://www.tce.mt.gov.br/geo-obras/486](https://www.tce.mt.gov.br/geo-obras/486)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-038** — [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-044** — [https://www.tce.mt.gov.br/documentos](https://www.tce.mt.gov.br/documentos)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-046** — [https://www.tce.mt.gov.br/processos](https://www.tce.mt.gov.br/processos)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-050** — [https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-060** — [https://www.tce.mt.gov.br/legislacoes/prejulgados](https://www.tce.mt.gov.br/legislacoes/prejulgados)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-066** — [https://www.tce.mt.gov.br/tvcontas](https://www.tce.mt.gov.br/tvcontas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-075** — [https://www.tce.mt.gov.br/mapa-da-transparencia/731](https://www.tce.mt.gov.br/mapa-da-transparencia/731)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-080** — [https://www.tce.mt.gov.br/plano-de-acao/984](https://www.tce.mt.gov.br/plano-de-acao/984)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-079** — [https://www.tce.mt.gov.br/quadrimestral/949](https://www.tce.mt.gov.br/quadrimestral/949)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-081** — [https://www.tce.mt.gov.br/ouvidoria-organizacional](https://www.tce.mt.gov.br/ouvidoria-organizacional)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-082** — [https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-092** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-093** — [https://www.tce.mt.gov.br/agenda](https://www.tce.mt.gov.br/agenda)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-094** — [https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797](https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-091** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-145** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia](https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-147** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-146** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade](https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-148** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma](https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-149** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica](https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-150** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos](https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-151** — [https://escolasuperiordecontas.tce.mt.gov.br/calendario](https://escolasuperiordecontas.tce.mt.gov.br/calendario)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-153** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-152** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro](https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-154** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho](https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-156** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-158** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-157** — [https://escolasuperiordecontas.tce.mt.gov.br/noticias](https://escolasuperiordecontas.tce.mt.gov.br/noticias)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-159** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-160** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire](https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-155** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites](https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-161** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos](https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-162** — [https://escolasuperiordecontas.tce.mt.gov.br/acervo](https://escolasuperiordecontas.tce.mt.gov.br/acervo)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-163** — [https://escolasuperiordecontas.tce.mt.gov.br/contato](https://escolasuperiordecontas.tce.mt.gov.br/contato)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-164** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao](https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-168** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-170** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-167** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades](https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-172** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-173** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-176** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-175** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao](https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-177** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-171** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-178** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-179** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841](https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-174** — [https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais](https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-180** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801](https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-182** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783](https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-181** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821](https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-184** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741](https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-183** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782](https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-185** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias](https://escolasuperiordecontas.tce.mt.gov.br/galerias)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento


- **ev-186** — [https://escolasuperiordecontas.tce.mt.gov.br/mapa](https://escolasuperiordecontas.tce.mt.gov.br/mapa)
  - Status: Confirmado | Confiança: Alta (85%)
  - Mecanismo de consentimento identificado no conteúdo.
  - Termos: consentimento





### 4.4 Direitos do titular

| Campo | Valor |
|-------|-------|
| **Status** | Confirmado |
| **Confiança** | Muito Alta (95%) |
| **Achados** | 12 |
| **Evidências** | ev-003, ev-019, ev-022, ev-041, ev-054, ev-073, ev-077, ev-078, ev-083, ev-273, ev-367, ev-368 |
| **Fundamentação** | art. 18 LGPD, art. 41 LGPD |




**Detalhes dos achados:**


- **ev-003** — [https://cartadeservicos.tce.mt.gov.br/](https://cartadeservicos.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: solicitação


- **ev-019** — [https://servicos.tce.mt.gov.br/](https://servicos.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: solicitação


- **ev-022** — [https://conta.tce.mt.gov.br/conta/recupera-senha](https://conta.tce.mt.gov.br/conta/recupera-senha)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Canal de contato institucional identificado para exercício de direitos.
  - Termos: titular


- **ev-041** — [https://servicos.tce.mt.gov.br/consulta-item](https://servicos.tce.mt.gov.br/consulta-item)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: solicitação


- **ev-054** — [https://www.tce.mt.gov.br/legislacoes/portarias](https://www.tce.mt.gov.br/legislacoes/portarias)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: titular


- **ev-073** — [https://www.tce.mt.gov.br/tipos-de-manifestacoes/724](https://www.tce.mt.gov.br/tipos-de-manifestacoes/724)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Canal de contato institucional identificado para exercício de direitos.
  - Termos: solicitação


- **ev-077** — [https://www.tce.mt.gov.br/fiscalize-corretamente/155](https://www.tce.mt.gov.br/fiscalize-corretamente/155)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: titular, solicitação


- **ev-078** — [https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes](https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Canal de contato institucional identificado para exercício de direitos.
  - Termos: solicitação


- **ev-083** — [https://cartadeservicos.tce.mt.gov.br/entidade/1119320](https://cartadeservicos.tce.mt.gov.br/entidade/1119320)
  - Status: Confirmado | Confiança: Muito Alta (95%)
  - Canal de contato institucional identificado para exercício de direitos.
  - Termos: solicitação


- **ev-273** — [https://servicos.tce.mt.gov.br/ouvidoria](https://servicos.tce.mt.gov.br/ouvidoria)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: solicitação


- **ev-367** — [https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026](https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: solicitação


- **ev-368** — [https://servicos.tce.mt.gov.br/consulta-item/historico](https://servicos.tce.mt.gov.br/consulta-item/historico)
  - Status: Inferência | Confiança: Média (65%)
  - Termos sobre direitos do titular encontrados.
  - Termos: solicitação





### 4.5 Segurança da informação

| Campo | Valor |
|-------|-------|
| **Status** | Confirmado |
| **Confiança** | Alta (85%) |
| **Achados** | 437 |
| **Evidências** | ev-002, ev-001, ev-003, ev-007, ev-004, ev-006, ev-005, ev-009, ev-010, ev-008, ev-012, ev-011, ev-013, ev-015, ev-017, ev-016, ev-014, ev-019, ev-018, ev-020, ev-021, ev-022, ev-023, ev-025, ev-024, ev-026, ev-027, ev-028, ev-030, ev-031, ev-033, ev-029, ev-032, ev-034, ev-037, ev-035, ev-036, ev-038, ev-040, ev-039, ev-043, ev-044, ev-042, ev-045, ev-046, ev-047, ev-049, ev-048, ev-050, ev-041, ev-051, ev-054, ev-053, ev-055, ev-052, ev-056, ev-057, ev-060, ev-058, ev-059, ev-061, ev-062, ev-063, ev-066, ev-064, ev-067, ev-065, ev-068, ev-069, ev-071, ev-070, ev-072, ev-073, ev-074, ev-075, ev-077, ev-076, ev-078, ev-080, ev-079, ev-081, ev-082, ev-083, ev-084, ev-085, ev-087, ev-089, ev-088, ev-086, ev-090, ev-092, ev-093, ev-094, ev-091, ev-096, ev-097, ev-095, ev-098, ev-099, ev-100, ev-101, ev-102, ev-103, ev-104, ev-105, ev-106, ev-107, ev-109, ev-108, ev-110, ev-111, ev-112, ev-113, ev-114, ev-115, ev-116, ev-117, ev-118, ev-119, ev-120, ev-121, ev-122, ev-123, ev-124, ev-125, ev-126, ev-127, ev-128, ev-129, ev-130, ev-131, ev-132, ev-133, ev-134, ev-135, ev-136, ev-137, ev-138, ev-139, ev-140, ev-141, ev-142, ev-143, ev-144, ev-145, ev-147, ev-146, ev-148, ev-149, ev-150, ev-151, ev-153, ev-152, ev-154, ev-156, ev-158, ev-157, ev-159, ev-160, ev-155, ev-161, ev-162, ev-165, ev-166, ev-163, ev-164, ev-169, ev-168, ev-170, ev-167, ev-172, ev-173, ev-176, ev-175, ev-177, ev-171, ev-178, ev-179, ev-174, ev-180, ev-182, ev-181, ev-187, ev-184, ev-188, ev-183, ev-189, ev-185, ev-186, ev-191, ev-190, ev-192, ev-193, ev-194, ev-196, ev-195, ev-197, ev-198, ev-199, ev-200, ev-201, ev-202, ev-203, ev-204, ev-260, ev-269, ev-274, ev-271, ev-273, ev-272, ev-276, ev-278, ev-279, ev-280, ev-281, ev-282, ev-283, ev-284, ev-285, ev-286, ev-287, ev-288, ev-289, ev-290, ev-291, ev-292, ev-293, ev-295, ev-296, ev-297, ev-298, ev-294, ev-299, ev-300, ev-301, ev-302, ev-303, ev-304, ev-306, ev-307, ev-309, ev-305, ev-310, ev-311, ev-308, ev-313, ev-314, ev-315, ev-312, ev-316, ev-317, ev-318, ev-319, ev-320, ev-321, ev-322, ev-323, ev-324, ev-325, ev-326, ev-327, ev-328, ev-329, ev-330, ev-331, ev-332, ev-333, ev-334, ev-335, ev-336, ev-337, ev-338, ev-339, ev-340, ev-341, ev-343, ev-342, ev-344, ev-345, ev-346, ev-347, ev-348, ev-349, ev-351, ev-350, ev-352, ev-353, ev-354, ev-355, ev-356, ev-358, ev-357, ev-359, ev-360, ev-361, ev-362, ev-363, ev-364, ev-366, ev-365, ev-369, ev-371, ev-372, ev-370, ev-373, ev-374, ev-375, ev-376, ev-367, ev-379, ev-378, ev-377, ev-380, ev-368, ev-384, ev-381, ev-382, ev-383, ev-385, ev-386, ev-387, ev-389, ev-388, ev-390, ev-392, ev-391, ev-394, ev-393, ev-395, ev-397, ev-396, ev-398, ev-399, ev-400, ev-401, ev-402, ev-404, ev-403, ev-405, ev-406, ev-407, ev-409, ev-408, ev-410, ev-411, ev-412, ev-413, ev-414, ev-415, ev-416, ev-417, ev-418, ev-419, ev-420, ev-421, ev-422, ev-423, ev-424, ev-425, ev-426, ev-427, ev-428, ev-429, ev-430, ev-431, ev-432, ev-433, ev-434, ev-435, ev-436, ev-437, ev-438, ev-439, ev-440, ev-441, ev-442, ev-443, ev-445, ev-447, ev-444, ev-446, ev-450, ev-448, ev-452, ev-451, ev-453, ev-449, ev-456, ev-455, ev-454, ev-459, ev-457, ev-458, ev-462, ev-460, ev-461, ev-463, ev-464, ev-467, ev-468, ev-465, ev-471, ev-466, ev-469, ev-470, ev-472, ev-476, ev-474, ev-473, ev-477, ev-480, ev-475, ev-478, ev-479, ev-482, ev-481, ev-483, ev-484, ev-486, ev-485, ev-487, ev-489, ev-488, ev-493, ev-491, ev-490, ev-492, ev-494, ev-496, ev-495, ev-497, ev-501, ev-498, ev-502, ev-503, ev-500, ev-499 |
| **Fundamentação** | art. 46 LGPD, ISO 27001 A.8.24 |




**Detalhes dos achados:**


- **ev-002** — [https://www.tce.mt.gov.br/corpo-deliberativo/15](https://www.tce.mt.gov.br/corpo-deliberativo/15)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-001** — [https://www.tce.mt.gov.br/](https://www.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-003** — [https://cartadeservicos.tce.mt.gov.br/](https://cartadeservicos.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-007** — [https://www.tce.mt.gov.br/tribunal-pleno/609](https://www.tce.mt.gov.br/tribunal-pleno/609)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-004** — [https://www.tce.mt.gov.br/historia/12](https://www.tce.mt.gov.br/historia/12)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-006** — [https://sic.tce.mt.gov.br/](https://sic.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-005** — [https://www.tce.mt.gov.br/acessibilidade-do-portal/1067](https://www.tce.mt.gov.br/acessibilidade-do-portal/1067)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-009** — [https://www.tce.mt.gov.br/instituto-memoria](https://www.tce.mt.gov.br/instituto-memoria)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-010** — [https://www.tce.mt.gov.br/conheca-o-tribunal/10](https://www.tce.mt.gov.br/conheca-o-tribunal/10)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: segurança, https


- **ev-008** — [https://www.tce.mt.gov.br/identidade/767](https://www.tce.mt.gov.br/identidade/767)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-012** — [https://www.tce.mt.gov.br/institucional/303](https://www.tce.mt.gov.br/institucional/303)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-011** — [https://www.tce.mt.gov.br/publico-de-relacionamento/878](https://www.tce.mt.gov.br/publico-de-relacionamento/878)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-013** — [https://www.tce.mt.gov.br/competencias-do-tribunal/876](https://www.tce.mt.gov.br/competencias-do-tribunal/876)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-015** — [https://www.tce.mt.gov.br/produtos-e-processos/877](https://www.tce.mt.gov.br/produtos-e-processos/877)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-017** — [https://www.tce.mt.gov.br/planejamento-estrategico/704](https://www.tce.mt.gov.br/planejamento-estrategico/704)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-016** — [https://www.tce.mt.gov.br/lgpd](https://www.tce.mt.gov.br/lgpd)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: segurança, https


- **ev-014** — [https://escolasuperiordecontas.tce.mt.gov.br/](https://escolasuperiordecontas.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-019** — [https://servicos.tce.mt.gov.br/](https://servicos.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-018** — [http://www.tce.mt.gov.br/conteudo/index/sid/939](http://www.tce.mt.gov.br/conteudo/index/sid/939)
  - Status: Inferência | Confiança: Baixa (40%)
  - Referências a segurança sem HTTPS confirmado.
  - Termos: certificado, segurança


- **ev-020** — [https://conta.tce.mt.gov.br/](https://conta.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-021** — [https://conta.tce.mt.gov.br/conta](https://conta.tce.mt.gov.br/conta)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-022** — [https://conta.tce.mt.gov.br/conta/recupera-senha](https://conta.tce.mt.gov.br/conta/recupera-senha)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-023** — [https://servicos.tce.mt.gov.br/fiscalizado/arp](https://servicos.tce.mt.gov.br/fiscalizado/arp)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-025** — [https://servicos.tce.mt.gov.br/tabela-interna](https://servicos.tce.mt.gov.br/tabela-interna)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-024** — [https://www.tce.mt.gov.br/calendario](https://www.tce.mt.gov.br/calendario)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-026** — [https://www.tce.mt.gov.br/aplic/485](https://www.tce.mt.gov.br/aplic/485)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-027** — [https://servicos.tce.mt.gov.br/fiscalizado/aplic/envio-carga](https://servicos.tce.mt.gov.br/fiscalizado/aplic/envio-carga)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-028** — [https://www.tce.mt.gov.br/assinatura](https://www.tce.mt.gov.br/assinatura)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-030** — [https://www.tce.mt.gov.br/distribuicao](https://www.tce.mt.gov.br/distribuicao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-031** — [https://servicos.tce.mt.gov.br/certidao](https://servicos.tce.mt.gov.br/certidao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-033** — [https://www.tce.mt.gov.br/contas](https://www.tce.mt.gov.br/contas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-029** — [https://servicos.tce.mt.gov.br/aplic/remessa](https://servicos.tce.mt.gov.br/aplic/remessa)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-032** — [https://servicos.tce.mt.gov.br/diario](https://servicos.tce.mt.gov.br/diario)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-034** — [https://www.tce.mt.gov.br/geo-obras/486](https://www.tce.mt.gov.br/geo-obras/486)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-037** — [https://push.tce.mt.gov.br/](https://push.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-035** — [https://servicos.tce.mt.gov.br/consulta-debitos](https://servicos.tce.mt.gov.br/consulta-debitos)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-036** — [https://servicos.tce.mt.gov.br/fiscalizado/conta/cadastro](https://servicos.tce.mt.gov.br/fiscalizado/conta/cadastro)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-038** — [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-040** — [https://servicos.tce.mt.gov.br/sessao-virtual/sustentacao-oral](https://servicos.tce.mt.gov.br/sessao-virtual/sustentacao-oral)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-039** — [https://pce.tce.mt.gov.br/juris](https://pce.tce.mt.gov.br/juris)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-043** — [https://servicos.tce.mt.gov.br/igfm](https://servicos.tce.mt.gov.br/igfm)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-044** — [https://www.tce.mt.gov.br/documentos](https://www.tce.mt.gov.br/documentos)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-042** — [https://servicos.tce.mt.gov.br/audiencias](https://servicos.tce.mt.gov.br/audiencias)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-045** — [https://www.tce.mt.gov.br/julgamento/presencial](https://www.tce.mt.gov.br/julgamento/presencial)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-046** — [https://www.tce.mt.gov.br/processos](https://www.tce.mt.gov.br/processos)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-047** — [https://www.tce.mt.gov.br/julgamento/virtual](https://www.tce.mt.gov.br/julgamento/virtual)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-049** — [https://www.tce.mt.gov.br/legislacoes/resolucao-normativa](https://www.tce.mt.gov.br/legislacoes/resolucao-normativa)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-048** — [https://www.tce.mt.gov.br/legislacoes/lei-organica](https://www.tce.mt.gov.br/legislacoes/lei-organica)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-050** — [https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-041** — [https://servicos.tce.mt.gov.br/consulta-item](https://servicos.tce.mt.gov.br/consulta-item)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-051** — [https://www.tce.mt.gov.br/legislacoes/regimento-interno](https://www.tce.mt.gov.br/legislacoes/regimento-interno)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-054** — [https://www.tce.mt.gov.br/legislacoes/portarias](https://www.tce.mt.gov.br/legislacoes/portarias)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-053** — [https://www.tce.mt.gov.br/legislacoes/decisoes-administrativas](https://www.tce.mt.gov.br/legislacoes/decisoes-administrativas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-055** — [https://www.tce.mt.gov.br/legislacoes](https://www.tce.mt.gov.br/legislacoes)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-052** — [https://www.tce.mt.gov.br/legislacoes/decisoes-normativas](https://www.tce.mt.gov.br/legislacoes/decisoes-normativas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-056** — [https://www.tce.mt.gov.br/legislacoes/instrucoes-normativas](https://www.tce.mt.gov.br/legislacoes/instrucoes-normativas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-057** — [https://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32](https://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-060** — [https://www.tce.mt.gov.br/legislacoes/prejulgados](https://www.tce.mt.gov.br/legislacoes/prejulgados)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-058** — [https://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta](https://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-059** — [https://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21](https://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-061** — [https://www.tce.mt.gov.br/legislacoes/sumulas](https://www.tce.mt.gov.br/legislacoes/sumulas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-062** — [https://www.tce.mt.gov.br/noticias](https://www.tce.mt.gov.br/noticias)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-063** — [https://www.tce.mt.gov.br/publicacao](https://www.tce.mt.gov.br/publicacao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-066** — [https://www.tce.mt.gov.br/tvcontas](https://www.tce.mt.gov.br/tvcontas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-064** — [https://www.tce.mt.gov.br/galeria](https://www.tce.mt.gov.br/galeria)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-067** — [https://www.tce.mt.gov.br/artigos](https://www.tce.mt.gov.br/artigos)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-065** — [https://sistema7.tce.mt.gov.br/jusconex-externo/tese](https://sistema7.tce.mt.gov.br/jusconex-externo/tese)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-068** — [https://www.tce.mt.gov.br/radio-tce/169](https://www.tce.mt.gov.br/radio-tce/169)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-069** — [https://radar.tce.mt.gov.br/extensions/radar-da-transparencia-publica/radar-da-transparencia-publica.html](https://radar.tce.mt.gov.br/extensions/radar-da-transparencia-publica/radar-da-transparencia-publica.html)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: segurança, https


- **ev-071** — [https://hotsites.tce.mt.gov.br/](https://hotsites.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-070** — [https://servicos.tce.mt.gov.br/sic/minhas-solicitacoes](https://servicos.tce.mt.gov.br/sic/minhas-solicitacoes)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-072** — [https://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149](https://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-073** — [https://www.tce.mt.gov.br/tipos-de-manifestacoes/724](https://www.tce.mt.gov.br/tipos-de-manifestacoes/724)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-074** — [https://www.tce.mt.gov.br/legislacao/148](https://www.tce.mt.gov.br/legislacao/148)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-075** — [https://www.tce.mt.gov.br/mapa-da-transparencia/731](https://www.tce.mt.gov.br/mapa-da-transparencia/731)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-077** — [https://www.tce.mt.gov.br/fiscalize-corretamente/155](https://www.tce.mt.gov.br/fiscalize-corretamente/155)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-076** — [https://www.tce.mt.gov.br/uploads/flipbook/carta-servicos-2024/index.html](https://www.tce.mt.gov.br/uploads/flipbook/carta-servicos-2024/index.html)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-078** — [https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes](https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: https, https


- **ev-080** — [https://www.tce.mt.gov.br/plano-de-acao/984](https://www.tce.mt.gov.br/plano-de-acao/984)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-079** — [https://www.tce.mt.gov.br/quadrimestral/949](https://www.tce.mt.gov.br/quadrimestral/949)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-081** — [https://www.tce.mt.gov.br/ouvidoria-organizacional](https://www.tce.mt.gov.br/ouvidoria-organizacional)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-082** — [https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-083** — [https://cartadeservicos.tce.mt.gov.br/entidade/1119320](https://cartadeservicos.tce.mt.gov.br/entidade/1119320)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-084** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=GzNkLvzXaYEqSCRZGVU7YRDKWet6Fg6bgFCkfF55](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=GzNkLvzXaYEqSCRZGVU7YRDKWet6Fg6bgFCkfF55)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-085** — [https://www.tce.mt.gov.br/noticias/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas/62637](https://www.tce.mt.gov.br/noticias/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas/62637)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-087** — [https://www.tce.mt.gov.br/noticias/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt/62635](https://www.tce.mt.gov.br/noticias/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt/62635)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-089** — [https://radar.tce.mt.gov.br/](https://radar.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: segurança, https


- **ev-088** — [https://www.tce.mt.gov.br/noticias/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao/62633](https://www.tce.mt.gov.br/noticias/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao/62633)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-086** — [https://www.tce.mt.gov.br/noticias/sergio-ricardo-determina-abertura-de-mesa-tecnica-para-destravar-regularizacao-ambiental-da-agricultura-familiar/62636](https://www.tce.mt.gov.br/noticias/sergio-ricardo-determina-abertura-de-mesa-tecnica-para-destravar-regularizacao-ambiental-da-agricultura-familiar/62636)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-090** — [https://geoobras.tce.mt.gov.br/cidadao](https://geoobras.tce.mt.gov.br/cidadao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-092** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-093** — [https://www.tce.mt.gov.br/agenda](https://www.tce.mt.gov.br/agenda)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-094** — [https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797](https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-091** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-096** — [https://www.tce.mt.gov.br/tvcontas/tce-noticias/seminario-nacional-resulta-em-carta-com-16-compromissos-pela-inclusao-educacional/33389](https://www.tce.mt.gov.br/tvcontas/tce-noticias/seminario-nacional-resulta-em-carta-com-16-compromissos-pela-inclusao-educacional/33389)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-097** — [https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-do-tce-mt-reune-especialistas-de-todo-pais-e-ganha-destaque-nacional/33390](https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-do-tce-mt-reune-especialistas-de-todo-pais-e-ganha-destaque-nacional/33390)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-095** — [https://www.tce.mt.gov.br/artigos/fortalecimento-do-controle-social-do-sus-em-mato-grosso/625](https://www.tce.mt.gov.br/artigos/fortalecimento-do-controle-social-do-sus-em-mato-grosso/625)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-098** — [https://www.tce.mt.gov.br/tvcontas/tce-noticias/sergio-ricardo-garante-apoio-tecnico-do-tce-a-demandas-de-boa-esperanca-do-norte/33388](https://www.tce.mt.gov.br/tvcontas/tce-noticias/sergio-ricardo-garante-apoio-tecnico-do-tce-a-demandas-de-boa-esperanca-do-norte/33388)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-099** — [https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-mobiliza-municipios-e-firma-compromisso-pela-melhoria-da-saude-publica-em-mt/33391](https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-mobiliza-municipios-e-firma-compromisso-pela-melhoria-da-saude-publica-em-mt/33391)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-100** — [https://www.tce.mt.gov.br/tvcontas/tce-noticias/tce-mt-capacita-conselheiros-de-saude-para-fortalecer-controle-social-nos-municipios/33387](https://www.tce.mt.gov.br/tvcontas/tce-noticias/tce-mt-capacita-conselheiros-de-saude-para-fortalecer-controle-social-nos-municipios/33387)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-101** — [https://intranet.tce.mt.gov.br/login](https://intranet.tce.mt.gov.br/login)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-102** — [https://www.tce.mt.gov.br/publicacao/administracao-publica/14](https://www.tce.mt.gov.br/publicacao/administracao-publica/14)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-103** — [https://www.tce.mt.gov.br/hotsites/lgpd/legislacao-politicas-de-cookies-no-ambito-do-tce-mt.html](https://www.tce.mt.gov.br/hotsites/lgpd/legislacao-politicas-de-cookies-no-ambito-do-tce-mt.html)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-104** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=Y521fuxmVKtUn2gWHUbv5CgwmGAqsQsJkhfLgAmA](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=Y521fuxmVKtUn2gWHUbv5CgwmGAqsQsJkhfLgAmA)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-105** — [https://www.tce.mt.gov.br/corpo-deliberativo](https://www.tce.mt.gov.br/corpo-deliberativo)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-106** — [https://www.tce.mt.gov.br/corpo-de-gestao/16](https://www.tce.mt.gov.br/corpo-de-gestao/16)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-107** — [https://www.tce.mt.gov.br/corpo-tecnico/17](https://www.tce.mt.gov.br/corpo-tecnico/17)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-109** — [https://www.tce.mt.gov.br/conteudo/index/sid/121](https://www.tce.mt.gov.br/conteudo/index/sid/121)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-108** — [https://www.tce.mt.gov.br/conteudo/sid/583](https://www.tce.mt.gov.br/conteudo/sid/583)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-110** — [https://www.tce.mt.gov.br/conteudo/index/sid/934](https://www.tce.mt.gov.br/conteudo/index/sid/934)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-111** — [https://www.tce.mt.gov.br/conteudo/index/sid/120](https://www.tce.mt.gov.br/conteudo/index/sid/120)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-112** — [https://www.tce.mt.gov.br/conteudo/index/sid/116](https://www.tce.mt.gov.br/conteudo/index/sid/116)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-113** — [https://www.tce.mt.gov.br/conteudo/index/sid/118](https://www.tce.mt.gov.br/conteudo/index/sid/118)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-114** — [https://cartadeservicos.tce.mt.gov.br/docs](https://cartadeservicos.tce.mt.gov.br/docs)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-115** — [https://www.tce.mt.gov.br/conteudo/index/sid/1063](https://www.tce.mt.gov.br/conteudo/index/sid/1063)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-116** — [https://www.tce.mt.gov.br/historia](https://www.tce.mt.gov.br/historia)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-117** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=aWbnJZXklFvpE0BHmegWUugf2x21Yb8pZRTNUACu](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=aWbnJZXklFvpE0BHmegWUugf2x21Yb8pZRTNUACu)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-118** — [https://www.tce.mt.gov.br/uploads/flipbook/70anos/index.html](https://www.tce.mt.gov.br/uploads/flipbook/70anos/index.html)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-119** — [https://www.tce.mt.gov.br/galeria/show/id/5](https://www.tce.mt.gov.br/galeria/show/id/5)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-120** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=08LpMRgDZdB1bHao508j98imF9hX5zoOIHRNkgxc](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=08LpMRgDZdB1bHao508j98imF9hX5zoOIHRNkgxc)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-121** — [https://sic.tce.mt.gov.br/docs](https://sic.tce.mt.gov.br/docs)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-122** — [https://sic.tce.mt.gov.br/saiba-mais](https://sic.tce.mt.gov.br/saiba-mais)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-123** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=c3nugtog5vcM4mLbMGQMH4ZR6j0tv2SCQVmBBW89](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=c3nugtog5vcM4mLbMGQMH4ZR6j0tv2SCQVmBBW89)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-124** — [https://www.tce.mt.gov.br/acessibilidade-do-portal](https://www.tce.mt.gov.br/acessibilidade-do-portal)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-125** — [https://www.tce.mt.gov.br/tribunal-pleno](https://www.tce.mt.gov.br/tribunal-pleno)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-126** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=E4zr95MYqcMMpFIyAv3bxdULkrKT93S4cAEKdCj0](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=E4zr95MYqcMMpFIyAv3bxdULkrKT93S4cAEKdCj0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-127** — [https://www.tce.mt.gov.br/a-instituicao-identidade](https://www.tce.mt.gov.br/a-instituicao-identidade)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-128** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=TgpcUAJPXb1c6x5QFLgIkps8DmzkiZRWUzSZqCCJ](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=TgpcUAJPXb1c6x5QFLgIkps8DmzkiZRWUzSZqCCJ)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-129** — [https://www.tce.mt.gov.br/instituto-memoria-conselheiros-e-procuradores/1170](https://www.tce.mt.gov.br/instituto-memoria-conselheiros-e-procuradores/1170)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-130** — [https://www.tce.mt.gov.br/instituto-memoria-sobre/1147](https://www.tce.mt.gov.br/instituto-memoria-sobre/1147)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-131** — [https://www.tce.mt.gov.br/instituto-memoria-sobre](https://www.tce.mt.gov.br/instituto-memoria-sobre)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-132** — [https://www.tce.mt.gov.br/instituto-memoria-mesas-diretoras/1171](https://www.tce.mt.gov.br/instituto-memoria-mesas-diretoras/1171)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-133** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=B1FYllri2k0Au24r9NBZEF8MUSAAqzKLaNxcDkHy](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=B1FYllri2k0Au24r9NBZEF8MUSAAqzKLaNxcDkHy)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-134** — [https://www.tce.mt.gov.br/instituto-memoria-galeria/1148](https://www.tce.mt.gov.br/instituto-memoria-galeria/1148)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-135** — [https://www.tce.mt.gov.br/conheca-o-tribunal](https://www.tce.mt.gov.br/conheca-o-tribunal)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-136** — [https://www.tce.mt.gov.br/logomarca-tce-mt/930](https://www.tce.mt.gov.br/logomarca-tce-mt/930)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-137** — [https://www.tce.mt.gov.br/bandeira-do-tce/20](https://www.tce.mt.gov.br/bandeira-do-tce/20)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-138** — [https://www.tce.mt.gov.br/coral/19](https://www.tce.mt.gov.br/coral/19)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-139** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CEFx4mkRbLTa3fOpI52ZoxTikT1BGWPs5QcM0hAm](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CEFx4mkRbLTa3fOpI52ZoxTikT1BGWPs5QcM0hAm)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-140** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=ughJ7gaXkYigsMDrB02Ta34juzMEOsQigV9nA3mr](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=ughJ7gaXkYigsMDrB02Ta34juzMEOsQigV9nA3mr)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-141** — [https://www.tce.mt.gov.br/publico-de-relacionamento](https://www.tce.mt.gov.br/publico-de-relacionamento)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-142** — [https://www.tce.mt.gov.br/corregedoria-institucional](https://www.tce.mt.gov.br/corregedoria-institucional)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-143** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=PXntxmST3XoGHasHnNuq0LjcW3rKSMpW3gBtBd8M](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=PXntxmST3XoGHasHnNuq0LjcW3rKSMpW3gBtBd8M)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-144** — [https://www.tce.mt.gov.br/competencias-do-tce](https://www.tce.mt.gov.br/competencias-do-tce)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-145** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia](https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-147** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-146** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade](https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-148** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma](https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-149** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica](https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-150** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos](https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-151** — [https://escolasuperiordecontas.tce.mt.gov.br/calendario](https://escolasuperiordecontas.tce.mt.gov.br/calendario)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-153** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-152** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro](https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-154** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho](https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-156** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-158** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-157** — [https://escolasuperiordecontas.tce.mt.gov.br/noticias](https://escolasuperiordecontas.tce.mt.gov.br/noticias)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-159** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-160** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire](https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-155** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites](https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-161** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos](https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-162** — [https://escolasuperiordecontas.tce.mt.gov.br/acervo](https://escolasuperiordecontas.tce.mt.gov.br/acervo)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-165** — [https://ead.tce.mt.gov.br/ava](https://ead.tce.mt.gov.br/ava)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-166** — [https://sga.tce.mt.gov.br/painel-aluno](https://sga.tce.mt.gov.br/painel-aluno)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-163** — [https://escolasuperiordecontas.tce.mt.gov.br/contato](https://escolasuperiordecontas.tce.mt.gov.br/contato)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-164** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao](https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-169** — [https://conta.tce.mt.gov.br/login](https://conta.tce.mt.gov.br/login)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-168** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-170** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-167** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades](https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-172** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, segurança, https


- **ev-173** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-176** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, segurança, https


- **ev-175** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao](https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-177** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-171** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, segurança, https


- **ev-178** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-179** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841](https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-174** — [https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais](https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-180** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801](https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, segurança, https


- **ev-182** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783](https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-181** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821](https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-187** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nVqtrKuOH77crlZTMbGJMoEIWAxswARRPaGveLoG](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nVqtrKuOH77crlZTMbGJMoEIWAxswARRPaGveLoG)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-184** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741](https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-188** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=M9jvFGWMuyArpvJevmneEyNcyIeWgvGxVomE0bMT](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=M9jvFGWMuyArpvJevmneEyNcyIeWgvGxVomE0bMT)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-183** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782](https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-189** — [https://www.tce.mt.gov.br/produtos-e-processos](https://www.tce.mt.gov.br/produtos-e-processos)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-185** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias](https://escolasuperiordecontas.tce.mt.gov.br/galerias)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-186** — [https://escolasuperiordecontas.tce.mt.gov.br/mapa](https://escolasuperiordecontas.tce.mt.gov.br/mapa)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: certificado, https


- **ev-191** — [https://www.tce.mt.gov.br/sobre-o-comite/1143](https://www.tce.mt.gov.br/sobre-o-comite/1143)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-190** — [https://www.tce.mt.gov.br/lgpd-boas-praticas-e-governanca/1079](https://www.tce.mt.gov.br/lgpd-boas-praticas-e-governanca/1079)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-192** — [https://www.tce.mt.gov.br/sobre-a-comissao/1144](https://www.tce.mt.gov.br/sobre-a-comissao/1144)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-193** — [https://www.tce.mt.gov.br/lgpd-programa-de-governanca-de-privacidade-de-dados/1086](https://www.tce.mt.gov.br/lgpd-programa-de-governanca-de-privacidade-de-dados/1086)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-194** — [https://www.tce.mt.gov.br/lgpd-alertas-e-recomendacoes/1093](https://www.tce.mt.gov.br/lgpd-alertas-e-recomendacoes/1093)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-196** — [https://www.tce.mt.gov.br/lgpd-plano-de-adequacao/1095](https://www.tce.mt.gov.br/lgpd-plano-de-adequacao/1095)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-195** — [https://www.tce.mt.gov.br/lgpd-no-tce-mt/1080](https://www.tce.mt.gov.br/lgpd-no-tce-mt/1080)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-197** — [https://www.tce.mt.gov.br/lgpd-central-de-conteudo/1081](https://www.tce.mt.gov.br/lgpd-central-de-conteudo/1081)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-198** — [https://www.tce.mt.gov.br/lgpd-dicas-de-seguranca/1105](https://www.tce.mt.gov.br/lgpd-dicas-de-seguranca/1105)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-199** — [https://www.tce.mt.gov.br/lgpd-legislacao/1082](https://www.tce.mt.gov.br/lgpd-legislacao/1082)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-200** — [https://www.tce.mt.gov.br/lgpd-politicas-tce/1145](https://www.tce.mt.gov.br/lgpd-politicas-tce/1145)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-201** — [https://www.tce.mt.gov.br/lgpd-contato/1085](https://www.tce.mt.gov.br/lgpd-contato/1085)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-202** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=BB6iTpKLY374FS1cVoAbiZSAdczHAqDC8X1W9aU0](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=BB6iTpKLY374FS1cVoAbiZSAdczHAqDC8X1W9aU0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-203** — [https://www.tce.mt.gov.br/lgpd-faq/1084](https://www.tce.mt.gov.br/lgpd-faq/1084)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-204** — [https://www.tce.mt.gov.br/publicacao/gestao-do-tce-mt/2](https://www.tce.mt.gov.br/publicacao/gestao-do-tce-mt/2)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-260** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=tgl8XHqNS8Lq77YNSEHdzr73nLTT8MMLGFUCzw9K](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=tgl8XHqNS8Lq77YNSEHdzr73nLTT8MMLGFUCzw9K)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-269** — [https://servicos.tce.mt.gov.br/login](https://servicos.tce.mt.gov.br/login)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-274** — [https://conta.tce.mt.gov.br/faq](https://conta.tce.mt.gov.br/faq)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-271** — [https://servicos.tce.mt.gov.br/empresas-inidoneas](https://servicos.tce.mt.gov.br/empresas-inidoneas)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-273** — [https://servicos.tce.mt.gov.br/ouvidoria](https://servicos.tce.mt.gov.br/ouvidoria)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-272** — [https://servicos.tce.mt.gov.br/inabilitacao-exercicio](https://servicos.tce.mt.gov.br/inabilitacao-exercicio)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-276** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=4JDkQUVoP6kjUEj2ADWbJVGMAmY7QGvbIsOrk3VQ](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=4JDkQUVoP6kjUEj2ADWbJVGMAmY7QGvbIsOrk3VQ)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-278** — [https://www.tce.mt.gov.br/calendario/02/2026](https://www.tce.mt.gov.br/calendario/02/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-279** — [https://www.tce.mt.gov.br/calendario/01/2026](https://www.tce.mt.gov.br/calendario/01/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-280** — [https://www.tce.mt.gov.br/calendario/04/2026](https://www.tce.mt.gov.br/calendario/04/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-281** — [https://www.tce.mt.gov.br/calendario/03/2026](https://www.tce.mt.gov.br/calendario/03/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-282** — [https://www.tce.mt.gov.br/calendario/05/2026](https://www.tce.mt.gov.br/calendario/05/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-283** — [https://www.tce.mt.gov.br/calendario/06/2026](https://www.tce.mt.gov.br/calendario/06/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-284** — [https://www.tce.mt.gov.br/calendario/07/2026](https://www.tce.mt.gov.br/calendario/07/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-285** — [https://www.tce.mt.gov.br/calendario/08/2026](https://www.tce.mt.gov.br/calendario/08/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-286** — [https://www.tce.mt.gov.br/calendario/09/2026](https://www.tce.mt.gov.br/calendario/09/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-287** — [https://www.tce.mt.gov.br/calendario/10/2026](https://www.tce.mt.gov.br/calendario/10/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-288** — [https://www.tce.mt.gov.br/calendario/11/2026](https://www.tce.mt.gov.br/calendario/11/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-289** — [https://pce.tce.mt.gov.br/juris?ent_codigo=](https://pce.tce.mt.gov.br/juris?ent_codigo=)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-290** — [https://www.tce.mt.gov.br/calendario/12/2026](https://www.tce.mt.gov.br/calendario/12/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-291** — [https://servicos.tce.mt.gov.br/solicitacao](https://servicos.tce.mt.gov.br/solicitacao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-292** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=K8ms2i6Bl26BiMZxpmlmvWSmltCIz618zp9iDdao](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=K8ms2i6Bl26BiMZxpmlmvWSmltCIz618zp9iDdao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-293** — [https://www.tce.mt.gov.br/sistemas-tecnicos-aplic-2](https://www.tce.mt.gov.br/sistemas-tecnicos-aplic-2)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-295** — [https://www.tce.mt.gov.br/arquivos/11866/f52a69bfa11ce08d1ac774dc580c395c81b84921/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/11866/f52a69bfa11ce08d1ac774dc580c395c81b84921/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-296** — [https://www.tce.mt.gov.br/arquivos/12335/93042288111db943a05592e4d8c34cf2460087de/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/12335/93042288111db943a05592e4d8c34cf2460087de/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-297** — [https://www.tce.mt.gov.br/arquivos/11763/a8f3e0adefc259f8b59477f23363150132340fd0/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/11763/a8f3e0adefc259f8b59477f23363150132340fd0/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-298** — [https://www.tce.mt.gov.br/arquivos/8780/e3c09e2da8d747a37a7d66340fc813bedb7b86d6/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/8780/e3c09e2da8d747a37a7d66340fc813bedb7b86d6/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-294** — [https://servicos.tce.mt.gov.br/log](https://servicos.tce.mt.gov.br/log)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-299** — [https://www.tce.mt.gov.br/acesso-externo/1014](https://www.tce.mt.gov.br/acesso-externo/1014)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-300** — [https://www.tce.mt.gov.br/arquivos/7588/2f2743bcfa5709b0b07eda5b93372129a1268efe/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7588/2f2743bcfa5709b0b07eda5b93372129a1268efe/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-301** — [https://www.tce.mt.gov.br/arquivos/7574/a562994b2af650b6bda2cc63516028e7ebd4525d/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7574/a562994b2af650b6bda2cc63516028e7ebd4525d/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-302** — [https://www.tce.mt.gov.br/arquivos/7584/546c25dbc5a78fee76a7b371f80b3861fc6aacd3/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7584/546c25dbc5a78fee76a7b371f80b3861fc6aacd3/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-303** — [https://www.tce.mt.gov.br/arquivos/7520/6178982ce0253b205512af52de7c7de7b3a11cd6/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7520/6178982ce0253b205512af52de7c7de7b3a11cd6/7594/d0a1198ede31e46b900227ca59244b105fef0394)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-304** — [https://servicos.tce.mt.gov.br/certidao/lista](https://servicos.tce.mt.gov.br/certidao/lista)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-306** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=zBYEGrZBKPFQdgDGa7NRXO1eXg6t6SeN7OZdG4Gl](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=zBYEGrZBKPFQdgDGa7NRXO1eXg6t6SeN7OZdG4Gl)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-307** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=uEk2k26EuiIIw9SWoJycGQkeWw5UnolcP6Ry07Uc](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=uEk2k26EuiIIw9SWoJycGQkeWw5UnolcP6Ry07Uc)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-309** — [https://servicos.tce.mt.gov.br/diario-writer](https://servicos.tce.mt.gov.br/diario-writer)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-305** — [https://servicos.tce.mt.gov.br/certidao/emissao](https://servicos.tce.mt.gov.br/certidao/emissao)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-310** — [https://www.tce.mt.gov.br/conteudo/sid/639](https://www.tce.mt.gov.br/conteudo/sid/639)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-311** — [https://www.tce.mt.gov.br/contas/municipais](https://www.tce.mt.gov.br/contas/municipais)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-308** — [https://servicos.tce.mt.gov.br/certidao/pedido-acompanhamento](https://servicos.tce.mt.gov.br/certidao/pedido-acompanhamento)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-313** — [https://www.tce.mt.gov.br/conteudo/sid/638](https://www.tce.mt.gov.br/conteudo/sid/638)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-314** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=yqOxnp9LrfmQC3PRdyscvEakpmz1nr0xgcvtAzsL](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=yqOxnp9LrfmQC3PRdyscvEakpmz1nr0xgcvtAzsL)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-315** — [https://www.tce.mt.gov.br/contas/assembleia-legislativa](https://www.tce.mt.gov.br/contas/assembleia-legislativa)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-312** — [https://limesurvey.tce.mt.gov.br/index.php/425193](https://limesurvey.tce.mt.gov.br/index.php/425193)
  - Status: Confirmado | Confiança: Alta (85%)
  - Página servida via HTTPS com referências a segurança.
  - Termos: segurança, https


- **ev-316** — [https://www.tce.mt.gov.br/contas/governo](https://www.tce.mt.gov.br/contas/governo)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-317** — [https://www.tce.mt.gov.br/contas/tj](https://www.tce.mt.gov.br/contas/tj)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-318** — [https://www.tce.mt.gov.br/contas/tce](https://www.tce.mt.gov.br/contas/tce)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-319** — [https://www.tce.mt.gov.br/contas/ministerio-publico](https://www.tce.mt.gov.br/contas/ministerio-publico)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-320** — [https://www.tce.mt.gov.br/contas/defensoria-publica](https://www.tce.mt.gov.br/contas/defensoria-publica)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-321** — [https://www.tce.mt.gov.br/contas/esfera/estadual](https://www.tce.mt.gov.br/contas/esfera/estadual)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-322** — [https://www.tce.mt.gov.br/contas/esfera/municipal](https://www.tce.mt.gov.br/contas/esfera/municipal)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-323** — [https://www.tce.mt.gov.br/processo/1915584/2024](https://www.tce.mt.gov.br/processo/1915584/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-324** — [https://www.tce.mt.gov.br/processo/1784390/2024](https://www.tce.mt.gov.br/processo/1784390/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-325** — [https://www.tce.mt.gov.br/processo/478792/2023](https://www.tce.mt.gov.br/processo/478792/2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-326** — [https://www.tce.mt.gov.br/processo/540234/2021](https://www.tce.mt.gov.br/processo/540234/2021)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-327** — [https://www.tce.mt.gov.br/processo/221538/2020](https://www.tce.mt.gov.br/processo/221538/2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-328** — [https://www.tce.mt.gov.br/processo/243370/2019](https://www.tce.mt.gov.br/processo/243370/2019)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-329** — [https://www.tce.mt.gov.br/processo/8567/2019](https://www.tce.mt.gov.br/processo/8567/2019)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-330** — [https://www.tce.mt.gov.br/processo/81710/2018](https://www.tce.mt.gov.br/processo/81710/2018)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-331** — [https://www.tce.mt.gov.br/processo/120413/2016](https://www.tce.mt.gov.br/processo/120413/2016)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-332** — [https://www.tce.mt.gov.br/processo/23396/2015](https://www.tce.mt.gov.br/processo/23396/2015)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-333** — [https://www.tce.mt.gov.br/processo/81760/2014](https://www.tce.mt.gov.br/processo/81760/2014)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-334** — [https://www.tce.mt.gov.br/processo/75493/2014](https://www.tce.mt.gov.br/processo/75493/2014)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-335** — [https://www.tce.mt.gov.br/processo/60844/2011](https://www.tce.mt.gov.br/processo/60844/2011)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-336** — [https://www.tce.mt.gov.br/processo/70017/2010](https://www.tce.mt.gov.br/processo/70017/2010)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-337** — [https://www.tce.mt.gov.br/processo/92797/2013](https://www.tce.mt.gov.br/processo/92797/2013)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-338** — [https://www.tce.mt.gov.br/processo/67369/2012](https://www.tce.mt.gov.br/processo/67369/2012)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-339** — [https://www.tce.mt.gov.br/processo/69639/2009](https://www.tce.mt.gov.br/processo/69639/2009)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-340** — [https://www.tce.mt.gov.br/processo/58963/2008](https://www.tce.mt.gov.br/processo/58963/2008)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-341** — [https://www.tce.mt.gov.br/processo/56219/2007](https://www.tce.mt.gov.br/processo/56219/2007)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-343** — [https://www.tce.mt.gov.br/processo/87106/2004](https://www.tce.mt.gov.br/processo/87106/2004)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-342** — [https://www.tce.mt.gov.br/processo/47210/2006](https://www.tce.mt.gov.br/processo/47210/2006)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-344** — [https://www.tce.mt.gov.br/processo/97977/2005](https://www.tce.mt.gov.br/processo/97977/2005)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-345** — [https://www.tce.mt.gov.br/processo/29459/2014](https://www.tce.mt.gov.br/processo/29459/2014)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-346** — [https://www.tce.mt.gov.br/processo/71480/2013](https://www.tce.mt.gov.br/processo/71480/2013)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-347** — [https://www.tce.mt.gov.br/processo/123633/2012](https://www.tce.mt.gov.br/processo/123633/2012)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-348** — [https://www.tce.mt.gov.br/processo/141860/2011](https://www.tce.mt.gov.br/processo/141860/2011)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-349** — [https://www.tce.mt.gov.br/processo/40070/2011](https://www.tce.mt.gov.br/processo/40070/2011)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-351** — [https://www.tce.mt.gov.br/processo/45756/2007](https://www.tce.mt.gov.br/processo/45756/2007)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-350** — [https://www.tce.mt.gov.br/processo/60429/2009](https://www.tce.mt.gov.br/processo/60429/2009)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-352** — [https://www.tce.mt.gov.br/processo/35815/2006](https://www.tce.mt.gov.br/processo/35815/2006)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-353** — [https://www.tce.mt.gov.br/processo/45748/2008](https://www.tce.mt.gov.br/processo/45748/2008)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-354** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=1fPk0wkgFZu8KKFSxK5eQ0HrGH4hA1tVrr1DnzHW](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=1fPk0wkgFZu8KKFSxK5eQ0HrGH4hA1tVrr1DnzHW)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-355** — [https://www.tce.mt.gov.br/processo/60089/2010](https://www.tce.mt.gov.br/processo/60089/2010)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-356** — [https://www.tce.mt.gov.br/sistemas-tecnicos-geo-obras-2](https://www.tce.mt.gov.br/sistemas-tecnicos-geo-obras-2)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-358** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=VyrLly47HF90Fs4FKGHINLV33zF2oWURZuUef6DQ](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=VyrLly47HF90Fs4FKGHINLV33zF2oWURZuUef6DQ)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-357** — [https://www.tce.mt.gov.br/geo-obras-jurisdicionado/171](https://www.tce.mt.gov.br/geo-obras-jurisdicionado/171)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-359** — [https://www.tce.mt.gov.br/como-funciona/1025](https://www.tce.mt.gov.br/como-funciona/1025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-360** — [https://www.tce.mt.gov.br/como-aderir/1026](https://www.tce.mt.gov.br/como-aderir/1026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-361** — [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-362** — [https://www.tce.mt.gov.br/acesso-aos-materiais-de-apoio/1029](https://www.tce.mt.gov.br/acesso-aos-materiais-de-apoio/1029)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-363** — [https://www.tce.mt.gov.br/mapas-estrategicos-2023-2034/1049](https://www.tce.mt.gov.br/mapas-estrategicos-2023-2034/1049)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-364** — [https://www.tce.mt.gov.br/resultados/1033](https://www.tce.mt.gov.br/resultados/1033)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-366** — [https://gpe2.tce.mt.gov.br/](https://gpe2.tce.mt.gov.br/)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-365** — [https://servicos.tce.mt.gov.br/consulta-item/solicitacao/acompanhamento](https://servicos.tce.mt.gov.br/consulta-item/solicitacao/acompanhamento)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-369** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=gEYCSMwye1WjfZiyAbJsQinOD5zjLEVRkz6mXhuK](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=gEYCSMwye1WjfZiyAbJsQinOD5zjLEVRkz6mXhuK)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-371** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2026](https://www.tce.mt.gov.br/julgamento/presencial?ano=2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-372** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CGMbbZmld9m9ZXEsH1WRQEawpvSFU3zETNx07YXx](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CGMbbZmld9m9ZXEsH1WRQEawpvSFU3zETNx07YXx)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-370** — [https://qapradar.tce.mt.gov.br/extensions/igfm/index.html](https://qapradar.tce.mt.gov.br/extensions/igfm/index.html)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-373** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2024](https://www.tce.mt.gov.br/julgamento/presencial?ano=2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-374** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2023](https://www.tce.mt.gov.br/julgamento/presencial?ano=2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-375** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2025](https://www.tce.mt.gov.br/julgamento/presencial?ano=2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-376** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2021](https://www.tce.mt.gov.br/julgamento/presencial?ano=2021)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-367** — [https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026](https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-379** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2019](https://www.tce.mt.gov.br/julgamento/presencial?ano=2019)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-378** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2020](https://www.tce.mt.gov.br/julgamento/presencial?ano=2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-377** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2022](https://www.tce.mt.gov.br/julgamento/presencial?ano=2022)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-380** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2018](https://www.tce.mt.gov.br/julgamento/presencial?ano=2018)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-368** — [https://servicos.tce.mt.gov.br/consulta-item/historico](https://servicos.tce.mt.gov.br/consulta-item/historico)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-384** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2012](https://www.tce.mt.gov.br/julgamento/presencial?ano=2012)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-381** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2017](https://www.tce.mt.gov.br/julgamento/presencial?ano=2017)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-382** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2015](https://www.tce.mt.gov.br/julgamento/presencial?ano=2015)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-383** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2016](https://www.tce.mt.gov.br/julgamento/presencial?ano=2016)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-385** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2014](https://www.tce.mt.gov.br/julgamento/presencial?ano=2014)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-386** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2011](https://www.tce.mt.gov.br/julgamento/presencial?ano=2011)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-387** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2013](https://www.tce.mt.gov.br/julgamento/presencial?ano=2013)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-389** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2009](https://www.tce.mt.gov.br/julgamento/presencial?ano=2009)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-388** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2010](https://www.tce.mt.gov.br/julgamento/presencial?ano=2010)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-390** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=02-06-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=02-06-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-392** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-S-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-S-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-391** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=09-06-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=09-06-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-394** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2008](https://www.tce.mt.gov.br/julgamento/presencial?ano=2008)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-393** — [https://www.tce.mt.gov.br/julgamento/presencial?ano=2007](https://www.tce.mt.gov.br/julgamento/presencial?ano=2007)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-395** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-397** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=14-04-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=14-04-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-396** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=28-04-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=28-04-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-398** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-03-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-03-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-399** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=17-03-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=17-03-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-400** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=19-05-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=19-05-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-401** — [https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-02-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-02-2026-O-0)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-402** — [https://www.tce.mt.gov.br/processo/2724227/2026](https://www.tce.mt.gov.br/processo/2724227/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-404** — [https://www.tce.mt.gov.br/processo/2741911/2026](https://www.tce.mt.gov.br/processo/2741911/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-403** — [https://www.tce.mt.gov.br/processo/2724251/2026](https://www.tce.mt.gov.br/processo/2724251/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-405** — [https://www.tce.mt.gov.br/processo/2758008/2026](https://www.tce.mt.gov.br/processo/2758008/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-406** — [https://www.tce.mt.gov.br/processo/2727064/2026](https://www.tce.mt.gov.br/processo/2727064/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-407** — [https://www.tce.mt.gov.br/processo/1961071/2025](https://www.tce.mt.gov.br/processo/1961071/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-409** — [https://www.tce.mt.gov.br/processo/2054531/2025](https://www.tce.mt.gov.br/processo/2054531/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-408** — [https://www.tce.mt.gov.br/processo/110795/2020](https://www.tce.mt.gov.br/processo/110795/2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-410** — [https://www.tce.mt.gov.br/processo/2002442/2025](https://www.tce.mt.gov.br/processo/2002442/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-411** — [https://www.tce.mt.gov.br/processo/1988735/2025](https://www.tce.mt.gov.br/processo/1988735/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-412** — [https://www.tce.mt.gov.br/processo/1887602/2024](https://www.tce.mt.gov.br/processo/1887602/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-413** — [https://www.tce.mt.gov.br/processo/2713721/2026](https://www.tce.mt.gov.br/processo/2713721/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-414** — [https://www.tce.mt.gov.br/processo/1805290/2024](https://www.tce.mt.gov.br/processo/1805290/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-415** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nkA5eNEJsZRGHCQ2QJkYX7MsBWMiDSpRMM0kezGX](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nkA5eNEJsZRGHCQ2QJkYX7MsBWMiDSpRMM0kezGX)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-416** — [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=bB28sxNrtSiBx7ubEW6AJQrNwLbygDw8D9WsoqAo](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=bB28sxNrtSiBx7ubEW6AJQrNwLbygDw8D9WsoqAo)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-417** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2025](https://www.tce.mt.gov.br/julgamento/virtual?ano=2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-418** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2024](https://www.tce.mt.gov.br/julgamento/virtual?ano=2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-419** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2023](https://www.tce.mt.gov.br/julgamento/virtual?ano=2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-420** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2026](https://www.tce.mt.gov.br/julgamento/virtual?ano=2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-421** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2021](https://www.tce.mt.gov.br/julgamento/virtual?ano=2021)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-422** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2020](https://www.tce.mt.gov.br/julgamento/virtual?ano=2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-423** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2022](https://www.tce.mt.gov.br/julgamento/virtual?ano=2022)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-424** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2018](https://www.tce.mt.gov.br/julgamento/virtual?ano=2018)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-425** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2019](https://www.tce.mt.gov.br/julgamento/virtual?ano=2019)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-426** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2017](https://www.tce.mt.gov.br/julgamento/virtual?ano=2017)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-427** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2014](https://www.tce.mt.gov.br/julgamento/virtual?ano=2014)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-428** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2013](https://www.tce.mt.gov.br/julgamento/virtual?ano=2013)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-429** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2012](https://www.tce.mt.gov.br/julgamento/virtual?ano=2012)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-430** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2015](https://www.tce.mt.gov.br/julgamento/virtual?ano=2015)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-431** — [https://www.tce.mt.gov.br/julgamento/virtual?ano=2016](https://www.tce.mt.gov.br/julgamento/virtual?ano=2016)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-432** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=25-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=25-05-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-433** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=18-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=18-05-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-434** — [https://www.tce.mt.gov.br/julgamento/virtual/estatisticas?ano=2026](https://www.tce.mt.gov.br/julgamento/virtual/estatisticas?ano=2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-435** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=11-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=11-05-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-436** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=04-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=04-05-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-437** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-03-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-438** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=13-04-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=13-04-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-439** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=06-04-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=06-04-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-440** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=09-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=09-03-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-441** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=16-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=16-03-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-442** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=02-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=02-03-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-443** — [https://www.tce.mt.gov.br/processo/2052164/2025](https://www.tce.mt.gov.br/processo/2052164/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-445** — [https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-02-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-02-2026-V-3)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-447** — [https://www.tce.mt.gov.br/processo/2052172/2025](https://www.tce.mt.gov.br/processo/2052172/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-444** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052164/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052164/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-446** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052164/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052164/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-450** — [https://www.tce.mt.gov.br/processo/1961179/2025](https://www.tce.mt.gov.br/processo/1961179/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-448** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052172/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052172/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-452** — [https://www.tce.mt.gov.br/processo/1983881/2025](https://www.tce.mt.gov.br/processo/1983881/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-451** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1961179/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1961179/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-453** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1961179/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1961179/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-449** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052172/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052172/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-456** — [https://www.tce.mt.gov.br/processo/13307/2021](https://www.tce.mt.gov.br/processo/13307/2021)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-455** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1983881/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1983881/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-454** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1983881/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1983881/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-459** — [https://www.tce.mt.gov.br/processo/2044137/2025](https://www.tce.mt.gov.br/processo/2044137/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-457** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/13307/2021](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/13307/2021)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-458** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/13307/2021](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/13307/2021)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-462** — [https://www.tce.mt.gov.br/processo/2035111/2025](https://www.tce.mt.gov.br/processo/2035111/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-460** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2044137/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2044137/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-461** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2044137/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2044137/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-463** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035111/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035111/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-464** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035111/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035111/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-467** — [https://www.tce.mt.gov.br/processo/2707098/2026](https://www.tce.mt.gov.br/processo/2707098/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-468** — [https://www.tce.mt.gov.br/processo/2060302/2025](https://www.tce.mt.gov.br/processo/2060302/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-465** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2060302/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2060302/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-471** — [https://www.tce.mt.gov.br/processo/1921860/2024](https://www.tce.mt.gov.br/processo/1921860/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-466** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2060302/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2060302/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-469** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2707098/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2707098/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-470** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2707098/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2707098/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-472** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1921860/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1921860/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-476** — [https://www.tce.mt.gov.br/processo/1819712/2024](https://www.tce.mt.gov.br/processo/1819712/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-474** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1819712/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1819712/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-473** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1819712/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1819712/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-477** — [https://www.tce.mt.gov.br/processo/2035839/2025](https://www.tce.mt.gov.br/processo/2035839/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-480** — [https://www.tce.mt.gov.br/processo/1817485/2024](https://www.tce.mt.gov.br/processo/1817485/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-475** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1921860/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1921860/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-478** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035839/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035839/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-479** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035839/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035839/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-482** — [https://www.tce.mt.gov.br/processo/2112710/2025](https://www.tce.mt.gov.br/processo/2112710/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-481** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1817485/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1817485/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-483** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2112710/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2112710/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-484** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1817485/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1817485/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-486** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2713721/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2713721/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-485** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2112710/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2112710/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-487** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/186449/2020](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/186449/2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-489** — [https://www.tce.mt.gov.br/processo/186449/2020](https://www.tce.mt.gov.br/processo/186449/2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-488** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2713721/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2713721/2026)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-493** — [https://www.tce.mt.gov.br/processo/1808176/2024](https://www.tce.mt.gov.br/processo/1808176/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-491** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1808176/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1808176/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-490** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/186449/2020](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/186449/2020)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-492** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1808176/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1808176/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-494** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1805290/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1805290/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-496** — [https://www.tce.mt.gov.br/processo/2088428/2025](https://www.tce.mt.gov.br/processo/2088428/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-495** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1805290/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1805290/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-497** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2088428/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2088428/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-501** — [https://www.tce.mt.gov.br/processo/500470/2023](https://www.tce.mt.gov.br/processo/500470/2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-498** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2088428/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2088428/2025)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-502** — [https://www.tce.mt.gov.br/processo/1819402/2024](https://www.tce.mt.gov.br/processo/1819402/2024)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-503** — [https://www.tce.mt.gov.br/processo/635456/2023](https://www.tce.mt.gov.br/processo/635456/2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-500** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/500470/2023](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/500470/2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https


- **ev-499** — [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/500470/2023](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/500470/2023)
  - Status: Confirmado | Confiança: Média (65%)
  - Página servida via HTTPS.
  - Termos: https





### 4.6 Cookies

| Campo | Valor |
|-------|-------|
| **Status** | Confirmado |
| **Confiança** | Alta (85%) |
| **Achados** | 64 |
| **Evidências** | ev-002, ev-007, ev-009, ev-017, ev-014, ev-028, ev-029, ev-034, ev-038, ev-044, ev-046, ev-050, ev-060, ev-066, ev-073, ev-075, ev-080, ev-079, ev-081, ev-082, ev-092, ev-093, ev-094, ev-091, ev-145, ev-147, ev-146, ev-148, ev-149, ev-150, ev-151, ev-153, ev-152, ev-154, ev-156, ev-158, ev-157, ev-159, ev-160, ev-155, ev-161, ev-162, ev-165, ev-163, ev-164, ev-168, ev-170, ev-167, ev-172, ev-173, ev-176, ev-175, ev-177, ev-171, ev-178, ev-179, ev-174, ev-180, ev-182, ev-181, ev-184, ev-183, ev-185, ev-186 |
| **Fundamentação** | art. 7 LGPD, art. 9 LGPD |




**Detalhes dos achados:**


- **ev-002** — [https://www.tce.mt.gov.br/corpo-deliberativo/15](https://www.tce.mt.gov.br/corpo-deliberativo/15)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-007** — [https://www.tce.mt.gov.br/tribunal-pleno/609](https://www.tce.mt.gov.br/tribunal-pleno/609)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-009** — [https://www.tce.mt.gov.br/instituto-memoria](https://www.tce.mt.gov.br/instituto-memoria)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-017** — [https://www.tce.mt.gov.br/planejamento-estrategico/704](https://www.tce.mt.gov.br/planejamento-estrategico/704)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-014** — [https://escolasuperiordecontas.tce.mt.gov.br/](https://escolasuperiordecontas.tce.mt.gov.br/)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-028** — [https://www.tce.mt.gov.br/assinatura](https://www.tce.mt.gov.br/assinatura)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-029** — [https://servicos.tce.mt.gov.br/aplic/remessa](https://servicos.tce.mt.gov.br/aplic/remessa)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-034** — [https://www.tce.mt.gov.br/geo-obras/486](https://www.tce.mt.gov.br/geo-obras/486)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-038** — [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-044** — [https://www.tce.mt.gov.br/documentos](https://www.tce.mt.gov.br/documentos)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-046** — [https://www.tce.mt.gov.br/processos](https://www.tce.mt.gov.br/processos)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-050** — [https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-060** — [https://www.tce.mt.gov.br/legislacoes/prejulgados](https://www.tce.mt.gov.br/legislacoes/prejulgados)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-066** — [https://www.tce.mt.gov.br/tvcontas](https://www.tce.mt.gov.br/tvcontas)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-073** — [https://www.tce.mt.gov.br/tipos-de-manifestacoes/724](https://www.tce.mt.gov.br/tipos-de-manifestacoes/724)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-075** — [https://www.tce.mt.gov.br/mapa-da-transparencia/731](https://www.tce.mt.gov.br/mapa-da-transparencia/731)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-080** — [https://www.tce.mt.gov.br/plano-de-acao/984](https://www.tce.mt.gov.br/plano-de-acao/984)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-079** — [https://www.tce.mt.gov.br/quadrimestral/949](https://www.tce.mt.gov.br/quadrimestral/949)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-081** — [https://www.tce.mt.gov.br/ouvidoria-organizacional](https://www.tce.mt.gov.br/ouvidoria-organizacional)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-082** — [https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-092** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-093** — [https://www.tce.mt.gov.br/agenda](https://www.tce.mt.gov.br/agenda)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-094** — [https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797](https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-091** — [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-145** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia](https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-147** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-146** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade](https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-148** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma](https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-149** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica](https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-150** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos](https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-151** — [https://escolasuperiordecontas.tce.mt.gov.br/calendario](https://escolasuperiordecontas.tce.mt.gov.br/calendario)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-153** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-152** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro](https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-154** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho](https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-156** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-158** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-157** — [https://escolasuperiordecontas.tce.mt.gov.br/noticias](https://escolasuperiordecontas.tce.mt.gov.br/noticias)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-159** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-160** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire](https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-155** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites](https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-161** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos](https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-162** — [https://escolasuperiordecontas.tce.mt.gov.br/acervo](https://escolasuperiordecontas.tce.mt.gov.br/acervo)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-165** — [https://ead.tce.mt.gov.br/ava](https://ead.tce.mt.gov.br/ava)
  - Status: Confirmado | Confiança: Alta (85%)
  - Política ou banner de cookies identificado.
  - Termos: cookie, cookies


- **ev-163** — [https://escolasuperiordecontas.tce.mt.gov.br/contato](https://escolasuperiordecontas.tce.mt.gov.br/contato)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-164** — [https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao](https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-168** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-170** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-167** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades](https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-172** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-173** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-176** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-175** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao](https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-177** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-171** — [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-178** — [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-179** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841](https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-174** — [https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais](https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-180** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801](https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-182** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783](https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-181** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821](https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-184** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741](https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-183** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782](https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-185** — [https://escolasuperiordecontas.tce.mt.gov.br/galerias](https://escolasuperiordecontas.tce.mt.gov.br/galerias)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies


- **ev-186** — [https://escolasuperiordecontas.tce.mt.gov.br/mapa](https://escolasuperiordecontas.tce.mt.gov.br/mapa)
  - Status: Inferência | Confiança: Média (65%)
  - Referência a cookies encontrada sem banner confirmado.
  - Termos: cookie, cookies






---

## 5. Uso da Inteligência Artificial

A ferramenta LGPD Auditor utiliza **classificadores heurísticos** (não generativos) para análise inicial. A IA generativa **não foi utilizada** nesta fase para emitir conclusões — todas as afirmações derivam de evidências coletadas automaticamente.

Critérios aplicados:
- Evidências verificáveis com `evidence_id`
- Reprodutibilidade via `audit_results.json`
- Em dúvida: `Não Localizado` em vez de inferência sem base

---

## 6. Resultados e Achados

### Resumo executivo


- **4.1** Transparência e política de privacidade: **Confirmado** (Muito Alta, 95%)

- **4.2** Coleta de dados: **Inferência** (Alta, 85%)

- **4.3** Consentimento: **Confirmado** (Alta, 85%)

- **4.4** Direitos do titular: **Confirmado** (Muito Alta, 95%)

- **4.5** Segurança da informação: **Confirmado** (Alta, 85%)

- **4.6** Cookies: **Confirmado** (Alta, 85%)


---

## 7. Recomendações


1. [4.2] Documentar finalidade e base legal em todos os formulários de coleta de dados pessoais.


---

## 8. Conclusão

A auditoria automatizada do portal **Tribunal de Contas do Estado de Mato Grosso** identificou 764 achados em 503 páginas analisadas com evidência documental, sobre 503 rotas visitadas.

Os resultados devem ser interpretados como **diagnóstico exploratório** com apoio de automação, sujeito a revisão humana qualificada antes de qualquer decisão institucional.

---

## 9. Referências

- Lei nº 13.709/2018 (LGPD)
- Autoridade Nacional de Proteção de Dados (ANPD) — [https://www.gov.br/anpd](https://www.gov.br/anpd)
- ISO/IEC 27001:2022 — Segurança da informação
- ISO/IEC 27701:2019 — Privacidade da informação
- OWASP Top 10 — 2021

---

## Diário de Engenharia

### Decisão 1 — fase-0
- **Data:** 2026-07-06T13:08:24.812746+00:00
- **Problema:** Projeto iniciado do zero sem código existente
- **Solução adotada:** Estrutura modular Python com Playwright, governança P0-P8 e legislation.yaml
- **Justificativa:** Atende requisitos MUST da especificação técnica e atividade acadêmica TCE-MT
- **Impacto:** Base para crawler, evidências, auditoria e relatório nas fases seguintes
- **Alternativas descartadas:** Node.js/Puppeteer, Auditoria manual sem automação

### Decisão 2 — fase-0
- **Data:** 2026-07-06T13:15:57.317429+00:00
- **Problema:** Projeto iniciado do zero sem código existente
- **Solução adotada:** Estrutura modular Python com Playwright, governança P0-P8 e legislation.yaml
- **Justificativa:** Atende requisitos MUST da especificação técnica e atividade acadêmica TCE-MT
- **Impacto:** Base para crawler, evidências, auditoria e relatório nas fases seguintes
- **Alternativas descartadas:** Node.js/Puppeteer, Auditoria manual sem automação

### Decisão 3 — fase-1
- **Data:** 2026-07-06T13:16:17.041326+00:00
- **Problema:** Necessidade de navegar o portal TCE-MT com retomada e rastreabilidade
- **Solução adotada:** CrawlerService BFS com Playwright, 5 workers, robots.txt e checkpoints
- **Justificativa:** Atende MUST de crawler, rotas visitadas e reprocessamento incremental
- **Impacto:** Base de URLs e HTML resumido para evidências (Fase 2) e auditoria LGPD (Fase 3)
- **Alternativas descartadas:** httpx sem renderização JS, Crawler sequencial sem workers

### Decisão 4 — fase-2
- **Data:** 2026-07-06T13:41:08.089258+00:00
- **Problema:** Rotas visitadas sem screenshots rastreáveis (screenshot: null)
- **Solução adotada:** EvidenceStore com PNG full-page, metadata.json e index.json por evidence_id
- **Justificativa:** Atende MUST de evidências verificáveis e rastreabilidade 100%
- **Impacto:** Screenshots vinculados ao visited_routes.json para relatório e auditoria LGPD
- **Alternativas descartadas:** Screenshots apenas em memória, Um único arquivo ZIP sem metadados

### Decisão 5 — fase-3
- **Data:** 2026-07-06T13:43:39.685933+00:00
- **Problema:** Necessidade de avaliar conformidade LGPD com evidências rastreáveis
- **Solução adotada:** LGPDRulesEngine + classificadores heurísticos com status e confiança
- **Justificativa:** Atende MUST de auditoria LGPD sem alucinação — achados ancorados em evidence_id
- **Impacto:** audit_results.json pronto para geração de relatório na Fase 4
- **Alternativas descartadas:** IA generativa sem evidências, Checklist manual sem automação

### Decisão 6 — fase-2
- **Data:** 2026-07-06T13:44:31.549019+00:00
- **Problema:** Rotas visitadas sem screenshots rastreáveis (screenshot: null)
- **Solução adotada:** EvidenceStore com PNG full-page, metadata.json e index.json por evidence_id
- **Justificativa:** Atende MUST de evidências verificáveis e rastreabilidade 100%
- **Impacto:** Screenshots vinculados ao visited_routes.json para relatório e auditoria LGPD
- **Alternativas descartadas:** Screenshots apenas em memória, Um único arquivo ZIP sem metadados

### Decisão 7 — fase-4
- **Data:** 2026-07-06T13:47:01.770291+00:00
- **Problema:** Necessidade de relatório estruturado para entrega acadêmica
- **Solução adotada:** ReportGenerator com templates Jinja2, Markdown, HTML e CSV de rotas
- **Justificativa:** Atende MUST de relatório, anexo de rotas e Diário de Engenharia
- **Impacto:** relatorio-lgpd-tce-mt.md pronto para revisão e entrega no AVA
- **Alternativas descartadas:** Relatório manual sem reprodutibilidade, Apenas JSON sem formato legível

### Decisão 8 — fase-5
- **Data:** 2026-07-06T13:48:59.903166+00:00
- **Problema:** Necessidade de PDF, dashboard e síntese para entrega acadêmica
- **Solução adotada:** ExportService com PDF (WeasyPrint), dashboard HTML, síntese restrita e OCR opcional
- **Justificativa:** Atende requisitos SHOULD sem violar política anti-alucinação
- **Impacto:** Artefatos complementares prontos para anexar ao relatório
- **Alternativas descartadas:** IA generativa sem ancoragem em evidence_id, PDF via captura de tela

### Decisão 9 — fase-5
- **Data:** 2026-07-06T13:49:23.025314+00:00
- **Problema:** Necessidade de PDF, dashboard e síntese para entrega acadêmica
- **Solução adotada:** ExportService com PDF (WeasyPrint), dashboard HTML, síntese restrita e OCR opcional
- **Justificativa:** Atende requisitos SHOULD sem violar política anti-alucinação
- **Impacto:** Artefatos complementares prontos para anexar ao relatório
- **Alternativas descartadas:** IA generativa sem ancoragem em evidence_id, PDF via captura de tela


---

## Anexo A — Rotas Visitadas (Evidência de Cobertura)

> Exportação CSV disponível em: `visited_routes.csv`

| Ordem | URL | HTTP | Evidence ID | Screenshot | Visitada em |
|-------|-----|------|-------------|------------|-------------|
| 1 | [https://www.tce.mt.gov.br/](https://www.tce.mt.gov.br/) | 200 | ev-001 | evidence/ev-001/screenshot.png | 2026-07-06T13:16:18.543532+00:00 |
| 2 | [https://www.tce.mt.gov.br/corpo-deliberativo/15](https://www.tce.mt.gov.br/corpo-deliberativo/15) | 200 | ev-002 | evidence/ev-002/screenshot.png | 2026-07-06T13:16:20.423812+00:00 |
| 3 | [https://cartadeservicos.tce.mt.gov.br/](https://cartadeservicos.tce.mt.gov.br/) | 200 | ev-003 | evidence/ev-003/screenshot.png | 2026-07-06T13:16:20.430166+00:00 |
| 4 | [https://www.tce.mt.gov.br/historia/12](https://www.tce.mt.gov.br/historia/12) | 200 | ev-004 | evidence/ev-004/screenshot.png | 2026-07-06T13:16:20.609365+00:00 |
| 5 | [https://www.tce.mt.gov.br/acessibilidade-do-portal/1067](https://www.tce.mt.gov.br/acessibilidade-do-portal/1067) | 200 | ev-005 | evidence/ev-005/screenshot.png | 2026-07-06T13:16:20.640171+00:00 |
| 6 | [https://sic.tce.mt.gov.br/](https://sic.tce.mt.gov.br/) | 200 | ev-006 | evidence/ev-006/screenshot.png | 2026-07-06T13:16:21.000890+00:00 |
| 7 | [https://www.tce.mt.gov.br/tribunal-pleno/609](https://www.tce.mt.gov.br/tribunal-pleno/609) | 200 | ev-007 | evidence/ev-007/screenshot.png | 2026-07-06T13:16:21.676340+00:00 |
| 8 | [https://www.tce.mt.gov.br/identidade/767](https://www.tce.mt.gov.br/identidade/767) | 200 | ev-008 | evidence/ev-008/screenshot.png | 2026-07-06T13:16:21.922180+00:00 |
| 9 | [https://www.tce.mt.gov.br/instituto-memoria](https://www.tce.mt.gov.br/instituto-memoria) | 200 | ev-009 | evidence/ev-009/screenshot.png | 2026-07-06T13:16:22.190010+00:00 |
| 10 | [https://www.tce.mt.gov.br/conheca-o-tribunal/10](https://www.tce.mt.gov.br/conheca-o-tribunal/10) | 200 | ev-010 | evidence/ev-010/screenshot.png | 2026-07-06T13:16:22.856329+00:00 |
| 11 | [https://www.tce.mt.gov.br/publico-de-relacionamento/878](https://www.tce.mt.gov.br/publico-de-relacionamento/878) | 200 | ev-011 | evidence/ev-011/screenshot.png | 2026-07-06T13:16:23.170103+00:00 |
| 12 | [https://www.tce.mt.gov.br/institucional/303](https://www.tce.mt.gov.br/institucional/303) | 200 | ev-012 | evidence/ev-012/screenshot.png | 2026-07-06T13:16:23.405730+00:00 |
| 13 | [https://www.tce.mt.gov.br/competencias-do-tribunal/876](https://www.tce.mt.gov.br/competencias-do-tribunal/876) | 200 | ev-013 | evidence/ev-013/screenshot.png | 2026-07-06T13:16:23.492396+00:00 |
| 14 | [https://escolasuperiordecontas.tce.mt.gov.br/](https://escolasuperiordecontas.tce.mt.gov.br/) | 200 | ev-014 | evidence/ev-014/screenshot.png | 2026-07-06T13:16:24.603793+00:00 |
| 15 | [https://www.tce.mt.gov.br/produtos-e-processos/877](https://www.tce.mt.gov.br/produtos-e-processos/877) | 200 | ev-015 | evidence/ev-015/screenshot.png | 2026-07-06T13:16:24.691529+00:00 |
| 16 | [https://www.tce.mt.gov.br/lgpd](https://www.tce.mt.gov.br/lgpd) | 200 | ev-016 | evidence/ev-016/screenshot.png | 2026-07-06T13:16:25.076144+00:00 |
| 17 | [https://www.tce.mt.gov.br/planejamento-estrategico/704](https://www.tce.mt.gov.br/planejamento-estrategico/704) | 200 | ev-017 | evidence/ev-017/screenshot.png | 2026-07-06T13:16:25.450781+00:00 |
| 18 | [http://www.tce.mt.gov.br/conteudo/index/sid/939](http://www.tce.mt.gov.br/conteudo/index/sid/939) | 200 | ev-018 | evidence/ev-018/screenshot.png | 2026-07-06T13:16:25.479842+00:00 |
| 19 | [https://servicos.tce.mt.gov.br/](https://servicos.tce.mt.gov.br/) | 200 | ev-019 | evidence/ev-019/screenshot.png | 2026-07-06T13:16:25.820929+00:00 |
| 20 | [https://conta.tce.mt.gov.br/](https://conta.tce.mt.gov.br/) | 200 | ev-020 | evidence/ev-020/screenshot.png | 2026-07-06T13:16:25.955447+00:00 |
| 21 | [https://conta.tce.mt.gov.br/conta](https://conta.tce.mt.gov.br/conta) | 200 | ev-021 | evidence/ev-021/screenshot.png | 2026-07-06T13:16:26.076637+00:00 |
| 22 | [https://conta.tce.mt.gov.br/conta/recupera-senha](https://conta.tce.mt.gov.br/conta/recupera-senha) | 200 | ev-022 | evidence/ev-022/screenshot.png | 2026-07-06T13:16:26.489219+00:00 |
| 23 | [https://servicos.tce.mt.gov.br/fiscalizado/arp](https://servicos.tce.mt.gov.br/fiscalizado/arp) | 200 | ev-023 | evidence/ev-023/screenshot.png | 2026-07-06T13:16:26.661163+00:00 |
| 24 | [https://www.tce.mt.gov.br/calendario](https://www.tce.mt.gov.br/calendario) | 200 | ev-024 | evidence/ev-024/screenshot.png | 2026-07-06T13:16:26.993705+00:00 |
| 25 | [https://servicos.tce.mt.gov.br/tabela-interna](https://servicos.tce.mt.gov.br/tabela-interna) | 200 | ev-025 | evidence/ev-025/screenshot.png | 2026-07-06T13:16:27.008626+00:00 |
| 26 | [https://www.tce.mt.gov.br/aplic/485](https://www.tce.mt.gov.br/aplic/485) | 200 | ev-026 | evidence/ev-026/screenshot.png | 2026-07-06T13:16:27.320339+00:00 |
| 27 | [https://servicos.tce.mt.gov.br/fiscalizado/aplic/envio-carga](https://servicos.tce.mt.gov.br/fiscalizado/aplic/envio-carga) | 200 | ev-027 | evidence/ev-027/screenshot.png | 2026-07-06T13:16:27.594765+00:00 |
| 28 | [https://www.tce.mt.gov.br/assinatura](https://www.tce.mt.gov.br/assinatura) | 200 | ev-028 | evidence/ev-028/screenshot.png | 2026-07-06T13:16:28.208994+00:00 |
| 29 | [https://servicos.tce.mt.gov.br/aplic/remessa](https://servicos.tce.mt.gov.br/aplic/remessa) | 200 | ev-029 | evidence/ev-029/screenshot.png | 2026-07-06T13:16:28.308694+00:00 |
| 30 | [https://www.tce.mt.gov.br/distribuicao](https://www.tce.mt.gov.br/distribuicao) | 200 | ev-030 | evidence/ev-030/screenshot.png | 2026-07-06T13:16:28.741158+00:00 |
| 31 | [https://servicos.tce.mt.gov.br/certidao](https://servicos.tce.mt.gov.br/certidao) | 200 | ev-031 | evidence/ev-031/screenshot.png | 2026-07-06T13:16:29.428219+00:00 |
| 32 | [https://servicos.tce.mt.gov.br/diario](https://servicos.tce.mt.gov.br/diario) | 200 | ev-032 | evidence/ev-032/screenshot.png | 2026-07-06T13:16:29.715644+00:00 |
| 33 | [https://www.tce.mt.gov.br/contas](https://www.tce.mt.gov.br/contas) | 200 | ev-033 | evidence/ev-033/screenshot.png | 2026-07-06T13:16:29.973770+00:00 |
| 34 | [https://www.tce.mt.gov.br/geo-obras/486](https://www.tce.mt.gov.br/geo-obras/486) | 200 | ev-034 | evidence/ev-034/screenshot.png | 2026-07-06T13:16:30.005998+00:00 |
| 35 | [https://servicos.tce.mt.gov.br/consulta-debitos](https://servicos.tce.mt.gov.br/consulta-debitos) | 200 | ev-035 | evidence/ev-035/screenshot.png | 2026-07-06T13:16:30.669965+00:00 |
| 36 | [https://servicos.tce.mt.gov.br/fiscalizado/conta/cadastro](https://servicos.tce.mt.gov.br/fiscalizado/conta/cadastro) | 200 | ev-036 | evidence/ev-036/screenshot.png | 2026-07-06T13:16:30.830379+00:00 |
| 37 | [https://push.tce.mt.gov.br/](https://push.tce.mt.gov.br/) | 200 | ev-037 | evidence/ev-037/screenshot.png | 2026-07-06T13:16:30.960379+00:00 |
| 38 | [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024) | 200 | ev-038 | evidence/ev-038/screenshot.png | 2026-07-06T13:16:31.274058+00:00 |
| 39 | [https://pce.tce.mt.gov.br/juris](https://pce.tce.mt.gov.br/juris) | 200 | ev-039 | evidence/ev-039/screenshot.png | 2026-07-06T13:16:31.923513+00:00 |
| 40 | [https://servicos.tce.mt.gov.br/sessao-virtual/sustentacao-oral](https://servicos.tce.mt.gov.br/sessao-virtual/sustentacao-oral) | 200 | ev-040 | evidence/ev-040/screenshot.png | 2026-07-06T13:16:32.027759+00:00 |
| 41 | [https://servicos.tce.mt.gov.br/consulta-item](https://servicos.tce.mt.gov.br/consulta-item) | 200 | ev-041 | evidence/ev-041/screenshot.png | 2026-07-06T13:16:32.591583+00:00 |
| 42 | [https://servicos.tce.mt.gov.br/audiencias](https://servicos.tce.mt.gov.br/audiencias) | 200 | ev-042 | evidence/ev-042/screenshot.png | 2026-07-06T13:16:32.741078+00:00 |
| 43 | [https://servicos.tce.mt.gov.br/igfm](https://servicos.tce.mt.gov.br/igfm) | 200 | ev-043 | evidence/ev-043/screenshot.png | 2026-07-06T13:16:32.973499+00:00 |
| 44 | [https://www.tce.mt.gov.br/documentos](https://www.tce.mt.gov.br/documentos) | 200 | ev-044 | evidence/ev-044/screenshot.png | 2026-07-06T13:16:33.088361+00:00 |
| 45 | [https://www.tce.mt.gov.br/julgamento/presencial](https://www.tce.mt.gov.br/julgamento/presencial) | 200 | ev-045 | evidence/ev-045/screenshot.png | 2026-07-06T13:16:33.404324+00:00 |
| 46 | [https://www.tce.mt.gov.br/processos](https://www.tce.mt.gov.br/processos) | 200 | ev-046 | evidence/ev-046/screenshot.png | 2026-07-06T13:16:34.016223+00:00 |
| 47 | [https://www.tce.mt.gov.br/julgamento/virtual](https://www.tce.mt.gov.br/julgamento/virtual) | 200 | ev-047 | evidence/ev-047/screenshot.png | 2026-07-06T13:16:35.197302+00:00 |
| 48 | [https://www.tce.mt.gov.br/legislacoes/lei-organica](https://www.tce.mt.gov.br/legislacoes/lei-organica) | 200 | ev-048 | evidence/ev-048/screenshot.png | 2026-07-06T13:16:35.251903+00:00 |
| 49 | [https://www.tce.mt.gov.br/legislacoes/resolucao-normativa](https://www.tce.mt.gov.br/legislacoes/resolucao-normativa) | 200 | ev-049 | evidence/ev-049/screenshot.png | 2026-07-06T13:16:35.586933+00:00 |
| 50 | [https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](https://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo) | 200 | ev-050 | evidence/ev-050/screenshot.png | 2026-07-06T13:16:35.679382+00:00 |
| 51 | [https://www.tce.mt.gov.br/legislacoes/regimento-interno](https://www.tce.mt.gov.br/legislacoes/regimento-interno) | 200 | ev-051 | evidence/ev-051/screenshot.png | 2026-07-06T13:16:35.716455+00:00 |
| 52 | [https://www.tce.mt.gov.br/legislacoes/decisoes-normativas](https://www.tce.mt.gov.br/legislacoes/decisoes-normativas) | 200 | ev-052 | evidence/ev-052/screenshot.png | 2026-07-06T13:16:36.788771+00:00 |
| 53 | [https://www.tce.mt.gov.br/legislacoes/decisoes-administrativas](https://www.tce.mt.gov.br/legislacoes/decisoes-administrativas) | 200 | ev-053 | evidence/ev-053/screenshot.png | 2026-07-06T13:16:37.251345+00:00 |
| 54 | [https://www.tce.mt.gov.br/legislacoes/portarias](https://www.tce.mt.gov.br/legislacoes/portarias) | 200 | ev-054 | evidence/ev-054/screenshot.png | 2026-07-06T13:16:37.442071+00:00 |
| 55 | [https://www.tce.mt.gov.br/legislacoes](https://www.tce.mt.gov.br/legislacoes) | 200 | ev-055 | evidence/ev-055/screenshot.png | 2026-07-06T13:16:37.494817+00:00 |
| 56 | [https://www.tce.mt.gov.br/legislacoes/instrucoes-normativas](https://www.tce.mt.gov.br/legislacoes/instrucoes-normativas) | 200 | ev-056 | evidence/ev-056/screenshot.png | 2026-07-06T13:16:37.968257+00:00 |
| 57 | [https://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32](https://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32) | 200 | ev-057 | evidence/ev-057/screenshot.png | 2026-07-06T13:16:38.165341+00:00 |
| 58 | [https://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta](https://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta) | 200 | ev-058 | evidence/ev-058/screenshot.png | 2026-07-06T13:16:38.567239+00:00 |
| 59 | [https://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21](https://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21) | 200 | ev-059 | evidence/ev-059/screenshot.png | 2026-07-06T13:16:39.057000+00:00 |
| 60 | [https://www.tce.mt.gov.br/legislacoes/prejulgados](https://www.tce.mt.gov.br/legislacoes/prejulgados) | 200 | ev-060 | evidence/ev-060/screenshot.png | 2026-07-06T13:16:39.284868+00:00 |
| 61 | [https://www.tce.mt.gov.br/legislacoes/sumulas](https://www.tce.mt.gov.br/legislacoes/sumulas) | 200 | ev-061 | evidence/ev-061/screenshot.png | 2026-07-06T13:16:39.711497+00:00 |
| 62 | [https://www.tce.mt.gov.br/noticias](https://www.tce.mt.gov.br/noticias) | 200 | ev-062 | evidence/ev-062/screenshot.png | 2026-07-06T13:16:39.834902+00:00 |
| 63 | [https://www.tce.mt.gov.br/publicacao](https://www.tce.mt.gov.br/publicacao) | 200 | ev-063 | evidence/ev-063/screenshot.png | 2026-07-06T13:16:40.381374+00:00 |
| 64 | [https://www.tce.mt.gov.br/galeria](https://www.tce.mt.gov.br/galeria) | 200 | ev-064 | evidence/ev-064/screenshot.png | 2026-07-06T13:16:40.819957+00:00 |
| 65 | [https://sistema7.tce.mt.gov.br/jusconex-externo/tese](https://sistema7.tce.mt.gov.br/jusconex-externo/tese) | 200 | ev-065 | evidence/ev-065/screenshot.png | 2026-07-06T13:16:41.200120+00:00 |
| 66 | [https://www.tce.mt.gov.br/tvcontas](https://www.tce.mt.gov.br/tvcontas) | 200 | ev-066 | evidence/ev-066/screenshot.png | 2026-07-06T13:16:41.239053+00:00 |
| 67 | [https://www.tce.mt.gov.br/artigos](https://www.tce.mt.gov.br/artigos) | 200 | ev-067 | evidence/ev-067/screenshot.png | 2026-07-06T13:16:41.508214+00:00 |
| 68 | [https://www.tce.mt.gov.br/radio-tce/169](https://www.tce.mt.gov.br/radio-tce/169) | 200 | ev-068 | evidence/ev-068/screenshot.png | 2026-07-06T13:16:42.344688+00:00 |
| 69 | [https://radar.tce.mt.gov.br/extensions/radar-da-transparencia-publica/radar-da-transparencia-publica.html](https://radar.tce.mt.gov.br/extensions/radar-da-transparencia-publica/radar-da-transparencia-publica.html) | 200 | ev-069 | evidence/ev-069/screenshot.png | 2026-07-06T13:16:42.418807+00:00 |
| 70 | [https://servicos.tce.mt.gov.br/sic/minhas-solicitacoes](https://servicos.tce.mt.gov.br/sic/minhas-solicitacoes) | 200 | ev-070 | evidence/ev-070/screenshot.png | 2026-07-06T13:16:42.498659+00:00 |
| 71 | [https://hotsites.tce.mt.gov.br/](https://hotsites.tce.mt.gov.br/) | 200 | ev-071 | evidence/ev-071/screenshot.png | 2026-07-06T13:16:42.784641+00:00 |
| 72 | [https://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149](https://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149) | 200 | ev-072 | evidence/ev-072/screenshot.png | 2026-07-06T13:16:42.887737+00:00 |
| 73 | [https://www.tce.mt.gov.br/tipos-de-manifestacoes/724](https://www.tce.mt.gov.br/tipos-de-manifestacoes/724) | 200 | ev-073 | evidence/ev-073/screenshot.png | 2026-07-06T13:16:43.622714+00:00 |
| 74 | [https://www.tce.mt.gov.br/legislacao/148](https://www.tce.mt.gov.br/legislacao/148) | 200 | ev-074 | evidence/ev-074/screenshot.png | 2026-07-06T13:16:43.750005+00:00 |
| 75 | [https://www.tce.mt.gov.br/mapa-da-transparencia/731](https://www.tce.mt.gov.br/mapa-da-transparencia/731) | 200 | ev-075 | evidence/ev-075/screenshot.png | 2026-07-06T13:16:44.106701+00:00 |
| 76 | [https://www.tce.mt.gov.br/uploads/flipbook/carta-servicos-2024/index.html](https://www.tce.mt.gov.br/uploads/flipbook/carta-servicos-2024/index.html) | 200 | ev-076 | evidence/ev-076/screenshot.png | 2026-07-06T13:16:44.264053+00:00 |
| 77 | [https://www.tce.mt.gov.br/fiscalize-corretamente/155](https://www.tce.mt.gov.br/fiscalize-corretamente/155) | 200 | ev-077 | evidence/ev-077/screenshot.png | 2026-07-06T13:16:44.605444+00:00 |
| 78 | [https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes](https://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes) | 200 | ev-078 | evidence/ev-078/screenshot.png | 2026-07-06T13:16:44.945025+00:00 |
| 79 | [https://www.tce.mt.gov.br/quadrimestral/949](https://www.tce.mt.gov.br/quadrimestral/949) | 200 | ev-079 | evidence/ev-079/screenshot.png | 2026-07-06T13:16:44.978928+00:00 |
| 80 | [https://www.tce.mt.gov.br/plano-de-acao/984](https://www.tce.mt.gov.br/plano-de-acao/984) | 200 | ev-080 | evidence/ev-080/screenshot.png | 2026-07-06T13:16:45.352094+00:00 |
| 81 | [https://www.tce.mt.gov.br/ouvidoria-organizacional](https://www.tce.mt.gov.br/ouvidoria-organizacional) | 200 | ev-081 | evidence/ev-081/screenshot.png | 2026-07-06T13:16:45.521938+00:00 |
| 82 | [https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](https://www.tce.mt.gov.br/pesquisa-de-satisfacao/871) | 200 | ev-082 | evidence/ev-082/screenshot.png | 2026-07-06T13:16:45.843916+00:00 |
| 83 | [https://cartadeservicos.tce.mt.gov.br/entidade/1119320](https://cartadeservicos.tce.mt.gov.br/entidade/1119320) | 200 | ev-083 | evidence/ev-083/screenshot.png | 2026-07-06T13:16:45.957015+00:00 |
| 84 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=GzNkLvzXaYEqSCRZGVU7YRDKWet6Fg6bgFCkfF55](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=GzNkLvzXaYEqSCRZGVU7YRDKWet6Fg6bgFCkfF55) | 200 | ev-084 | evidence/ev-084/screenshot.png | 2026-07-06T13:16:46.018816+00:00 |
| 85 | [https://www.tce.mt.gov.br/noticias/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas/62637](https://www.tce.mt.gov.br/noticias/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas/62637) | 200 | ev-085 | evidence/ev-085/screenshot.png | 2026-07-06T13:16:46.518903+00:00 |
| 86 | [https://www.tce.mt.gov.br/noticias/sergio-ricardo-determina-abertura-de-mesa-tecnica-para-destravar-regularizacao-ambiental-da-agricultura-familiar/62636](https://www.tce.mt.gov.br/noticias/sergio-ricardo-determina-abertura-de-mesa-tecnica-para-destravar-regularizacao-ambiental-da-agricultura-familiar/62636) | 200 | ev-086 | evidence/ev-086/screenshot.png | 2026-07-06T13:16:46.757690+00:00 |
| 87 | [https://www.tce.mt.gov.br/noticias/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt/62635](https://www.tce.mt.gov.br/noticias/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt/62635) | 200 | ev-087 | evidence/ev-087/screenshot.png | 2026-07-06T13:16:47.062402+00:00 |
| 88 | [https://www.tce.mt.gov.br/noticias/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao/62633](https://www.tce.mt.gov.br/noticias/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao/62633) | 200 | ev-088 | evidence/ev-088/screenshot.png | 2026-07-06T13:16:47.190258+00:00 |
| 89 | [https://radar.tce.mt.gov.br/](https://radar.tce.mt.gov.br/) | 200 | ev-089 | evidence/ev-089/screenshot.png | 2026-07-06T13:16:47.907968+00:00 |
| 90 | [https://geoobras.tce.mt.gov.br/cidadao](https://geoobras.tce.mt.gov.br/cidadao) | 200 | ev-090 | evidence/ev-090/screenshot.png | 2026-07-06T13:16:48.346705+00:00 |
| 91 | [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-3-dia/4796) | 200 | ev-091 | evidence/ev-091/screenshot.png | 2026-07-06T13:16:48.737800+00:00 |
| 92 | [https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794](https://www.tce.mt.gov.br/galeria/capacitacao-para-o-fortalecimento-do-controle-na-saude-2-dia/4794) | 200 | ev-092 | evidence/ev-092/screenshot.png | 2026-07-06T13:16:48.788291+00:00 |
| 93 | [https://www.tce.mt.gov.br/agenda](https://www.tce.mt.gov.br/agenda) | 200 | ev-093 | evidence/ev-093/screenshot.png | 2026-07-06T13:16:49.198556+00:00 |
| 94 | [https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797](https://www.tce.mt.gov.br/galeria/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas/4797) | 200 | ev-094 | evidence/ev-094/screenshot.png | 2026-07-06T13:16:49.247236+00:00 |
| 95 | [https://www.tce.mt.gov.br/artigos/fortalecimento-do-controle-social-do-sus-em-mato-grosso/625](https://www.tce.mt.gov.br/artigos/fortalecimento-do-controle-social-do-sus-em-mato-grosso/625) | 200 | ev-095 | evidence/ev-095/screenshot.png | 2026-07-06T13:16:50.274306+00:00 |
| 96 | [https://www.tce.mt.gov.br/tvcontas/tce-noticias/seminario-nacional-resulta-em-carta-com-16-compromissos-pela-inclusao-educacional/33389](https://www.tce.mt.gov.br/tvcontas/tce-noticias/seminario-nacional-resulta-em-carta-com-16-compromissos-pela-inclusao-educacional/33389) | 200 | ev-096 | evidence/ev-096/screenshot.png | 2026-07-06T13:16:50.635726+00:00 |
| 97 | [https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-do-tce-mt-reune-especialistas-de-todo-pais-e-ganha-destaque-nacional/33390](https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-do-tce-mt-reune-especialistas-de-todo-pais-e-ganha-destaque-nacional/33390) | 200 | ev-097 | evidence/ev-097/screenshot.png | 2026-07-06T13:16:50.744303+00:00 |
| 98 | [https://www.tce.mt.gov.br/tvcontas/tce-noticias/sergio-ricardo-garante-apoio-tecnico-do-tce-a-demandas-de-boa-esperanca-do-norte/33388](https://www.tce.mt.gov.br/tvcontas/tce-noticias/sergio-ricardo-garante-apoio-tecnico-do-tce-a-demandas-de-boa-esperanca-do-norte/33388) | 200 | ev-098 | evidence/ev-098/screenshot.png | 2026-07-06T13:16:50.787373+00:00 |
| 99 | [https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-mobiliza-municipios-e-firma-compromisso-pela-melhoria-da-saude-publica-em-mt/33391](https://www.tce.mt.gov.br/tvcontas/tce-noticias/capacitacao-mobiliza-municipios-e-firma-compromisso-pela-melhoria-da-saude-publica-em-mt/33391) | 200 | ev-099 | evidence/ev-099/screenshot.png | 2026-07-06T13:16:51.020304+00:00 |
| 100 | [https://www.tce.mt.gov.br/tvcontas/tce-noticias/tce-mt-capacita-conselheiros-de-saude-para-fortalecer-controle-social-nos-municipios/33387](https://www.tce.mt.gov.br/tvcontas/tce-noticias/tce-mt-capacita-conselheiros-de-saude-para-fortalecer-controle-social-nos-municipios/33387) | 200 | ev-100 | evidence/ev-100/screenshot.png | 2026-07-06T13:16:51.703768+00:00 |
| 101 | [https://intranet.tce.mt.gov.br/login](https://intranet.tce.mt.gov.br/login) | 200 | ev-101 | evidence/ev-101/screenshot.png | 2026-07-06T13:19:02.462839+00:00 |
| 102 | [https://www.tce.mt.gov.br/publicacao/administracao-publica/14](https://www.tce.mt.gov.br/publicacao/administracao-publica/14) | 200 | ev-102 | evidence/ev-102/screenshot.png | 2026-07-06T13:19:02.521609+00:00 |
| 103 | [https://www.tce.mt.gov.br/hotsites/lgpd/legislacao-politicas-de-cookies-no-ambito-do-tce-mt.html](https://www.tce.mt.gov.br/hotsites/lgpd/legislacao-politicas-de-cookies-no-ambito-do-tce-mt.html) | 200 | ev-103 | evidence/ev-103/screenshot.png | 2026-07-06T13:19:03.233792+00:00 |
| 104 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=Y521fuxmVKtUn2gWHUbv5CgwmGAqsQsJkhfLgAmA](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=Y521fuxmVKtUn2gWHUbv5CgwmGAqsQsJkhfLgAmA) | 200 | ev-104 | evidence/ev-104/screenshot.png | 2026-07-06T13:19:03.809270+00:00 |
| 105 | [https://www.tce.mt.gov.br/corpo-deliberativo](https://www.tce.mt.gov.br/corpo-deliberativo) | 200 | ev-105 | evidence/ev-105/screenshot.png | 2026-07-06T13:19:03.901125+00:00 |
| 106 | [https://www.tce.mt.gov.br/corpo-de-gestao/16](https://www.tce.mt.gov.br/corpo-de-gestao/16) | 200 | ev-106 | evidence/ev-106/screenshot.png | 2026-07-06T13:19:04.379980+00:00 |
| 107 | [https://www.tce.mt.gov.br/corpo-tecnico/17](https://www.tce.mt.gov.br/corpo-tecnico/17) | 200 | ev-107 | evidence/ev-107/screenshot.png | 2026-07-06T13:19:04.589718+00:00 |
| 108 | [https://www.tce.mt.gov.br/conteudo/sid/583](https://www.tce.mt.gov.br/conteudo/sid/583) | 200 | ev-108 | evidence/ev-108/screenshot.png | 2026-07-06T13:19:05.105886+00:00 |
| 109 | [https://www.tce.mt.gov.br/conteudo/index/sid/121](https://www.tce.mt.gov.br/conteudo/index/sid/121) | 200 | ev-109 | evidence/ev-109/screenshot.png | 2026-07-06T13:19:05.523950+00:00 |
| 110 | [https://www.tce.mt.gov.br/conteudo/index/sid/934](https://www.tce.mt.gov.br/conteudo/index/sid/934) | 200 | ev-110 | evidence/ev-110/screenshot.png | 2026-07-06T13:19:05.612258+00:00 |
| 111 | [https://www.tce.mt.gov.br/conteudo/index/sid/120](https://www.tce.mt.gov.br/conteudo/index/sid/120) | 200 | ev-111 | evidence/ev-111/screenshot.png | 2026-07-06T13:19:05.782522+00:00 |
| 112 | [https://www.tce.mt.gov.br/conteudo/index/sid/116](https://www.tce.mt.gov.br/conteudo/index/sid/116) | 200 | ev-112 | evidence/ev-112/screenshot.png | 2026-07-06T13:19:06.281110+00:00 |
| 113 | [https://www.tce.mt.gov.br/conteudo/index/sid/118](https://www.tce.mt.gov.br/conteudo/index/sid/118) | 200 | ev-113 | evidence/ev-113/screenshot.png | 2026-07-06T13:19:06.770803+00:00 |
| 114 | [https://cartadeservicos.tce.mt.gov.br/docs](https://cartadeservicos.tce.mt.gov.br/docs) | 200 | ev-114 | evidence/ev-114/screenshot.png | 2026-07-06T13:19:07.604640+00:00 |
| 115 | [https://www.tce.mt.gov.br/conteudo/index/sid/1063](https://www.tce.mt.gov.br/conteudo/index/sid/1063) | 200 | ev-115 | evidence/ev-115/screenshot.png | 2026-07-06T13:19:07.835023+00:00 |
| 116 | [https://www.tce.mt.gov.br/historia](https://www.tce.mt.gov.br/historia) | 200 | ev-116 | evidence/ev-116/screenshot.png | 2026-07-06T13:19:08.007622+00:00 |
| 117 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=aWbnJZXklFvpE0BHmegWUugf2x21Yb8pZRTNUACu](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=aWbnJZXklFvpE0BHmegWUugf2x21Yb8pZRTNUACu) | 200 | ev-117 | evidence/ev-117/screenshot.png | 2026-07-06T13:19:08.434910+00:00 |
| 118 | [https://www.tce.mt.gov.br/uploads/flipbook/70anos/index.html](https://www.tce.mt.gov.br/uploads/flipbook/70anos/index.html) | 200 | ev-118 | evidence/ev-118/screenshot.png | 2026-07-06T13:19:08.478009+00:00 |
| 119 | [https://www.tce.mt.gov.br/galeria/show/id/5](https://www.tce.mt.gov.br/galeria/show/id/5) | 404 | ev-119 | evidence/ev-119/screenshot.png | 2026-07-06T13:19:08.632676+00:00 |
| 120 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=08LpMRgDZdB1bHao508j98imF9hX5zoOIHRNkgxc](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=08LpMRgDZdB1bHao508j98imF9hX5zoOIHRNkgxc) | 200 | ev-120 | evidence/ev-120/screenshot.png | 2026-07-06T13:19:08.998264+00:00 |
| 121 | [https://sic.tce.mt.gov.br/docs](https://sic.tce.mt.gov.br/docs) | 200 | ev-121 | evidence/ev-121/screenshot.png | 2026-07-06T13:19:09.370894+00:00 |
| 122 | [https://sic.tce.mt.gov.br/saiba-mais](https://sic.tce.mt.gov.br/saiba-mais) | 200 | ev-122 | evidence/ev-122/screenshot.png | 2026-07-06T13:19:09.698324+00:00 |
| 123 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=c3nugtog5vcM4mLbMGQMH4ZR6j0tv2SCQVmBBW89](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=c3nugtog5vcM4mLbMGQMH4ZR6j0tv2SCQVmBBW89) | 200 | ev-123 | evidence/ev-123/screenshot.png | 2026-07-06T13:19:09.949319+00:00 |
| 124 | [https://www.tce.mt.gov.br/acessibilidade-do-portal](https://www.tce.mt.gov.br/acessibilidade-do-portal) | 200 | ev-124 | evidence/ev-124/screenshot.png | 2026-07-06T13:19:10.521836+00:00 |
| 125 | [https://www.tce.mt.gov.br/tribunal-pleno](https://www.tce.mt.gov.br/tribunal-pleno) | 200 | ev-125 | evidence/ev-125/screenshot.png | 2026-07-06T13:19:10.564199+00:00 |
| 126 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=E4zr95MYqcMMpFIyAv3bxdULkrKT93S4cAEKdCj0](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=E4zr95MYqcMMpFIyAv3bxdULkrKT93S4cAEKdCj0) | 200 | ev-126 | evidence/ev-126/screenshot.png | 2026-07-06T13:19:10.682860+00:00 |
| 127 | [https://www.tce.mt.gov.br/a-instituicao-identidade](https://www.tce.mt.gov.br/a-instituicao-identidade) | 200 | ev-127 | evidence/ev-127/screenshot.png | 2026-07-06T13:19:11.167255+00:00 |
| 128 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=TgpcUAJPXb1c6x5QFLgIkps8DmzkiZRWUzSZqCCJ](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=TgpcUAJPXb1c6x5QFLgIkps8DmzkiZRWUzSZqCCJ) | 200 | ev-128 | evidence/ev-128/screenshot.png | 2026-07-06T13:19:11.577965+00:00 |
| 129 | [https://www.tce.mt.gov.br/instituto-memoria-conselheiros-e-procuradores/1170](https://www.tce.mt.gov.br/instituto-memoria-conselheiros-e-procuradores/1170) | 200 | ev-129 | evidence/ev-129/screenshot.png | 2026-07-06T13:19:12.744821+00:00 |
| 130 | [https://www.tce.mt.gov.br/instituto-memoria-sobre/1147](https://www.tce.mt.gov.br/instituto-memoria-sobre/1147) | 200 | ev-130 | evidence/ev-130/screenshot.png | 2026-07-06T13:19:12.805820+00:00 |
| 131 | [https://www.tce.mt.gov.br/instituto-memoria-sobre](https://www.tce.mt.gov.br/instituto-memoria-sobre) | 200 | ev-131 | evidence/ev-131/screenshot.png | 2026-07-06T13:19:12.851971+00:00 |
| 132 | [https://www.tce.mt.gov.br/instituto-memoria-mesas-diretoras/1171](https://www.tce.mt.gov.br/instituto-memoria-mesas-diretoras/1171) | 200 | ev-132 | evidence/ev-132/screenshot.png | 2026-07-06T13:19:13.418422+00:00 |
| 133 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=B1FYllri2k0Au24r9NBZEF8MUSAAqzKLaNxcDkHy](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=B1FYllri2k0Au24r9NBZEF8MUSAAqzKLaNxcDkHy) | 200 | ev-133 | evidence/ev-133/screenshot.png | 2026-07-06T13:19:14.129825+00:00 |
| 134 | [https://www.tce.mt.gov.br/instituto-memoria-galeria/1148](https://www.tce.mt.gov.br/instituto-memoria-galeria/1148) | 200 | ev-134 | evidence/ev-134/screenshot.png | 2026-07-06T13:19:14.253221+00:00 |
| 135 | [https://www.tce.mt.gov.br/conheca-o-tribunal](https://www.tce.mt.gov.br/conheca-o-tribunal) | 200 | ev-135 | evidence/ev-135/screenshot.png | 2026-07-06T13:19:14.737608+00:00 |
| 136 | [https://www.tce.mt.gov.br/logomarca-tce-mt/930](https://www.tce.mt.gov.br/logomarca-tce-mt/930) | 200 | ev-136 | evidence/ev-136/screenshot.png | 2026-07-06T13:19:15.015983+00:00 |
| 137 | [https://www.tce.mt.gov.br/bandeira-do-tce/20](https://www.tce.mt.gov.br/bandeira-do-tce/20) | 200 | ev-137 | evidence/ev-137/screenshot.png | 2026-07-06T13:19:15.318318+00:00 |
| 138 | [https://www.tce.mt.gov.br/coral/19](https://www.tce.mt.gov.br/coral/19) | 200 | ev-138 | evidence/ev-138/screenshot.png | 2026-07-06T13:19:15.598056+00:00 |
| 139 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CEFx4mkRbLTa3fOpI52ZoxTikT1BGWPs5QcM0hAm](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CEFx4mkRbLTa3fOpI52ZoxTikT1BGWPs5QcM0hAm) | 200 | ev-139 | evidence/ev-139/screenshot.png | 2026-07-06T13:19:16.361183+00:00 |
| 140 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=ughJ7gaXkYigsMDrB02Ta34juzMEOsQigV9nA3mr](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=ughJ7gaXkYigsMDrB02Ta34juzMEOsQigV9nA3mr) | 200 | ev-140 | evidence/ev-140/screenshot.png | 2026-07-06T13:19:16.686989+00:00 |
| 141 | [https://www.tce.mt.gov.br/publico-de-relacionamento](https://www.tce.mt.gov.br/publico-de-relacionamento) | 200 | ev-141 | evidence/ev-141/screenshot.png | 2026-07-06T13:19:16.749676+00:00 |
| 142 | [https://www.tce.mt.gov.br/corregedoria-institucional](https://www.tce.mt.gov.br/corregedoria-institucional) | 200 | ev-142 | evidence/ev-142/screenshot.png | 2026-07-06T13:19:16.958221+00:00 |
| 143 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=PXntxmST3XoGHasHnNuq0LjcW3rKSMpW3gBtBd8M](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=PXntxmST3XoGHasHnNuq0LjcW3rKSMpW3gBtBd8M) | 200 | ev-143 | evidence/ev-143/screenshot.png | 2026-07-06T13:19:17.395600+00:00 |
| 144 | [https://www.tce.mt.gov.br/competencias-do-tce](https://www.tce.mt.gov.br/competencias-do-tce) | 200 | ev-144 | evidence/ev-144/screenshot.png | 2026-07-06T13:19:18.057904+00:00 |
| 145 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia](https://escolasuperiordecontas.tce.mt.gov.br/pages/nossa-historia) | 200 | ev-145 | evidence/ev-145/screenshot.png | 2026-07-06T13:19:18.797371+00:00 |
| 146 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade](https://escolasuperiordecontas.tce.mt.gov.br/pages/identidade) | 200 | ev-146 | evidence/ev-146/screenshot.png | 2026-07-06T13:19:19.003069+00:00 |
| 147 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/gestao-2026) | 200 | ev-147 | evidence/ev-147/screenshot.png | 2026-07-06T13:19:19.439457+00:00 |
| 148 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma](https://escolasuperiordecontas.tce.mt.gov.br/pages/organograma) | 200 | ev-148 | evidence/ev-148/screenshot.png | 2026-07-06T13:19:19.473584+00:00 |
| 149 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica](https://escolasuperiordecontas.tce.mt.gov.br/pages/estrutura-fisica) | 200 | ev-149 | evidence/ev-149/screenshot.png | 2026-07-06T13:19:20.771055+00:00 |
| 150 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos](https://escolasuperiordecontas.tce.mt.gov.br/pages/objetivos-estrategicos) | 200 | ev-150 | evidence/ev-150/screenshot.png | 2026-07-06T13:19:20.913870+00:00 |
| 151 | [https://escolasuperiordecontas.tce.mt.gov.br/calendario](https://escolasuperiordecontas.tce.mt.gov.br/calendario) | 200 | ev-151 | evidence/ev-151/screenshot.png | 2026-07-06T13:19:21.106902+00:00 |
| 152 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro](https://escolasuperiordecontas.tce.mt.gov.br/pages/memorial-rosario-congro) | 200 | ev-152 | evidence/ev-152/screenshot.png | 2026-07-06T13:19:21.722974+00:00 |
| 153 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20242025) | 200 | ev-153 | evidence/ev-153/screenshot.png | 2026-07-06T13:19:22.291315+00:00 |
| 154 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho](https://escolasuperiordecontas.tce.mt.gov.br/pages/agenda-semanal-de-atividades-06-a-10-de-julho) | 200 | ev-154 | evidence/ev-154/screenshot.png | 2026-07-06T13:19:22.891325+00:00 |
| 155 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites](https://escolasuperiordecontas.tce.mt.gov.br/pages/hotsites) | 200 | ev-155 | evidence/ev-155/screenshot.png | 2026-07-06T13:19:22.964167+00:00 |
| 156 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023](https://escolasuperiordecontas.tce.mt.gov.br/pages/resultados-alcancados-gestao-20222023) | 200 | ev-156 | evidence/ev-156/screenshot.png | 2026-07-06T13:19:23.488155+00:00 |
| 157 | [https://escolasuperiordecontas.tce.mt.gov.br/noticias](https://escolasuperiordecontas.tce.mt.gov.br/noticias) | 200 | ev-157 | evidence/ev-157/screenshot.png | 2026-07-06T13:19:23.785590+00:00 |
| 158 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2026) | 200 | ev-158 | evidence/ev-158/screenshot.png | 2026-07-06T13:19:24.388878+00:00 |
| 159 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025](https://escolasuperiordecontas.tce.mt.gov.br/pages/mba-2025) | 200 | ev-159 | evidence/ev-159/screenshot.png | 2026-07-06T13:19:24.696976+00:00 |
| 160 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire](https://escolasuperiordecontas.tce.mt.gov.br/pages/biblioteca-poeta-silva-freire) | 200 | ev-160 | evidence/ev-160/screenshot.png | 2026-07-06T13:19:24.787415+00:00 |
| 161 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos](https://escolasuperiordecontas.tce.mt.gov.br/pages/artigos) | 200 | ev-161 | evidence/ev-161/screenshot.png | 2026-07-06T13:19:25.678883+00:00 |
| 162 | [https://escolasuperiordecontas.tce.mt.gov.br/acervo](https://escolasuperiordecontas.tce.mt.gov.br/acervo) | 200 | ev-162 | evidence/ev-162/screenshot.png | 2026-07-06T13:19:25.898326+00:00 |
| 163 | [https://escolasuperiordecontas.tce.mt.gov.br/contato](https://escolasuperiordecontas.tce.mt.gov.br/contato) | 200 | ev-163 | evidence/ev-163/screenshot.png | 2026-07-06T13:21:26.367582+00:00 |
| 164 | [https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao](https://escolasuperiordecontas.tce.mt.gov.br/pages/legislacao) | 200 | ev-164 | evidence/ev-164/screenshot.png | 2026-07-06T13:21:26.386725+00:00 |
| 165 | [https://ead.tce.mt.gov.br/ava](https://ead.tce.mt.gov.br/ava) | 200 | ev-165 | evidence/ev-165/screenshot.png | 2026-07-06T13:21:26.868420+00:00 |
| 166 | [https://sga.tce.mt.gov.br/painel-aluno](https://sga.tce.mt.gov.br/painel-aluno) | 200 | ev-166 | evidence/ev-166/screenshot.png | 2026-07-06T13:21:27.799960+00:00 |
| 167 | [https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades](https://escolasuperiordecontas.tce.mt.gov.br/noticia/comunicado-institucional-recesso-academico-mba-em-gestao-de-cidades) | 200 | ev-167 | evidence/ev-167/screenshot.png | 2026-07-06T13:21:28.572912+00:00 |
| 168 | [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/sistema-geo-obras-jurisdicionados) | 200 | ev-168 | evidence/ev-168/screenshot.png | 2026-07-06T13:21:28.766151+00:00 |
| 169 | [https://conta.tce.mt.gov.br/login](https://conta.tce.mt.gov.br/login) | 200 | ev-169 | evidence/ev-169/screenshot.png | 2026-07-06T13:21:28.900437+00:00 |
| 170 | [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/2a-edicao-do-programa-tricotando-sobre-ouvidoria-2026) | 200 | ev-170 | evidence/ev-170/screenshot.png | 2026-07-06T13:21:30.428276+00:00 |
| 171 | [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/programa-tce-pro-mulher-implantacao-e-implementacao-dos-planos-de-metas) | 200 | ev-171 | evidence/ev-171/screenshot.png | 2026-07-06T13:21:30.785216+00:00 |
| 172 | [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/lancamento-do-livro-a-mesa-tecnica-nos-tribunais-de-contas) | 200 | ev-172 | evidence/ev-172/screenshot.png | 2026-07-06T13:21:30.830659+00:00 |
| 173 | [https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11](https://escolasuperiordecontas.tce.mt.gov.br/cursos-e-eventos/mba-em-gestao-de-cidades-aula-modulo-11) | 200 | ev-173 | evidence/ev-173/screenshot.png | 2026-07-06T13:21:31.346819+00:00 |
| 174 | [https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais](https://escolasuperiordecontas.tce.mt.gov.br/acoes-educacionais) | 200 | ev-174 | evidence/ev-174/screenshot.png | 2026-07-06T13:21:32.721785+00:00 |
| 175 | [https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao](https://escolasuperiordecontas.tce.mt.gov.br/noticia/servidores-comissionados-do-tce-mt-fundam-associacao-voltada-a-capacitacao-e-integracao) | 200 | ev-175 | evidence/ev-175/screenshot.png | 2026-07-06T13:21:33.421710+00:00 |
| 176 | [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tce-mt-capacita-servidores-para-auditorias-e-avaliacoes-de-politicas-publicas) | 200 | ev-176 | evidence/ev-176/screenshot.png | 2026-07-06T13:21:33.503878+00:00 |
| 177 | [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-conselheiro-defende-estruturacao-das-ouvidorias-e-destaca-contribuicao-do-tce-mt) | 200 | ev-177 | evidence/ev-177/screenshot.png | 2026-07-06T13:21:33.549451+00:00 |
| 178 | [https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2](https://escolasuperiordecontas.tce.mt.gov.br/noticia/tricotando-sobre-ouvidoria-do-tce-mt-aborda-funcao-do-ouvidor-e-perspectivas-futuras-nesta-quinta-feira-2) | 200 | ev-178 | evidence/ev-178/screenshot.png | 2026-07-06T13:21:34.925280+00:00 |
| 179 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841](https://escolasuperiordecontas.tce.mt.gov.br/galerias/25-anos-da-escola-superior-de-contas/841) | 200 | ev-179 | evidence/ev-179/screenshot.png | 2026-07-06T13:21:35.940963+00:00 |
| 180 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801](https://escolasuperiordecontas.tce.mt.gov.br/galerias/semin-rio-de-pol-ticas-p-blicas-de-enfrentamento-viol-ncia-contra-crian-as-e-adolescentes/801) | 200 | ev-180 | evidence/ev-180/screenshot.png | 2026-07-06T13:21:36.016533+00:00 |
| 181 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821](https://escolasuperiordecontas.tce.mt.gov.br/galerias/8-congresso-internacional-de-direito-tribut-rio-e-financeiro/821) | 200 | ev-181 | evidence/ev-181/screenshot.png | 2026-07-06T13:21:36.138767+00:00 |
| 182 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783](https://escolasuperiordecontas.tce.mt.gov.br/galerias/tcestudantil-recebe-alunos-de-ci-ncias-cont-beis-da-unemat-de-tangar-da-serra/783) | 200 | ev-182 | evidence/ev-182/screenshot.png | 2026-07-06T13:21:37.080395+00:00 |
| 183 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782](https://escolasuperiordecontas.tce.mt.gov.br/galerias/i-encontro-t-cnico-sobre-a-reforma-tribut-ria-para-munic-pios/782) | 200 | ev-183 | evidence/ev-183/screenshot.png | 2026-07-06T13:21:37.712852+00:00 |
| 184 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741](https://escolasuperiordecontas.tce.mt.gov.br/galerias/viii-encontro-intersetorial-de-promo-o-da-vida-e-preven-o-do-suic-dio/741) | 200 | ev-184 | evidence/ev-184/screenshot.png | 2026-07-06T13:21:38.265861+00:00 |
| 185 | [https://escolasuperiordecontas.tce.mt.gov.br/galerias](https://escolasuperiordecontas.tce.mt.gov.br/galerias) | 200 | ev-185 | evidence/ev-185/screenshot.png | 2026-07-06T13:21:38.376177+00:00 |
| 186 | [https://escolasuperiordecontas.tce.mt.gov.br/mapa](https://escolasuperiordecontas.tce.mt.gov.br/mapa) | 200 | ev-186 | evidence/ev-186/screenshot.png | 2026-07-06T13:21:38.616472+00:00 |
| 187 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nVqtrKuOH77crlZTMbGJMoEIWAxswARRPaGveLoG](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nVqtrKuOH77crlZTMbGJMoEIWAxswARRPaGveLoG) | 200 | ev-187 | evidence/ev-187/screenshot.png | 2026-07-06T13:21:38.723801+00:00 |
| 188 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=M9jvFGWMuyArpvJevmneEyNcyIeWgvGxVomE0bMT](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=M9jvFGWMuyArpvJevmneEyNcyIeWgvGxVomE0bMT) | 200 | ev-188 | evidence/ev-188/screenshot.png | 2026-07-06T13:21:39.370360+00:00 |
| 189 | [https://www.tce.mt.gov.br/produtos-e-processos](https://www.tce.mt.gov.br/produtos-e-processos) | 200 | ev-189 | evidence/ev-189/screenshot.png | 2026-07-06T13:21:39.532607+00:00 |
| 190 | [https://www.tce.mt.gov.br/lgpd-boas-praticas-e-governanca/1079](https://www.tce.mt.gov.br/lgpd-boas-praticas-e-governanca/1079) | 200 | ev-190 | evidence/ev-190/screenshot.png | 2026-07-06T13:21:39.845097+00:00 |
| 191 | [https://www.tce.mt.gov.br/sobre-o-comite/1143](https://www.tce.mt.gov.br/sobre-o-comite/1143) | 200 | ev-191 | evidence/ev-191/screenshot.png | 2026-07-06T13:21:39.950749+00:00 |
| 192 | [https://www.tce.mt.gov.br/sobre-a-comissao/1144](https://www.tce.mt.gov.br/sobre-a-comissao/1144) | 200 | ev-192 | evidence/ev-192/screenshot.png | 2026-07-06T13:21:40.610163+00:00 |
| 193 | [https://www.tce.mt.gov.br/lgpd-programa-de-governanca-de-privacidade-de-dados/1086](https://www.tce.mt.gov.br/lgpd-programa-de-governanca-de-privacidade-de-dados/1086) | 200 | ev-193 | evidence/ev-193/screenshot.png | 2026-07-06T13:21:40.776474+00:00 |
| 194 | [https://www.tce.mt.gov.br/lgpd-alertas-e-recomendacoes/1093](https://www.tce.mt.gov.br/lgpd-alertas-e-recomendacoes/1093) | 200 | ev-194 | evidence/ev-194/screenshot.png | 2026-07-06T13:21:41.068786+00:00 |
| 195 | [https://www.tce.mt.gov.br/lgpd-no-tce-mt/1080](https://www.tce.mt.gov.br/lgpd-no-tce-mt/1080) | 200 | ev-195 | evidence/ev-195/screenshot.png | 2026-07-06T13:21:41.243971+00:00 |
| 196 | [https://www.tce.mt.gov.br/lgpd-plano-de-adequacao/1095](https://www.tce.mt.gov.br/lgpd-plano-de-adequacao/1095) | 200 | ev-196 | evidence/ev-196/screenshot.png | 2026-07-06T13:21:41.885146+00:00 |
| 197 | [https://www.tce.mt.gov.br/lgpd-central-de-conteudo/1081](https://www.tce.mt.gov.br/lgpd-central-de-conteudo/1081) | 200 | ev-197 | evidence/ev-197/screenshot.png | 2026-07-06T13:21:42.028726+00:00 |
| 198 | [https://www.tce.mt.gov.br/lgpd-dicas-de-seguranca/1105](https://www.tce.mt.gov.br/lgpd-dicas-de-seguranca/1105) | 200 | ev-198 | evidence/ev-198/screenshot.png | 2026-07-06T13:21:42.316652+00:00 |
| 199 | [https://www.tce.mt.gov.br/lgpd-legislacao/1082](https://www.tce.mt.gov.br/lgpd-legislacao/1082) | 200 | ev-199 | evidence/ev-199/screenshot.png | 2026-07-06T13:21:42.564632+00:00 |
| 200 | [https://www.tce.mt.gov.br/lgpd-politicas-tce/1145](https://www.tce.mt.gov.br/lgpd-politicas-tce/1145) | 200 | ev-200 | evidence/ev-200/screenshot.png | 2026-07-06T13:21:43.091496+00:00 |
| 201 | [https://www.tce.mt.gov.br/lgpd-contato/1085](https://www.tce.mt.gov.br/lgpd-contato/1085) | 200 | ev-201 | evidence/ev-201/screenshot.png | 2026-07-06T13:21:43.533943+00:00 |
| 202 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=BB6iTpKLY374FS1cVoAbiZSAdczHAqDC8X1W9aU0](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=BB6iTpKLY374FS1cVoAbiZSAdczHAqDC8X1W9aU0) | 200 | ev-202 | evidence/ev-202/screenshot.png | 2026-07-06T13:21:43.603711+00:00 |
| 203 | [https://www.tce.mt.gov.br/lgpd-faq/1084](https://www.tce.mt.gov.br/lgpd-faq/1084) | 200 | ev-203 | evidence/ev-203/screenshot.png | 2026-07-06T13:21:44.208863+00:00 |
| 204 | [https://www.tce.mt.gov.br/publicacao/gestao-do-tce-mt/2](https://www.tce.mt.gov.br/publicacao/gestao-do-tce-mt/2) | 200 | ev-204 | evidence/ev-204/screenshot.png | 2026-07-06T13:21:44.454938+00:00 |
| 205 | [http://www.tce.mt.gov.br/](http://www.tce.mt.gov.br/) | 200 | ev-205 | evidence/ev-205/screenshot.png | 2026-07-06T13:21:44.913429+00:00 |
| 206 | [http://www.tce.mt.gov.br/historia/12](http://www.tce.mt.gov.br/historia/12) | 200 | ev-206 | evidence/ev-206/screenshot.png | 2026-07-06T13:21:45.439171+00:00 |
| 207 | [http://www.tce.mt.gov.br/corpo-deliberativo/15](http://www.tce.mt.gov.br/corpo-deliberativo/15) | 200 | ev-207 | evidence/ev-207/screenshot.png | 2026-07-06T13:21:45.689242+00:00 |
| 208 | [http://www.tce.mt.gov.br/acessibilidade-do-portal/1067](http://www.tce.mt.gov.br/acessibilidade-do-portal/1067) | 200 | ev-208 | evidence/ev-208/screenshot.png | 2026-07-06T13:21:45.726395+00:00 |
| 209 | [http://www.tce.mt.gov.br/identidade/767](http://www.tce.mt.gov.br/identidade/767) | 200 | ev-209 | evidence/ev-209/screenshot.png | 2026-07-06T13:21:46.109197+00:00 |
| 210 | [http://www.tce.mt.gov.br/tribunal-pleno/609](http://www.tce.mt.gov.br/tribunal-pleno/609) | 200 | ev-210 | evidence/ev-210/screenshot.png | 2026-07-06T13:21:46.660941+00:00 |
| 211 | [http://www.tce.mt.gov.br/instituto-memoria](http://www.tce.mt.gov.br/instituto-memoria) | 200 | ev-211 | evidence/ev-211/screenshot.png | 2026-07-06T13:21:47.082397+00:00 |
| 212 | [http://www.tce.mt.gov.br/competencias-do-tribunal/876](http://www.tce.mt.gov.br/competencias-do-tribunal/876) | 200 | ev-212 | evidence/ev-212/screenshot.png | 2026-07-06T13:21:47.362370+00:00 |
| 213 | [http://www.tce.mt.gov.br/conheca-o-tribunal/10](http://www.tce.mt.gov.br/conheca-o-tribunal/10) | 200 | ev-213 | evidence/ev-213/screenshot.png | 2026-07-06T13:21:47.400483+00:00 |
| 214 | [http://www.tce.mt.gov.br/publico-de-relacionamento/878](http://www.tce.mt.gov.br/publico-de-relacionamento/878) | 200 | ev-214 | evidence/ev-214/screenshot.png | 2026-07-06T13:21:47.918253+00:00 |
| 215 | [http://www.tce.mt.gov.br/institucional/303](http://www.tce.mt.gov.br/institucional/303) | 200 | ev-215 | evidence/ev-215/screenshot.png | 2026-07-06T13:21:48.251678+00:00 |
| 216 | [http://www.tce.mt.gov.br/produtos-e-processos/877](http://www.tce.mt.gov.br/produtos-e-processos/877) | 200 | ev-216 | evidence/ev-216/screenshot.png | 2026-07-06T13:21:48.715889+00:00 |
| 217 | [http://www.tce.mt.gov.br/planejamento-estrategico/704](http://www.tce.mt.gov.br/planejamento-estrategico/704) | 200 | ev-217 | evidence/ev-217/screenshot.png | 2026-07-06T13:21:49.058355+00:00 |
| 218 | [http://www.tce.mt.gov.br/lgpd](http://www.tce.mt.gov.br/lgpd) | 200 | ev-218 | evidence/ev-218/screenshot.png | 2026-07-06T13:21:49.152445+00:00 |
| 219 | [http://www.tce.mt.gov.br/calendario](http://www.tce.mt.gov.br/calendario) | 200 | ev-219 | evidence/ev-219/screenshot.png | 2026-07-06T13:21:49.430726+00:00 |
| 220 | [http://www.tce.mt.gov.br/aplic/485](http://www.tce.mt.gov.br/aplic/485) | 200 | ev-220 | evidence/ev-220/screenshot.png | 2026-07-06T13:21:50.106467+00:00 |
| 221 | [http://www.tce.mt.gov.br/assinatura](http://www.tce.mt.gov.br/assinatura) | 200 | ev-221 | evidence/ev-221/screenshot.png | 2026-07-06T13:21:50.277450+00:00 |
| 222 | [http://www.tce.mt.gov.br/contas](http://www.tce.mt.gov.br/contas) | 200 | ev-222 | evidence/ev-222/screenshot.png | 2026-07-06T13:21:50.786067+00:00 |
| 223 | [http://www.tce.mt.gov.br/distribuicao](http://www.tce.mt.gov.br/distribuicao) | 200 | ev-223 | evidence/ev-223/screenshot.png | 2026-07-06T13:21:50.847683+00:00 |
| 224 | [http://www.tce.mt.gov.br/geo-obras/486](http://www.tce.mt.gov.br/geo-obras/486) | 200 | ev-224 | evidence/ev-224/screenshot.png | 2026-07-06T13:21:51.329464+00:00 |
| 225 | [http://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024](http://www.tce.mt.gov.br/o-que-e-o-programa-gpe/1024) | 200 | ev-225 | evidence/ev-225/screenshot.png | 2026-07-06T13:21:51.617833+00:00 |
| 226 | [http://www.tce.mt.gov.br/documentos](http://www.tce.mt.gov.br/documentos) | 200 | ev-226 | evidence/ev-226/screenshot.png | 2026-07-06T13:21:52.454667+00:00 |
| 227 | [http://www.tce.mt.gov.br/processos](http://www.tce.mt.gov.br/processos) | 200 | ev-227 | evidence/ev-227/screenshot.png | 2026-07-06T13:21:52.629118+00:00 |
| 228 | [http://www.tce.mt.gov.br/julgamento/presencial](http://www.tce.mt.gov.br/julgamento/presencial) | 200 | ev-228 | evidence/ev-228/screenshot.png | 2026-07-06T13:21:53.037785+00:00 |
| 229 | [http://www.tce.mt.gov.br/julgamento/virtual](http://www.tce.mt.gov.br/julgamento/virtual) | 200 | ev-229 | evidence/ev-229/screenshot.png | 2026-07-06T13:21:53.150784+00:00 |
| 230 | [http://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo](http://www.tce.mt.gov.br/legislacoes/codigo-de-processo-de-controle-externo) | 200 | ev-230 | evidence/ev-230/screenshot.png | 2026-07-06T13:21:54.072896+00:00 |
| 231 | [http://www.tce.mt.gov.br/legislacoes/regimento-interno](http://www.tce.mt.gov.br/legislacoes/regimento-interno) | 200 | ev-231 | evidence/ev-231/screenshot.png | 2026-07-06T13:21:54.458494+00:00 |
| 232 | [http://www.tce.mt.gov.br/legislacoes/lei-organica](http://www.tce.mt.gov.br/legislacoes/lei-organica) | 200 | ev-232 | evidence/ev-232/screenshot.png | 2026-07-06T13:21:54.938544+00:00 |
| 233 | [http://www.tce.mt.gov.br/legislacoes/instrucoes-normativas](http://www.tce.mt.gov.br/legislacoes/instrucoes-normativas) | 200 | ev-233 | evidence/ev-233/screenshot.png | 2026-07-06T13:21:55.446857+00:00 |
| 234 | [http://www.tce.mt.gov.br/legislacoes/resolucao-normativa](http://www.tce.mt.gov.br/legislacoes/resolucao-normativa) | 200 | ev-234 | evidence/ev-234/screenshot.png | 2026-07-06T13:21:55.540423+00:00 |
| 235 | [http://www.tce.mt.gov.br/legislacoes/decisoes-normativas](http://www.tce.mt.gov.br/legislacoes/decisoes-normativas) | 200 | ev-235 | evidence/ev-235/screenshot.png | 2026-07-06T13:21:55.785857+00:00 |
| 236 | [http://www.tce.mt.gov.br/legislacoes/decisoes-administrativas](http://www.tce.mt.gov.br/legislacoes/decisoes-administrativas) | 200 | ev-236 | evidence/ev-236/screenshot.png | 2026-07-06T13:21:56.234588+00:00 |
| 237 | [http://www.tce.mt.gov.br/legislacoes/portarias](http://www.tce.mt.gov.br/legislacoes/portarias) | 200 | ev-237 | evidence/ev-237/screenshot.png | 2026-07-06T13:21:56.801276+00:00 |
| 238 | [http://www.tce.mt.gov.br/legislacoes](http://www.tce.mt.gov.br/legislacoes) | 200 | ev-238 | evidence/ev-238/screenshot.png | 2026-07-06T13:21:57.066223+00:00 |
| 239 | [http://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32](http://www.tce.mt.gov.br/publicacao/informativo-de-precedentes/32) | 200 | ev-239 | evidence/ev-239/screenshot.png | 2026-07-06T13:21:57.184977+00:00 |
| 240 | [http://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21](http://www.tce.mt.gov.br/publicacao/boletim-da-jurisprudencia/21) | 200 | ev-240 | evidence/ev-240/screenshot.png | 2026-07-06T13:21:57.656373+00:00 |
| 241 | [http://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta](http://www.tce.mt.gov.br/legislacoes/resolucao-de-consulta) | 200 | ev-241 | evidence/ev-241/screenshot.png | 2026-07-06T13:21:58.009009+00:00 |
| 242 | [http://www.tce.mt.gov.br/legislacoes/sumulas](http://www.tce.mt.gov.br/legislacoes/sumulas) | 200 | ev-242 | evidence/ev-242/screenshot.png | 2026-07-06T13:21:58.210252+00:00 |
| 243 | [http://www.tce.mt.gov.br/noticias](http://www.tce.mt.gov.br/noticias) | 200 | ev-243 | evidence/ev-243/screenshot.png | 2026-07-06T13:21:58.424604+00:00 |
| 244 | [http://www.tce.mt.gov.br/publicacao](http://www.tce.mt.gov.br/publicacao) | 200 | ev-244 | evidence/ev-244/screenshot.png | 2026-07-06T13:21:58.996613+00:00 |
| 245 | [http://www.tce.mt.gov.br/galeria](http://www.tce.mt.gov.br/galeria) | 200 | ev-245 | evidence/ev-245/screenshot.png | 2026-07-06T13:21:59.291677+00:00 |
| 246 | [http://www.tce.mt.gov.br/legislacoes/prejulgados](http://www.tce.mt.gov.br/legislacoes/prejulgados) | 200 | ev-246 | evidence/ev-246/screenshot.png | 2026-07-06T13:21:59.510685+00:00 |
| 247 | [http://www.tce.mt.gov.br/tvcontas](http://www.tce.mt.gov.br/tvcontas) | 200 | ev-247 | evidence/ev-247/screenshot.png | 2026-07-06T13:21:59.642019+00:00 |
| 248 | [http://www.tce.mt.gov.br/artigos](http://www.tce.mt.gov.br/artigos) | 200 | ev-248 | evidence/ev-248/screenshot.png | 2026-07-06T13:21:59.893503+00:00 |
| 249 | [http://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149](http://www.tce.mt.gov.br/fale-nos-queremos-te-ouvir/149) | 200 | ev-249 | evidence/ev-249/screenshot.png | 2026-07-06T13:22:00.635877+00:00 |
| 250 | [http://www.tce.mt.gov.br/fiscalize-corretamente/155](http://www.tce.mt.gov.br/fiscalize-corretamente/155) | 200 | ev-250 | evidence/ev-250/screenshot.png | 2026-07-06T13:22:00.935972+00:00 |
| 251 | [http://www.tce.mt.gov.br/tipos-de-manifestacoes/724](http://www.tce.mt.gov.br/tipos-de-manifestacoes/724) | 200 | ev-251 | evidence/ev-251/screenshot.png | 2026-07-06T13:22:01.179088+00:00 |
| 252 | [http://www.tce.mt.gov.br/radio-tce/169](http://www.tce.mt.gov.br/radio-tce/169) | 200 | ev-252 | evidence/ev-252/screenshot.png | 2026-07-06T13:22:01.229099+00:00 |
| 253 | [http://www.tce.mt.gov.br/legislacao/148](http://www.tce.mt.gov.br/legislacao/148) | 200 | ev-253 | evidence/ev-253/screenshot.png | 2026-07-06T13:22:01.370271+00:00 |
| 254 | [http://www.tce.mt.gov.br/uploads/flipbook/carta-servicos-2024/index.html](http://www.tce.mt.gov.br/uploads/flipbook/carta-servicos-2024/index.html) | 200 | ev-254 | evidence/ev-254/screenshot.png | 2026-07-06T13:22:01.909065+00:00 |
| 255 | [http://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes](http://www.tce.mt.gov.br/ouvidoria-perguntas-frequentes) | 200 | ev-255 | evidence/ev-255/screenshot.png | 2026-07-06T13:22:02.057697+00:00 |
| 256 | [http://www.tce.mt.gov.br/mapa-da-transparencia/731](http://www.tce.mt.gov.br/mapa-da-transparencia/731) | 200 | ev-256 | evidence/ev-256/screenshot.png | 2026-07-06T13:22:02.217349+00:00 |
| 257 | [http://www.tce.mt.gov.br/plano-de-acao/984](http://www.tce.mt.gov.br/plano-de-acao/984) | 200 | ev-257 | evidence/ev-257/screenshot.png | 2026-07-06T13:22:02.544794+00:00 |
| 258 | [http://www.tce.mt.gov.br/ouvidoria-organizacional](http://www.tce.mt.gov.br/ouvidoria-organizacional) | 200 | ev-258 | evidence/ev-258/screenshot.png | 2026-07-06T13:22:02.796709+00:00 |
| 259 | [http://www.tce.mt.gov.br/pesquisa-de-satisfacao/871](http://www.tce.mt.gov.br/pesquisa-de-satisfacao/871) | 200 | ev-259 | evidence/ev-259/screenshot.png | 2026-07-06T13:22:03.076332+00:00 |
| 260 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=tgl8XHqNS8Lq77YNSEHdzr73nLTT8MMLGFUCzw9K](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=tgl8XHqNS8Lq77YNSEHdzr73nLTT8MMLGFUCzw9K) | 200 | ev-260 | evidence/ev-260/screenshot.png | 2026-07-06T13:22:03.138919+00:00 |
| 261 | [http://www.tce.mt.gov.br/o-tce-e-a-iso/939](http://www.tce.mt.gov.br/o-tce-e-a-iso/939) | 200 | ev-261 | evidence/ev-261/screenshot.png | 2026-07-06T13:22:03.839124+00:00 |
| 262 | [http://www.tce.mt.gov.br/politica-da-qualidade/885](http://www.tce.mt.gov.br/politica-da-qualidade/885) | 200 | ev-262 | evidence/ev-262/screenshot.png | 2026-07-06T13:22:04.065843+00:00 |
| 263 | [http://www.tce.mt.gov.br/o-tce-e-a-iso](http://www.tce.mt.gov.br/o-tce-e-a-iso) | 200 | ev-263 | evidence/ev-263/screenshot.png | 2026-07-06T13:22:04.353592+00:00 |
| 264 | [http://www.tce.mt.gov.br/sistema-de-gestao-da-qualidade/940](http://www.tce.mt.gov.br/sistema-de-gestao-da-qualidade/940) | 200 | ev-264 | evidence/ev-264/screenshot.png | 2026-07-06T13:22:04.448269+00:00 |
| 265 | [http://www.tce.mt.gov.br/sistema-de-gestao-da-energia/1040](http://www.tce.mt.gov.br/sistema-de-gestao-da-energia/1040) | 200 | ev-265 | evidence/ev-265/screenshot.png | 2026-07-06T13:22:05.200990+00:00 |
| 266 | [http://www.tce.mt.gov.br/politica-energetica/1039](http://www.tce.mt.gov.br/politica-energetica/1039) | 200 | ev-266 | evidence/ev-266/screenshot.png | 2026-07-06T13:22:05.313761+00:00 |
| 267 | [http://www.tce.mt.gov.br/processos-certificados/626](http://www.tce.mt.gov.br/processos-certificados/626) | 200 | ev-267 | evidence/ev-267/screenshot.png | 2026-07-06T13:22:05.493773+00:00 |
| 268 | [http://www.tce.mt.gov.br/certificados/754](http://www.tce.mt.gov.br/certificados/754) | 200 | ev-268 | evidence/ev-268/screenshot.png | 2026-07-06T13:22:05.870426+00:00 |
| 269 | [https://servicos.tce.mt.gov.br/login](https://servicos.tce.mt.gov.br/login) | 200 | ev-269 | evidence/ev-269/screenshot.png | 2026-07-06T13:22:05.947225+00:00 |
| 270 | [http://conta.tce.mt.gov.br/oauth/authorize?client_id=1&redirect_uri=https://servicos.tce.mt.gov.br/oauth/login&response_type=code&scope=info vinculos credenciais&state=deAwMWL9k6YoqUwKeWX3FzLSVcLtr7p2UIRefMQn](http://conta.tce.mt.gov.br/oauth/authorize?client_id=1&redirect_uri=https://servicos.tce.mt.gov.br/oauth/login&response_type=code&scope=info vinculos credenciais&state=deAwMWL9k6YoqUwKeWX3FzLSVcLtr7p2UIRefMQn) | 200 | ev-270 | evidence/ev-270/screenshot.png | 2026-07-06T13:22:06.244704+00:00 |
| 271 | [https://servicos.tce.mt.gov.br/empresas-inidoneas](https://servicos.tce.mt.gov.br/empresas-inidoneas) | 200 | ev-271 | evidence/ev-271/screenshot.png | 2026-07-06T13:22:06.389828+00:00 |
| 272 | [https://servicos.tce.mt.gov.br/inabilitacao-exercicio](https://servicos.tce.mt.gov.br/inabilitacao-exercicio) | 200 | ev-272 | evidence/ev-272/screenshot.png | 2026-07-06T13:22:06.875886+00:00 |
| 273 | [https://servicos.tce.mt.gov.br/ouvidoria](https://servicos.tce.mt.gov.br/ouvidoria) | 200 | ev-273 | evidence/ev-273/screenshot.png | 2026-07-06T13:22:07.413079+00:00 |
| 274 | [https://conta.tce.mt.gov.br/faq](https://conta.tce.mt.gov.br/faq) | 200 | ev-274 | evidence/ev-274/screenshot.png | 2026-07-06T13:22:07.431535+00:00 |
| 275 | [http://geoobrascidadao.tce.mt.gov.br/](http://geoobrascidadao.tce.mt.gov.br/) | 200 | ev-275 | evidence/ev-275/screenshot.png | 2026-07-06T13:22:07.476336+00:00 |
| 276 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=4JDkQUVoP6kjUEj2ADWbJVGMAmY7QGvbIsOrk3VQ](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=4JDkQUVoP6kjUEj2ADWbJVGMAmY7QGvbIsOrk3VQ) | 200 | ev-276 | evidence/ev-276/screenshot.png | 2026-07-06T13:22:07.904635+00:00 |
| 277 | [http://sic.tce.mt.gov.br/](http://sic.tce.mt.gov.br/) | 200 | ev-277 | evidence/ev-277/screenshot.png | 2026-07-06T13:22:08.370955+00:00 |
| 278 | [https://www.tce.mt.gov.br/calendario/02/2026](https://www.tce.mt.gov.br/calendario/02/2026) | 200 | ev-278 | evidence/ev-278/screenshot.png | 2026-07-06T13:22:08.592178+00:00 |
| 279 | [https://www.tce.mt.gov.br/calendario/01/2026](https://www.tce.mt.gov.br/calendario/01/2026) | 200 | ev-279 | evidence/ev-279/screenshot.png | 2026-07-06T13:22:08.797027+00:00 |
| 280 | [https://www.tce.mt.gov.br/calendario/04/2026](https://www.tce.mt.gov.br/calendario/04/2026) | 200 | ev-280 | evidence/ev-280/screenshot.png | 2026-07-06T13:22:09.063111+00:00 |
| 281 | [https://www.tce.mt.gov.br/calendario/03/2026](https://www.tce.mt.gov.br/calendario/03/2026) | 200 | ev-281 | evidence/ev-281/screenshot.png | 2026-07-06T13:22:09.439887+00:00 |
| 282 | [https://www.tce.mt.gov.br/calendario/05/2026](https://www.tce.mt.gov.br/calendario/05/2026) | 200 | ev-282 | evidence/ev-282/screenshot.png | 2026-07-06T13:22:09.574595+00:00 |
| 283 | [https://www.tce.mt.gov.br/calendario/06/2026](https://www.tce.mt.gov.br/calendario/06/2026) | 200 | ev-283 | evidence/ev-283/screenshot.png | 2026-07-06T13:22:09.833452+00:00 |
| 284 | [https://www.tce.mt.gov.br/calendario/07/2026](https://www.tce.mt.gov.br/calendario/07/2026) | 200 | ev-284 | evidence/ev-284/screenshot.png | 2026-07-06T13:22:09.958496+00:00 |
| 285 | [https://www.tce.mt.gov.br/calendario/08/2026](https://www.tce.mt.gov.br/calendario/08/2026) | 200 | ev-285 | evidence/ev-285/screenshot.png | 2026-07-06T13:22:10.202499+00:00 |
| 286 | [https://www.tce.mt.gov.br/calendario/09/2026](https://www.tce.mt.gov.br/calendario/09/2026) | 200 | ev-286 | evidence/ev-286/screenshot.png | 2026-07-06T13:22:10.656326+00:00 |
| 287 | [https://www.tce.mt.gov.br/calendario/10/2026](https://www.tce.mt.gov.br/calendario/10/2026) | 200 | ev-287 | evidence/ev-287/screenshot.png | 2026-07-06T13:22:10.803241+00:00 |
| 288 | [https://www.tce.mt.gov.br/calendario/11/2026](https://www.tce.mt.gov.br/calendario/11/2026) | 200 | ev-288 | evidence/ev-288/screenshot.png | 2026-07-06T13:22:11.019879+00:00 |
| 289 | [https://pce.tce.mt.gov.br/juris?ent_codigo=](https://pce.tce.mt.gov.br/juris?ent_codigo=) | 200 | ev-289 | evidence/ev-289/screenshot.png | 2026-07-06T13:22:11.133135+00:00 |
| 290 | [https://www.tce.mt.gov.br/calendario/12/2026](https://www.tce.mt.gov.br/calendario/12/2026) | 200 | ev-290 | evidence/ev-290/screenshot.png | 2026-07-06T13:22:11.184293+00:00 |
| 291 | [https://servicos.tce.mt.gov.br/solicitacao](https://servicos.tce.mt.gov.br/solicitacao) | 200 | ev-291 | evidence/ev-291/screenshot.png | 2026-07-06T13:22:11.788184+00:00 |
| 292 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=K8ms2i6Bl26BiMZxpmlmvWSmltCIz618zp9iDdao](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=K8ms2i6Bl26BiMZxpmlmvWSmltCIz618zp9iDdao) | 200 | ev-292 | evidence/ev-292/screenshot.png | 2026-07-06T13:22:12.490143+00:00 |
| 293 | [https://www.tce.mt.gov.br/sistemas-tecnicos-aplic-2](https://www.tce.mt.gov.br/sistemas-tecnicos-aplic-2) | 200 | ev-293 | evidence/ev-293/screenshot.png | 2026-07-06T13:22:12.603221+00:00 |
| 294 | [https://servicos.tce.mt.gov.br/log](https://servicos.tce.mt.gov.br/log) | 200 | ev-294 | evidence/ev-294/screenshot.png | 2026-07-06T13:22:12.861446+00:00 |
| 295 | [https://www.tce.mt.gov.br/arquivos/11866/f52a69bfa11ce08d1ac774dc580c395c81b84921/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/11866/f52a69bfa11ce08d1ac774dc580c395c81b84921/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-295 | evidence/ev-295/screenshot.png | 2026-07-06T13:22:13.691808+00:00 |
| 296 | [https://www.tce.mt.gov.br/arquivos/12335/93042288111db943a05592e4d8c34cf2460087de/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/12335/93042288111db943a05592e4d8c34cf2460087de/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-296 | evidence/ev-296/screenshot.png | 2026-07-06T13:22:13.893116+00:00 |
| 297 | [https://www.tce.mt.gov.br/arquivos/11763/a8f3e0adefc259f8b59477f23363150132340fd0/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/11763/a8f3e0adefc259f8b59477f23363150132340fd0/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-297 | evidence/ev-297/screenshot.png | 2026-07-06T13:22:13.946159+00:00 |
| 298 | [https://www.tce.mt.gov.br/arquivos/8780/e3c09e2da8d747a37a7d66340fc813bedb7b86d6/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/8780/e3c09e2da8d747a37a7d66340fc813bedb7b86d6/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-298 | evidence/ev-298/screenshot.png | 2026-07-06T13:22:14.147581+00:00 |
| 299 | [https://www.tce.mt.gov.br/acesso-externo/1014](https://www.tce.mt.gov.br/acesso-externo/1014) | 200 | ev-299 | evidence/ev-299/screenshot.png | 2026-07-06T13:22:14.429839+00:00 |
| 300 | [https://www.tce.mt.gov.br/arquivos/7588/2f2743bcfa5709b0b07eda5b93372129a1268efe/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7588/2f2743bcfa5709b0b07eda5b93372129a1268efe/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-300 | evidence/ev-300/screenshot.png | 2026-07-06T13:22:15.244918+00:00 |
| 301 | [https://www.tce.mt.gov.br/arquivos/7574/a562994b2af650b6bda2cc63516028e7ebd4525d/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7574/a562994b2af650b6bda2cc63516028e7ebd4525d/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-301 | evidence/ev-301/screenshot.png | 2026-07-06T13:22:15.487649+00:00 |
| 302 | [https://www.tce.mt.gov.br/arquivos/7584/546c25dbc5a78fee76a7b371f80b3861fc6aacd3/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7584/546c25dbc5a78fee76a7b371f80b3861fc6aacd3/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-302 | evidence/ev-302/screenshot.png | 2026-07-06T13:22:16.163302+00:00 |
| 303 | [https://www.tce.mt.gov.br/arquivos/7520/6178982ce0253b205512af52de7c7de7b3a11cd6/7594/d0a1198ede31e46b900227ca59244b105fef0394](https://www.tce.mt.gov.br/arquivos/7520/6178982ce0253b205512af52de7c7de7b3a11cd6/7594/d0a1198ede31e46b900227ca59244b105fef0394) | 200 | ev-303 | evidence/ev-303/screenshot.png | 2026-07-06T13:22:16.445724+00:00 |
| 304 | [https://servicos.tce.mt.gov.br/certidao/lista](https://servicos.tce.mt.gov.br/certidao/lista) | 200 | ev-304 | evidence/ev-304/screenshot.png | 2026-07-06T13:22:18.319701+00:00 |
| 305 | [https://servicos.tce.mt.gov.br/certidao/emissao](https://servicos.tce.mt.gov.br/certidao/emissao) | 200 | ev-305 | evidence/ev-305/screenshot.png | 2026-07-06T13:22:19.074545+00:00 |
| 306 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=zBYEGrZBKPFQdgDGa7NRXO1eXg6t6SeN7OZdG4Gl](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=zBYEGrZBKPFQdgDGa7NRXO1eXg6t6SeN7OZdG4Gl) | 200 | ev-306 | evidence/ev-306/screenshot.png | 2026-07-06T13:22:19.106954+00:00 |
| 307 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=uEk2k26EuiIIw9SWoJycGQkeWw5UnolcP6Ry07Uc](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=uEk2k26EuiIIw9SWoJycGQkeWw5UnolcP6Ry07Uc) | 200 | ev-307 | evidence/ev-307/screenshot.png | 2026-07-06T13:22:19.158412+00:00 |
| 308 | [https://servicos.tce.mt.gov.br/certidao/pedido-acompanhamento](https://servicos.tce.mt.gov.br/certidao/pedido-acompanhamento) | 200 | ev-308 | evidence/ev-308/screenshot.png | 2026-07-06T13:22:19.209829+00:00 |
| 309 | [https://servicos.tce.mt.gov.br/diario-writer](https://servicos.tce.mt.gov.br/diario-writer) | 200 | ev-309 | evidence/ev-309/screenshot.png | 2026-07-06T13:22:19.385430+00:00 |
| 310 | [https://www.tce.mt.gov.br/conteudo/sid/639](https://www.tce.mt.gov.br/conteudo/sid/639) | 200 | ev-310 | evidence/ev-310/screenshot.png | 2026-07-06T13:22:20.591372+00:00 |
| 311 | [https://www.tce.mt.gov.br/contas/municipais](https://www.tce.mt.gov.br/contas/municipais) | 200 | ev-311 | evidence/ev-311/screenshot.png | 2026-07-06T13:22:21.023198+00:00 |
| 312 | [https://limesurvey.tce.mt.gov.br/index.php/425193](https://limesurvey.tce.mt.gov.br/index.php/425193) | 200 | ev-312 | evidence/ev-312/screenshot.png | 2026-07-06T13:22:21.083922+00:00 |
| 313 | [https://www.tce.mt.gov.br/conteudo/sid/638](https://www.tce.mt.gov.br/conteudo/sid/638) | 200 | ev-313 | evidence/ev-313/screenshot.png | 2026-07-06T13:22:21.130634+00:00 |
| 314 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=yqOxnp9LrfmQC3PRdyscvEakpmz1nr0xgcvtAzsL](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=yqOxnp9LrfmQC3PRdyscvEakpmz1nr0xgcvtAzsL) | 200 | ev-314 | evidence/ev-314/screenshot.png | 2026-07-06T13:22:21.263639+00:00 |
| 315 | [https://www.tce.mt.gov.br/contas/assembleia-legislativa](https://www.tce.mt.gov.br/contas/assembleia-legislativa) | 200 | ev-315 | evidence/ev-315/screenshot.png | 2026-07-06T13:22:21.870231+00:00 |
| 316 | [https://www.tce.mt.gov.br/contas/governo](https://www.tce.mt.gov.br/contas/governo) | 200 | ev-316 | evidence/ev-316/screenshot.png | 2026-07-06T13:22:22.364248+00:00 |
| 317 | [https://www.tce.mt.gov.br/contas/tj](https://www.tce.mt.gov.br/contas/tj) | 200 | ev-317 | evidence/ev-317/screenshot.png | 2026-07-06T13:22:22.568937+00:00 |
| 318 | [https://www.tce.mt.gov.br/contas/tce](https://www.tce.mt.gov.br/contas/tce) | 200 | ev-318 | evidence/ev-318/screenshot.png | 2026-07-06T13:22:22.722027+00:00 |
| 319 | [https://www.tce.mt.gov.br/contas/ministerio-publico](https://www.tce.mt.gov.br/contas/ministerio-publico) | 200 | ev-319 | evidence/ev-319/screenshot.png | 2026-07-06T13:22:23.125696+00:00 |
| 320 | [https://www.tce.mt.gov.br/contas/defensoria-publica](https://www.tce.mt.gov.br/contas/defensoria-publica) | 200 | ev-320 | evidence/ev-320/screenshot.png | 2026-07-06T13:22:23.543106+00:00 |
| 321 | [https://www.tce.mt.gov.br/contas/esfera/estadual](https://www.tce.mt.gov.br/contas/esfera/estadual) | 200 | ev-321 | evidence/ev-321/screenshot.png | 2026-07-06T13:22:23.718733+00:00 |
| 322 | [https://www.tce.mt.gov.br/contas/esfera/municipal](https://www.tce.mt.gov.br/contas/esfera/municipal) | 200 | ev-322 | evidence/ev-322/screenshot.png | 2026-07-06T13:22:23.941143+00:00 |
| 323 | [https://www.tce.mt.gov.br/processo/1915584/2024](https://www.tce.mt.gov.br/processo/1915584/2024) | 200 | ev-323 | evidence/ev-323/screenshot.png | 2026-07-06T13:22:24.171305+00:00 |
| 324 | [https://www.tce.mt.gov.br/processo/1784390/2024](https://www.tce.mt.gov.br/processo/1784390/2024) | 200 | ev-324 | evidence/ev-324/screenshot.png | 2026-07-06T13:22:24.696619+00:00 |
| 325 | [https://www.tce.mt.gov.br/processo/478792/2023](https://www.tce.mt.gov.br/processo/478792/2023) | 200 | ev-325 | evidence/ev-325/screenshot.png | 2026-07-06T13:22:25.094174+00:00 |
| 326 | [https://www.tce.mt.gov.br/processo/540234/2021](https://www.tce.mt.gov.br/processo/540234/2021) | 200 | ev-326 | evidence/ev-326/screenshot.png | 2026-07-06T13:22:25.275768+00:00 |
| 327 | [https://www.tce.mt.gov.br/processo/221538/2020](https://www.tce.mt.gov.br/processo/221538/2020) | 200 | ev-327 | evidence/ev-327/screenshot.png | 2026-07-06T13:22:25.836131+00:00 |
| 328 | [https://www.tce.mt.gov.br/processo/243370/2019](https://www.tce.mt.gov.br/processo/243370/2019) | 200 | ev-328 | evidence/ev-328/screenshot.png | 2026-07-06T13:22:26.077728+00:00 |
| 329 | [https://www.tce.mt.gov.br/processo/8567/2019](https://www.tce.mt.gov.br/processo/8567/2019) | 200 | ev-329 | evidence/ev-329/screenshot.png | 2026-07-06T13:22:26.332826+00:00 |
| 330 | [https://www.tce.mt.gov.br/processo/81710/2018](https://www.tce.mt.gov.br/processo/81710/2018) | 200 | ev-330 | evidence/ev-330/screenshot.png | 2026-07-06T13:22:26.701891+00:00 |
| 331 | [https://www.tce.mt.gov.br/processo/120413/2016](https://www.tce.mt.gov.br/processo/120413/2016) | 200 | ev-331 | evidence/ev-331/screenshot.png | 2026-07-06T13:22:26.874241+00:00 |
| 332 | [https://www.tce.mt.gov.br/processo/23396/2015](https://www.tce.mt.gov.br/processo/23396/2015) | 200 | ev-332 | evidence/ev-332/screenshot.png | 2026-07-06T13:22:27.372148+00:00 |
| 333 | [https://www.tce.mt.gov.br/processo/81760/2014](https://www.tce.mt.gov.br/processo/81760/2014) | 200 | ev-333 | evidence/ev-333/screenshot.png | 2026-07-06T13:22:27.698356+00:00 |
| 334 | [https://www.tce.mt.gov.br/processo/75493/2014](https://www.tce.mt.gov.br/processo/75493/2014) | 200 | ev-334 | evidence/ev-334/screenshot.png | 2026-07-06T13:22:27.890178+00:00 |
| 335 | [https://www.tce.mt.gov.br/processo/60844/2011](https://www.tce.mt.gov.br/processo/60844/2011) | 200 | ev-335 | evidence/ev-335/screenshot.png | 2026-07-06T13:22:28.704416+00:00 |
| 336 | [https://www.tce.mt.gov.br/processo/70017/2010](https://www.tce.mt.gov.br/processo/70017/2010) | 200 | ev-336 | evidence/ev-336/screenshot.png | 2026-07-06T13:22:29.090871+00:00 |
| 337 | [https://www.tce.mt.gov.br/processo/92797/2013](https://www.tce.mt.gov.br/processo/92797/2013) | 200 | ev-337 | evidence/ev-337/screenshot.png | 2026-07-06T13:22:29.181264+00:00 |
| 338 | [https://www.tce.mt.gov.br/processo/67369/2012](https://www.tce.mt.gov.br/processo/67369/2012) | 200 | ev-338 | evidence/ev-338/screenshot.png | 2026-07-06T13:22:29.235602+00:00 |
| 339 | [https://www.tce.mt.gov.br/processo/69639/2009](https://www.tce.mt.gov.br/processo/69639/2009) | 200 | ev-339 | evidence/ev-339/screenshot.png | 2026-07-06T13:22:29.445378+00:00 |
| 340 | [https://www.tce.mt.gov.br/processo/58963/2008](https://www.tce.mt.gov.br/processo/58963/2008) | 200 | ev-340 | evidence/ev-340/screenshot.png | 2026-07-06T13:22:30.195111+00:00 |
| 341 | [https://www.tce.mt.gov.br/processo/56219/2007](https://www.tce.mt.gov.br/processo/56219/2007) | 200 | ev-341 | evidence/ev-341/screenshot.png | 2026-07-06T13:22:30.798440+00:00 |
| 342 | [https://www.tce.mt.gov.br/processo/47210/2006](https://www.tce.mt.gov.br/processo/47210/2006) | 200 | ev-342 | evidence/ev-342/screenshot.png | 2026-07-06T13:22:30.941806+00:00 |
| 343 | [https://www.tce.mt.gov.br/processo/87106/2004](https://www.tce.mt.gov.br/processo/87106/2004) | 200 | ev-343 | evidence/ev-343/screenshot.png | 2026-07-06T13:22:31.032023+00:00 |
| 344 | [https://www.tce.mt.gov.br/processo/97977/2005](https://www.tce.mt.gov.br/processo/97977/2005) | 200 | ev-344 | evidence/ev-344/screenshot.png | 2026-07-06T13:22:31.618335+00:00 |
| 345 | [https://www.tce.mt.gov.br/processo/29459/2014](https://www.tce.mt.gov.br/processo/29459/2014) | 200 | ev-345 | evidence/ev-345/screenshot.png | 2026-07-06T13:22:31.674348+00:00 |
| 346 | [https://www.tce.mt.gov.br/processo/71480/2013](https://www.tce.mt.gov.br/processo/71480/2013) | 200 | ev-346 | evidence/ev-346/screenshot.png | 2026-07-06T13:22:32.225544+00:00 |
| 347 | [https://www.tce.mt.gov.br/processo/123633/2012](https://www.tce.mt.gov.br/processo/123633/2012) | 200 | ev-347 | evidence/ev-347/screenshot.png | 2026-07-06T13:22:32.439028+00:00 |
| 348 | [https://www.tce.mt.gov.br/processo/141860/2011](https://www.tce.mt.gov.br/processo/141860/2011) | 200 | ev-348 | evidence/ev-348/screenshot.png | 2026-07-06T13:22:32.718273+00:00 |
| 349 | [https://www.tce.mt.gov.br/processo/40070/2011](https://www.tce.mt.gov.br/processo/40070/2011) | 200 | ev-349 | evidence/ev-349/screenshot.png | 2026-07-06T13:22:33.057607+00:00 |
| 350 | [https://www.tce.mt.gov.br/processo/60429/2009](https://www.tce.mt.gov.br/processo/60429/2009) | 200 | ev-350 | evidence/ev-350/screenshot.png | 2026-07-06T13:22:33.668771+00:00 |
| 351 | [https://www.tce.mt.gov.br/processo/45756/2007](https://www.tce.mt.gov.br/processo/45756/2007) | 200 | ev-351 | evidence/ev-351/screenshot.png | 2026-07-06T13:22:34.048392+00:00 |
| 352 | [https://www.tce.mt.gov.br/processo/35815/2006](https://www.tce.mt.gov.br/processo/35815/2006) | 200 | ev-352 | evidence/ev-352/screenshot.png | 2026-07-06T13:22:34.429346+00:00 |
| 353 | [https://www.tce.mt.gov.br/processo/45748/2008](https://www.tce.mt.gov.br/processo/45748/2008) | 200 | ev-353 | evidence/ev-353/screenshot.png | 2026-07-06T13:22:34.616537+00:00 |
| 354 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=1fPk0wkgFZu8KKFSxK5eQ0HrGH4hA1tVrr1DnzHW](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=1fPk0wkgFZu8KKFSxK5eQ0HrGH4hA1tVrr1DnzHW) | 200 | ev-354 | evidence/ev-354/screenshot.png | 2026-07-06T13:22:34.701712+00:00 |
| 355 | [https://www.tce.mt.gov.br/processo/60089/2010](https://www.tce.mt.gov.br/processo/60089/2010) | 200 | ev-355 | evidence/ev-355/screenshot.png | 2026-07-06T13:22:35.018146+00:00 |
| 356 | [https://www.tce.mt.gov.br/sistemas-tecnicos-geo-obras-2](https://www.tce.mt.gov.br/sistemas-tecnicos-geo-obras-2) | 200 | ev-356 | evidence/ev-356/screenshot.png | 2026-07-06T13:22:35.285357+00:00 |
| 357 | [https://www.tce.mt.gov.br/geo-obras-jurisdicionado/171](https://www.tce.mt.gov.br/geo-obras-jurisdicionado/171) | 200 | ev-357 | evidence/ev-357/screenshot.png | 2026-07-06T13:22:35.723860+00:00 |
| 358 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=VyrLly47HF90Fs4FKGHINLV33zF2oWURZuUef6DQ](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=VyrLly47HF90Fs4FKGHINLV33zF2oWURZuUef6DQ) | 200 | ev-358 | evidence/ev-358/screenshot.png | 2026-07-06T13:22:35.790250+00:00 |
| 359 | [https://www.tce.mt.gov.br/como-funciona/1025](https://www.tce.mt.gov.br/como-funciona/1025) | 200 | ev-359 | evidence/ev-359/screenshot.png | 2026-07-06T13:22:36.256577+00:00 |
| 360 | [https://www.tce.mt.gov.br/como-aderir/1026](https://www.tce.mt.gov.br/como-aderir/1026) | 200 | ev-360 | evidence/ev-360/screenshot.png | 2026-07-06T13:22:36.573537+00:00 |
| 361 | [https://www.tce.mt.gov.br/o-que-e-o-programa-gpe](https://www.tce.mt.gov.br/o-que-e-o-programa-gpe) | 200 | ev-361 | evidence/ev-361/screenshot.png | 2026-07-06T13:22:36.790416+00:00 |
| 362 | [https://www.tce.mt.gov.br/acesso-aos-materiais-de-apoio/1029](https://www.tce.mt.gov.br/acesso-aos-materiais-de-apoio/1029) | 200 | ev-362 | evidence/ev-362/screenshot.png | 2026-07-06T13:22:37.274225+00:00 |
| 363 | [https://www.tce.mt.gov.br/mapas-estrategicos-2023-2034/1049](https://www.tce.mt.gov.br/mapas-estrategicos-2023-2034/1049) | 200 | ev-363 | evidence/ev-363/screenshot.png | 2026-07-06T13:22:37.590337+00:00 |
| 364 | [https://www.tce.mt.gov.br/resultados/1033](https://www.tce.mt.gov.br/resultados/1033) | 200 | ev-364 | evidence/ev-364/screenshot.png | 2026-07-06T13:22:37.931417+00:00 |
| 365 | [https://servicos.tce.mt.gov.br/consulta-item/solicitacao/acompanhamento](https://servicos.tce.mt.gov.br/consulta-item/solicitacao/acompanhamento) | 200 | ev-365 | evidence/ev-365/screenshot.png | 2026-07-06T13:22:38.030180+00:00 |
| 366 | [https://gpe2.tce.mt.gov.br/](https://gpe2.tce.mt.gov.br/) | 200 | ev-366 | evidence/ev-366/screenshot.png | 2026-07-06T13:22:38.181704+00:00 |
| 367 | [https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026](https://servicos.tce.mt.gov.br/consulta-item/historico/03-07-2026) | 200 | ev-367 | evidence/ev-367/screenshot.png | 2026-07-06T13:22:38.706303+00:00 |
| 368 | [https://servicos.tce.mt.gov.br/consulta-item/historico](https://servicos.tce.mt.gov.br/consulta-item/historico) | 200 | ev-368 | evidence/ev-368/screenshot.png | 2026-07-06T13:22:40.920318+00:00 |
| 369 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=gEYCSMwye1WjfZiyAbJsQinOD5zjLEVRkz6mXhuK](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=gEYCSMwye1WjfZiyAbJsQinOD5zjLEVRkz6mXhuK) | 200 | ev-369 | evidence/ev-369/screenshot.png | 2026-07-06T13:24:13.401669+00:00 |
| 370 | [https://qapradar.tce.mt.gov.br/extensions/igfm/index.html](https://qapradar.tce.mt.gov.br/extensions/igfm/index.html) | 200 | ev-370 | evidence/ev-370/screenshot.png | 2026-07-06T13:24:13.516565+00:00 |
| 371 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2026](https://www.tce.mt.gov.br/julgamento/presencial?ano=2026) | 200 | ev-371 | evidence/ev-371/screenshot.png | 2026-07-06T13:24:14.556128+00:00 |
| 372 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CGMbbZmld9m9ZXEsH1WRQEawpvSFU3zETNx07YXx](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=CGMbbZmld9m9ZXEsH1WRQEawpvSFU3zETNx07YXx) | 200 | ev-372 | evidence/ev-372/screenshot.png | 2026-07-06T13:24:14.633157+00:00 |
| 373 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2024](https://www.tce.mt.gov.br/julgamento/presencial?ano=2024) | 200 | ev-373 | evidence/ev-373/screenshot.png | 2026-07-06T13:24:14.782494+00:00 |
| 374 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2023](https://www.tce.mt.gov.br/julgamento/presencial?ano=2023) | 200 | ev-374 | evidence/ev-374/screenshot.png | 2026-07-06T13:24:14.920323+00:00 |
| 375 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2025](https://www.tce.mt.gov.br/julgamento/presencial?ano=2025) | 200 | ev-375 | evidence/ev-375/screenshot.png | 2026-07-06T13:24:15.609247+00:00 |
| 376 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2021](https://www.tce.mt.gov.br/julgamento/presencial?ano=2021) | 200 | ev-376 | evidence/ev-376/screenshot.png | 2026-07-06T13:24:15.937835+00:00 |
| 377 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2022](https://www.tce.mt.gov.br/julgamento/presencial?ano=2022) | 200 | ev-377 | evidence/ev-377/screenshot.png | 2026-07-06T13:24:16.001267+00:00 |
| 378 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2020](https://www.tce.mt.gov.br/julgamento/presencial?ano=2020) | 200 | ev-378 | evidence/ev-378/screenshot.png | 2026-07-06T13:24:16.511766+00:00 |
| 379 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2019](https://www.tce.mt.gov.br/julgamento/presencial?ano=2019) | 200 | ev-379 | evidence/ev-379/screenshot.png | 2026-07-06T13:24:16.915188+00:00 |
| 380 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2018](https://www.tce.mt.gov.br/julgamento/presencial?ano=2018) | 200 | ev-380 | evidence/ev-380/screenshot.png | 2026-07-06T13:24:17.278113+00:00 |
| 381 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2017](https://www.tce.mt.gov.br/julgamento/presencial?ano=2017) | 200 | ev-381 | evidence/ev-381/screenshot.png | 2026-07-06T13:24:17.651661+00:00 |
| 382 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2015](https://www.tce.mt.gov.br/julgamento/presencial?ano=2015) | 200 | ev-382 | evidence/ev-382/screenshot.png | 2026-07-06T13:24:18.124631+00:00 |
| 383 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2016](https://www.tce.mt.gov.br/julgamento/presencial?ano=2016) | 200 | ev-383 | evidence/ev-383/screenshot.png | 2026-07-06T13:24:18.559316+00:00 |
| 384 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2012](https://www.tce.mt.gov.br/julgamento/presencial?ano=2012) | 200 | ev-384 | evidence/ev-384/screenshot.png | 2026-07-06T13:24:19.470273+00:00 |
| 385 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2014](https://www.tce.mt.gov.br/julgamento/presencial?ano=2014) | 200 | ev-385 | evidence/ev-385/screenshot.png | 2026-07-06T13:24:20.291027+00:00 |
| 386 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2011](https://www.tce.mt.gov.br/julgamento/presencial?ano=2011) | 200 | ev-386 | evidence/ev-386/screenshot.png | 2026-07-06T13:24:20.444264+00:00 |
| 387 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2013](https://www.tce.mt.gov.br/julgamento/presencial?ano=2013) | 200 | ev-387 | evidence/ev-387/screenshot.png | 2026-07-06T13:24:20.554795+00:00 |
| 388 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2010](https://www.tce.mt.gov.br/julgamento/presencial?ano=2010) | 200 | ev-388 | evidence/ev-388/screenshot.png | 2026-07-06T13:24:21.315475+00:00 |
| 389 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2009](https://www.tce.mt.gov.br/julgamento/presencial?ano=2009) | 200 | ev-389 | evidence/ev-389/screenshot.png | 2026-07-06T13:24:21.727557+00:00 |
| 390 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=02-06-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=02-06-2026-O-0) | 200 | ev-390 | evidence/ev-390/screenshot.png | 2026-07-06T13:24:22.677464+00:00 |
| 391 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=09-06-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=09-06-2026-O-0) | 200 | ev-391 | evidence/ev-391/screenshot.png | 2026-07-06T13:24:23.082404+00:00 |
| 392 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-S-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-S-0) | 200 | ev-392 | evidence/ev-392/screenshot.png | 2026-07-06T13:24:23.151955+00:00 |
| 393 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2007](https://www.tce.mt.gov.br/julgamento/presencial?ano=2007) | 200 | ev-393 | evidence/ev-393/screenshot.png | 2026-07-06T13:24:23.234035+00:00 |
| 394 | [https://www.tce.mt.gov.br/julgamento/presencial?ano=2008](https://www.tce.mt.gov.br/julgamento/presencial?ano=2008) | 200 | ev-394 | evidence/ev-394/screenshot.png | 2026-07-06T13:24:23.541135+00:00 |
| 395 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=26-05-2026-O-0) | 200 | ev-395 | evidence/ev-395/screenshot.png | 2026-07-06T13:24:24.088892+00:00 |
| 396 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=28-04-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=28-04-2026-O-0) | 200 | ev-396 | evidence/ev-396/screenshot.png | 2026-07-06T13:24:24.649335+00:00 |
| 397 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=14-04-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=14-04-2026-O-0) | 200 | ev-397 | evidence/ev-397/screenshot.png | 2026-07-06T13:24:24.802365+00:00 |
| 398 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-03-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-03-2026-O-0) | 200 | ev-398 | evidence/ev-398/screenshot.png | 2026-07-06T13:24:25.019564+00:00 |
| 399 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=17-03-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=17-03-2026-O-0) | 200 | ev-399 | evidence/ev-399/screenshot.png | 2026-07-06T13:24:25.387905+00:00 |
| 400 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=19-05-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=19-05-2026-O-0) | 200 | ev-400 | evidence/ev-400/screenshot.png | 2026-07-06T13:24:25.614610+00:00 |
| 401 | [https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-02-2026-O-0](https://www.tce.mt.gov.br/julgamento/presencial?pauta=24-02-2026-O-0) | 200 | ev-401 | evidence/ev-401/screenshot.png | 2026-07-06T13:24:26.008977+00:00 |
| 402 | [https://www.tce.mt.gov.br/processo/2724227/2026](https://www.tce.mt.gov.br/processo/2724227/2026) | 200 | ev-402 | evidence/ev-402/screenshot.png | 2026-07-06T13:24:26.255402+00:00 |
| 403 | [https://www.tce.mt.gov.br/processo/2724251/2026](https://www.tce.mt.gov.br/processo/2724251/2026) | 200 | ev-403 | evidence/ev-403/screenshot.png | 2026-07-06T13:24:26.462329+00:00 |
| 404 | [https://www.tce.mt.gov.br/processo/2741911/2026](https://www.tce.mt.gov.br/processo/2741911/2026) | 200 | ev-404 | evidence/ev-404/screenshot.png | 2026-07-06T13:24:26.889982+00:00 |
| 405 | [https://www.tce.mt.gov.br/processo/2758008/2026](https://www.tce.mt.gov.br/processo/2758008/2026) | 200 | ev-405 | evidence/ev-405/screenshot.png | 2026-07-06T13:24:27.285067+00:00 |
| 406 | [https://www.tce.mt.gov.br/processo/2727064/2026](https://www.tce.mt.gov.br/processo/2727064/2026) | 200 | ev-406 | evidence/ev-406/screenshot.png | 2026-07-06T13:24:27.587300+00:00 |
| 407 | [https://www.tce.mt.gov.br/processo/1961071/2025](https://www.tce.mt.gov.br/processo/1961071/2025) | 200 | ev-407 | evidence/ev-407/screenshot.png | 2026-07-06T13:24:27.910941+00:00 |
| 408 | [https://www.tce.mt.gov.br/processo/110795/2020](https://www.tce.mt.gov.br/processo/110795/2020) | 200 | ev-408 | evidence/ev-408/screenshot.png | 2026-07-06T13:24:27.985846+00:00 |
| 409 | [https://www.tce.mt.gov.br/processo/2054531/2025](https://www.tce.mt.gov.br/processo/2054531/2025) | 200 | ev-409 | evidence/ev-409/screenshot.png | 2026-07-06T13:24:28.434717+00:00 |
| 410 | [https://www.tce.mt.gov.br/processo/2002442/2025](https://www.tce.mt.gov.br/processo/2002442/2025) | 200 | ev-410 | evidence/ev-410/screenshot.png | 2026-07-06T13:24:28.992834+00:00 |
| 411 | [https://www.tce.mt.gov.br/processo/1988735/2025](https://www.tce.mt.gov.br/processo/1988735/2025) | 200 | ev-411 | evidence/ev-411/screenshot.png | 2026-07-06T13:24:29.206897+00:00 |
| 412 | [https://www.tce.mt.gov.br/processo/1887602/2024](https://www.tce.mt.gov.br/processo/1887602/2024) | 200 | ev-412 | evidence/ev-412/screenshot.png | 2026-07-06T13:24:29.415786+00:00 |
| 413 | [https://www.tce.mt.gov.br/processo/2713721/2026](https://www.tce.mt.gov.br/processo/2713721/2026) | 200 | ev-413 | evidence/ev-413/screenshot.png | 2026-07-06T13:24:29.707040+00:00 |
| 414 | [https://www.tce.mt.gov.br/processo/1805290/2024](https://www.tce.mt.gov.br/processo/1805290/2024) | 200 | ev-414 | evidence/ev-414/screenshot.png | 2026-07-06T13:24:29.947156+00:00 |
| 415 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nkA5eNEJsZRGHCQ2QJkYX7MsBWMiDSpRMM0kezGX](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=nkA5eNEJsZRGHCQ2QJkYX7MsBWMiDSpRMM0kezGX) | 200 | ev-415 | evidence/ev-415/screenshot.png | 2026-07-06T13:24:30.092745+00:00 |
| 416 | [https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=bB28sxNrtSiBx7ubEW6AJQrNwLbygDw8D9WsoqAo](https://conta.tce.mt.gov.br/oauth/authorize?client_id=22&redirect_uri=https://www.tce.mt.gov.br/login/callback&response_type=code&scope=info&state=bB28sxNrtSiBx7ubEW6AJQrNwLbygDw8D9WsoqAo) | 200 | ev-416 | evidence/ev-416/screenshot.png | 2026-07-06T13:24:30.263458+00:00 |
| 417 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2025](https://www.tce.mt.gov.br/julgamento/virtual?ano=2025) | 200 | ev-417 | evidence/ev-417/screenshot.png | 2026-07-06T13:24:32.056896+00:00 |
| 418 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2024](https://www.tce.mt.gov.br/julgamento/virtual?ano=2024) | 200 | ev-418 | evidence/ev-418/screenshot.png | 2026-07-06T13:24:32.411096+00:00 |
| 419 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2023](https://www.tce.mt.gov.br/julgamento/virtual?ano=2023) | 200 | ev-419 | evidence/ev-419/screenshot.png | 2026-07-06T13:24:33.522447+00:00 |
| 420 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2026](https://www.tce.mt.gov.br/julgamento/virtual?ano=2026) | 200 | ev-420 | evidence/ev-420/screenshot.png | 2026-07-06T13:24:34.525469+00:00 |
| 421 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2021](https://www.tce.mt.gov.br/julgamento/virtual?ano=2021) | 200 | ev-421 | evidence/ev-421/screenshot.png | 2026-07-06T13:24:35.069098+00:00 |
| 422 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2020](https://www.tce.mt.gov.br/julgamento/virtual?ano=2020) | 200 | ev-422 | evidence/ev-422/screenshot.png | 2026-07-06T13:24:36.336247+00:00 |
| 423 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2022](https://www.tce.mt.gov.br/julgamento/virtual?ano=2022) | 200 | ev-423 | evidence/ev-423/screenshot.png | 2026-07-06T13:24:37.423751+00:00 |
| 424 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2018](https://www.tce.mt.gov.br/julgamento/virtual?ano=2018) | 200 | ev-424 | evidence/ev-424/screenshot.png | 2026-07-06T13:24:39.092697+00:00 |
| 425 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2019](https://www.tce.mt.gov.br/julgamento/virtual?ano=2019) | 200 | ev-425 | evidence/ev-425/screenshot.png | 2026-07-06T13:24:39.233224+00:00 |
| 426 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2017](https://www.tce.mt.gov.br/julgamento/virtual?ano=2017) | 200 | ev-426 | evidence/ev-426/screenshot.png | 2026-07-06T13:24:39.823919+00:00 |
| 427 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2014](https://www.tce.mt.gov.br/julgamento/virtual?ano=2014) | 200 | ev-427 | evidence/ev-427/screenshot.png | 2026-07-06T13:24:41.145332+00:00 |
| 428 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2013](https://www.tce.mt.gov.br/julgamento/virtual?ano=2013) | 200 | ev-428 | evidence/ev-428/screenshot.png | 2026-07-06T13:24:41.614927+00:00 |
| 429 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2012](https://www.tce.mt.gov.br/julgamento/virtual?ano=2012) | 200 | ev-429 | evidence/ev-429/screenshot.png | 2026-07-06T13:24:41.930193+00:00 |
| 430 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2015](https://www.tce.mt.gov.br/julgamento/virtual?ano=2015) | 200 | ev-430 | evidence/ev-430/screenshot.png | 2026-07-06T13:24:42.528665+00:00 |
| 431 | [https://www.tce.mt.gov.br/julgamento/virtual?ano=2016](https://www.tce.mt.gov.br/julgamento/virtual?ano=2016) | 200 | ev-431 | evidence/ev-431/screenshot.png | 2026-07-06T13:24:43.686344+00:00 |
| 432 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=25-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=25-05-2026-V-3) | 200 | ev-432 | evidence/ev-432/screenshot.png | 2026-07-06T13:24:44.455276+00:00 |
| 433 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=18-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=18-05-2026-V-3) | 200 | ev-433 | evidence/ev-433/screenshot.png | 2026-07-06T13:24:44.582272+00:00 |
| 434 | [https://www.tce.mt.gov.br/julgamento/virtual/estatisticas?ano=2026](https://www.tce.mt.gov.br/julgamento/virtual/estatisticas?ano=2026) | 200 | ev-434 | evidence/ev-434/screenshot.png | 2026-07-06T13:24:44.640303+00:00 |
| 435 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=11-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=11-05-2026-V-3) | 200 | ev-435 | evidence/ev-435/screenshot.png | 2026-07-06T13:24:45.460379+00:00 |
| 436 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=04-05-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=04-05-2026-V-3) | 200 | ev-436 | evidence/ev-436/screenshot.png | 2026-07-06T13:24:46.480952+00:00 |
| 437 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-03-2026-V-3) | 200 | ev-437 | evidence/ev-437/screenshot.png | 2026-07-06T13:24:47.174986+00:00 |
| 438 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=13-04-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=13-04-2026-V-3) | 200 | ev-438 | evidence/ev-438/screenshot.png | 2026-07-06T13:24:47.752294+00:00 |
| 439 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=06-04-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=06-04-2026-V-3) | 200 | ev-439 | evidence/ev-439/screenshot.png | 2026-07-06T13:24:48.479026+00:00 |
| 440 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=09-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=09-03-2026-V-3) | 200 | ev-440 | evidence/ev-440/screenshot.png | 2026-07-06T13:24:48.996579+00:00 |
| 441 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=16-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=16-03-2026-V-3) | 200 | ev-441 | evidence/ev-441/screenshot.png | 2026-07-06T13:24:49.212005+00:00 |
| 442 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=02-03-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=02-03-2026-V-3) | 200 | ev-442 | evidence/ev-442/screenshot.png | 2026-07-06T13:24:50.094147+00:00 |
| 443 | [https://www.tce.mt.gov.br/processo/2052164/2025](https://www.tce.mt.gov.br/processo/2052164/2025) | 200 | ev-443 | evidence/ev-443/screenshot.png | 2026-07-06T13:24:50.758246+00:00 |
| 444 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052164/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052164/2025) | 200 | ev-444 | evidence/ev-444/screenshot.png | 2026-07-06T13:24:51.310881+00:00 |
| 445 | [https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-02-2026-V-3](https://www.tce.mt.gov.br/julgamento/virtual?pauta=23-02-2026-V-3) | 200 | ev-445 | evidence/ev-445/screenshot.png | 2026-07-06T13:24:52.268196+00:00 |
| 446 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052164/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052164/2025) | 200 | ev-446 | evidence/ev-446/screenshot.png | 2026-07-06T13:24:52.697776+00:00 |
| 447 | [https://www.tce.mt.gov.br/processo/2052172/2025](https://www.tce.mt.gov.br/processo/2052172/2025) | 200 | ev-447 | evidence/ev-447/screenshot.png | 2026-07-06T13:24:52.758439+00:00 |
| 448 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052172/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2052172/2025) | 200 | ev-448 | evidence/ev-448/screenshot.png | 2026-07-06T13:24:53.125182+00:00 |
| 449 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052172/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2052172/2025) | 200 | ev-449 | evidence/ev-449/screenshot.png | 2026-07-06T13:24:53.630964+00:00 |
| 450 | [https://www.tce.mt.gov.br/processo/1961179/2025](https://www.tce.mt.gov.br/processo/1961179/2025) | 200 | ev-450 | evidence/ev-450/screenshot.png | 2026-07-06T13:24:54.005895+00:00 |
| 451 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1961179/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1961179/2025) | 200 | ev-451 | evidence/ev-451/screenshot.png | 2026-07-06T13:24:54.139889+00:00 |
| 452 | [https://www.tce.mt.gov.br/processo/1983881/2025](https://www.tce.mt.gov.br/processo/1983881/2025) | 200 | ev-452 | evidence/ev-452/screenshot.png | 2026-07-06T13:24:54.484348+00:00 |
| 453 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1961179/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1961179/2025) | 200 | ev-453 | evidence/ev-453/screenshot.png | 2026-07-06T13:24:54.672249+00:00 |
| 454 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1983881/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1983881/2025) | 200 | ev-454 | evidence/ev-454/screenshot.png | 2026-07-06T13:24:55.152024+00:00 |
| 455 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1983881/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1983881/2025) | 200 | ev-455 | evidence/ev-455/screenshot.png | 2026-07-06T13:24:55.552075+00:00 |
| 456 | [https://www.tce.mt.gov.br/processo/13307/2021](https://www.tce.mt.gov.br/processo/13307/2021) | 200 | ev-456 | evidence/ev-456/screenshot.png | 2026-07-06T13:24:55.665231+00:00 |
| 457 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/13307/2021](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/13307/2021) | 200 | ev-457 | evidence/ev-457/screenshot.png | 2026-07-06T13:24:55.819038+00:00 |
| 458 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/13307/2021](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/13307/2021) | 200 | ev-458 | evidence/ev-458/screenshot.png | 2026-07-06T13:24:56.176858+00:00 |
| 459 | [https://www.tce.mt.gov.br/processo/2044137/2025](https://www.tce.mt.gov.br/processo/2044137/2025) | 200 | ev-459 | evidence/ev-459/screenshot.png | 2026-07-06T13:24:56.579196+00:00 |
| 460 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2044137/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2044137/2025) | 200 | ev-460 | evidence/ev-460/screenshot.png | 2026-07-06T13:24:56.952703+00:00 |
| 461 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2044137/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2044137/2025) | 200 | ev-461 | evidence/ev-461/screenshot.png | 2026-07-06T13:24:57.128047+00:00 |
| 462 | [https://www.tce.mt.gov.br/processo/2035111/2025](https://www.tce.mt.gov.br/processo/2035111/2025) | 200 | ev-462 | evidence/ev-462/screenshot.png | 2026-07-06T13:24:57.216509+00:00 |
| 463 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035111/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035111/2025) | 200 | ev-463 | evidence/ev-463/screenshot.png | 2026-07-06T13:24:57.429506+00:00 |
| 464 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035111/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035111/2025) | 200 | ev-464 | evidence/ev-464/screenshot.png | 2026-07-06T13:24:57.909560+00:00 |
| 465 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2060302/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2060302/2025) | 200 | ev-465 | evidence/ev-465/screenshot.png | 2026-07-06T13:24:58.520488+00:00 |
| 466 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2060302/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2060302/2025) | 200 | ev-466 | evidence/ev-466/screenshot.png | 2026-07-06T13:24:58.561958+00:00 |
| 467 | [https://www.tce.mt.gov.br/processo/2707098/2026](https://www.tce.mt.gov.br/processo/2707098/2026) | 200 | ev-467 | evidence/ev-467/screenshot.png | 2026-07-06T13:24:58.968251+00:00 |
| 468 | [https://www.tce.mt.gov.br/processo/2060302/2025](https://www.tce.mt.gov.br/processo/2060302/2025) | 200 | ev-468 | evidence/ev-468/screenshot.png | 2026-07-06T13:24:59.127011+00:00 |
| 469 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2707098/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2707098/2026) | 200 | ev-469 | evidence/ev-469/screenshot.png | 2026-07-06T13:24:59.219351+00:00 |
| 470 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2707098/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2707098/2026) | 200 | ev-470 | evidence/ev-470/screenshot.png | 2026-07-06T13:24:59.893382+00:00 |
| 471 | [https://www.tce.mt.gov.br/processo/1921860/2024](https://www.tce.mt.gov.br/processo/1921860/2024) | 200 | ev-471 | evidence/ev-471/screenshot.png | 2026-07-06T13:24:59.986302+00:00 |
| 472 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1921860/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1921860/2024) | 200 | ev-472 | evidence/ev-472/screenshot.png | 2026-07-06T13:25:00.489684+00:00 |
| 473 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1819712/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1819712/2024) | 200 | ev-473 | evidence/ev-473/screenshot.png | 2026-07-06T13:25:01.135267+00:00 |
| 474 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1819712/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1819712/2024) | 200 | ev-474 | evidence/ev-474/screenshot.png | 2026-07-06T13:25:01.290822+00:00 |
| 475 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1921860/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1921860/2024) | 200 | ev-475 | evidence/ev-475/screenshot.png | 2026-07-06T13:25:01.399050+00:00 |
| 476 | [https://www.tce.mt.gov.br/processo/1819712/2024](https://www.tce.mt.gov.br/processo/1819712/2024) | 200 | ev-476 | evidence/ev-476/screenshot.png | 2026-07-06T13:25:01.786660+00:00 |
| 477 | [https://www.tce.mt.gov.br/processo/2035839/2025](https://www.tce.mt.gov.br/processo/2035839/2025) | 200 | ev-477 | evidence/ev-477/screenshot.png | 2026-07-06T13:25:01.963348+00:00 |
| 478 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035839/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2035839/2025) | 200 | ev-478 | evidence/ev-478/screenshot.png | 2026-07-06T13:25:02.498403+00:00 |
| 479 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035839/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2035839/2025) | 200 | ev-479 | evidence/ev-479/screenshot.png | 2026-07-06T13:25:02.862705+00:00 |
| 480 | [https://www.tce.mt.gov.br/processo/1817485/2024](https://www.tce.mt.gov.br/processo/1817485/2024) | 200 | ev-480 | evidence/ev-480/screenshot.png | 2026-07-06T13:25:03.165554+00:00 |
| 481 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1817485/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1817485/2024) | 200 | ev-481 | evidence/ev-481/screenshot.png | 2026-07-06T13:25:03.263599+00:00 |
| 482 | [https://www.tce.mt.gov.br/processo/2112710/2025](https://www.tce.mt.gov.br/processo/2112710/2025) | 200 | ev-482 | evidence/ev-482/screenshot.png | 2026-07-06T13:25:03.970148+00:00 |
| 483 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2112710/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2112710/2025) | 200 | ev-483 | evidence/ev-483/screenshot.png | 2026-07-06T13:25:04.130826+00:00 |
| 484 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1817485/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1817485/2024) | 200 | ev-484 | evidence/ev-484/screenshot.png | 2026-07-06T13:25:04.335651+00:00 |
| 485 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2112710/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2112710/2025) | 200 | ev-485 | evidence/ev-485/screenshot.png | 2026-07-06T13:25:04.666176+00:00 |
| 486 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2713721/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2713721/2026) | 200 | ev-486 | evidence/ev-486/screenshot.png | 2026-07-06T13:25:04.810404+00:00 |
| 487 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/186449/2020](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/186449/2020) | 200 | ev-487 | evidence/ev-487/screenshot.png | 2026-07-06T13:25:05.581166+00:00 |
| 488 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2713721/2026](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2713721/2026) | 200 | ev-488 | evidence/ev-488/screenshot.png | 2026-07-06T13:25:05.626715+00:00 |
| 489 | [https://www.tce.mt.gov.br/processo/186449/2020](https://www.tce.mt.gov.br/processo/186449/2020) | 200 | ev-489 | evidence/ev-489/screenshot.png | 2026-07-06T13:25:05.902310+00:00 |
| 490 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/186449/2020](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/186449/2020) | 200 | ev-490 | evidence/ev-490/screenshot.png | 2026-07-06T13:25:06.015517+00:00 |
| 491 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1808176/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1808176/2024) | 200 | ev-491 | evidence/ev-491/screenshot.png | 2026-07-06T13:25:06.803853+00:00 |
| 492 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1808176/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1808176/2024) | 200 | ev-492 | evidence/ev-492/screenshot.png | 2026-07-06T13:25:06.851879+00:00 |
| 493 | [https://www.tce.mt.gov.br/processo/1808176/2024](https://www.tce.mt.gov.br/processo/1808176/2024) | 200 | ev-493 | evidence/ev-493/screenshot.png | 2026-07-06T13:25:06.975718+00:00 |
| 494 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1805290/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/1805290/2024) | 200 | ev-494 | evidence/ev-494/screenshot.png | 2026-07-06T13:25:07.508996+00:00 |
| 495 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1805290/2024](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/1805290/2024) | 200 | ev-495 | evidence/ev-495/screenshot.png | 2026-07-06T13:25:07.545365+00:00 |
| 496 | [https://www.tce.mt.gov.br/processo/2088428/2025](https://www.tce.mt.gov.br/processo/2088428/2025) | 200 | ev-496 | evidence/ev-496/screenshot.png | 2026-07-06T13:25:08.119814+00:00 |
| 497 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2088428/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/2088428/2025) | 200 | ev-497 | evidence/ev-497/screenshot.png | 2026-07-06T13:25:08.244504+00:00 |
| 498 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2088428/2025](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/2088428/2025) | 200 | ev-498 | evidence/ev-498/screenshot.png | 2026-07-06T13:25:08.330535+00:00 |
| 499 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/500470/2023](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/discussao/500470/2023) | 200 | ev-499 | evidence/ev-499/screenshot.png | 2026-07-06T13:25:08.901770+00:00 |
| 500 | [https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/500470/2023](https://plenariovirtual.tce.mt.gov.br/pauta/2026-05-25/V/3/votacao/500470/2023) | 200 | ev-500 | evidence/ev-500/screenshot.png | 2026-07-06T13:25:09.432339+00:00 |
| 501 | [https://www.tce.mt.gov.br/processo/500470/2023](https://www.tce.mt.gov.br/processo/500470/2023) | 200 | ev-501 | evidence/ev-501/screenshot.png | 2026-07-06T13:25:09.862956+00:00 |
| 502 | [https://www.tce.mt.gov.br/processo/1819402/2024](https://www.tce.mt.gov.br/processo/1819402/2024) | 200 | ev-502 | evidence/ev-502/screenshot.png | 2026-07-06T13:25:10.354611+00:00 |
| 503 | [https://www.tce.mt.gov.br/processo/635456/2023](https://www.tce.mt.gov.br/processo/635456/2023) | 200 | ev-503 | evidence/ev-503/screenshot.png | 2026-07-06T13:25:10.488529+00:00 |


---

*Relatório gerado automaticamente por LGPD Auditor. Reprodutível a partir de `audit_results.json` e `visited_routes.json`.*