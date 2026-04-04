# nexia — Instruções de Desenvolvimento

Você está desenvolvendo o **nexia**: uma plataforma de produção de conteúdo com IA que usa a arquitetura WAT (Workflows, Agents, Tools) como camada de operação interna.

## O que é o nexia

nexia é o produto. WAT é como ele opera por dentro.

- **nexia** → o que o cliente vê e usa
- **WAT** → a arquitetura interna (Workflows + Agents + Tools)
- **Claude Code** → o runtime que executa tudo

O cliente não precisa saber que existe WAT. Assim como usuário de Gmail não precisa saber que existe MVC.

## Modelo multi-AI

O nexia usa dois agentes com papéis distintos:

| Agente | Papel | Quando usar |
|--------|-------|-------------|
| **Claude** | Orquestrador + entregáveis finais | Decisões, código, escrita final, coordenação |
| **Gemini** | Pesquisa + volume + briefs | Leitura de docs densos, 10+ variações de copy, audits de voz, tendências |

**Regra:** Claude nunca lê arquivos de contexto de cliente diretamente — chama `tools/call_gemini_api.py` e lê o `<brief>` resultante. Isso economiza tokens e mantém o contexto limpo.

## Arquitetura WAT

**Workflows** (`workflows/`) — SOPs em Markdown. Definem o quê fazer, quais tools usar, como tratar erros. Não crie nem sobrescreva sem pedir.

**Tools** (`tools/`) — Scripts Python determinísticos. Fazem o trabalho real: chamadas de API, transformações, operações de arquivo. Sempre procure uma tool existente antes de criar nova.

**Agent (você)** — Lê o workflow relevante, executa tools na sequência correta, recupera de erros, melhora o sistema quando algo quebra.

## Estrutura de arquivos

```
tools/                  # Scripts Python — execução determinística
workflows/              # SOPs Markdown — instruções de operação
frontend/               # FastAPI + HTML/JS
  server.py
  static/               # index.html, style.css, app.js
clients/                # Um folder por cliente — contexto isolado
  <slug>/
    context/
      negocio/          # Contexto do negócio
      conteudo/         # Tom e estilo de conteúdo
      pesquisas/        # Pesquisas de mercado
      memoria/          # Memória persistente entre sessões
    projects/           # Entregáveis do cliente
    client.json         # Metadados: nome, slug, workflows ativos
    .env                # API keys do cliente (NUNCA em outro lugar)
docs/                   # Specs e referências (flat — sem subpastas)
gemini/                 # Sandbox do Gemini (só call_gemini_api.py escreve aqui)
  briefs/
  drafts/
  research/
  audits/
.tmp/                   # Arquivos temporários — descartáveis
```

## Regras de folder hygiene

- NUNCA criar pastas com nomes de tools, plugins ou frameworks (`superpowers/`, `gsd/`, `claude/`)
- `docs/` é flat — nada de subpastas por ferramenta
- Infraestrutura de plugins vive em `~/.claude/` — nunca sangra pro projeto
- `.tmp/` é descartável — nada importante vai aqui

## Como desenvolver

**Ao adicionar uma nova tool:**
1. Verifique se já existe algo em `tools/` que resolve
2. Siga o padrão de `call_gemini_api.py`: argparse, dotenv, stderr para logs, stdout para output
3. Docstring no topo com uso, exemplo de comando e o que a tool faz
4. Teste antes de referenciar em qualquer workflow

**Ao adicionar ou atualizar um workflow:**
1. Peça confirmação antes de criar ou sobrescrever
2. Formato: objetivo → inputs → steps → outputs → edge cases
3. Documente rate limits, quirks de API e aprendizados na seção Edge Cases
4. Workflows evoluem com o sistema — mantenha atualizados

**Ao encontrar um erro:**
1. Leia o trace completo
2. Corrija a tool e reteste
3. Se usar API paga: confirme antes de rodar de novo
4. Atualize o workflow com o que aprendeu

## Princípios

- Arquivos locais são para processamento. Entregáveis finais vão para serviços cloud (Google Sheets, Slides, etc.)
- Gemini escreve apenas em `gemini/` — Claude lê de lá mas não delega escrita fora dessa pasta
- Entregáveis aprovados: Claude move de `gemini/drafts/` para `clients/<slug>/projects/`
