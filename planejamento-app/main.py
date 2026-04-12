"""
App de Planejamento Local — FastAPI
Porta configurável em config.json. Zero hardcode.
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import data

app = FastAPI(title="App de Planejamento")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def ctx(request: Request, extra: dict = None) -> dict:
    cfg = data.ler_config()
    base = {
        "request": request,
        "config": cfg,
        "producoes": data.ler_producoes(),
    }
    if extra:
        base.update(extra)
    return base


# ── Dashboard ─────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    sprint_html = data.ler_sprint_html()
    return templates.TemplateResponse("dashboard.html", ctx(request, {
        "sprint_html": sprint_html,
        "pagina": "dashboard",
    }))


# ── Produção ──────────────────────────────────────────────────────────────────

ABAS_VALIDAS = ["visao-geral", "andamento", "anotacoes", "futuro", "insights"]


@app.get("/producao/{prod_id}", response_class=HTMLResponse)
def producao_default(request: Request, prod_id: str):
    return producao(request, prod_id, "visao-geral")


@app.get("/producao/{prod_id}/{aba}", response_class=HTMLResponse)
def producao(request: Request, prod_id: str, aba: str):
    prod = data.ler_producao(prod_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    if aba not in ABAS_VALIDAS:
        aba = "visao-geral"

    conteudo_md = None
    anotacoes = None

    if aba == "anotacoes":
        anotacoes = data.ler_anotacoes(prod_id)
    else:
        conteudo_md = data.ler_md(prod_id, aba)

    return templates.TemplateResponse("producao.html", ctx(request, {
        "prod": prod,
        "aba_ativa": aba,
        "abas": ABAS_VALIDAS,
        "conteudo_md": conteudo_md,
        "anotacoes": anotacoes,
        "pagina": "producao",
    }))


# ── API: Produções ────────────────────────────────────────────────────────────

class NovaProducaoBody(BaseModel):
    id: str
    nome: str
    descricao: str = ""


@app.get("/api/producoes")
def listar_producoes():
    return data.ler_producoes()


@app.post("/api/producoes")
def nova_producao(body: NovaProducaoBody):
    return data.criar_producao(body.id, body.nome, body.descricao)


# ── API: Anotações ────────────────────────────────────────────────────────────

class AnotacaoBody(BaseModel):
    texto: str


@app.post("/api/anotacoes/{prod_id}")
def criar_anotacao(prod_id: str, body: AnotacaoBody):
    prod = data.ler_producao(prod_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    return data.criar_anotacao(prod_id, body.texto)


@app.put("/api/anotacoes/{prod_id}/{anotacao_id}")
def editar_anotacao(prod_id: str, anotacao_id: str, body: AnotacaoBody):
    if not data.editar_anotacao(prod_id, anotacao_id, body.texto):
        raise HTTPException(status_code=404, detail="Anotação não encontrada")
    return {"ok": True}


@app.delete("/api/anotacoes/{prod_id}/{anotacao_id}")
def apagar_anotacao(prod_id: str, anotacao_id: str):
    if not data.apagar_anotacao(prod_id, anotacao_id):
        raise HTTPException(status_code=404, detail="Anotação não encontrada")
    return {"ok": True}


# ── Health ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "ok"}
