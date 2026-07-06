# Guia de Uso

Este guia descreve o fluxo operacional do **LGPD Auditor**, desde a instalação até a entrega dos artefatos finais.

## Pré-requisitos

1. Ambiente virtual Python 3.11+ ativado
2. Pacote instalado em modo editável: `pip install -e ".[dev]"`
3. Navegador Chromium do Playwright: `playwright install chromium`
4. Todos os comandos executados a partir do diretório raiz `lgpd-auditor/`

## Visão geral do fluxo

```
init → run → evidence → audit → report → export
                  └──────────── finalize ────────────┘
```

O comando `finalize` orquestra automaticamente as etapas de evidências, auditoria, relatório, exportação e validação. Use-o após o crawler (`run`) para uma execução completa.

## Passo a passo

### 1. Inicializar (`init`)

Cria os diretórios da auditoria e registra a primeira entrada no Diário de Engenharia.

```bash
lgpd-auditor init --config config/tce-mt.yaml
```

**Saída esperada:** confirmação do ID da auditoria e caminho do diário em `audits/tce-mt/engineering_diary.jsonl`.

### 2. Crawler (`run`)

Navega o portal em largura (BFS) com workers concorrentes, respeitando `robots.txt` e o domínio permitido.

```bash
lgpd-auditor run --config config/tce-mt.yaml
```

**Artefatos gerados:**

| Arquivo | Descrição |
|---------|-----------|
| `audits/tce-mt/visited_routes.json` | Log de todas as rotas visitadas |
| `audits/tce-mt/checkpoints/` | Estado retomável do crawler |
| `audits/tce-mt/checkpoints/html_resumo/` | Resumo HTML por URL |

O crawler pode ser interrompido e retomado: os checkpoints preservam o progresso.

### 3. Captura de evidências (`evidence`)

Para cada rota visitada, captura screenshot PNG, resumo textual da página e metadados com hashes de integridade.

```bash
# Captura completa
lgpd-auditor evidence --config config/tce-mt.yaml

# Teste com limite de rotas
lgpd-auditor evidence --config config/tce-mt.yaml --limit 5
```

**Estrutura por evidência:**

```
audits/tce-mt/evidence/ev-001/
├── metadata.json       # URL, hashes, timestamps, status HTTP
├── screenshot.png      # Captura visual da página
└── page_summary.txt    # Texto extraído para análise
```

A captura é **incremental**: rotas já evidenciadas são ignoradas automaticamente.

### 4. Auditoria LGPD (`audit`)

Aplica regras heurísticas definidas em `legislation.yaml` sobre o texto das evidências.

```bash
lgpd-auditor audit --config config/tce-mt.yaml
```

**Seções avaliadas:**

| ID | Seção | Prioridade |
|----|-------|------------|
| 4.1 | Transparência (política de privacidade) | P0 |
| 4.2 | Coleta de dados (formulários) | P2 |
| 4.3 | Consentimento | P0 |
| 4.4 | Direitos do titular | P0 |
| 4.5 | Segurança da informação | P1 |
| 4.6 | Cookies | P2 |

**Saída:** `audits/tce-mt/audit_results.json` com achados, resumo por seção, nível de confiança e IDs de evidência vinculados.

### 5. Relatório (`report`)

Gera o relatório estruturado a partir dos resultados da auditoria.

```bash
lgpd-auditor report --config config/tce-mt.yaml
```

**Artefatos em `audits/tce-mt/reports/`:**

| Arquivo | Formato |
|---------|---------|
| `relatorio-lgpd-tce-mt.md` | Markdown (fonte principal) |
| `relatorio-lgpd-tce-mt.html` | HTML renderizado |
| `visited_routes.csv` | Planilha de rotas visitadas |

### 6. Exportação (`export`)

Gera artefatos complementares para entrega e visualização.

