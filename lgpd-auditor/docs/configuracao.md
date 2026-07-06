# Configuração

Referência dos arquivos de configuração do **LGPD Auditor**.

## Arquivo de auditoria (`config/*.yaml`)

Cada portal auditado possui um arquivo YAML validado por Pydantic. Exemplo: `config/tce-mt.yaml`.

### Seção `audit`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | string | Identificador único da auditoria (ex: `tce-mt`) |
| `nome` | string | Nome institucional para relatórios |
| `url_base` | URL | Ponto de partida do crawler |
| `dominio_permitido` | string | Domínio aceito (links externos são ignorados) |

```yaml
audit:
  id: tce-mt
  nome: "Tribunal de Contas do Estado de Mato Grosso"
  url_base: "https://www.tce.mt.gov.br/"
  dominio_permitido: "tce.mt.gov.br"
```

### Seção `crawler`

| Campo | Padrão | Descrição |
|-------|--------|-----------|
| `max_workers` | `5` | Workers concorrentes do Playwright |
| `max_paginas` | `500` | Limite de páginas por execução |
| `max_paginas_escalavel` | `20000` | Limite máximo para validação RNF |
| `rate_limit_segundos` | `0.5` | Intervalo mínimo entre requisições por worker |
| `timeout_segundos` | `30` | Timeout de carregamento por página |
| `respeitar_robots_txt` | `true` | Honrar regras do `robots.txt` |
| `user_agent` | `LGPD-Auditor/0.1.0` | User-Agent enviado nas requisições |

```yaml
crawler:
  max_workers: 5
  max_paginas: 500
  max_paginas_escalavel: 20000
  rate_limit_segundos: 0.5
  timeout_segundos: 30
  respeitar_robots_txt: true
  user_agent: "LGPD-Auditor/0.1.0 (auditoria-academica; +https://www.tce.mt.gov.br)"
```

### Seção `performance`

| Campo | Padrão | Descrição |
|-------|--------|-----------|
| `tempo_maximo_minutos` | `15` | Referência para validação de tempo |
| `memoria_maxima_mb` | `2048` | Limite de memória do processo (RNF) |

### Seção `paths`

Caminhos relativos ao diretório raiz do projeto. Todos são criados automaticamente pelo comando `init`.

```yaml
paths:
  audit_dir: "audits/tce-mt"
  checkpoints: "audits/tce-mt/checkpoints"
  evidence: "audits/tce-mt/evidence"
  visited_routes: "audits/tce-mt/visited_routes.json"
  reports: "audits/tce-mt/reports"
  engineering_diary: "audits/tce-mt/engineering_diary.jsonl"
```

### Campo `legislation`

Caminho para o arquivo de normas e regras (padrão: `legislation.yaml`).

```yaml
legislation: "legislation.yaml"
```

## Legislação e regras (`legislation.yaml`)

Arquivo versionado com referências normativas e regras de conformidade aplicadas pelo motor de auditoria.

### Referências normativas

| Seção | Conteúdo |
|-------|----------|
| `lgpd` | Lei 13.709/2018 — artigos relevantes |
| `anpd` | Guias e referências da ANPD |
| `iso27001` | Controles de segurança da informação |
| `iso27701` | Controles de privacidade |
| `owasp` | Categorias OWASP Top 10 |

### Regras de conformidade

Cada regra em `regras_conformidade` define:

| Campo | Descrição |
|-------|-----------|
| `id` | Identificador da seção no relatório (ex: `4.1`) |
| `descricao` | Texto descritivo da verificação |
| `prioridade` | `P0` (crítica), `P1` (alta), `P2` (média) |
| `keywords` | Termos buscados no texto das páginas |
| `fundamentacao` | Base legal (ex: `art. 9 LGPD`) |

Exemplo:

```yaml
regras_conformidade:
  transparencia:
    id: "4.1"
    descricao: "Política de privacidade acessível e clara"
    prioridade: P0
    keywords:
      - privacidade
      - política de privacidade
      - proteção de dados
    fundamentacao: ["art. 9 LGPD"]
```

> **Importante:** quando uma norma sofrer alteração, registre no Diário de Engenharia: *"Norma alterada. Necessária revisão das regras de conformidade."*

## Criar auditoria para novo portal

1. Copie o template:

```bash
cp config/tce-mt.yaml config/meu-portal.yaml
```

2. Edite os campos de `audit`, `crawler.user_agent` e `paths`:

```yaml
audit:
  id: meu-portal
  nome: "Nome da Instituição"
  url_base: "https://www.exemplo.gov.br/"
  dominio_permitido: "exemplo.gov.br"

paths:
  audit_dir: "audits/meu-portal"
  checkpoints: "audits/meu-portal/checkpoints"
  evidence: "audits/meu-portal/evidence"
  visited_routes: "audits/meu-portal/visited_routes.json"
  reports: "audits/meu-portal/reports"
  engineering_diary: "audits/meu-portal/engineering_diary.jsonl"
```

3. Execute com o novo config:

```bash
lgpd-auditor init --config config/meu-portal.yaml
lgpd-auditor run --config config/meu-portal.yaml
lgpd-auditor finalize --config config/meu-portal.yaml
```

## Variáveis de ambiente

O projeto não utiliza variáveis de ambiente obrigatórias. Toda configuração é feita via arquivos YAML.

Dependências de sistema para funcionalidades opcionais:

| Funcionalidade | Dependência de sistema |
|----------------|------------------------|
| Crawler / evidências | Chromium (via `playwright install`) |
| OCR (`--ocr`) | Tesseract OCR instalado no SO |
| PDF | Bibliotecas do WeasyPrint (cairo, pango) |

## Versionamento de artefatos

Recomendações para controle de versão:

| Conteúdo | Versionar? |
|----------|------------|
| Código-fonte (`src/`) | Sim |
| Configurações (`config/`, `legislation.yaml`) | Sim |
| Templates (`templates/`) | Sim |
| Relatórios gerados (`reports/`) | Opcional |
| Screenshots (`evidence/**/screenshot.png`) | Opcional (podem ser grandes) |
| Checkpoints e caches | Não |
| Ambiente virtual (`.venv/`) | Não |

O `.gitignore` já exclui `.venv/`, `__pycache__/` e caches de teste. Para excluir screenshots, descomente a linha correspondente no `.gitignore`.
