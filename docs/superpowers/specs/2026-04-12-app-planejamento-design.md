# Spec — App de Planejamento Local

Data: 2026-04-12
Status: aprovado por Mayara

---

## Visão geral

App web local (FastAPI + Python) que centraliza o planejamento do negócio da Mayara. Roda na máquina, abre no navegador, tem ícone na área de trabalho. Claude lê e edita os arquivos por baixo dos panos. Mayara visualiza tudo em linguagem de negócio e edita apenas a aba IDEIAS de cada produção.

---

## Stack técnica

- **Backend:** Python + FastAPI
- **Templates:** Jinja2
- **Markdown:** `python-markdown` (renderiza .md como HTML)
- **Dados IDEIAS:** JSON por produção
- **Inicialização:** `.bat` + `.vbs` (abre sem janela de terminal) + atalho `.lnk` na área de trabalho
- **Porta:** 8765 (fixa, fácil de lembrar)

---

## Estrutura de pastas do app

```
planejamento-app/
├── main.py                  # FastAPI app
├── requirements.txt
├── iniciar.bat              # Inicia o servidor
├── iniciar.vbs              # Wrapper sem janela de terminal
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   └── producao.html
└── static/
    └── style.css
```

---

## Estrutura de dados (arquivos existentes)

```
docs/Planejamento/
├── sprint.md                # Sprint atual (global)
├── roadmap.md               # Plano geral (global)
├── producoes/
│   ├── landing-page/
│   │   ├── visao-geral.md
│   │   ├── andamento.md
│   │   ├── futuro.md
│   │   ├── insights.md
│   │   └── ideias.json
│   ├── carrosseis/
│   │   └── (mesma estrutura)
│   ├── reels/
│   │   └── (mesma estrutura)
│   └── stories/
│       └── (mesma estrutura)
└── producoes.json           # Lista de produções + metadados
```

### Formato `producoes.json`
```json
[
  {
    "id": "landing-page",
    "nome": "Landing Page",
    "descricao": "Programa Essência — quiz, copy, prova social",
    "progresso": 70,
    "status": "em andamento"
  }
]
```

### Formato `ideias.json`
```json
[
  {
    "id": "uuid",
    "texto": "Texto da ideia",
    "criado_em": "2026-04-12T14:32:00"
  }
]
```

---

## Layout do app

### Sidebar (esquerda, fixa, escura)
- Logo + nome "Mayara Farias"
- Link: **Dashboard**
- Seção: **PRODUÇÕES**
  - Item por produção (com dot colorido: laranja = ativo, cinza = parado)
  - Botão: + Nova produção
- Rodapé: Configurações (futuro)

**Cores sidebar:** fundo `#1e3532`, texto `rgba(255,255,255,.55)`, ativo `white`

### Dashboard (home)
- Saudação: "Olá, Mayara 👋"
- Banner da sprint atual (de `sprint.md`): nome, progresso %, dias restantes, pills das 5 sprints
- Grid 2×2 de cards de produções — cada card mostra nome, status, barra de progresso, % e é clicável

### Produção — 5 abas
Cada produção abre com 5 abas na parte superior:

| Aba | Fonte | Editável |
|-----|-------|----------|
| VISÃO GERAL | `visao-geral.md` | Não (Claude edita) |
| EM ANDAMENTO | `andamento.md` | Não (Claude edita) |
| IDEIAS | `ideias.json` | Sim (Mayara) |
| FUTURO | `futuro.md` | Não (Claude edita) |
| INSIGHTS | `insights.md` | Não (Claude edita) |

---

## Aba IDEIAS — comportamento detalhado

- Blocos verticais empilhados, sem numeração
- Cada bloco tem: dot laranja `●`, data/hora automática, texto, ícones de ação (aparecem no hover)
- Ícones: lápis (editar) + lixeira (apagar) — apenas SVG, sem texto, com tooltip
- **+ Adicionar:** botão ícone laranja no header, tooltip "Adicionar ideia"
- **Adicionar/Editar:** abre modal com textarea livre, botões Cancelar / Salvar
- **Apagar:** abre modal de confirmação antes de deletar
- Dados salvos em `ideias.json` via POST para a API

---

## API — endpoints FastAPI

```
GET  /                          → dashboard
GET  /producao/{id}             → produção (aba VISÃO GERAL por padrão)
GET  /producao/{id}/{aba}       → produção com aba ativa

POST /api/ideias/{id}           → criar ideia
PUT  /api/ideias/{id}/{ideia_id}→ editar ideia
DEL  /api/ideias/{id}/{ideia_id}→ apagar ideia

GET  /api/producoes             → lista produções (para sidebar)
POST /api/producoes             → nova produção
```

---

## Atalho na área de trabalho (Windows)

1. `iniciar.bat` — inicia `uvicorn main:app --port 8765` e abre `http://localhost:8765` no navegador
2. `iniciar.vbs` — executa o `.bat` sem abrir janela de terminal
3. Atalho `.lnk` na área de trabalho apontando para `iniciar.vbs`
4. Ícone: arquivo `.ico` com folha verde (gerado ou baixado)

---

## Fora do escopo (v1)

- Autenticação
- Múltiplos usuários
- Sincronização em nuvem
- Edição das abas que não são IDEIAS (Claude faz isso via filesystem)
- Mobile

---

## Critério de pronto

- App abre clicando no ícone da área de trabalho
- Dashboard mostra sprint e produções corretamente
- Cada produção abre com as 5 abas
- Aba IDEIAS: criar, editar, apagar funcionando
- Demais abas renderizam o conteúdo dos .md formatado
- Arquivos .md existentes em `docs/Planejamento/` são migrados para a nova estrutura de pastas
