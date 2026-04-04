# Workflow: Claude Code — Desenvolvimento Estruturado

## Objetivo

Guiar a construção de aplicações profissionais no Claude Code usando um processo em 4 etapas (Spec → Break → Plan → Execute) que evita os padrões problemáticos do Vibe Coding: contexto lotado, código duplicado, IA desobediente, efeito cobertor, e gafes de segurança.

Baseado no workflow da Deborah Folloni (canal: Deborah Folloni, vídeo: "Vibe Coding não funciona – Novo Workflow no Claude Code").

---

## Inputs Necessários

- `project_description`: Descrição em linguagem natural do que será construído
- `references/architecture.md`: Documento de arquitetura do projeto (padrões, estrutura de pastas, regras de segurança)
- `references/design-system.md`: Documentação do design system (componentes, tokens)
- `references/spec.md`: (gerado na Etapa 1) Spec completa da aplicação

---

## Ferramentas

Nenhuma tool Python necessária — o processo é inteiramente conduzido via comandos do Claude Code com skills e agentes especializados.

Agentes especializados por camada (configurar como skills no Claude Code):
- `model-writer`: Responsável por arquivos de banco de dados e modelos
- `component-writer`: Responsável por componentes de front end
- Demais agentes por camada conforme necessidade do projeto

---

## Processo

### Etapa 1 — Escrever a Spec (`/spec`)

**Objetivo:** Criar um documento que define exatamente o que será construído antes de qualquer linha de código.

Execute no Claude Code:
```
/spec <descrição do projeto>
```

O comando gera `references/spec.md` com:

| Elemento | Descrição |
|---|---|
| **Visão geral** | O que é o projeto e para quem é |
| **Páginas** | Lista de todas as páginas da aplicação |
| **Componentes** | Para cada página, os componentes presentes |
| **Behaviors** | Para cada componente, os comportamentos do usuário possíveis |

**Regra crítica:** Cada behavior vai virar uma tarefinha na próxima etapa. Quanto mais precisa a spec, melhores serão as tarefas geradas.

---

### Etapa 2 — Quebrar em Tarefas (`/break`)

**Objetivo:** Transformar a spec em tarefas pequenas e independentes para preservar a janela de contexto do modelo.

Execute no Claude Code:
```
/break @references/spec.md
```

O comando gera uma pasta de tasks (issues), onde:
- **Cada página** → 1 tarefa de protótipo (só front end estático)
- **Cada behavior** → 1 tarefa de implementação funcional

**Ordem de execução:** Protótipos primeiro, funcionais depois. Isso permite validar as telas antes de conectar a lógica.

**Por que funciona:** Tarefas menores = janela de contexto limpa = maior performance do modelo.

---

### Etapa 3 — Planejar cada Tarefa (`/plan`)

**Objetivo:** Antes de implementar, enriquecer a tarefa com contexto suficiente para que a IA não improvise.

Execute no Claude Code para cada tarefa:
```
/plan @tasks/<nome-da-tarefa>.md
```

O planejamento faz duas pesquisas:

**Pesquisa interna (codebase):**
- Identifica arquivos e trechos de código existentes que podem ser importados/reutilizados
- Evita duplicação de código (ex: não criar um segundo `Button` se já existe um)

**Pesquisa externa (internet/docs):**
- Busca documentação de dependências externas
- Identifica padrões de implementação comprovados
- Evita que o modelo "reinvente a roda"

**Output do planejamento** — a tarefa é enriquecida com:

```
- Descrição detalhada do comportamento
- Cenário feliz (happy path)
- Edge cases
- Cenários de erro
- Tabelas de banco de dados necessárias (com colunas)
- Arquivos a criar ou modificar (com o que muda em cada um)
- Dependências externas
- Checklist de execução
```

**Por que isso importa:** Quando os arquivos a modificar estão listados explicitamente, a IA só mexe neles. A "desobediência" da IA desaparece quando o contexto é claro.

---

### Etapa 4 — Executar (`/execute`)

**Objetivo:** Implementar o planejamento usando agentes especializados por camada.

Execute no Claude Code:
```
/execute @tasks/<nome-da-tarefa>.md
```

Durante a execução, o agente orquestrador delega para agentes especializados:

| Camada | Agente | Skill |
|---|---|---|
| Banco de dados / Modelos | `model-writer` | `write-models` |
| Componentes UI | `component-writer` | `write-components` |
| Backend / API | *(conforme projeto)* | *(conforme projeto)* |

Cada agente lê sua skill correspondente e executa apenas dentro da sua responsabilidade.

---

### Documentos de Apoio (pasta `references/`)

Manter sempre atualizado:

| Arquivo | Conteúdo |
|---|---|
| `architecture.md` | Estrutura de pastas, padrão de isolamento por comportamento, regra thin-client/fat-server, o que é proibido no front end |
| `design-system.md` | Tokens, componentes existentes, padrões visuais |
| `spec.md` | Spec gerada na Etapa 1 |

**Regra de segurança obrigatória no `architecture.md`:**
> "O front end captura intenções do usuário e envia ao back end. Nenhuma regra de negócio, validação de permissão ou chave de API pode existir no front end."

---

## Outputs

- `references/spec.md`: Documento de especificação completo
- `tasks/`: Pasta com todas as tarefas planejadas
- Código implementado seguindo a arquitetura documentada
- Base de código modular, auditável e sem duplicação

---

## Padrões Problemáticos que este Workflow Previne

| Problema (Vibe Coding) | Solução neste Workflow |
|---|---|
| IA engasga em tarefas grandes | Etapa 2: quebrar em tarefas pequenas |
| Código duplicado | Etapa 3: pesquisa interna antes de implementar |
| IA reinventa a roda | Etapa 3: pesquisa externa em docs comprovados |
| IA mexe em arquivos errados | Etapa 3: lista explícita de arquivos no planejamento |
| Arrumar uma coisa quebra outra | `architecture.md` com isolamento por behavior |
| Gafes de segurança | Regra thin-client/fat-server no `architecture.md` |

---

## Edge Cases

| Situação | Como lidar |
|---|---|
| `/spec` gera behaviors muito amplos | Refinar manualmente antes de rodar `/break` |
| Tarefa planejada ainda é grande | Dividir manualmente em 2 tarefas antes de `/execute` |
| Agente especializado não existe para a camada | Usar o agente genérico e documentar a lacuna para criar a skill |
| `architecture.md` não existe ainda | Criar antes da Etapa 4; sem ele, o execute não tem guardrails |
| Protótipo aprovado mas comportamento mudou | Atualizar a tarefa funcional correspondente antes do `/plan` |
