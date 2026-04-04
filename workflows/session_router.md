# Workflow: Session Router (Master)

## Objetivo

Primeiro workflow a ser lido em qualquer sessão. Define quem executa o quê — Gemini ou Claude — e como despachar cada tipo de tarefa. Cobre roteamento e execução de dispatch.

## Quando Usar

**Sempre.** No início de cada sessão, antes de qualquer execução.

---

## Passo 1 — Carregar contexto do cliente

1. Leia `clients/<active_client>/client.json`
2. Verifique se existe brief recente em `gemini/briefs/` (mesmo dia)
   - **Se existir:** use como contexto — não releia os arquivos originais
   - **Se não existir:** delegue leitura ao Gemini (Passo 3)
3. Leia `clients/<active_client>/context/memoria/` apenas se não houver brief do dia

---

## Passo 2 — Classificar a tarefa

| Tipo de tarefa | Quem executa | Passo |
|---|---|---|
| Leitura/destilação de docs densos | **Gemini** | → Passo 3 |
| Pesquisa (YouTube, Instagram, PubMed, tendências) | **Gemini** | → Passo 3 |
| Geração de volume (10+ variações de copy, hooks) | **Gemini** | → Passo 3 |
| Audit de voz de marca | **Gemini** | → Passo 3 |
| Geração de imagens | **Gemini (imagens)** | → Passo 4 |
| Imagens com fundo removido | **Manus** | → Passo 5 |
| Código, scripts Python, tools, workflows | **Claude** | → Passo 6 |
| Entregável final (roteiro, copy, landing page) | **Claude** | → Passo 6 |
| Orquestração WAT | **Claude** | → Passo 6 |

Tarefas mistas: Gemini/Manus executam primeiro, Claude integra depois.

---

## Passo 3 — Dispatch Gemini (pesquisa, contexto, conteúdo)

```bash
python tools/call_gemini_api.py \
  --task "descrição da tarefa" \
  --files caminho/dos/arquivos/ \
  --output-dir gemini/[briefs|research|drafts|audits]/ \
  --model ${GEMINI_MODEL:-gemini-2.5-flash}
```

Use `gemini-2.5-flash-lite` para volume alto (mais de 10 variações, listas longas).

**Pastas de output:**

| Tipo | Pasta |
|---|---|
| Resumo de contexto | `gemini/briefs/` |
| Pesquisa de mercado/tendências | `gemini/research/` |
| Rascunhos de conteúdo | `gemini/drafts/` |
| Audit de voz | `gemini/audits/` |

Aguarde o output. Gemini salva o arquivo e retorna bloco `<brief>`. Siga para o Passo 6.

---

## Passo 4 — Dispatch Gemini (imagens)

```bash
python tools/generate_images_api.py prompts.json --output images/
```

Aguarde os arquivos de imagem antes de prosseguir. Siga para o Passo 6.

---

## Passo 5 — Dispatch Manus (imagens com fundo removido)

```bash
python tools/generate_images_manus.py prompts.json --output images/ --remove-bg
```

Aguarde os arquivos PNG antes de prosseguir. Siga para o Passo 6.

---

## Passo 6 — Execução Claude

1. Leia o output do passo anterior em `gemini/` ou `images/` (se aplicável)
2. Execute a tarefa com o contexto compacto disponível
3. Salve entregáveis finais em `clients/<active_client>/projects/`
4. Nunca delegue escrita fora de `gemini/` ao Gemini

---

## Regras de Sandbox

- Gemini escreve **apenas** em `gemini/`
- Claude lê de `gemini/` mas nunca delega escrita fora dessa pasta
- Entregáveis finais aprovados: Claude move de `gemini/drafts/` para `clients/<active_client>/projects/`

---

## Edge Cases

| Situação | Como lidar |
|---|---|
| Gemini API indisponível | Claude lê arquivos originais diretamente |
| Brief com mais de 2 dias | Ignorar, solicitar novo brief |
| Tarefa urgente | Pular delegação, Claude executa com contexto disponível |
| AI externa indisponível | Documentar falha, oferecer alternativa manual |
| Output inutilizável | Refinar prompt e redispatchar — máximo 2 tentativas |
| Custo inesperado | Confirmar com usuário antes de qualquer chamada paga |
| Dependência circular entre subtarefas | Reordenar — se impossível, quebrar em fases |

---

## Extensão do Router

Quando uma nova AI for integrada:
1. Criar script em `tools/`
2. Adicionar linha na tabela do Passo 2
3. Criar Passo N com o comando de dispatch
4. Documentar edge cases específicos aqui
