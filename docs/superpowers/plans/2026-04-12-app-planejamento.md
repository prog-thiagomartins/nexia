# App de Planejamento — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir um app web local (FastAPI) com sidebar de produções, dashboard e abas por produção — rodando na máquina da Mayara com ícone na área de trabalho.

**Architecture:** FastAPI serve HTML via Jinja2. Dados ficam em arquivos .md (leitura) e .json (escrita). Sem banco de dados. A aba IDEIAS é a única editável pela Mayara — as demais são editadas pelo Claude via filesystem.

**Tech Stack:** Python 3.10+, FastAPI, Uvicorn, Jinja2, python-markdown, Windows .bat + .vbs para launcher

---

## Estrutura de arquivos

```
planejamento-app/
├── main.py                      # FastAPI app + todas as rotas
├── data.py                      # Funções de leitura/escrita de arquivos
├── requirements.txt
├── iniciar.bat                  # Launcher Windows
├── iniciar.vbs                  # Wrapper sem janela de terminal
├── templates/
│   ├── base.html                # Layout: sidebar + slot de conteúdo
│   ├── dashboard.html           # Página home
│   └── producao.html            # Página de produção (5 abas)
└── static/
    └── style.css                # Todos os estilos

docs/Planejamento/
├── sprint.md                    # Sprint atual (já existe)
├── roadmap.md                   # Plano geral (já existe)
├── producoes.json               # Lista de produções + metadados (novo)
└── producoes/
    ├── landing-page/
    │   ├── visao-geral.md
    │   ├── andamento.md
    │   ├── futuro.md
    │   ├── insights.md
    │   └── ideias.json
    ├── carrosseis/
    │   └── (mesma estrutura)
    ├── reels/
    │   └── (mesma estrutura)
    └── stories/
        └── (mesma estrutura)
```

---

## Task 1: Setup do projeto

**Files:**
- Create: `planejamento-app/requirements.txt`
- Create: `planejamento-app/main.py`

- [ ] **Step 1: Criar pasta do app**

```bash
mkdir -p planejamento-app/templates planejamento-app/static
```

- [ ] **Step 2: Criar requirements.txt**

```
fastapi==0.111.0
uvicorn==0.29.0
jinja2==3.1.4
markdown==3.6
python-multipart==0.0.9
```

- [ ] **Step 3: Instalar dependências**

```bash
cd planejamento-app && pip install -r requirements.txt
```

Expected: todas instaladas sem erro.

- [ ] **Step 4: Criar main.py com health check**

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/health")
def health():
    return {"status": "ok"}
```

- [ ] **Step 5: Testar que o servidor sobe**

```bash
cd planejamento-app && uvicorn main:app --port 8765 --reload
```

Abrir `http://localhost:8765/health` — esperado: `{"status": "ok"}`

- [ ] **Step 6: Commit**

```bash
git add planejamento-app/
git commit -m "feat: setup inicial do app de planejamento"
```

---

## Task 2: Camada de dados (data.py)

**Files:**
- Create: `planejamento-app/data.py`
- Create: `docs/Planejamento/producoes.json`
- Create: `docs/Planejamento/producoes/landing-page/ideias.json` (e demais produções)

- [ ] **Step 1: Criar producoes.json**

```json
[
  {
    "id": "landing-page",
    "nome": "Landing Page",
    "descricao": "Programa Essência — quiz, copy, prova social",
    "progresso": 70,
    "status": "em andamento"
  },
  {
    "id": "carrosseis",
    "nome": "Carrosséis",
    "descricao": "5 dias × 2 carrosséis — campanha Essência",
    "progresso": 20,
    "status": "em andamento"
  },
  {
    "id": "reels",
    "nome": "Reels",
    "descricao": "8 roteiros — 5 gestacional + 3 emagrecimento",
    "progresso": 0,
    "status": "não iniciado"
  },
  {
    "id": "stories",
    "nome": "Stories",
    "descricao": "Rotina semanal de stories para campanha",
    "progresso": 0,
    "status": "não iniciado"
  }
]
```

Salvar em: `docs/Planejamento/producoes.json`

- [ ] **Step 2: Criar estrutura de pastas e ideias.json vazios**

```bash
for d in landing-page carrosseis reels stories; do
  mkdir -p "docs/Planejamento/producoes/$d"
  echo "[]" > "docs/Planejamento/producoes/$d/ideias.json"
done
```

- [ ] **Step 3: Criar arquivos .md iniciais para cada produção**

Para cada produção, criar os 4 arquivos .md com conteúdo inicial.

`docs/Planejamento/producoes/landing-page/visao-geral.md`:
```markdown
# Visão Geral — Landing Page

**Campanha:** Essência  
**Progresso:** 70%  
**Status:** Em andamento

## Objetivo
Converter visitantes em agendamentos da sessão diagnóstica (R$97) via quiz de qualificação.

## Funil
Instagram → Landing Page → Quiz → WhatsApp → Sessão Diagnóstica → Programa
```