```bash
# Exportação padrão (PDF + dashboard + síntese)
lgpd-auditor export --config config/tce-mt.yaml

# Com OCR nos screenshots
lgpd-auditor export --config config/tce-mt.yaml --ocr --ocr-limit 10

# Exportação parcial
lgpd-auditor export --config config/tce-mt.yaml --no-pdf --no-synthesis
```

**Artefatos adicionais:**

| Arquivo | Descrição |
|---------|-----------|
| `relatorio-lgpd-tce-mt.pdf` | Relatório em PDF (requer WeasyPrint) |
| `dashboard.html` | Painel visual com resumo da auditoria |
| `sintese-executiva.md` | Síntese gerada automaticamente |

### 7. Pipeline final (`finalize`)

Executa em sequência: evidências → auditoria → relatório → export → validação de RNFs.

```bash
# Execução completa
lgpd-auditor finalize --config config/tce-mt.yaml

# Reprocessar sem recapturar evidências
lgpd-auditor finalize --config config/tce-mt.yaml --skip-evidence
```

**Validações realizadas:**

- Requisitos não funcionais (workers, memória, cobertura de evidências)
- Checklist MUST da especificação técnica
- Relatório `audits/tce-mt/validation_report.json`

**Códigos de saída:**

| Código | Significado |
|--------|-------------|
| `0` | Entrega aprovada para submissão |
| `2` | Entrega parcial — complete evidências e reexecute |

## Cenários comuns

### Teste rápido (desenvolvimento)

```bash
lgpd-auditor init --config config/tce-mt.yaml
lgpd-auditor run --config config/tce-mt.yaml
lgpd-auditor evidence --config config/tce-mt.yaml --limit 5
lgpd-auditor audit --config config/tce-mt.yaml
lgpd-auditor report --config config/tce-mt.yaml
```

### Auditoria completa (entrega)

```bash
lgpd-auditor init --config config/tce-mt.yaml
lgpd-auditor run --config config/tce-mt.yaml
lgpd-auditor finalize --config config/tce-mt.yaml
```

### Reprocessar relatório sem recapturar

```bash
lgpd-auditor audit --config config/tce-mt.yaml
lgpd-auditor report --config config/tce-mt.yaml
lgpd-auditor export --config config/tce-mt.yaml
```

## Referência de flags

### `evidence`

| Flag | Tipo | Descrição |
|------|------|-----------|
| `--config` | string | Caminho do YAML (padrão: `config/tce-mt.yaml`) |
| `--limit` | int | Limita quantidade de rotas a capturar |

### `export`

| Flag | Descrição |
|------|-----------|
| `--no-pdf` | Não gera PDF |
| `--no-dashboard` | Não gera dashboard HTML |
| `--no-synthesis` | Não gera síntese executiva |
| `--ocr` | Executa OCR nos screenshots (requer Tesseract) |
| `--ocr-limit` | Limita quantidade de screenshots para OCR |

### `finalize`

| Flag | Descrição |
|------|-----------|
| `--skip-evidence` | Pula captura de evidências (usa existentes) |

## Troubleshooting

### `Erro: configuração não encontrada`

Execute os comandos a partir do diretório `lgpd-auditor/` ou informe o caminho absoluto em `--config`.

### Crawler com muitos erros

- Verifique conectividade com o portal
- Aumente `timeout_segundos` em `config/tce-mt.yaml`
- Confira se o portal está acessível e não bloqueia o user-agent

### PDF não gerado

Instale as dependências opcionais e bibliotecas de sistema do WeasyPrint:

```bash
pip install -e ".[pdf]"
```

### OCR indisponível

Instale o Tesseract no sistema operacional e o pacote Python:

```bash
pip install -e ".[ocr]"
# Fedora: sudo dnf install tesseract
# Ubuntu: sudo apt install tesseract-ocr
```

### `finalize` retorna código 2

Indica entrega parcial. Verifique:

1. Quantidade de rotas com screenshot vs. total em `visited_routes.json`
2. Conteúdo de `validation_report.json`
3. Reexecute `evidence` sem `--limit` e depois `finalize`
