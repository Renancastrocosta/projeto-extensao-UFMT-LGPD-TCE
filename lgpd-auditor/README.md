# LGPD Auditor

Ferramenta Python para **auditoria automatizada de conformidade LGPD** em portais institucionais. O projeto navega o site-alvo, coleta evidências auditáveis, aplica regras heurísticas baseadas na legislação e gera relatórios estruturados para análise acadêmica e institucional.

## Objetivo

Automatizar a avaliação de portais públicos quanto à aderência à **Lei Geral de Proteção de Dados (LGPD)**, com rastreabilidade completa: cada achado é vinculado a evidências (screenshots, metadados e hashes), fundamentação legal e decisões registradas no Diário de Engenharia.

O caso de referência atual é o portal do **Tribunal de Contas do Estado de Mato Grosso (TCE-MT)**, mas a arquitetura permite auditar outros portais via arquivo de configuração.

## O que o projeto faz

| Etapa | Comando | Resultado |
|-------|---------|-----------|
| Inicialização | `init` | Cria diretórios e registra decisões de fundação |
| Crawler | `run` | Navega o portal (BFS), respeita `robots.txt`, gera checkpoints |
| Evidências | `evidence` | Captura screenshots e metadados por rota visitada |
| Auditoria | `audit` | Aplica regras LGPD heurísticas sobre as evidências |
| Relatório | `report` | Gera Markdown, HTML e CSV de rotas |
| Exportação | `export` | PDF, dashboard HTML, síntese executiva e OCR opcional |
| Pipeline completo | `finalize` | Executa todas as etapas e valida requisitos (RNFs) |

## Requisitos

- **Python** 3.11 ou superior
- **Chromium** (instalado via Playwright)
- **Tesseract OCR** (opcional, apenas para `--ocr`)
- **WeasyPrint** (opcional, para exportação em PDF — dependências de sistema podem ser necessárias)

## Instalação

```bash
cd lgpd-auditor
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -e ".[dev]"
playwright install chromium
```

Dependências opcionais:

```bash
pip install -e ".[ocr]"   # OCR com Tesseract
pip install -e ".[pdf]"   # Exportação PDF
```

## Início rápido

Execute os comandos a partir do diretório raiz do projeto (`lgpd-auditor/`):

```bash
# 1. Inicializar estrutura da auditoria
lgpd-auditor init --config config/tce-mt.yaml

# 2. Navegar o portal e registrar rotas
lgpd-auditor run --config config/tce-mt.yaml

# 3. Pipeline completo (recomendado após o crawler)
lgpd-auditor finalize --config config/tce-mt.yaml
```

Para um teste rápido com poucas páginas:

```bash
lgpd-auditor evidence --config config/tce-mt.yaml --limit 5
lgpd-auditor audit --config config/tce-mt.yaml
lgpd-auditor report --config config/tce-mt.yaml
```

## Comandos CLI

```bash
lgpd-auditor --version
lgpd-auditor init    --config config/tce-mt.yaml
lgpd-auditor run     --config config/tce-mt.yaml
lgpd-auditor evidence --config config/tce-mt.yaml [--limit N]
lgpd-auditor audit   --config config/tce-mt.yaml
lgpd-auditor report  --config config/tce-mt.yaml
lgpd-auditor export  --config config/tce-mt.yaml [--ocr] [--ocr-limit N] [--no-pdf] [--no-dashboard] [--no-synthesis]
lgpd-auditor finalize --config config/tce-mt.yaml [--skip-evidence]
```

Consulte o [Guia de Uso](docs/guia-de-uso.md) para detalhes de cada comando, flags e cenários de execução.

## Estrutura do projeto

```
lgpd-auditor/
├── config/                  # Configurações por portal auditado
│   └── tce-mt.yaml
├── legislation.yaml         # Normas e regras de conformidade versionadas
├── src/lgpd_auditor/        # Código-fonte modular
│   ├── cli.py               # Interface de linha de comando
│   ├── crawler/             # Navegação BFS com Playwright
│   ├── evidence/            # Captura e armazenamento de evidências
│   ├── audit/               # Motor de regras e classificadores LGPD
│   ├── report/              # Geração de relatórios
│   ├── validation/          # Validação de RNFs e checklist MUST
│   └── governance/          # Diário de Engenharia
├── templates/report/        # Templates Jinja2 para relatórios
├── audits/tce-mt/           # Artefatos da auditoria TCE-MT
│   ├── checkpoints/         # Estado retomável do crawler
│   ├── evidence/            # Screenshots e metadados (ev-NNN/)
│   ├── reports/             # Relatórios gerados
│   └── engineering_diary.jsonl
├── tests/                   # Testes automatizados
└── docs/                    # Documentação detalhada
```

## Documentação

| Documento | Conteúdo |
|-----------|----------|
| [Guia de Uso](docs/guia-de-uso.md) | Fluxo completo, comandos, artefatos e troubleshooting |
| [Arquitetura](docs/arquitetura.md) | Módulos, pipeline de dados e governança |
| [Configuração](docs/configuracao.md) | YAML de auditoria, legislação e novo portal |

## Testes

```bash
pytest
```

## Fases de desenvolvimento

| Fase | Descrição | Status |
|------|-----------|--------|
| 0 | Fundação e governança | Concluída |
| 1 | Crawler e checkpoints | Concluída |
| 2 | Evidências | Concluída |
| 3 | Motor LGPD | Concluída |
| 4 | Relatório | Concluída |
| 5 | OCR / PDF / síntese | Concluída |
| 6 | Execução final e validação | Concluída |

## Licença

MIT — veja `pyproject.toml`.
