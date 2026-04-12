# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Quem é a usuária

**Mayara Farias** — nutricionista, dona deste projeto. Não é desenvolvedora. Não digita comandos no terminal. Claude executa tudo que envolve código, scripts e ferramentas. Mayara pede resultados em linguagem natural.

Sempre responda em **português brasileiro**. Tom direto, sem jargão técnico desnecessário.

---

## O que Mayara pode pedir e como Claude responde

### Conteúdo para Instagram
Mayara pode pedir roteiros de reels, carrosséis, legendas, hooks, copies, ideias de campanha.

Antes de gerar qualquer conteúdo, leia:
- `docs/memoria/voz_marca.md` — voz, tom, posicionamento (arquivo autoritativo)
- `docs/memoria/preferencias.md` — o que funciona, o que não funciona, regras de pipeline
- `docs/memoria/palavras_chave_nicho.md` — hashtags e palavras para usar

Nicho principal: **Diabetes Gestacional**. Nicho secundário: **Emagrecimento Comportamental Feminino**.

### Reels a partir de vídeo
Quando Mayara trouxer um vídeo (local ou link do YouTube) e pedir para transformar em reel, siga `workflows/reels_com_ia.md`. Claude monta o config e executa `tools/create_reel.py`. Mayara só abre o resultado no CapCut para aparar e publicar.

### Pesquisa de mercado, tendências, análise
Use o Gemini para tarefas de leitura densa, pesquisa e volume. Execute:
```bash
python tools/call_gemini_api.py \
  --task "descrição do que pesquisar" \
  --files docs/memoria/ \
  --output-dir gemini/research/ \
  --model gemini-2.5-flash
```
Leia o output em `gemini/research/` e use para produzir o entregável final.

### Planejamento (sprint, backlog, roadmap)
Quando Mayara mencionar "planejamento", "sprint", "próximo passo", "o que falta", "backlog" ou "roadmap": leia e siga `workflows/planejamento.md`. Durante planejamento, acesse **só** os arquivos de `docs/Planejamento/`.

### Protótipos e landing pages
Siga `workflows/landing_page_builder.md`. Entregáveis HTML vão em `projects/`.

---

## Como o sistema funciona (para Claude entender)

Este projeto usa o padrão **WAT** — Workflows, Agente, Tools:

- **Workflows** (`workflows/`) — instruções do que fazer e como. Sempre ler o workflow relevante antes de executar.
- **Agente** (Claude) — orquestra, decide, produz os entregáveis finais.
- **Tools** (`tools/`) — scripts Python que fazem o trabalho pesado (chamadas de API, processamento de vídeo, buscas). Claude chama esses scripts; nunca reimplementa o que eles fazem inline.

**Roteamento multi-AI:**
- Pesquisa, leitura de contexto denso, geração em volume → **Gemini** (`tools/call_gemini_api.py`)
- Entregáveis finais, código, orquestração → **Claude**
- Gemini escreve **apenas** em `gemini/`. Claude lê de lá e produz os finais em `projects/`.

**Início de sessão:**
1. Leia `workflows/session_router.md`
2. Verifique `gemini/briefs/` por um brief do dia — se existir, use em vez de reler os arquivos originais
3. Se não houver brief do dia: leia `docs/memoria/`

---

## Onde ficam as coisas

```
docs/memoria/      Contexto ativo — voz de marca, preferências, keywords (ler sempre antes de criar conteúdo)
docs/negocio/      Contexto do negócio — serviços, posicionamento, funis
docs/estudos/      Pesquisas e referências — análises, roteiros de estudo, competitivos
docs/Planejamento/ Sprint, backlog, roadmap — só acessar em sessões de planejamento
projects/          Entregáveis finais (HTML, roteiros aprovados, campanhas)
gemini/            Sandbox do Gemini — só o script call_gemini_api.py escreve aqui
.tmp/              Arquivos temporários de processamento — descartável
tools/             Scripts Python de execução
workflows/         SOPs em markdown — um por capacidade
```

---

## Regras do pipeline de reels

- Sempre adicionar **5s de padding** no início e fim — Mayara apara no CapCut, nunca tentar acertar o corte exato
- Texto sempre no **bottom third** (`y > 1480px`) — nunca cobrir o rosto
- Sem box de fundo no texto — usar outline (`borderw`) + sombra (`shadowcolor`)
- Fontes: **Bebas Neue** (keywords) + **Montserrat** (contexto) — baixadas automaticamente pelo script
- Evitar `:`, `ç`, `ã`, `é` nos textos do ffmpeg — quebra no Windows; usar versão sem acento

---

## Higiene de pastas

- **Nunca** criar pastas com nomes de ferramentas ou plugins (`superpowers/`, `claude/`, `gsd/`, etc.)
- `docs/` tem quatro categorias fixas: `memoria/`, `negocio/`, `estudos/`, `Planejamento/`
- `.tmp/` nunca vai para o git

---

## Fim de sessão

1. Atualizar os arquivos relevantes de `docs/memoria/` com aprendizados, preferências novas ou decisões tomadas
2. Documentar problemas com ferramentas na seção Edge Cases do workflow correspondente
