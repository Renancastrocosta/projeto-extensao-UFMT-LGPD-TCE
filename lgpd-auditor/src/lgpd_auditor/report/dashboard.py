"""Dashboard HTML estático a partir dos resultados da auditoria."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


DASHBOARD_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Dashboard LGPD — {{ audit_id }}</title>
  <style>
    * { box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; margin: 0; background: #f4f6f9; color: #1a1a1a; }
    header { background: #0d3b66; color: white; padding: 1.5rem 2rem; }
    main { padding: 2rem; max-width: 1100px; margin: 0 auto; }
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
    .card { background: white; border-radius: 8px; padding: 1.2rem; box-shadow: 0 1px 4px rgba(0,0,0,.1); }
    .card h3 { margin: 0 0 .5rem; font-size: .85rem; color: #555; text-transform: uppercase; }
    .card .valor { font-size: 2rem; font-weight: 700; color: #0d3b66; }
    table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,.1); }
    th, td { padding: .75rem 1rem; text-align: left; border-bottom: 1px solid #eee; }
    th { background: #e8f0fe; }
    .badge { display: inline-block; padding: .2rem .6rem; border-radius: 12px; font-size: .8rem; font-weight: 600; }
    .badge-confirmado { background: #d4edda; color: #155724; }
    .badge-inferencia { background: #fff3cd; color: #856404; }
    .badge-nao { background: #f8d7da; color: #721c24; }
    .barra { height: 8px; background: #e0e0e0; border-radius: 4px; margin-top: .3rem; }
    .barra-fill { height: 100%; background: #0d3b66; border-radius: 4px; }
  </style>
</head>
<body>
  <header>
    <h1>Dashboard LGPD — {{ portal_nome }}</h1>
    <p>{{ url_base }} | Gerado em {{ gerado_em }}</p>
  </header>
  <main>
    <div class="cards">
      <div class="card"><h3>Rotas visitadas</h3><div class="valor">{{ total_rotas }}</div></div>
      <div class="card"><h3>Páginas analisadas</h3><div class="valor">{{ total_paginas }}</div></div>
      <div class="card"><h3>Total achados</h3><div class="valor">{{ total_achados }}</div></div>
      <div class="card"><h3>Evidências capturadas</h3><div class="valor">{{ total_evidencias }}</div></div>
    </div>

    <h2>Status por seção LGPD</h2>
    <table>
      <tr><th>Seção</th><th>Título</th><th>Status</th><th>Confiança</th><th>Evidências</th></tr>
      {% for secao in secoes %}
      <tr>
        <td>{{ secao.id }}</td>
        <td>{{ secao.titulo }}</td>
        <td><span class="badge badge-{{ secao.badge }}">{{ secao.status }}</span></td>
        <td>
          {{ secao.confianca }} ({{ secao.percentual }}%)
          <div class="barra"><div class="barra-fill" style="width:{{ secao.percentual }}%"></div></div>
        </td>
        <td>{{ secao.evidence_count }}</td>
      </tr>
      {% endfor %}
    </table>

    <h2 style="margin-top:2rem">Distribuição de status (achados)</h2>
    <table>
      <tr><th>Status</th><th>Quantidade</th></tr>
      {% for status, count in status_counts.items() %}
      <tr><td>{{ status }}</td><td>{{ count }}</td></tr>
      {% endfor %}
    </table>
  </main>
</body>
</html>
"""


class DashboardGenerator:
    """Gera dashboard HTML estático."""

    def __init__(self, project_root: Path) -> None:
        self._project_root = project_root

    def gerar(
        self,
        audit_data: dict,
        total_rotas: int,
        total_evidencias: int,
        output_path: Path,
        portal_nome: str = "",
        url_base: str = "",
    ) -> Path:
        resumo = audit_data.get("resumo_por_secao", {})
        achados = audit_data.get("achados", [])

        secoes = []
        for secao_id in sorted(resumo.keys()):
            dados = resumo[secao_id]
            status = dados.get("status", "")
            badge = (
                "confirmado" if status == "Confirmado"
                else "inferencia" if status == "Inferência"
                else "nao"
            )
            secoes.append({
                "id": secao_id,
                "titulo": dados.get("titulo", ""),
                "status": status,
                "confianca": dados.get("confianca", ""),
                "percentual": dados.get("percentual", 0),
                "evidence_count": len(dados.get("evidence_ids", [])),
                "badge": badge,
            })

        status_counts = dict(Counter(a.get("status", "") for a in achados))

        env = Environment(autoescape=select_autoescape(["html"]))
        template = env.from_string(DASHBOARD_TEMPLATE)
        html = template.render(
            audit_id=audit_data.get("audit_id", ""),
            portal_nome=portal_nome,
            url_base=url_base,
            gerado_em=audit_data.get("gerado_em", ""),
            total_rotas=total_rotas,
            total_paginas=audit_data.get("total_paginas_analisadas", 0),
            total_achados=len(achados),
            total_evidencias=total_evidencias,
            secoes=secoes,
            status_counts=status_counts,
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")
        return output_path

    @staticmethod
    def carregar_audit_results(path: Path) -> dict:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