`docs/Planejamento/producoes/landing-page/andamento.md`:
```markdown
# Em Andamento — Landing Page

## Concluído
- [x] Hero reescrito com fio narrativo (headline → sub → CTA)
- [x] Quiz de 5 perguntas com envio para WhatsApp com perfil
- [x] R$97 visível na página e no resultado do quiz
- [x] Credenciais no hero: CRN 64803 + Nutrição Comportamental
- [x] Seção Mayara na posição correta (depois das Crenças)
- [x] Análise CRO documentada

## Falta
- [ ] Depoimentos com nome mais completo + resultado concreto
- [ ] Mosaico de prova social — substituir por prints legíveis
- [ ] Resultado do quiz personalizado por perfil
- [ ] Deletar arquivos órfãos (css/styles.css, js/animations.js, etc.)
```

`docs/Planejamento/producoes/landing-page/futuro.md`:
```markdown
# Futuro — Landing Page

- Personalizar resultado do quiz por perfil (hoje genérico)
- Adicionar seção explicando funil completo (quiz → sessão → programa)
- Testes A/B no hero após primeira rodada de tráfego
```

`docs/Planejamento/producoes/landing-page/insights.md`:
```markdown
# Insights — Landing Page

## Análise CRO (2026-04-12)

**Maiores pontos de abandono identificados:**
1. Hero sem proposta de valor concreta → resolvido
2. Seção Mayara fora de posição → resolvido
3. Prova social com imagens ilegíveis → pendente
4. Preço oculto criava ansiedade → resolvido (R$97 visível)
5. Resultado do quiz genérico → resolvido na copy, personalização pendente

**Referência competitiva:** Dr. Harley Pandolfi (Balão Deglutível)  
O que ele faz bem: credenciais no hero, headline direta, CTA com o que a pessoa recebe.  
Adaptado para Mayara: credenciais adicionadas ao hero.
```

Repetir arquivos similares (mais simples) para carrosseis, reels e stories.

`docs/Planejamento/producoes/carrosseis/andamento.md`:
```markdown
# Em Andamento — Carrosséis

## Concluído
- [x] Dia 1 — C1: "Você não é o problema" (manhã)
- [x] Dia 1 — C2: Apresentação do Essência (tarde)
- [x] Visualizador HTML dos dois carrosséis

## Falta
- [ ] Corrigir CTA do C2: "Me chama no DM" → "Link na bio"
- [ ] Dias 2–5 (8 carrosséis restantes)
```

`docs/Planejamento/producoes/carrosseis/visao-geral.md`:
```markdown
# Visão Geral — Carrosséis

**Campanha:** Essência  
**Progresso:** 20%  
**Formato:** 5 dias × 2 carrosséis (manhã + tarde/noite)

## Objetivo
Aquecer a audiência durante os 5 dias de campanha e direcionar para a landing page.
```

`docs/Planejamento/producoes/carrosseis/futuro.md`:
```markdown
# Futuro — Carrosséis

- Carrosséis para campanha de Diabetes Gestacional (Sprint 4+)
- Templates reutilizáveis para campanhas futuras
```

`docs/Planejamento/producoes/carrosseis/insights.md`:
```markdown
# Insights — Carrosséis

- C1 performou bem em teste interno — tom anti-culpa ressoa com o público
- C2 precisa ter CTA atualizado antes de publicar
```

`docs/Planejamento/producoes/reels/visao-geral.md`:
```markdown
# Visão Geral — Reels

**Campanha:** Essência  
**Progresso:** 0%  
**Meta:** 8 roteiros prontos para gravar
```

`docs/Planejamento/producoes/reels/andamento.md`:
```markdown
# Em Andamento — Reels

## Falta
- [ ] 5 roteiros — Diabetes Gestacional
- [ ] 3 roteiros — Emagrecimento Comportamental Feminino
- [ ] Gravar e editar no CapCut
```

`docs/Planejamento/producoes/reels/futuro.md`:
```markdown
# Futuro — Reels

- Reels educativos sobre DG para topo de funil
- Série "mitos da alimentação na gestação"
```

`docs/Planejamento/producoes/reels/insights.md`:
```markdown
# Insights — Reels

- Nicho gestacional tem baixa concorrência em vídeo curto
- Hooks sobre "o que comer com diabetes gestacional" têm alta busca orgânica
```

`docs/Planejamento/producoes/stories/visao-geral.md`:
```markdown
# Visão Geral — Stories

**Campanha:** Essência  
**Progresso:** 0%  
**Meta:** Rotina semanal documentada e pronta para executar
```

`docs/Planejamento/producoes/stories/andamento.md`:
```markdown
# Em Andamento — Stories

## Falta
- [ ] Definir o que postar cada dia da semana
- [ ] Documentar formato e frequência
- [ ] Criar templates base
```

`docs/Planejamento/producoes/stories/futuro.md`:
```markdown
# Futuro — Stories

- Automação de lembretes de stories
- Enquetes e caixinhas de perguntas para geração de conteúdo
```

`docs/Planejamento/producoes/stories/insights.md`:
```markdown
# Insights — Stories

- Stories diários aumentam alcance orgânico dos reels
- Caixinha de perguntas sobre DG gera material para novos reels
```

