"""
Tool: audit_architecture.py
Audita divergências entre o diagrama de arquitetura e a realidade do projeto.

Uso:
  python tools/audit_architecture.py
  python tools/audit_architecture.py --output-dir gemini/audits/
  python tools/audit_architecture.py --diagram docs/wat-studio-architecture.html

O que faz:
  1. Auto-descobre arquivos reais: tools/, workflows/, clients/*/client.json
  2. Lê o diagrama HTML da arquitetura
  3. Envia ao Gemini para análise comparativa
  4. Gera relatório de divergências em gemini/audits/

Output esperado:
  - Tabela: O QUE O DIAGRAMA MOSTRA vs REALIDADE vs STATUS
  - Gap crítico (se houver)
  - Sugestões de próximo passo
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv()

ROOT = Path(__file__).parent.parent
DIAGRAM_PATH = ROOT / "docs" / "wat-studio-architecture.html"


def discover_project_state() -> dict:
    """Auto-descobre o estado real do projeto. Retorna dicionário estruturado."""
    state = {}

    # Tools reais
    tools_dir = ROOT / "tools"
    state["tools"] = sorted(f.name for f in tools_dir.glob("*.py") if f.is_file())

    # Workflows reais
    workflows_dir = ROOT / "workflows"
    state["workflows"] = sorted(f.name for f in workflows_dir.glob("*.md") if f.is_file())

    # Clients
    clients_dir = ROOT / "clients"
    state["clients"] = []
    if clients_dir.exists():
        for client_dir in sorted(clients_dir.iterdir()):
            if client_dir.is_dir():
                client_json = client_dir / "client.json"
                entry = {"slug": client_dir.name, "has_client_json": client_json.exists()}
                if client_json.exists():
                    try:
                        entry["client_json"] = client_json.read_text(encoding="utf-8")
                    except Exception:
                        pass
                state["clients"].append(entry)

    # Docs
    docs_dir = ROOT / "docs"
    state["docs"] = sorted(f.name for f in docs_dir.glob("*") if f.is_file())

    # Verifica arquivos esperados mas ausentes
    expected_files = [
        "CLAUDE.template.md",
        "tools/generate_images_api.py",
        "tools/generate_images_manus.py",
    ]
    state["missing_expected"] = [
        f for f in expected_files if not (ROOT / f).exists()
    ]

    # Frontend
    frontend_dir = ROOT / "frontend"
    if frontend_dir.exists():
        state["frontend"] = sorted(
            str(f.relative_to(ROOT)) for f in frontend_dir.rglob("*") if f.is_file()
        )

    return state


def format_state_as_text(state: dict) -> str:
    lines = ["## ESTADO REAL DO PROJETO\n"]

    lines.append(f"### tools/ ({len(state.get('tools', []))} scripts)")
    for t in state.get("tools", []):
        lines.append(f"  - {t}")

    lines.append(f"\n### workflows/ ({len(state.get('workflows', []))} arquivos)")
    for w in state.get("workflows", []):
        lines.append(f"  - {w}")

    lines.append(f"\n### clients/ ({len(state.get('clients', []))} clientes)")
    for c in state.get("clients", []):
        lines.append(f"  - {c['slug']} (client.json: {'sim' if c['has_client_json'] else 'não'})")

    lines.append(f"\n### docs/ ({len(state.get('docs', []))} arquivos)")
    for d in state.get("docs", []):
        lines.append(f"  - {d}")

    if state.get("frontend"):
        lines.append(f"\n### frontend/")
        for f in state["frontend"]:
            lines.append(f"  - {f}")

    missing = state.get("missing_expected", [])
    if missing:
        lines.append(f"\n### Arquivos esperados mas AUSENTES ({len(missing)})")
        for m in missing:
            lines.append(f"  ✗ {m}")

    return "\n".join(lines)


def read_diagram(diagram_path: Path) -> str:
    if not diagram_path.exists():
        return f"[ERRO] Diagrama não encontrado em {diagram_path}"
    return diagram_path.read_text(encoding="utf-8")


def build_audit_prompt(state_text: str, diagram_html: str) -> str:
    return f"""Você é um auditor de arquitetura de software. Sua tarefa é comparar o diagrama de arquitetura com o estado real do projeto e identificar divergências.

{state_text}

---

## DIAGRAMA DE ARQUITETURA (HTML — leia os nós e edges do Cytoscape)

{diagram_html}

---

## TAREFA

Compare o diagrama acima com o estado real do projeto e produza:

### 1. Tabela de Divergências
Use este formato:
| # | O diagrama mostra | Realidade | Status | Ação recomendada |
|---|---|---|---|---|

Status possíveis: ✅ OK | ◌ Planejado | ✗ Ausente no diagrama | ⚠ Divergente

### 2. Gap Crítico
Identifique o gap mais importante que pode causar falhas operacionais (ex: caminho de migração não documentado, tool referenciada mas não criada).

### 3. Próximos Passos Prioritários
Liste 3 ações concretas, em ordem de impacto.

---

Seja objetivo e preciso. Foque em divergências que afetam a operação real do sistema.

<brief>
TAREFA: Audit de divergências arquitetura vs realidade
ARQUIVOS LIDOS: diagrama HTML + estado auto-descoberto do projeto
RESUMO: [preencher com 3-5 linhas do que foi encontrado]
PRÓXIMO PASSO PARA O CLAUDE: Aplicar correções no diagrama e criar arquivos ausentes identificados
</brief>
"""


def call_gemini(prompt: str, model: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[ERRO] GEMINI_API_KEY não encontrada no .env", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text


def save_output(content: str, output_dir: str) -> Path:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}_audit-architecture.md"
    filepath = out_path / filename
    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Audita divergências entre diagrama e realidade")
    parser.add_argument("--output-dir", default="gemini/audits/", help="Pasta de destino do relatório")
    parser.add_argument("--diagram", default=str(DIAGRAM_PATH), help="Caminho para o diagrama HTML")
    parser.add_argument("--model", default=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"))
    args = parser.parse_args()

    print("[INFO] Descobrindo estado real do projeto...", file=sys.stderr)
    state = discover_project_state()
    state_text = format_state_as_text(state)

    print("[INFO] Lendo diagrama...", file=sys.stderr)
    diagram_html = read_diagram(Path(args.diagram))

    prompt = build_audit_prompt(state_text, diagram_html)
    tokens_est = len(prompt) // 4
    print(f"[INFO] Tokens estimados: ~{tokens_est:,}", file=sys.stderr)

    print(f"[INFO] Chamando {args.model}...", file=sys.stderr)
    resultado = call_gemini(prompt, args.model)

    filepath = save_output(resultado, args.output_dir)
    print(f"[OK] Relatório salvo em: {filepath}", file=sys.stderr)

    sys.stdout.buffer.write((resultado + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
