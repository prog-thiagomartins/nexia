"""
Camada de dados do app de planejamento.
Lê de arquivos .md e .json. Escreve apenas em ideias.json.
Configurações vêm de config.json — zero hardcode.
"""

import json
import uuid
from pathlib import Path
from datetime import datetime
import markdown

# ── Config ────────────────────────────────────────────────────────────────────

APP_DIR = Path(__file__).parent
CONFIG_PATH = APP_DIR / "config.json"


def ler_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def _base_dir() -> Path:
    cfg = ler_config()
    raw = cfg["dados"]["base_dir"]
    return (APP_DIR / raw).resolve()


def _producoes_path() -> Path:
    cfg = ler_config()
    raw = cfg["dados"]["producoes_json"]
    return (APP_DIR / raw).resolve()


def _sprint_path() -> Path:
    cfg = ler_config()
    raw = cfg["dados"]["sprint_md"]
    return (APP_DIR / raw).resolve()


# ── Produções ─────────────────────────────────────────────────────────────────

def ler_producoes() -> list[dict]:
    path = _producoes_path()
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def ler_producao(prod_id: str) -> dict | None:
    prods = ler_producoes()
    return next((p for p in prods if p["id"] == prod_id), None)


def salvar_producoes(producoes: list[dict]) -> None:
    path = _producoes_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(producoes, f, ensure_ascii=False, indent=2)


def criar_producao(id_: str, nome: str, descricao: str = "") -> dict:
    prods = ler_producoes()
    nova = {"id": id_, "nome": nome, "descricao": descricao, "progresso": 0, "status": "não iniciado"}
    prods.append(nova)
    salvar_producoes(prods)
    # Criar pasta e arquivos .md vazios
    pasta = _base_dir() / "producoes" / id_
    pasta.mkdir(parents=True, exist_ok=True)
    for aba in ["visao-geral", "andamento", "concluido", "futuro", "insights"]:
        md_path = pasta / f"{aba}.md"
        if not md_path.exists():
            md_path.write_text(f"# {nome}\n\n", encoding="utf-8")
    anotacoes_path = pasta / "anotacoes.json"
    if not anotacoes_path.exists():
        anotacoes_path.write_text("[]", encoding="utf-8")
    return nova


# ── Markdown ──────────────────────────────────────────────────────────────────

ABA_PARA_ARQUIVO = {
    "visao-geral": "visao-geral.md",
    "andamento": "andamento.md",
    "concluido": "concluido.md",
    "futuro": "futuro.md",
    "insights": "insights.md",
}


def ler_md(prod_id: str, aba: str) -> str:
    """Retorna conteúdo .md renderizado como HTML."""
    nome_arquivo = ABA_PARA_ARQUIVO.get(aba)
    if not nome_arquivo:
        return "<p>Aba não encontrada.</p>"
    path = _base_dir() / "producoes" / prod_id / nome_arquivo
    if not path.exists():
        return "<p><em>Arquivo ainda não criado.</em></p>"
    texto = path.read_text(encoding="utf-8")
    return markdown.markdown(texto, extensions=["tables", "fenced_code"])


def ler_sprint_html() -> str:
    """Retorna sprint.md renderizado como HTML."""
    path = _sprint_path()
    if not path.exists():
        return "<p><em>sprint.md não encontrado.</em></p>"
    texto = path.read_text(encoding="utf-8")
    return markdown.markdown(texto, extensions=["tables", "fenced_code"])


# ── Anotações ─────────────────────────────────────────────────────────────────

def _anotacoes_path(prod_id: str) -> Path:
    return _base_dir() / "producoes" / prod_id / "anotacoes.json"


def ler_anotacoes(prod_id: str) -> list[dict]:
    path = _anotacoes_path(prod_id)
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _salvar_anotacoes(prod_id: str, anotacoes: list[dict]) -> None:
    path = _anotacoes_path(prod_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(anotacoes, f, ensure_ascii=False, indent=2)


def criar_anotacao(prod_id: str, texto: str) -> dict:
    anotacoes = ler_anotacoes(prod_id)
    nova = {
        "id": str(uuid.uuid4()),
        "texto": texto.strip(),
        "criado_em": datetime.now().isoformat(timespec="seconds"),
    }
    anotacoes.insert(0, nova)  # mais recente no topo
    _salvar_anotacoes(prod_id, anotacoes)
    return nova


def editar_anotacao(prod_id: str, anotacao_id: str, texto: str) -> bool:
    anotacoes = ler_anotacoes(prod_id)
    for a in anotacoes:
        if a["id"] == anotacao_id:
            a["texto"] = texto.strip()
            a["editado_em"] = datetime.now().isoformat(timespec="seconds")
            _salvar_anotacoes(prod_id, anotacoes)
            return True
    return False


def apagar_anotacao(prod_id: str, anotacao_id: str) -> bool:
    anotacoes = ler_anotacoes(prod_id)
    antes = len(anotacoes)
    anotacoes = [a for a in anotacoes if a["id"] != anotacao_id]
    if len(anotacoes) < antes:
        _salvar_anotacoes(prod_id, anotacoes)
        return True
    return False
