Como Pesquisador e Destilador de Contexto para o projeto Mayara, processei sua solicitação sobre padrões multi-tenant com Supabase para a plataforma WAT Studio.

---

## Documento de Referência: Padrões Multi-Tenant com Supabase para WAT Studio

Este documento detalha as melhores práticas e padrões para implementar um ambiente multi-tenant no Supabase (PostgreSQL, Auth, RLS, Storage) para a plataforma WAT Studio, focada em nutricionistas.

### 1. Boas Práticas de Isolação por Tenant com RLS (Row Level Security)

A isolação de dados é fundamental em um ambiente multi-tenant. O RLS do PostgreSQL é a ferramenta ideal para isso no Supabase.

*   **Princípio Fundamental: Coluna `tenant_id`**: Todas as tabelas que contêm dados específicos de um tenant devem possuir uma coluna `tenant_id` (tipo `UUID`) que referencia a tabela `public.tenants`.
*   **Tabelas Essenciais:**
    *   `public.tenants`: Armazena informações sobre cada cliente/tenant (ex: `id UUID PRIMARY KEY`, `nome`, `plano`, `voz_de_marca_json`).
    *   `public.profiles`: Vincula usuários do Supabase Auth a um tenant e armazena dados de perfil.
        ```sql
        CREATE TABLE public.profiles (
            id UUID REFERENCES auth.users(id) PRIMARY KEY, -- FK para auth.users
            tenant_id UUID REFERENCES public.tenants(id) NOT NULL, -- FK para tenants
            nome TEXT,
            ... -- outros dados do perfil do usuário
        );
        ```
*   **Políticas RLS**: Ative o RLS para todas as tabelas de dados do tenant (`ALTER TABLE <tabela> ENABLE ROW LEVEL SECURITY;`). Crie políticas que garantam que um usuário só acesse dados de seu próprio tenant.
    *   `USING`: Define quais linhas podem ser *selecionadas, atualizadas ou excluídas*.
    *   `WITH CHECK`: Define quais linhas podem ser *inseridas ou atualizadas* (garante que novos dados sejam criados com o `tenant_id` correto).
    *   **Exemplo de Política RLS (SELECT/UPDATE/DELETE):**
        ```sql
        CREATE POLICY "Allow tenant to manage their own projects" ON public.projetos
        FOR ALL TO authenticated
        USING (tenant_id = (SELECT tenant_id FROM public.profiles WHERE id = auth.uid()))
        WITH CHECK (tenant_id = (SELECT tenant_id FROM public.profiles WHERE id = auth.uid()));
        ```
        (Repita para `briefs`, `entregaveis`, etc.)

### 2. Mapeamento de `auth.uid()` para `client_id` (Tenant ID)

*   **`auth.uid()`**: É o `UUID` único do usuário atualmente autenticado no sistema de autenticação do Supabase (`auth.users`).
*   **`client_id` (Tenant ID)**: No contexto de WAT Studio, `client_id` refere-se ao `tenant_id`.
*   **Mapeamento**: O elo entre `auth.uid()` e o `tenant_id` é a tabela `public.profiles`.
    *   Quando um usuário faz login, `auth.uid()` é acessível nas políticas RLS.
    *   Para obter o `tenant_id` associado a esse usuário, você consulta a tabela `public.profiles`:
        ```sql
        (SELECT tenant_id FROM public.profiles WHERE id = auth.uid())
        ```
    *   Este padrão é usado consistentemente em todas as políticas RLS para garantir a isolação.

### 3. Padrão de Schema Multi-Tenant no Supabase

*   **Shared Database, Shared Schema (Discriminator Column)**: Este é o padrão mais recomendado e amplamente utilizado com Supabase.
    *   **Descrição**: Todos os tenants compartilham o mesmo banco de dados PostgreSQL e o mesmo schema público (`public`). A distinção entre os dados dos tenants é feita pela coluna `tenant_id` em cada tabela relevante. O RLS é configurado para aplicar essa distinção.
    *   **Vantagens**:
        *   **Simplicidade**: Fácil de configurar e gerenciar.
        *   **Custo-benefício**: Utiliza eficientemente os recursos de um único banco de dados.
        *   **Manutenção**: Migrações de schema são aplicadas a todos os tenants de uma vez.
        *   **Escalabilidade**: Bem suportado pelo Supabase e PostgreSQL.
    *   **Considerações**: Requer RLS bem configurado e testado para garantir a segurança dos dados.

### 4. Magic Link vs. Email+Password para Usuários Não-Tech

Para nutricionistas (usuários não-tech), a escolha do método de autenticação impacta diretamente a experiência do usuário e a carga de suporte.

*   **Magic Link (Email OTP)**:
    *   **Prós**: Experiência sem senha ("passwordless"), extremamente amigável para não-tech. Reduz a sobrecarga de lembrar/redefinir senhas. Mais seguro (sem senhas a serem roubadas/adivinhadas).
    *   **Contras**: Depende do acesso ao email do usuário no momento do login. Pode ser um pouco mais lento que um login de senha.
