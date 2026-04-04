# Workflow: YouTube → Workflow Recommender

## Objetivo

Analisar um vídeo do YouTube e recomendar workflows relevantes com base no conteúdo apresentado.

## Inputs Necessários

- `youtube_url`: URL completa do vídeo (ex: `https://www.youtube.com/watch?v=...`)

## Ferramentas

- `tools/fetch_youtube_info.py`: Extrai título, canal e transcrição do vídeo

## Processo

### Passo 1 — Extrair conteúdo do vídeo

Execute a tool com a URL fornecida:

```bash
python tools/fetch_youtube_info.py <youtube_url>
```

O output será um JSON com:
- `title`: título do vídeo
- `author`: nome do canal
- `transcript`: texto completo das legendas (até 8.000 caracteres)
- `transcript_error`: mensagem de erro se não houver legendas disponíveis

### Passo 2 — Analisar o conteúdo

Com base no JSON retornado, identifique:

1. **Tema central**: O que o vídeo ensina ou apresenta?
2. **Subtemas e técnicas**: Ferramentas, métodos, processos mencionados
3. **Público-alvo**: Para quem é o conteúdo?
4. **Ações práticas**: O que alguém pode fazer depois de assistir?

Se `transcript` estiver vazio (legendas indisponíveis), use título e canal para inferir o conteúdo.

### Passo 3 — Verificar workflows existentes

Leia os arquivos em `workflows/` para verificar se já existe algum workflow relacionado ao tema identificado.

```
ls workflows/
```

Avalie cada workflow existente pelo nome e conteúdo. Marque como:
- **Diretamente relevante**: O workflow trata exatamente do que o vídeo ensina
- **Parcialmente relevante**: O workflow pode ser adaptado ou combinado
- **Não relevante**: Sem conexão

### Passo 4 — Gerar recomendações

Apresente as recomendações neste formato:

---

**Vídeo:** [título] — [canal]

**Tema identificado:** [1-2 frases resumindo o conteúdo]

**Recomendações:**

#### Workflows existentes relevantes
(Se houver)
- `workflows/nome_do_workflow.md` — [por que é relevante para este vídeo]

#### Novos workflows sugeridos
(Workflows que ainda não existem, mas o vídeo justifica criar)

| Workflow sugerido | Por que criar | Prioridade |
|---|---|---|
| `nome_descritivo.md` | [o que o vídeo ensina que justifica isso] | Alta / Média / Baixa |

#### Próximo passo
[Ação clara: ex. "Criar `workflows/nome.md` com base no método X ensinado no vídeo"]

---

### Passo 5 — Criar workflows (se aprovado)

Se o usuário aprovar a criação de um novo workflow, crie o arquivo em `workflows/` seguindo o padrão:

```markdown
# Workflow: [Nome]

## Objetivo
[O que este workflow faz]

## Inputs Necessários
[Lista de inputs]

## Ferramentas
[Scripts em tools/ que serão usados]

## Processo
[Passo a passo]

## Outputs
[O que é gerado]

## Edge Cases
[Situações especiais e como lidar]
```

## Edge Cases

| Situação | Como lidar |
|---|---|
| Vídeo sem legendas | Usar título + canal para inferir tema. Avisar o usuário que a análise é baseada em metadados apenas. |
| Legendas em idioma desconhecido | Reportar o idioma e perguntar se o usuário quer prosseguir assim mesmo. |
| URL inválida | Reportar o erro do script e pedir uma URL válida. |
| Vídeo muito genérico | Pedir ao usuário que descreva o que mais chamou atenção no vídeo para refinar as recomendações. |
| Workflow existente cobre o tema | Indicar o existente e perguntar se quer atualizar ou criar uma variação. |

## Outputs

- Análise de tema e subtemas do vídeo
- Lista de workflows existentes relevantes (se houver)
- Tabela de novos workflows sugeridos
- Arquivos `.md` novos em `workflows/` (apenas se aprovados)
