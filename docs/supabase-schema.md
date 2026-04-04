# nexia — Supabase Schema

**Padrão:** Shared Database, Shared Schema com `tenant_id` discriminator  
**Auth:** Magic Link (passwordless) — recomendado para usuários não-tech  
**Gerado em:** 2026-04-04  
**Fonte:** Pesquisa Gemini (`gemini/research/2026-04-04_pesquise-padrões-de-multi-tenant-com-sup.md`)

---

## Mapeamento: Arquivos Locais → Tabelas

| Arquivo local | Tabela Supabase |
|---|---|
| `clients/<slug>/client.json` | `tenants` |
| `auth.users` (Supabase) | `profiles` |
| `context/negocio/*.md` | `context_business` |
| `context/memoria/voz_marca.md` | `brand_voice` |
| `context/memoria/preferencias.md` | `preferences` |
| `context/memoria/historico_temas.md` | `topic_history` |
| `context/pesquisas/*.md` | `research_notes` |
| `gemini/briefs/*.md` | `ai_outputs` (type='brief') |
| `gemini/drafts/*.md` | `ai_outputs` (type='draft') |
| `gemini/research/*.md` | `ai_outputs` (type='research') |
| `gemini/audits/*.md` | `ai_outputs` (type='audit') |
| `projects/reels/`, `projects/prototipos/` | `projects` + Storage |

---

## SQL — Migration Completa