- [ ] **Step 4: Criar data.py**

```python
import json
import markdown
import uuid
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent  # raiz do workspace
PLAN_DIR = BASE_DIR / "docs" / "Planejamento"
PROD_DIR = PLAN_DIR / "producoes"

ABAS = ["visao-geral", "andamento", "futuro", "insights"]
ABAS_NOMES = {
    "visao-geral": "VISÃO GERAL",
    "andamento":   "EM ANDAMENTO",
    "ideias":      "IDEIAS",
    "futuro":      "FUTURO",
    "insights":    "INSIGHTS",
}


def ler_producoes() -> list[dict]:
    path = PLAN_DIR / "producoes.json"
    return json.loads(path.read_text(encoding="utf-8"))


def ler_producao(prod_id: str) -> dict | None:
    producoes = ler_producoes()
    return next((p for p in producoes if p["id"] == prod_id), None)


def ler_md(prod_id: str, aba: str) -> str:
    """Lê um arquivo .md e retorna HTML renderizado."""
    path = PROD_DIR / prod_id / f"{aba}.md"
    if not path.exists():
        return "<p><em>Conteúdo ainda não disponível.</em></p>"
    texto = path.read_text(encoding="utf-8")
    return markdown.markdown(texto, extensions=["tables", "fenced_code"])


def ler_ideias(prod_id: str) -> list[dict]:
    path = PROD_DIR / prod_id / "ideias.json"
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def salvar_ideias(prod_id: str, ideias: list[dict]) -> None:
    path = PROD_DIR / prod_id / "ideias.json"
    path.write_text(json.dumps(ideias, ensure_ascii=False, indent=2), encoding="utf-8")


def criar_ideia(prod_id: str, texto: str) -> dict:
    ideias = ler_ideias(prod_id)
    nova = {
        "id": str(uuid.uuid4()),
        "texto": texto,
        "criado_em": datetime.now().strftime("%d/%m · %H:%M"),
    }
    ideias.append(nova)
    salvar_ideias(prod_id, ideias)
    return nova


def editar_ideia(prod_id: str, ideia_id: str, texto: str) -> bool:
    ideias = ler_ideias(prod_id)
    for i in ideias:
        if i["id"] == ideia_id:
            i["texto"] = texto
            salvar_ideias(prod_id, ideias)
            return True
    return False


def apagar_ideia(prod_id: str, ideia_id: str) -> bool:
    ideias = ler_ideias(prod_id)
    novas = [i for i in ideias if i["id"] != ideia_id]
    if len(novas) == len(ideias):
        return False
    salvar_ideias(prod_id, novas)
    return True


def ler_sprint_html() -> str:
    path = PLAN_DIR / "sprint.md"
    if not path.exists():
        return ""
    texto = path.read_text(encoding="utf-8")
    return markdown.markdown(texto, extensions=["tables"])
```

- [ ] **Step 5: Testar data.py no Python**

```bash
cd planejamento-app
python -c "import data; print(data.ler_producoes())"
```

Expected: lista com 4 produções.

- [ ] **Step 6: Commit**

```bash
git add docs/Planejamento/ planejamento-app/data.py
git commit -m "feat: camada de dados e arquivos iniciais de planejamento"
```

---

## Task 3: Templates base e CSS

**Files:**
- Create: `planejamento-app/templates/base.html`
- Create: `planejamento-app/static/style.css`

- [ ] **Step 1: Criar style.css**

