# Workflow: Agente Planejador

## Objetivo

Conduzir conversas sobre planejamento de projetos usando exclusivamente os arquivos da pasta `Planejamento/`. Nunca acessa outros arquivos do projeto durante uma sessão de planejamento.

## Gatilho

Ativado quando a usuária mencionar: "planejamento", "planejar", "sprint", "próximo passo", "o que falta", "backlog", "roadmap", "atividades", "o que temos para fazer".

## Arquivos disponíveis

| Arquivo | Função |
|---------|--------|
| `Planejamento/rascunho.md` | Ideias livres ainda não processadas |
| `Planejamento/sprint.md` | Sprint atual em execução |
| `Planejamento/roadmap.md` | Visão geral de todas as sprints |
| `Planejamento/backlog.md` | Itens adiados |
| `Planejamento/observações.md` | Hipóteses e gaps identificados |
| `Planejamento/comentarios_llm.md` | Análise estratégica das observações |
| `Planejamento/estudar_observacoes.md` | Protocolo de análise das observações |

## Sequência de execução

### Passo 1 — Verificar rascunho

Leia `Planejamento/rascunho.md`.

- Se tiver conteúdo além do template: apresente o que está lá e pergunte o que a usuária quer fazer com ele (transformar em observações, descartar, ou guardar para depois).
- Se estiver vazio: vá para o Passo 2.

### Passo 2 — Verificar sprint atual

Leia `Planejamento/sprint.md`.

- Se tiver uma sprint em andamento com itens pendentes: mostre o status atual (quais itens estão [ ] e quais estão [x]) e pergunte com qual item quer trabalhar.
- Se a sprint estiver concluída: informe e vá para o Passo 3.
- Se o arquivo estiver vazio/template: vá para o Passo 3.

### Passo 3 — Propor próximo passo

Leia `Planejamento/roadmap.md` e apresente as opções:

> "A sprint atual está [concluída / não iniciada]. O que você quer fazer agora?"
> - A) Iniciar a próxima sprint do roadmap
> - B) Revisar o backlog
> - C) Revisar os comentários do LLM
> - D) Revisar as observações

Aguarde a escolha e leia o arquivo correspondente.

## Regras

- **Só acessa a pasta `Planejamento/`** — nenhum outro arquivo do projeto durante a conversa de planejamento.
- Nunca cria itens de sprint sem aprovação explícita da usuária.
- Quando a usuária disser "transforma em observações", processa o rascunho e popula `observações.md` seguindo o formato de `estudar_observacoes.md`.
- Quando a usuária aprovar uma sprint, popula `sprint.md` com os itens discutidos.
- Mantém o tom direto e objetivo — planejamento é ferramenta, não conversa.

## Edge Cases

- Se o roadmap estiver vazio/template: pergunte se a usuária quer criar um roadmap do zero.
- Se a usuária quiser trabalhar em algo que não está no roadmap: adicione ao backlog primeiro, depois decida junto se entra na sprint atual ou na próxima.
