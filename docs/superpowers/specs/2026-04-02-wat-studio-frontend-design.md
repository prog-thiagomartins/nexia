# WAT Studio — Frontend Design Spec
**Data:** 2026-04-02  
**Status:** Aprovado

---

## Objetivo

Construir um frontend web local para que clientes não-técnicos (ex: Mayara Farias, nutricionista) interajam com o framework WAT sem precisar usar o terminal. A interface deve ser:

- Usável sem nenhum conhecimento técnico
- Desktop-first (uso com estagiária)
- Reutilizável como template para qualquer cliente futuro
- Expansível para features futuras sem reescrever a base

---

## Arquitetura

### Stack
- **Backend:** FastAPI (Python) — wrapper fino sobre o Claude Code CLI
- **Frontend:** HTML + CSS + JS puro, sem frameworks
- **IA:** Claude Code CLI (usa conta existente do usuário, sem API key separada)
- **Streaming:** Server-Sent Events (SSE) via `EventSource` nativo do browser

### Fluxo de dados
```
Browser → FastAPI (server.py) → Claude Code CLI → tools/*.py
                ↑                      ↓
           SSE streaming         lê workflows/ e clients/<nome>/context/
```

### Estrutura de diretórios
```
workflows/
  tools/                    ← scripts Python de execução
  workflows/                ← SOPs markdown
  CLAUDE.md                 ← instrução do agente (genérico, sem info de cliente)
  frontend/
    server.py               ← FastAPI, ponto de entrada
    static/
      index.html
      style.css
      app.js
  clients/
    mayara/
      context/
        negocio/
        conteudo/
        memoria/            ← memória persistente entre sessões
      projects/
      .env
      client.json           ← define nome, workflows ativos, configurações
  docs/
```

### client.json (contrato do template)
```json
{
  "name": "Mayara Farias",
  "slug": "mayara",
  "workflows": ["pesquisa", "youtube", "imagem", "landing_page"],
  "context_path": "clients/mayara/context",
  "memory_path":  "clients/mayara/context/memoria"
}
```
Cada cliente novo = nova pasta em `clients/` com esse arquivo. O frontend monta a interface dinamicamente a partir dele.

---

## Endpoints FastAPI

| Método | Endpoint        | Descrição |
|--------|----------------|-----------|
| GET    | `/client`       | Retorna `client.json` — monta sidebar e cards |
| POST   | `/run`          | Dispara workflow ou mensagem de chat; faz streaming via SSE |
| GET    | `/history`      | Últimas execuções salvas em `.tmp/` |
| GET    | `/context`      | Lista arquivos de contexto/memória do cliente |
| POST   | `/memory/save`  | Salva nota na memória persistente do cliente |

---

## Interface (3 zonas fixas)

```
┌─────────────────────────────────────────────┐
│  [WAT Studio]           [Cliente ●] [⚙]     │  Header
├──────────┬──────────────────────┬────────────┤
│ Sidebar  │   Zona Central       │ Job Panel  │
│          │                      │            │
│ Workflows│  Home / Wizard /     │ Progresso  │
│ Recentes │  Chat                │ das tasks  │
│ [Chat]   │                      │            │
└──────────┴──────────────────────┴────────────┘
```

### Sidebar
- Cards de navegação dos workflows (lidos do `client.json`)
- Histórico das últimas execuções
- Botão de Chat livre no final

### Zona Central — 3 modos
1. **Home:** grid de workflow cards com último uso
2. **Workflow Wizard:** 3 passos — Configurar → Confirmar → Resultado
3. **Chat:** conversa livre com o agente

### Job Panel (direita)
- Recolhível
- Mostra steps em linguagem simples + tempo decorrido + progress bar
- Expansível no futuro para múltiplas tasks em paralelo

---

## Sistema de Memória Persistente

Arquivos em `clients/<slug>/context/memoria/` são carregados automaticamente no contexto de cada sessão. O agente "lembra" o que foi salvo.

Exemplos:
- `preferencias.md` — o que ela gosta/não gosta nos resultados
- `historico_temas.md` — temas já pesquisados, evita repetição
- `voz_marca.md` — tom de comunicação, público-alvo
- `notas_sessao.md` — decisões importantes de conversas anteriores

Ao final de sessões produtivas, o agente pode sugerir salvar informações relevantes.

---

## Isolamento de Contexto

Cada cliente tem sua própria pasta isolada. O frontend carrega apenas o contexto do cliente ativo (definido em `client.json`). Clientes nunca veem dados uns dos outros.

Isso também isola: credenciais (`.env`), projetos, memória e workflows ativos de cada cliente.

---

## Estética

- **Paleta:** dark forest green (`#0A1810`) com dourado terroso (`#C9A96E`) e sage green (`#6FA880`)
- **Tipografia:** Cormorant Garamond (display/títulos) + DM Sans (corpo)
- **Tom:** studio editorial premium — não painel técnico, não app de wellness genérico
- **Animações:** fadein nas views, pulse no job panel, transições de wizard

---

## Limitações e Fora de Escopo (v1)

- Sem autenticação (uso local, máquina única)
- Sem deploy em nuvem
- Sem suporte mobile
- Sem múltiplos usuários simultâneos
- SaaS / billing são decisões futuras, não implementadas agora