```css
/* ── Reset ── */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; }
body {
  font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif;
  background: #f4f1ed;
  display: flex;
  color: #1c1c1c;
}

/* ── Sidebar ── */
.sidebar {
  width: 210px; flex-shrink: 0;
  background: #1e3532;
  display: flex; flex-direction: column;
  height: 100vh; position: sticky; top: 0;
}
.sidebar-logo { padding: 18px 16px 14px; border-bottom: 1px solid rgba(255,255,255,.07); }
.sidebar-logo-title { color: white; font-weight: 800; font-size: 12px; letter-spacing: .06em; }
.sidebar-logo-sub { color: rgba(255,255,255,.35); font-size: 10px; margin-top: 2px; }

.sidebar-section {
  padding: 14px 12px 5px;
  font-size: 9px; font-weight: 800; text-transform: uppercase;
  letter-spacing: .12em; color: rgba(255,255,255,.25);
}
.sidebar-item {
  margin: 2px 8px; padding: 8px 10px; border-radius: 8px;
  font-size: 12px; color: rgba(255,255,255,.55); cursor: pointer;
  display: flex; align-items: center; gap: 8px;
  text-decoration: none; transition: all .15s;
}
.sidebar-item:hover { background: rgba(255,255,255,.07); color: rgba(255,255,255,.8); }
.sidebar-item.active { background: rgba(255,255,255,.12); color: white; font-weight: 600; }
.sidebar-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }

.sidebar-add {
  margin: 8px 8px 0; padding: 8px 10px; border-radius: 8px;
  font-size: 11px; color: rgba(255,255,255,.3); cursor: pointer;
  display: flex; align-items: center; gap: 8px;
  border: 1px dashed rgba(255,255,255,.12); transition: all .15s;
  text-decoration: none;
}
.sidebar-add:hover { border-color: rgba(255,255,255,.25); color: rgba(255,255,255,.5); }
.sidebar-bottom {
  margin-top: auto; padding: 12px 8px;
  border-top: 1px solid rgba(255,255,255,.07);
}

/* ── Main ── */
.main { flex: 1; min-height: 100vh; display: flex; flex-direction: column; overflow: hidden; }

/* ── Tabs ── */
.tabs {
  background: white; border-bottom: 1px solid #e8e2da;
  padding: 0 24px; display: flex; flex-shrink: 0;
}
.tab {
  padding: 12px 16px; font-size: 11px; font-weight: 600;
  color: #aaa; white-space: nowrap; cursor: pointer;
  letter-spacing: .05em; text-decoration: none; transition: color .15s;
}
.tab:hover { color: #666; }
.tab.active {
  font-weight: 800; color: #2d4a47;
  border-bottom: 3px solid #2d4a47; margin-bottom: -1px;
}

/* ── Content ── */
.content { flex: 1; overflow-y: auto; padding: 28px 24px; }

/* ── Dashboard ── */
.dash-header { margin-bottom: 20px; }
.dash-title { font-size: 22px; font-weight: 800; }
.dash-sub { font-size: 13px; color: #aaa; margin-top: 3px; }

.sprint-banner {
  background: white; border-radius: 12px; padding: 16px 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,.06); margin-bottom: 20px;
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
  flex-wrap: wrap;
}
.sprint-info strong { font-size: 14px; color: #1c1c1c; display: block; }
.sprint-info span { font-size: 12px; color: #aaa; }
.sprint-pills { display: flex; gap: 6px; flex-wrap: wrap; }
.pill { padding: 4px 11px; border-radius: 20px; font-size: 10px; font-weight: 700; }
.pill-done { background: #e8f0ec; color: #2d4a47; }
.pill-now  { background: #2d4a47; color: white; }
.pill-next { background: #f0ece6; color: #bbb; }

.section-label {
  font-size: 10px; font-weight: 800; text-transform: uppercase;
  letter-spacing: .1em; color: #bbb; margin-bottom: 14px;
}
.prod-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }

.prod-card {
  background: white; border-radius: 12px; padding: 18px 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,.06); cursor: pointer;
  border-left: 4px solid #e8e2da; text-decoration: none; color: inherit;
  transition: box-shadow .15s, transform .1s; display: block;
}
.prod-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,.1); transform: translateY(-1px); }
.prod-card.ativo  { border-left-color: #c17f5b; }
.prod-card.parado { border-left-color: #ddd; }

.prod-card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.prod-card-name { font-size: 13px; font-weight: 800; }
.badge { font-size: 9px; font-weight: 700; padding: 3px 8px; border-radius: 20px; text-transform: uppercase; letter-spacing: .04em; }
.badge-ativo  { background: #fdf0e6; color: #c17f5b; }
.badge-parado { background: #f4f1ed; color: #bbb; }

.prod-card-desc { font-size: 12px; color: #999; margin-bottom: 12px; line-height: 1.4; }
.prog-bar { height: 5px; background: #eee; border-radius: 3px; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 3px; background: #c17f5b; }
.prod-card-pct { font-size: 10px; color: #bbb; margin-top: 4px; }

/* ── Produção — conteúdo renderizado ── */
.md-content { background: white; border-radius: 12px; padding: 24px 28px; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.md-content h1 { font-size: 20px; font-weight: 800; margin-bottom: 16px; color: #1c1c1c; }
.md-content h2 { font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; color: #aaa; margin: 20px 0 10px; padding-bottom: 6px; border-bottom: 1px solid #f0ece6; }
.md-content h3 { font-size: 14px; font-weight: 700; margin: 16px 0 8px; }
.md-content p { font-size: 14px; line-height: 1.75; color: #333; margin-bottom: 12px; }
.md-content ul, .md-content ol { padding-left: 20px; margin-bottom: 12px; }
.md-content li { font-size: 14px; line-height: 1.8; color: #333; }
.md-content li input[type=checkbox] { margin-right: 6px; }
.md-content strong { font-weight: 700; color: #1c1c1c; }
.md-content em { color: #888; }
.md-content table { width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 13px; }
.md-content th { background: #f4f1ed; padding: 8px 12px; text-align: left; font-weight: 700; }
.md-content td { padding: 8px 12px; border-bottom: 1px solid #f0ece6; }

/* ── IDEIAS ── */
.ideias-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.ideias-title { font-size: 15px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }

.btn-icon {
  background: #c17f5b; border: none; color: white;
  border-radius: 8px; padding: 8px 10px; cursor: pointer;
  line-height: 0; transition: background .15s; position: relative;
}
.btn-icon:hover { background: #a86a4a; }
.btn-icon[data-tip]::after {
  content: attr(data-tip); position: absolute; bottom: calc(100% + 6px);
  left: 50%; transform: translateX(-50%); background: #1c1c1c; color: white;
  font-size: 10px; font-weight: 600; padding: 4px 8px; border-radius: 5px;
  white-space: nowrap; pointer-events: none; opacity: 0; transition: opacity .15s;
}
.btn-icon[data-tip]:hover::after { opacity: 1; }

.blocos { display: flex; flex-direction: column; gap: 10px; }
.bloco {
  background: white; border-radius: 12px; padding: 16px 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,.06); display: flex; align-items: flex-start;
  gap: 12px; transition: box-shadow .15s;
}
.bloco:hover { box-shadow: 0 3px 12px rgba(0,0,0,.09); }
.bloco-dot { width: 8px; height: 8px; border-radius: 50%; background: #c17f5b; flex-shrink: 0; margin-top: 5px; }
.bloco-corpo { flex: 1; }
.bloco-data { font-size: 10px; color: #ccc; margin-bottom: 6px; }
.bloco-texto { font-size: 14px; color: #333; line-height: 1.75; }
.bloco-acoes { display: flex; flex-direction: column; gap: 2px; opacity: 0; transition: opacity .15s; }
.bloco:hover .bloco-acoes { opacity: 1; }
.btn-acao {
  background: none; border: none; cursor: pointer; padding: 6px;
  color: #ddd; border-radius: 6px; transition: all .15s; line-height: 0;
  position: relative;
}
.btn-acao:hover { background: #f0ece6; color: #c17f5b; }
.btn-acao[data-tip]::after {
  content: attr(data-tip); position: absolute; right: calc(100% + 6px); top: 50%;
  transform: translateY(-50%); background: #1c1c1c; color: white;
  font-size: 10px; font-weight: 600; padding: 4px 8px; border-radius: 5px;
  white-space: nowrap; pointer-events: none; opacity: 0; transition: opacity .15s;
}
.btn-acao[data-tip]:hover::after { opacity: 1; }

/* ── Modal ── */
.overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,.45); z-index: 100;
  align-items: center; justify-content: center;
}
.overlay.open { display: flex; }
.modal {
  background: white; border-radius: 16px; padding: 28px;
  width: 100%; max-width: 480px; box-shadow: 0 16px 56px rgba(0,0,0,.2);
}
.modal-title { font-size: 13px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; margin-bottom: 16px; }
.modal textarea {
  width: 100%; border: 1.5px solid #e8e2da; border-radius: 10px;
  padding: 14px 16px; font-size: 14px; line-height: 1.75; color: #333;
  resize: none; height: 160px; font-family: inherit; outline: none;
}
.modal textarea:focus { border-color: #c17f5b; }
.modal-footer { display: flex; justify-content: flex-end; gap: 10px; margin-top: 16px; }
.btn-cancel {
  background: transparent; border: 1.5px solid #e8e2da; border-radius: 8px;
  padding: 9px 18px; font-size: 11px; font-weight: 700; letter-spacing: .06em;
  text-transform: uppercase; color: #aaa; cursor: pointer;
}
.btn-save {
  background: #c17f5b; border: none; border-radius: 8px; padding: 9px 20px;
  font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
  color: white; cursor: pointer;
}
.btn-save:hover { background: #a86a4a; }
.btn-danger { background: #e05c5c; }
.btn-danger:hover { background: #c04040; }

@media (max-width: 700px) {
  .sidebar { display: none; }
  .prod-grid { grid-template-columns: 1fr; }
}
```

