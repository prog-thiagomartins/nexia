# Workflow: Image Generation Pipeline

## Objetivo

Gerar imagens (ilustrações, banners, assets) para landing pages e sites usando Nano Banana / Gemini, decidindo automaticamente qual das três rotas usar com base em custo, contexto e qualidade necessária.

## Inputs Necessários

- `image_descriptions`: Lista de imagens a gerar (descrição de cada uma)
- `style`: Estilo visual desejado (ex: ilustração flat, 3D, minimalista, fotorrealista)
- `remove_background`: `true` ou `false` — se as imagens precisam de fundo transparente (PNG)
- `route`: `auto`, `flow`, `api` ou `manus` (ver rotas abaixo)

## As Três Rotas

### Rota 1 — Flow (Gratuito)
**Quando usar:** Projetos próprios, testes, protótipos, quando não há urgência
**Como:** Acesse o Nano Banana Flow, gere manualmente, baixe e salve em `images/`
**Limitação:** Manual, não automatizável via script

### Rota 2 — API Direta (Pago, automatizado)
**Quando usar:** Volume alto de imagens, projeto de cliente, pipeline automatizado
**Como:** Claude Code chama a API do Gemini diretamente para gerar as imagens
**Custo:** Pago por uso de API — sempre confirmar com o usuário antes de disparar

### Rota 3 — Via Manus (Pago, com remoção de fundo incluída)
**Quando usar:** Quando precisar de ilustrações sem fundo (PNG transparente) prontas para uso
**Como:** Claude Code envia tarefas ao Manus, que gera as imagens e já entrega com fundo removido
**Vantagem:** Economiza a etapa de remoção de fundo — o PNG vem pronto

## Ferramentas

- `tools/generate_images_api.py` — Rota 2: chamada à API do Gemini
- `tools/generate_images_manus.py` — Rota 3: integração com Manus

## Processo

### Passo 1 — Decidir a rota

Se `route` for `auto`, use esta lógica de decisão:

```
remove_background = true?
  → Rota 3 (Manus) — entrega PNG transparente pronto

Volume > 5 imagens E projeto de cliente?
  → Rota 2 (API) — automatizado e rastreável

Caso contrário?
  → Rota 1 (Flow) — gratuito, sem setup
```

Confirme com o usuário antes de usar qualquer rota paga (2 ou 3).

### Passo 2 — Preparar os prompts

Para cada imagem em `image_descriptions`, escreva um prompt estruturado:

```
[estilo], [descrição do objeto/cena], [cor predominante], [fundo],
[composição], sem texto, alta qualidade
```

Exemplo:
```
flat illustration, laptop with code on screen, blue and white tones,
white background, centered composition, no text, high quality
```

Salve os prompts em `.tmp/image_prompts_<project_name>.json`.

### Passo 3 — Executar a geração

**Rota 1 (Flow — manual):**
Apresente os prompts formatados para o usuário copiar no Nano Banana Flow. Aguarde o usuário baixar e mover para `images/`.

**Rota 2 (API):**
```bash
python tools/generate_images_api.py .tmp/image_prompts_<project_name>.json --output images/
```

**Rota 3 (Manus):**
```bash
python tools/generate_images_manus.py .tmp/image_prompts_<project_name>.json --output images/ --remove-bg
```

### Passo 4 — Verificar e aplicar

1. Confirme que todos os arquivos estão em `images/`
2. Verifique se os PNGs com fundo removido têm transparência correta
3. Aplique as imagens nos arquivos HTML do projeto substituindo os placeholders

## Outputs

- Arquivos de imagem em `images/` (PNG ou WEBP)
- Fundo removido quando `remove_background = true`
- Imagens referenciadas corretamente no HTML do projeto

## Edge Cases

| Situação | Como lidar |
|---|---|
| Rota 2 ou 3 sem credenciais no `.env` | Parar. Informar quais variáveis estão faltando. Não prosseguir. |
| Imagem gerada não condiz com o pedido | Refinar o prompt adicionando mais especificidade de estilo e composição. Tentar novamente. |
| Fundo não removido corretamente pelo Manus | Processar manualmente ou usar `remove.bg` API como fallback |
| Usuário quer usar imagens próprias | Pular geração. Mover os arquivos para `images/` e seguir para o Passo 4. |
| Muitas imagens com custo alto | Apresentar estimativa de custo antes de executar. Aguardar aprovação. |

## Referências do Vídeo

- Canal: Mateus Dias — "CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000"
- Rota 3 (Manus) destacada como a mais prática para design — PNG sem fundo já incluso
- Claude Code atua como orquestrador: dispara a tarefa, aguarda, baixa e aplica