```sql
-- ============================================================
-- 0. EXTENSIONS
-- ============================================================
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================
-- 1. TENANTS (clientes do nexia)
-- ============================================================
CREATE TABLE public.tenants (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    slug        TEXT UNIQUE NOT NULL,           -- 'mayara', 'joao', etc.
    name        TEXT NOT NULL,
    niche       TEXT,                           -- 'nutrição', 'fisioterapia', etc.
    plan        TEXT DEFAULT 'pilot',           -- 'pilot', 'starter', 'pro'
    workflows   TEXT[] DEFAULT '{}',            -- workflows habilitados
    active      BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 2. PROFILES (liga auth.users → tenant)
-- ============================================================
CREATE TABLE public.profiles (
    id          UUID REFERENCES auth.users(id) PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    name        TEXT,
    role        TEXT DEFAULT 'owner',           -- 'owner', 'member', 'admin'
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 3. CONTEXT_BUSINESS (context/negocio/*.md)
-- ============================================================
CREATE TABLE public.context_business (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    topic       TEXT NOT NULL,                  -- 'aquisicao', 'conversao', 'escalabilidade', etc.
    content     TEXT NOT NULL,
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 4. BRAND_VOICE (context/memoria/voz_marca.md)
-- ============================================================
CREATE TABLE public.brand_voice (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) UNIQUE NOT NULL,
    version     INTEGER DEFAULT 1,
    content     TEXT NOT NULL,                  -- markdown completo
    confidence  FLOAT DEFAULT 0.0,
    sources     TEXT[],
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 5. PREFERENCES (context/memoria/preferencias.md)
-- ============================================================
CREATE TABLE public.preferences (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) UNIQUE NOT NULL,
    content     TEXT NOT NULL,                  -- markdown com preferências
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 6. TOPIC_HISTORY (context/memoria/historico_temas.md)
-- ============================================================
CREATE TABLE public.topic_history (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    topic       TEXT NOT NULL,
    produced_at DATE NOT NULL,
    notes       TEXT,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 7. RESEARCH_NOTES (context/pesquisas/*.md)
-- ============================================================
CREATE TABLE public.research_notes (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    title       TEXT NOT NULL,
    content     TEXT NOT NULL,
    tags        TEXT[] DEFAULT '{}',
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 8. AI_OUTPUTS (gemini/briefs/, drafts/, research/, audits/)
-- ============================================================
CREATE TABLE public.ai_outputs (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    type        TEXT NOT NULL CHECK (type IN ('brief','draft','research','audit')),
    task        TEXT NOT NULL,                  -- tarefa que gerou o output
    model       TEXT,                           -- 'gemini-2.5-flash', etc.
    content     TEXT NOT NULL,
    produced_at DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 9. PROJECTS (clients/mayara/projects/)
-- ============================================================
CREATE TABLE public.projects (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    name        TEXT NOT NULL,
    type        TEXT NOT NULL CHECK (type IN ('reel','prototipo','landing_page','campanha','outro')),
    status      TEXT DEFAULT 'draft' CHECK (status IN ('draft','review','approved','published')),
    notes       TEXT,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 10. FILES (Supabase Storage metadata)
-- ============================================================
CREATE TABLE public.files (
    id          UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id   UUID REFERENCES public.tenants(id) NOT NULL,
    project_id  UUID REFERENCES public.projects(id),
    bucket      TEXT NOT NULL DEFAULT 'nexia', -- env: SUPABASE_BUCKET
    path        TEXT NOT NULL UNIQUE,           -- 'mayara/reels/azia/v5.mp4'
    filename    TEXT NOT NULL,
    mime_type   TEXT,
    size_bytes  BIGINT,
    uploaded_by UUID REFERENCES auth.users(id),
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- 11. RLS — ENABLE
-- ============================================================
ALTER TABLE public.tenants           ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.profiles          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.context_business  ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.brand_voice       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.preferences       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.topic_history     ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.research_notes    ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.ai_outputs        ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.projects          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.files             ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 12. RLS — HELPER FUNCTION (evita subquery repetida)
-- ============================================================
CREATE OR REPLACE FUNCTION public.my_tenant_id()
RETURNS UUID LANGUAGE SQL SECURITY DEFINER STABLE AS $$
    SELECT tenant_id FROM public.profiles WHERE id = auth.uid();
$$;

-- ============================================================
-- 13. RLS — POLICIES
-- ============================================================

-- profiles: cada usuário vê e edita só o próprio
CREATE POLICY "profiles_self" ON public.profiles
    FOR ALL TO authenticated
    USING (id = auth.uid())
    WITH CHECK (id = auth.uid());

-- tenants: tenant só vê o próprio
CREATE POLICY "tenants_self" ON public.tenants
    FOR SELECT TO authenticated
    USING (id = public.my_tenant_id());

-- tabelas de dados: isolação total por tenant
CREATE POLICY "context_business_tenant" ON public.context_business
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "brand_voice_tenant" ON public.brand_voice
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "preferences_tenant" ON public.preferences
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "topic_history_tenant" ON public.topic_history
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "research_notes_tenant" ON public.research_notes
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "ai_outputs_tenant" ON public.ai_outputs
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "projects_tenant" ON public.projects
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

CREATE POLICY "files_tenant" ON public.files
    FOR ALL TO authenticated
    USING (tenant_id = public.my_tenant_id())
    WITH CHECK (tenant_id = public.my_tenant_id());

-- ============================================================
-- 14. RLS — STORAGE (bucket: nexia / env: SUPABASE_BUCKET)
-- ============================================================
CREATE POLICY "storage_read_tenant" ON storage.objects
    FOR SELECT TO authenticated
    USING (
        bucket_id = 'nexia' AND EXISTS (  -- bucket: env SUPABASE_BUCKET
            SELECT 1 FROM public.files
            WHERE path = name
            AND tenant_id = public.my_tenant_id()
        )
    );

CREATE POLICY "storage_insert_tenant" ON storage.objects
    FOR INSERT TO authenticated
    WITH CHECK (
        bucket_id = 'nexia' AND EXISTS (  -- bucket: env SUPABASE_BUCKET
            SELECT 1 FROM public.files
            WHERE path = name
            AND tenant_id = public.my_tenant_id()
        )
    );

-- ============================================================
-- 15. INDEXES
-- ============================================================
CREATE INDEX idx_context_business_tenant   ON public.context_business(tenant_id);
CREATE INDEX idx_brand_voice_tenant        ON public.brand_voice(tenant_id);
CREATE INDEX idx_ai_outputs_tenant_type    ON public.ai_outputs(tenant_id, type);
CREATE INDEX idx_ai_outputs_date           ON public.ai_outputs(produced_at DESC);
CREATE INDEX idx_projects_tenant           ON public.projects(tenant_id);
CREATE INDEX idx_files_tenant              ON public.files(tenant_id);
CREATE INDEX idx_topic_history_tenant_date ON public.topic_history(tenant_id, produced_at DESC);
```

---

## Auth Flow

```
1. Usuário informa email no nexia
2. Supabase envia Magic Link para o email
3. Usuário clica no link → autenticado
4. Frontend chama profiles para obter tenant_id
5. Todas as queries seguintes usam RLS automaticamente
```

## Storage — Convenção de Paths

```
nexia/
  <tenant_slug>/
    reels/<project_id>/<filename>
    prototipos/<project_id>/<filename>
    campanha/<project_id>/<filename>
```
