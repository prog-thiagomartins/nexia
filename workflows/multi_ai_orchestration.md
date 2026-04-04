# Workflow: Multi-AI Orchestration

## Objetivo

Usar Claude Code como orquestrador central que delega tarefas específicas para outros AIs (Gemini/Nano Banana, Manus, Codex, etc.), coleta os resultados e os aplica no projeto. Cada AI faz o que faz melhor.

## Quando Usar

- O projeto precisa de capacidades que Claude Code não executa diretamente (geração de imagem, vídeo, áudio)
- Uma tarefa específica é mais barata ou melhor em outro modelo
- Você quer automatizar um pipeline que cruza múltiplas ferramentas de IA

## Mapa de Responsabilidades

| AI | Melhor para | Integração |
|---|---|---|
| **Claude Code** | Orquestração, código, raciocínio, escrita | Central — sempre presente |
| **Gemini / Nano Banana** | Geração de imagens, análise multimodal | API direta ou Flow manual |
| **Manus** | Imagens com fundo removido, automações visuais | Task dispatch via API |
| **Codex** | Geração de código em contextos específicos | Substituição pontual do Claude |

## Inputs Necessários

- `task`: Descrição do que precisa ser feito
- `required_capabilities`: Lista de capacidades necessárias (ex: `["image_generation", "code", "background_removal"]`)
- `budget`: `free`, `low`, `any` — define quais rotas pagas estão liberadas

## Ferramentas

- `tools/generate_images_api.py` — Gemini API para imagens
- `tools/generate_images_manus.py` — Manus para imagens com fundo removido
- Outros scripts adicionados conforme novas integrações forem criadas

## Processo

### Passo 1 — Mapear a tarefa

Decomponha a tarefa em subtarefas atômicas e mapeie qual AI executa cada uma:

```
Tarefa: Criar landing page completa

Subtarefa 1: Estrutura HTML/CSS/JS → Claude Code
Subtarefa 2: Gerar 4 ilustrações   → Gemini API (ou Manus se precisar de PNG)
Subtarefa 3: Escrever copy          → Claude Code
Subtarefa 4: Aplicar imagens        → Claude Code (após receber os arquivos)
```

Documente esse mapa em `.tmp/orchestration_plan_<task_name>.md`.

### Passo 2 — Executar subtarefas na ordem correta

Identifique dependências:
- Subtarefas independentes podem rodar em paralelo
- Subtarefas que dependem de output de outra devem aguardar

Exemplo de sequência para landing page:
```
[paralelo]  HTML/CSS + Copy
[aguarda]   Geração de imagens (precisa saber quais imagens o HTML usa)
[sequencial] Aplicar imagens no HTML finalizado
```

### Passo 3 — Dispatcher para cada AI

**Dispatch para Gemini (imagens):**
```bash
python tools/generate_images_api.py prompts.json --output images/
```

**Dispatch para Manus (imagens com fundo removido):**
```bash
python tools/generate_images_manus.py prompts.json --output images/ --remove-bg
```

**Claude Code direto:** Executar inline — sem script necessário.

### Passo 4 — Coletar e integrar outputs

1. Aguarde a conclusão de cada subtarefa
2. Mova outputs para os diretórios corretos do projeto
3. Aplique os resultados (ex: caminhos de imagens no HTML, copy nos textos)
4. Valide que o output de cada AI foi aplicado corretamente

### Passo 5 — Revisão de coerência

Após integrar tudo, revisar:
- O estilo visual é consistente entre as imagens geradas?
- O copy está alinhado com o objetivo da página?
- Os arquivos de código referenciam os assets corretamente?

## Outputs

- Projeto completo com contribuições de múltiplos AIs integradas
- Log do plano de orquestração em `.tmp/orchestration_plan_<task_name>.md`

## Edge Cases

| Situação | Como lidar |
|---|---|
| AI externa está indisponível | Documentar qual etapa falhou. Oferecer alternativa (ex: Rota 1 manual para imagens). |
| Output de outro AI não é utilizável | Refinar o prompt e redispatchar. Máximo 2 tentativas antes de escalar para o usuário. |
| Custo inesperado | Sempre confirmar com o usuário antes de qualquer chamada paga. Nunca assumir que está liberado. |
| Dependência circular | Reordenar as subtarefas. Se impossível, quebrar em fases separadas. |

## Extensão do Workflow

Quando uma nova integração de AI for adicionada ao sistema:

1. Criar o script em `tools/`
2. Adicionar uma linha na tabela "Mapa de Responsabilidades"
3. Adicionar o bloco de dispatch no Passo 3
4. Documentar edge cases específicos dessa integração

## Referências do Vídeo

- Canal: Mateus Dias — "CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000"
- Padrão validado em produção: Claude Code → Manus → download PNG → aplicar no site
- Mesmo padrão usado para gerar slides de vídeos e treinamentos
