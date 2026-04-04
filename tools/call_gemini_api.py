"""
Tool: call_gemini_api.py
Chama o Gemini API com arquivos e task — Claude não lê os arquivos, só o resultado.

Uso:
  python tools/call_gemini_api.py \
    --task "Resuma o contexto do negócio em 1 página" \
    --files clients/mayara/context/negocio/ \
    --output-dir gemini/briefs/ \
    --model gemini-2.5-flash

Modelos disponíveis (free tier):
  gemini-2.5-flash       → até 250 req/dia  — qualidade principal
  gemini-2.5-flash-lite  → até 1000 req/dia — volume alto
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ── Limites de segurança (free tier) ────────────────────────────────────────
TOKEN_LIMIT_WARNING = 800_000   # Avisa se o input estiver chegando perto de 1M
MAX_FILE_SIZE_KB = 500          # Ignora arquivos maiores que isso (binários, etc.)

# ── Tipos de output por pasta de destino ────────────────────────────────────
OUTPUT_TYPES = {
    "gemini/briefs":    "brief de contexto",
    "gemini/research":  "pesquisa",
    "gemini/drafts":    "rascunho de conteúdo",
    "gemini/audits":    "audit de voz",
}


def collect_files(paths: list[str]) -> dict[str, str]:
    """Lê arquivos e pastas. Retorna {caminho: conteudo}."""
    collected = {}
    for p in paths:
        path = Path(p)
        if path.is_file():
            _read_file(path, collected)
        elif path.is_dir():
            for f in sorted(path.rglob("*.md")) + sorted(path.rglob("*.txt")) + sorted(path.rglob("*.json")):
                _read_file(f, collected)
        else:
            print(f"[AVISO] Caminho não encontrado: {p}", file=sys.stderr)
    return collected


def _read_file(path: Path, collected: dict):
    size_kb = path.stat().st_size / 1024
    if size_kb > MAX_FILE_SIZE_KB:
        print(f"[IGNORADO] {path} ({size_kb:.0f}KB > limite {MAX_FILE_SIZE_KB}KB)", file=sys.stderr)
        return
    try:
        collected[str(path)] = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERRO ao ler {path}]: {e}", file=sys.stderr)


def build_prompt(task: str, files: dict[str, str]) -> str:
    """Monta o prompt com os arquivos embutidos."""
    sections = []
    for filepath, content in files.items():
        sections.append(f"--- ARQUIVO: {filepath} ---\n{content}")

    files_block = "\n\n".join(sections) if sections else "(nenhum arquivo fornecido)"

    return f"""Você é o Pesquisador e Destilador de Contexto do projeto Mayara.
Sua função é processar os arquivos abaixo e executar a tarefa com precisão.

## TAREFA
{task}

## ARQUIVOS DE CONTEXTO
{files_block}

## FORMATO DE RESPOSTA
Responda de forma objetiva e compacta.
Ao final, inclua obrigatoriamente o bloco:

<brief>
TAREFA: [resumo da tarefa executada]
ARQUIVOS LIDOS: [quantidade e lista resumida]
RESUMO: [3-5 linhas do que foi produzido]
PRÓXIMO PASSO PARA O CLAUDE: [o que ele deve fazer com esse output]
</brief>
"""


def estimate_tokens(text: str) -> int:
    """Estimativa grosseira: ~4 chars por token."""
    return len(text) // 4


def call_gemini(prompt: str, model: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[ERRO] GEMINI_API_KEY não encontrada no .env", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text


def save_output(content: str, output_dir: str, task: str) -> Path:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = task[:40].lower().replace(" ", "-").replace("/", "-")
    slug = "".join(c for c in slug if c.isalnum() or c == "-")
    filename = f"{date_str}_{slug}.md"
    filepath = out_path / filename

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Chama Gemini API com arquivos de contexto")
    parser.add_argument("--task", required=True, help="O que o Gemini deve fazer")
    parser.add_argument("--files", nargs="*", default=[], help="Arquivos ou pastas a incluir")
    parser.add_argument("--output-dir", default="gemini/briefs/", help="Pasta de destino do resultado")
    parser.add_argument("--model", default="gemini-2.5-flash", choices=["gemini-2.5-flash", "gemini-2.5-flash-lite"],
                        help="Modelo a usar (flash=qualidade, flash-lite=volume)")
    args = parser.parse_args()

    # Coleta arquivos
    files = collect_files(args.files) if args.files else {}
    print(f"[INFO] {len(files)} arquivo(s) carregado(s)", file=sys.stderr)

    # Monta prompt
    prompt = build_prompt(args.task, files)

    # Verifica tamanho estimado
    tokens_estimados = estimate_tokens(prompt)
    print(f"[INFO] Tokens estimados no input: ~{tokens_estimados:,}", file=sys.stderr)
    if tokens_estimados > TOKEN_LIMIT_WARNING:
        print(f"[AVISO] Input grande (~{tokens_estimados:,} tokens). Considere reduzir arquivos.", file=sys.stderr)

    # Chama Gemini
    print(f"[INFO] Chamando {args.model}...", file=sys.stderr)
    resultado = call_gemini(prompt, args.model)

    # Salva resultado
    filepath = save_output(resultado, args.output_dir, args.task)
    print(f"[OK] Resultado salvo em: {filepath}", file=sys.stderr)

    # Imprime resultado pra Claude ler (UTF-8 safe)
    sys.stdout.buffer.write((resultado + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