- [ ] **Step 2: Criar base.html**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Planejamento — Mayara Farias</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>

  <!-- Sidebar -->
  <div class="sidebar">
    <div class="sidebar-logo">
      <div class="sidebar-logo-title">🌿 Planejamento</div>
      <div class="sidebar-logo-sub">Mayara Farias</div>
    </div>

    <div class="sidebar-section">Geral</div>
    <a href="/" class="sidebar-item {% if pagina == 'dashboard' %}active{% endif %}">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/>
        <rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>
      </svg>
      Dashboard
    </a>

    <div class="sidebar-section">Produções</div>
    {% for p in producoes %}
    <a href="/producao/{{ p.id }}" class="sidebar-item {% if prod_id == p.id %}active{% endif %}">
      <div class="sidebar-dot" style="background: {{ '#c17f5b' if p.status == 'em andamento' else '#666' }};"></div>
      {{ p.nome }}
    </a>
    {% endfor %}

    <a href="/producao/nova" class="sidebar-add">
      <span style="font-size:14px;">+</span> Nova produção
    </a>
  </div>

  <!-- Main -->
  <div class="main">
    {% block content %}{% endblock %}
  </div>

  {% block scripts %}{% endblock %}
</body>
</html>
```

- [ ] **Step 3: Commit**

```bash
git add planejamento-app/templates/base.html planejamento-app/static/style.css
git commit -m "feat: template base e CSS completo"
```

---

## Task 4: Dashboard

**Files:**
- Create: `planejamento-app/templates/dashboard.html`
- Modify: `planejamento-app/main.py`

- [ ] **Step 1: Criar dashboard.html**

```html
{% extends "base.html" %}
{% block content %}
<div class="content">

  <div class="dash-header">
    <div class="dash-title">Olá, Mayara 👋</div>
    <div class="dash-sub">Aqui está o resumo do seu projeto hoje.</div>
  </div>

  <div class="sprint-banner">
    <div class="sprint-info">
      <strong>Sprint 2 — Produção de Conteúdo</strong>
      <span>42% concluído · Prazo: 24 de abril</span>
    </div>
    <div class="sprint-pills">
      <div class="pill pill-done">Sprint 1 ✓</div>
      <div class="pill pill-now">Sprint 2</div>
      <div class="pill pill-next">Sprint 3</div>
      <div class="pill pill-next">Sprint 4</div>
      <div class="pill pill-next">Sprint 5</div>
    </div>
  </div>

  <div class="section-label">Produções em andamento</div>
  <div class="prod-grid">
    {% for p in producoes %}
    <a href="/producao/{{ p.id }}" class="prod-card {{ 'ativo' if p.status == 'em andamento' else 'parado' }}">
      <div class="prod-card-header">
        <div class="prod-card-name">{{ p.nome }}</div>
        <div class="badge {{ 'badge-ativo' if p.status == 'em andamento' else 'badge-parado' }}">
          {{ p.status }}
        </div>
      </div>
      <div class="prod-card-desc">{{ p.descricao }}</div>
      <div class="prog-bar">
        <div class="prog-fill" style="width: {{ p.progresso }}%;"></div>
      </div>
      <div class="prod-card-pct">{{ p.progresso }}%</div>
    </a>
    {% endfor %}
  </div>

