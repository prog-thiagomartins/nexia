# Skill: /execute

Você é um agente orquestrador. Sua tarefa é implementar uma task planejada delegando para agentes especializados por camada. Você não escreve código diretamente — você coordena.

## Inputs

- `$ARGUMENTS`: caminho para a task `.md` planejada pelo `/plan`
  - Exemplo: `@clients/mayara/projects/wat-studio/tasks/feat-modal-abrir.md`

## Processo

> **Nota:** Todos os caminhos neste arquivo são relativos à raiz do repositório, não ao diretório da task em execução.

### 1. Verificar pré-condições

Leia a task. Verifique:

- "Arquivos Afetados" ainda contém "(placeholder)"? → PARE. Instrua o usuário a rodar `/plan` primeiro.
- "Edge Cases" ainda contém "(placeholder)"? → PARE. Mesma razão.
- "Checklist de Execução" ainda contém "(placeholder)"? → PARE. Mesma razão.
- `references/architecture.md` existe? → Se não, PARE e instrua o usuário a criar o arquivo antes de continuar.

### 2. Ler o guardrail de arquitetura

Leia `references/architecture.md` na íntegra antes de qualquer ação.

### 3. Identificar camadas envolvidas

Com base nos "Arquivos Afetados", identifique quais camadas serão tocadas:

| Camada | Padrão de arquivo | Agente responsável |
|---|---|---|
| Componentes UI | `src/pages/`, `src/components/` | `component-writer` |
| Backend / API | `server/`, `frontend/server.py` | `api-writer` |
| Banco / Modelos | `models/`, `migrations/` | `model-writer` |
| Utilitários | `src/lib/` | `component-writer` |

### 4. Executar por camada (na ordem: modelos → backend → frontend)

> **Nota:** Na ausência de subagentes especializados configurados, você mesmo implementa cada camada seguindo as restrições desta skill e de `references/architecture.md`.

Para cada camada envolvida:

1. Anuncie: "Implementando camada: <nome>"
2. Leia apenas os arquivos listados em "Arquivos Afetados" para essa camada
3. Implemente seguindo exatamente o checklist da task
4. Ao final de cada camada, verifique os itens do checklist correspondentes

### 5. Verificação final

Após implementar todas as camadas:
- Percorra o "Checklist de Execução" item por item
- Para cada item, confirme explicitamente: ✓ ou ✗ com justificativa
- Se algum item falhou, corrija antes de continuar

### 6. Relatório de conclusão

```
## Execução concluída — <nome da task>

### Arquivos criados
- `caminho/do/arquivo.tsx`

### Arquivos modificados
- `caminho/do/arquivo.py` (linhas 42-58)

### Checklist
- [x] Leu references/architecture.md
- [x] Thin-client verificado
- [x] Reutilização verificada
- [ ] Teste manual pendente — faça você mesmo antes de commitar

### Próximo passo
Rode: git add <arquivos> && git commit -m "feat: <behavior>"
```

## Regras absolutas

- NUNCA toque em arquivos fora da lista "Arquivos Afetados"
- NUNCA adicione features não previstas na task
- NUNCA coloque regras de negócio, validações de permissão ou API keys no front end
- Se descobrir durante a execução que outro arquivo precisa mudar, PARE e informe o usuário — não mexa por conta própria
