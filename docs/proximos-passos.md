# nexia — Próximos Passos

## Feito nessa sessão

- [x] CLAUDE.md reescrito — foco em desenvolvimento do nexia, modelo multi-AI, WAT como camada
- [x] Hooks GSD removidos do `~/.claude/settings.json` (SessionStart, PostToolUse, PreToolUse, statusLine)
- [x] Diagrama de arquitetura atualizado — nós planejados com visual distinto, novos tools adicionados, arestas com routing ortogonal
- [x] `tools/audit_architecture.py` criado — compara diagrama vs realidade via Gemini

---

## Pendente — por ordem de impacto

### 1. Definir UX do nexia
**O que é:** Decidir quem usa qual interface e com qual experiência.

Duas personas distintas:
- **Você (operador):** já usa via Claude Code, precisa de melhor feedback visual no frontend quando tools rodam
- **Cliente (Mayara, futuros):** precisa de uma UX simplificada — não vê tool calls, só inputs e outputs

**Por que importa:** essa decisão define o que construir no frontend. Se for só para você, a UX pode expor o pipeline. Se for para cliente, precisa abstrair tudo.

**Próxima ação:** definir as duas telas — operador vs cliente — antes de tocar no frontend.

---

### 2. Criar `CLAUDE.template.md`
**O que é:** Template base para onboarding de novos clientes no nexia. Quando um novo cliente entra, esse template vira o `CLAUDE.md` do repo `nexia-<slug>`.

**Conteúdo esperado:**
- Quem é o cliente e o negócio dele
- Voz de marca e tom de conteúdo
- Workflows ativos para esse cliente
- Paths de context e projects

**Próxima ação:** criar `CLAUDE.template.md` na raiz do projeto com placeholders para cada seção.

---

### 3. Criar tools de geração de imagens
**O que é:** `tools/generate_images_api.py` e `tools/generate_images_manus.py` — referenciados no `session_router.md` mas não existem ainda.

**Gap:** o `session_router.md` roteia tarefas de imagem para esses scripts, mas eles não existem. Se alguém pedir geração de imagem hoje, o fluxo quebra.

**Próxima ação:** criar os dois scripts seguindo o padrão de `call_gemini_api.py`, ou remover as referências do session_router até estarem prontos.

---

### 4. Documento de migração filesystem → Supabase
**O que é:** O schema do Supabase está pronto (`docs/supabase-schema.md`), mas não existe nenhum documento descrevendo como migrar os dados de `clients/<slug>/` para o banco.

**Gap crítico:** sem esse documento, a migração vai ser feita na força bruta quando chegar a hora, com risco de perda de dados ou estrutura inconsistente.

**Conteúdo esperado:**
- Mapeamento: qual pasta local → qual tabela Supabase
- Estratégia de RLS (tenant_id por slug)
- Script de migração inicial
- Como o frontend passa a ler do DB em vez do filesystem

**Próxima ação:** criar `docs/supabase-migration.md` com o mapeamento e a estratégia antes de começar qualquer implementação.

---

## Horizonte mais longe

- [ ] Supabase Auth (Magic Link) — planejado, não iniciado
- [ ] Supabase Storage para reels e projetos — planejado, não iniciado
- [ ] Frontend com feedback em tempo real de tool calls
- [ ] Sistema de onboarding de novo cliente (criar repo + CLAUDE.md a partir do template)