</div>
{% endblock %}
```

- [ ] **Step 2: Adicionar rota dashboard no main.py**

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import data

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    producoes = data.ler_producoes()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "producoes": producoes,
        "pagina": "dashboard",
        "prod_id": None,
    })
```

- [ ] **Step 3: Testar dashboard**

```bash
cd planejamento-app && uvicorn main:app --port 8765 --reload
```

Abrir `http://localhost:8765` — esperado: dashboard com 4 cards de produção.

- [ ] **Step 4: Commit**

```bash
git add planejamento-app/templates/dashboard.html planejamento-app/main.py
git commit -m "feat: dashboard com sprint e cards de produções"
```

---

## Task 5: Produção — abas de leitura

**Files:**
- Create: `planejamento-app/templates/producao.html`
- Modify: `planejamento-app/main.py`

- [ ] **Step 1: Criar producao.html (abas leitura)**

```html
{% extends "base.html" %}
{% block content %}

<!-- Tabs -->
<div class="tabs">
  {% for aba_id, aba_nome in abas %}
  <a href="/producao/{{ producao.id }}/{{ aba_id }}"
     class="tab {% if aba_ativa == aba_id %}active{% endif %}">
    {{ aba_nome }}
  </a>
  {% endfor %}
</div>

<!-- Conteúdo -->
<div class="content">

  {% if aba_ativa == "ideias" %}
    {# bloco IDEIAS — será preenchido na Task 6 #}
    <div class="ideias-header">
      <div class="ideias-title">Ideias</div>
      <button class="btn-icon" data-tip="Adicionar ideia" onclick="abrirModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
          <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
        </svg>
      </button>
    </div>
    <div class="blocos" id="blocos">
      {% for ideia in ideias %}
      <div class="bloco" data-id="{{ ideia.id }}">
        <div class="bloco-dot"></div>
        <div class="bloco-corpo">
          <div class="bloco-data">{{ ideia.criado_em }}</div>
          <div class="bloco-texto">{{ ideia.texto }}</div>
        </div>
        <div class="bloco-acoes">
          <button class="btn-acao" data-tip="Editar" onclick="editarModal(this)">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
            </svg>
          </button>
          <button class="btn-acao" data-tip="Apagar" onclick="confirmarApagar(this)">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="3 6 5 6 21 6"/>
              <path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/>
              <path d="M10 11v6"/><path d="M14 11v6"/>
              <path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/>
            </svg>
          </button>
        </div>
      </div>
      {% endfor %}
    </div>

  {% else %}
    <div class="md-content">{{ conteudo_html | safe }}</div>
  {% endif %}

</div>

<!-- Modal criar/editar -->
<div class="overlay" id="overlay-modal">
  <div class="modal">
    <div class="modal-title" id="modal-title">Nova ideia</div>
    <textarea id="modal-texto" placeholder="Escreva sua ideia aqui..."></textarea>
    <div class="modal-footer">
      <button class="btn-cancel" onclick="fecharModal('overlay-modal')">Cancelar</button>
      <button class="btn-save" onclick="salvarIdeia()">Salvar</button>
    </div>
  </div>
</div>

<!-- Modal confirmação apagar -->
<div class="overlay" id="overlay-apagar">
  <div class="modal">
    <div class="modal-title">Apagar ideia?</div>
    <p style="font-size:14px;color:#666;margin-bottom:8px;">Esta ação não pode ser desfeita.</p>
    <div class="modal-footer">
      <button class="btn-cancel" onclick="fecharModal('overlay-apagar')">Cancelar</button>
      <button class="btn-save btn-danger" onclick="executarApagar()">Apagar</button>
    </div>
  </div>
</div>

{% endblock %}

{% block scripts %}
<script>
  const PROD_ID = "{{ producao.id }}";
  let editandoId = null;
  let apagandoEl = null;

  function abrirModal() {
    editandoId = null;
    document.getElementById("modal-title").textContent = "Nova ideia";
    document.getElementById("modal-texto").value = "";
    document.getElementById("overlay-modal").classList.add("open");
    setTimeout(() => document.getElementById("modal-texto").focus(), 100);
  }

  function editarModal(btn) {
    const bloco = btn.closest(".bloco");
    editandoId = bloco.dataset.id;
    document.getElementById("modal-title").textContent = "Editar ideia";
    document.getElementById("modal-texto").value = bloco.querySelector(".bloco-texto").textContent;
    document.getElementById("overlay-modal").classList.add("open");
    setTimeout(() => document.getElementById("modal-texto").focus(), 100);
  }

  function confirmarApagar(btn) {
    apagandoEl = btn.closest(".bloco");
    document.getElementById("overlay-apagar").classList.add("open");
  }

  function fecharModal(id) {
    document.getElementById(id).classList.remove("open");
    editandoId = null; apagandoEl = null;
  }

  async function salvarIdeia() {
    const texto = document.getElementById("modal-texto").value.trim();
    if (!texto) return;

    if (editandoId) {
      const res = await fetch(`/api/ideias/${PROD_ID}/${editandoId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto }),
      });
      if (res.ok) {
        const bloco = document.querySelector(`.bloco[data-id="${editandoId}"]`);
        bloco.querySelector(".bloco-texto").textContent = texto;
      }
    } else {
      const res = await fetch(`/api/ideias/${PROD_ID}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto }),
      });
      if (res.ok) {
        const nova = await res.json();
        adicionarBlocoDOM(nova);
      }
    }
    fecharModal("overlay-modal");
  }

  async function executarApagar() {
    if (!apagandoEl) return;
    const id = apagandoEl.dataset.id;
    const res = await fetch(`/api/ideias/${PROD_ID}/${id}`, { method: "DELETE" });
    if (res.ok) apagandoEl.remove();
    fecharModal("overlay-apagar");
  }

  function adicionarBlocoDOM(ideia) {
    const svg1 = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>`;
    const svg2 = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>`;
    const el = document.createElement("div");
    el.className = "bloco"; el.dataset.id = ideia.id;
    el.innerHTML = `
      <div class="bloco-dot"></div>
      <div class="bloco-corpo">
        <div class="bloco-data">${ideia.criado_em}</div>
        <div class="bloco-texto">${ideia.texto}</div>
      </div>
      <div class="bloco-acoes">
        <button class="btn-acao" data-tip="Editar" onclick="editarModal(this)">${svg1}</button>
        <button class="btn-acao" data-tip="Apagar" onclick="confirmarApagar(this)">${svg2}</button>
      </div>`;
    document.getElementById("blocos").appendChild(el);
  }

  // Fechar modal clicando fora
  document.querySelectorAll(".overlay").forEach(o => {
    o.addEventListener("click", e => { if (e.target === o) o.classList.remove("open"); });
  });
</script>
{% endblock %}
```

- [ ] **Step 2: Adicionar rotas de produção no main.py**

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import data

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ABAS = [
    ("visao-geral", "VISÃO GERAL"),
    ("andamento",   "EM ANDAMENTO"),
    ("ideias",      "IDEIAS"),
    ("futuro",      "FUTURO"),
    ("insights",    "INSIGHTS"),
]


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "producoes": data.ler_producoes(),
        "pagina": "dashboard",
        "prod_id": None,
    })


