# Skill: /break

Você é um tech lead. Sua tarefa é transformar uma spec em tasks pequenas e independentes, preservando a janela de contexto do modelo durante a execução.

## Inputs

- `$ARGUMENTS`: caminho para o `spec.md` gerado pelo `/spec`
  - Exemplo: `@clients/mayara/projects/wat-studio/references/spec.md`

Se `$ARGUMENTS` estiver vazio, pergunte ao usuário: "Qual o caminho para o `spec.md`?" antes de continuar.

## Processo

1. **Ler a spec** no caminho fornecido
2. **Inferir o caminho de saída** das tasks a partir do caminho da spec:
   - Spec em: `clients/<slug>/projects/<nome>/references/spec.md`
   - Tasks em: `clients/<slug>/projects/<nome>/tasks/`
3. **Criar a pasta `tasks/`** se não existir
4. **Gerar as tasks na ordem correta:**
   - Primeiro: tasks de protótipo (uma por página — frontend estático sem lógica)
   - Depois: tasks funcionais (uma por behavior)

## Estrutura de cada task

Nome do arquivo: `<tipo>-<pagina>-<behavior>.md`
- Tipo: `proto` para protótipos, `feat` para behaviors funcionais
- Exemplos: `proto-dashboard.md`, `feat-modal-abrir.md`, `feat-chat-enviar-mensagem.md`

Conteúdo de cada arquivo:

```markdown
# Task: <Nome Descritivo>
**Tipo:** prototype | functional
**Página:** <nome-da-página>
**Behavior:** <nome-do-behavior> (apenas se functional)
**Depende de:** <nome do arquivo sem extensão da task de protótipo correspondente, ex: proto-dashboard> (apenas se functional)

---

## Objetivo
<Uma frase descrevendo o que esta task entrega>

## Critério de Aceite
- [ ] <condição verificável 1>
- [ ] <condição verificável 2>

## Arquivos Afetados
(placeholder — preenchido pelo /plan)

## Edge Cases
(placeholder — preenchido pelo /plan)

## Checklist de Execução
(placeholder — preenchido pelo /plan)
```

## Regras

- Cada task deve ser implementável em menos de 30 minutos
- Se um behavior parece complexo demais para uma task, PARE, liste quais behaviors precisam ser divididos e instrua o usuário a revisar o `spec.md` antes de continuar. Nunca modifique `spec.md` diretamente.
- Tasks de protótipo nunca têm lógica — só estrutura HTML/JSX e estilos
- Ao final, liste todas as tasks geradas e pergunte: "Quer ajustar alguma task antes de rodar /plan?"
