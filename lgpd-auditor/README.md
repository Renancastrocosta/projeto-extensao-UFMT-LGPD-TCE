# LGPD Auditor

Ferramenta Python para auditoria de conformidade LGPD em portais institucionais.

## Instalação

```bash
cd lgpd-auditor
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
playwright install chromium
```

## Uso (Fase 0)

```bash
lgpd-auditor --version
lgpd-auditor init --config config/tce-mt.yaml
lgpd-auditor run --config config/tce-mt.yaml
lgpd-auditor evidence --config config/tce-mt.yaml
lgpd-auditor evidence --config config/tce-mt.yaml --limit 5
lgpd-auditor audit --config config/tce-mt.yaml
lgpd-auditor report --config config/tce-mt.yaml
lgpd-auditor export --config config/tce-mt.yaml
lgpd-auditor export --config config/tce-mt.yaml --ocr --ocr-limit 5
lgpd-auditor finalize --config config/tce-mt.yaml
```

## Estrutura

- `legislation.yaml` — normas e regras de conformidade versionadas
- `config/tce-mt.yaml` — configuração da auditoria do portal TCE-MT
- `src/lgpd_auditor/` — código-fonte modular
- `audits/tce-mt/` — artefatos de auditoria (checkpoints, evidências, relatórios)

## Fases de desenvolvimento

| Fase | Status |
|------|--------|
| 0 — Fundação e governança | Concluída |
| 1 — Crawler e checkpoints | Concluída |
| 2 — Evidências | Concluída |
| 3 — Motor LGPD | Concluída |
| 4 — Relatório | Concluída |
| 5 — OCR/PDF/IA | Concluída |
| 6 — Execução final | Concluída |
