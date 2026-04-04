"""
fix_hardcodes.py — Remove hardcodes bloqueantes para multi-tenant/multi-domain.
Foco: nomes de cliente, paths com slug fixo, região/nicho fixo em workflows.
Execução: python tools/fix_hardcodes.py [--dry-run]
"""
import re, sys
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv
ROOT = Path(__file__).parent.parent

changes = []

def replace_file(path, replacements):
    """Aplica lista de (pattern, replacement) em um arquivo."""
    p = ROOT / path
    if not p.exists():
        print(f"  SKIP (não encontrado): {path}")
        return
    original = p.read_text(encoding="utf-8")
    result = original
    for pattern, repl, desc in replacements:
        new = re.sub(pattern, repl, result)
        if new != result:
            changes.append(f"  [{path}] {desc}")
        result = new
    if result != original:
        if not DRY_RUN:
            p.write_text(result, encoding="utf-8")
        print(f"  CHANGED: {path}")
    else:
        print(f"  OK (sem mudança): {path}")

# ── 1. session_router.md — paths com slug fixo da Mayara ──────────────────
replace_file("workflows/session_router.md", [
    (r"clients/mayara/client\.json",        "clients/<active_client>/client.json",      "path client.json"),
    (r"clients/mayara/context/memoria/",    "clients/<active_client>/context/memoria/", "path memoria"),
    (r"clients/mayara/context/",            "clients/<active_client>/context/",         "path context"),
    (r"clients/mayara/projects/",           "clients/<active_client>/projects/",        "path projects"),
    (r"clients/mayara/",                    "clients/<active_client>/",                 "path client root"),
    (r"--model gemini-2\.5-flash-lite",     "--model ${GEMINI_MODEL_LITE:-gemini-2.5-flash-lite}", "model lite"),
    (r"--model gemini-2\.5-flash\b",        "--model ${GEMINI_MODEL:-gemini-2.5-flash}",           "model default"),
])

# ── 2. research_niche.md — nome, nicho e região fixos ─────────────────────
replace_file("workflows/research_niche.md", [
    (r"Mayara Farias \(Nutrition\)",        "[CLIENT_NAME] ([CLIENT_NICHE])",      "título do workflow"),
    (r"\bMayara Farias\b",                  "[CLIENT_NAME]",                       "nome do cliente"),
    (r"\bMayara\b",                         "[CLIENT_NAME]",                       "nome curto do cliente"),
    (r'"nutrition"',                        '"[CLIENT_NICHE]"',                    "nicho hardcoded (aspas)"),
    (r"\bnutrition\b",                      "[CLIENT_NICHE]",                      "nicho hardcoded"),
    (r"\bnutritionist\b",                   "[CLIENT_ROLE]",                       "papel/profissão"),
    (r"--region br-pt",                     "--region ${CLIENT_REGION:-br-pt}",    "região"),
    (r'"br-pt"',                            '"${CLIENT_REGION:-br-pt}"',           "região (aspas)"),
])

# ── 3. call_gemini_api.py — mover model defaults para constantes .env-aware
replace_file("tools/call_gemini_api.py", [
    (r'model gemini-2\.5-flash-lite\b',     'model ${GEMINI_MODEL_LITE:-gemini-2.5-flash-lite}', "model lite em docstring"),
    (r'"gemini-2\.5-flash-lite"',           'os.getenv("GEMINI_MODEL_LITE", "gemini-2.5-flash-lite")', "model lite hardcoded"),
    (r'"gemini-2\.5-flash"',                'os.getenv("GEMINI_MODEL", "gemini-2.5-flash")',            "model hardcoded"),
])

# ── 4. supabase-schema.md — bucket name fixo ──────────────────────────────
replace_file("docs/supabase-schema.md", [
    (r"'wat-studio'",   "'nexia'  -- env: SUPABASE_BUCKET",  "bucket name SQL"),
    (r'"wat-studio"',   '"nexia"  -- env: SUPABASE_BUCKET',  "bucket name SQL (aspas duplas)"),
    (r"wat-studio/",    "nexia/",                            "bucket path"),
    (r"WAT Studio",     "nexia",                             "nome do produto"),
])

# ── 5. start.bat — URL e port fixos ───────────────────────────────────────
replace_file("start.bat", [
    (r"http://127\.0\.0\.1:8000", "http://127.0.0.1:%PORT%", "port hardcoded"),
])

# ── Sumário ────────────────────────────────────────────────────────────────
print(f"\n{'[DRY RUN] ' if DRY_RUN else ''}Trocas realizadas ({len(changes)}):")
for c in changes:
    print(c)

if DRY_RUN:
    print("\nRodar sem --dry-run para aplicar.")