*   **Email + Senha**:
    *   **Prós**: Familiar para muitos usuários. Login imediato se a senha for lembrada.
    *   **Contras**: Gerenciamento de senhas (esquecimento, redefinição) é uma fonte comum de frustração e tickets de suporte. Maior risco de segurança (senhas fracas, reutilização).
*   **Recomendação para WAT Studio**: **Magic Link** é fortemente recomendado. Ele oferece uma experiência de usuário mais suave e segura para o público-alvo de nutricionistas, minimizando atritos e a necessidade de suporte para problemas de autenticação. O Supabase o suporta nativamente. Você pode oferecer a opção de email+password como alternativa, mas o Magic Link deve ser a opção principal.

### 5. Como Usar Storage com RLS por Tenant

O Supabase Storage também pode e deve ser protegido com RLS para isolar arquivos por tenant.

*   **Princípio**: As políticas RLS do Storage são aplicadas ao `storage.objects` e podem utilizar `auth.uid()` para determinar permissões.
*   **Abordagem com Metadata Table**: Para controle robusto, crie uma tabela de metadados no schema `public` que vincule os arquivos aos tenants.
    *   **Exemplo de Schema de Metadata (`public.arquivos_tenant`):**
        ```sql
        CREATE TABLE public.arquivos_tenant (
            id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
            tenant_id UUID REFERENCES public.tenants(id) NOT NULL,
            bucket_name TEXT NOT NULL,          -- Nome do bucket do Supabase Storage
            object_path TEXT NOT NULL UNIQUE,   -- Caminho completo do objeto no Storage (ex: 'projetos/id_projeto/imagem.jpg')
            nome_original TEXT,
            tipo_mime TEXT,
            tamanho_bytes BIGINT,
            uploaded_by UUID REFERENCES auth.users(id),
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
        ALTER TABLE public.arquivos_tenant ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Allow tenant to see their file metadata" ON public.arquivos_tenant
        FOR SELECT TO authenticated USING (tenant_id = (SELECT tenant_id FROM public.profiles WHERE id = auth.uid()));
        -- Adicione políticas para INSERT, UPDATE, DELETE conforme necessário
        ```
*   **Exemplos de Políticas RLS para Storage (`storage.objects`)**:
    *   Garanta que apenas usuários autenticados possam acessar objetos, e apenas aqueles que pertencem ao seu tenant.
    *   **Política para ACESSO (SELECT/DOWNLOAD):**
        ```sql
        CREATE POLICY "Allow authenticated users to read their own tenant files" ON storage.objects
        FOR SELECT TO authenticated
        USING (
            bucket_id = 'wat-studio-files' AND EXISTS (
                SELECT 1 FROM public.arquivos_tenant
                WHERE object_path = name AND tenant_id = (SELECT tenant_id FROM public.profiles WHERE id = auth.uid())
            )
        );
        ```
    *   **Política para CRIAÇÃO/UPLOAD (INSERT):**
        ```sql
        CREATE POLICY "Allow authenticated users to upload their own tenant files" ON storage.objects
        FOR INSERT TO authenticated
        WITH CHECK (
            bucket_id = 'wat-studio-files' AND EXISTS (
                SELECT 1 FROM public.arquivos_tenant
                WHERE object_path = name AND tenant_id = (SELECT tenant_id FROM public.profiles WHERE id = auth.uid())
            )
        );
        ```
        *Nota:* Para `INSERT` no Storage, você precisará primeiro inserir o registro na `public.arquivos_tenant` com o `object_path` e `tenant_id` corretos *antes* de tentar fazer o upload do arquivo real via Storage SDK. O `WITH CHECK` garante que o `object_path` que está sendo inserido no Storage já tenha uma entrada válida na sua tabela de metadados.

---
<brief>
TAREFA: Pesquisar e detalhar padrões de multi-tenant com Supabase (PostgreSQL + Auth + RLS + Storage) para uma plataforma SaaS (WAT Studio) focada em nutricionistas, cobrindo isolamento com RLS, mapeamento auth.uid() para client_id, padrões de schema, métodos de autenticação e uso de Storage com RLS.
ARQUIVOS LIDOS: 0 (nenhum arquivo de contexto fornecido)
RESUMO: O documento prático fornecido aborda as melhores práticas de isolamento de dados via RLS, o mapeamento do ID do usuário autenticado para o ID do tenant, e o padrão de schema recomendado (Shared Database, Shared Schema). Recomenda Magic Link para usuários não-tech e detalha como implementar RLS para o Supabase Storage, utilizando uma tabela de metadados para controle granular de acesso por tenant.
PRÓXIMO PASSO PARA O CLAUDE: O Claude deve usar este documento como base para guiar a implementação da arquitetura multi-tenant do projeto Mayara no Supabase, focando nos detalhes de configuração e segurança. Pode ser solicitado a gerar exemplos de código SQL mais completos para as políticas RLS ou modelos de classes para a aplicação.
</brief>