@app.get("/producao/{prod_id}", response_class=HTMLResponse)
@app.get("/producao/{prod_id}/{aba}", response_class=HTMLResponse)
def producao(request: Request, prod_id: str, aba: str = "visao-geral"):
    prod = data.ler_producao(prod_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Produção não encontrada")

    conteudo_html = ""
    ideias = []
    if aba == "ideias":
        ideias = data.ler_ideias(prod_id)
    else:
        conteudo_html = data.ler_md(prod_id, aba)

    return templates.TemplateResponse("producao.html", {
        "request": request,
        "producoes": data.ler_producoes(),
        "producao": prod,
        "abas": ABAS,
        "aba_ativa": aba,
        "conteudo_html": conteudo_html,
        "ideias": ideias,
        "pagina": "producao",
        "prod_id": prod_id,
    })
```

- [ ] **Step 3: Testar produção**

```bash
uvicorn main:app --port 8765 --reload
```

Abrir `http://localhost:8765/producao/landing-page` — esperado: página com 5 abas e conteúdo do `visao-geral.md` renderizado.

- [ ] **Step 4: Commit**

```bash
git add planejamento-app/templates/producao.html planejamento-app/main.py
git commit -m "feat: página de produção com 5 abas e renderização de markdown"
```

---

## Task 6: API IDEIAS (CRUD)

**Files:**
- Modify: `planejamento-app/main.py`

- [ ] **Step 1: Adicionar endpoints da API no main.py**

Adicionar após as rotas existentes:

```python
class IdeiaCreate(BaseModel):
    texto: str

class IdeiaUpdate(BaseModel):
    texto: str


@app.post("/api/ideias/{prod_id}")
def api_criar_ideia(prod_id: str, body: IdeiaCreate):
    prod = data.ler_producao(prod_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    nova = data.criar_ideia(prod_id, body.texto)
    return nova


@app.put("/api/ideias/{prod_id}/{ideia_id}")
def api_editar_ideia(prod_id: str, ideia_id: str, body: IdeiaUpdate):
    ok = data.editar_ideia(prod_id, ideia_id, body.texto)
    if not ok:
        raise HTTPException(status_code=404, detail="Ideia não encontrada")
    return {"ok": True}


@app.delete("/api/ideias/{prod_id}/{ideia_id}")
def api_apagar_ideia(prod_id: str, ideia_id: str):
    ok = data.apagar_ideia(prod_id, ideia_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Ideia não encontrada")
    return {"ok": True}
```

- [ ] **Step 2: Testar CRUD via terminal**

```bash
# Criar ideia
curl -X POST http://localhost:8765/api/ideias/landing-page \
  -H "Content-Type: application/json" \
  -d '{"texto": "Ideia de teste"}'
```

Expected: `{"id": "...", "texto": "Ideia de teste", "criado_em": "..."}`

```bash
# Verificar que foi salvo
cat "../docs/Planejamento/producoes/landing-page/ideias.json"
```

Expected: JSON com a ideia criada.

- [ ] **Step 3: Testar na interface**

Abrir `http://localhost:8765/producao/landing-page/ideias` — clicar em + Adicionar, escrever algo, salvar. Verificar que aparece na lista.

- [ ] **Step 4: Testar editar e apagar com confirmação**

Passar o mouse sobre um bloco → clicar no lápis → editar → salvar.
Passar o mouse sobre um bloco → clicar na lixeira → confirmar → bloco some.

- [ ] **Step 5: Commit**

```bash
git add planejamento-app/main.py
git commit -m "feat: API CRUD para ideias com confirmação de apagar"
```

---

## Task 7: Launcher Windows

**Files:**
- Create: `planejamento-app/iniciar.bat`
- Create: `planejamento-app/iniciar.vbs`

- [ ] **Step 1: Criar iniciar.bat**

```bat
@echo off
cd /d "%~dp0"
start "" http://localhost:8765
uvicorn main:app --port 8765
```

- [ ] **Step 2: Criar iniciar.vbs** (abre sem janela de terminal)

```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & WScript.ScriptFullName & chr(34), 0
Set oShell = CreateObject("Shell.Application")
WshShell.Run "cmd /c cd /d """ & Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\")) & """ && start """" http://localhost:8765 && uvicorn main:app --port 8765", 0, False
```

- [ ] **Step 3: Criar atalho na área de trabalho**

Executar no PowerShell (uma única vez):

```powershell
$ws = New-Object -ComObject WScript.Shell
$atalho = $ws.CreateShortcut("$env:USERPROFILE\Desktop\Planejamento.lnk")
$atalho.TargetPath = "wscript.exe"
$atalho.Arguments = '"C:\Users\mayar\Desktop\claude-workspace\planejamento-app\iniciar.vbs"'
$atalho.WorkingDirectory = "C:\Users\mayar\Desktop\claude-workspace\planejamento-app"
$atalho.IconLocation = "C:\Windows\System32\shell32.dll,175"
$atalho.Description = "Meu Planejamento — Mayara Farias"
$atalho.Save()
```

- [ ] **Step 4: Testar o launcher**

Dar duplo clique no atalho da área de trabalho.
Expected: navegador abre em `http://localhost:8765` com o dashboard.

- [ ] **Step 5: Commit**

```bash
git add planejamento-app/iniciar.bat planejamento-app/iniciar.vbs
git commit -m "feat: launcher Windows com atalho na área de trabalho"
```

---

## Self-Review

**Spec coverage:**
- ✅ FastAPI + Python
- ✅ Sidebar com produções + dot colorido por status
- ✅ Dashboard com sprint e cards de produções
- ✅ 5 abas por produção (VISÃO GERAL, EM ANDAMENTO, IDEIAS, FUTURO, INSIGHTS)
- ✅ IDEIAS: criar, editar, apagar (com confirmação), sem numeração, dot laranja, modal
- ✅ Demais abas: read-only, renderizam .md
- ✅ Launcher .bat + .vbs + atalho .lnk na área de trabalho
- ✅ Arquivos .md iniciais com conteúdo real da Mayara
- ✅ Port 8765

**Placeholder scan:** nenhum TBD ou "similar ao task N" encontrado.

**Type consistency:** `prod_id` usado consistentemente em data.py e main.py. `ideia.id` é UUID string em todos os lugares.
