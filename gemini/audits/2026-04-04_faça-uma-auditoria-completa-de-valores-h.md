Aqui está a auditoria completa de valores hardcoded em todos os arquivos do projeto, estruturada por categoria de risco.

---

## Auditoria de Valores Hardcoded do Projeto Mayara

### 1. Riscos ALTOS (Hardcodes que DEVEM ser parametrizados para multi-tenant/multi-domínio e segurança)

| Arquivo e Linha | Valor Hardcoded | Categoria | Risco | Como Parametrizar |
|---|---|---|---|---|
| `workflows\image_generation_pipeline.md:16` | `images/` | Path | Alto | Variável de configuração para diretório de saída de imagens, ou caminho dinâmico baseado no projeto/cliente. |
| `workflows\image_generation_pipeline.md:31` | `tools/generate_images_api.py` | Path | Alto | Variável de configuração para o caminho da ferramenta ou lookup dinâmico de ferramentas. |
| `workflows\image_generation_pipeline.md:32` | `tools/generate_images_manus.py` | Path | Alto | Variável de configuração para o caminho da ferramenta ou lookup dinâmico de ferramentas. |
| `workflows\image_generation_pipeline.md:65` | `.tmp/image_prompts_<project_name>.json` | Path | Alto | Variável de configuração para o diretório temporário e nome de arquivo dinâmico baseado no projeto/contexto. |
| `workflows\image_generation_pipeline.md:69`, `73` | `images/` | Path | Alto | Variável de configuração para diretório de saída de imagens, ou caminho dinâmico baseado no projeto/cliente. |
| `workflows\image_generation_pipeline.md:70`, `74` | `--output images/` | Path | Alto | Variável de configuração para diretório de saída de imagens, ou caminho dinâmico baseado no projeto/cliente. |
| `workflows\image_generation_pipeline.md:85` | `.env` | Credencial | Alto | Já é um padrão, mas a referência explícita é um hardcode do nome do arquivo de credenciais. A parametrização deve ser via mecanismos de variáveis de ambiente. |
| `workflows\landing_page_builder.md:28` | `<project_name>/` | Path | Alto | Placeholder indica que o nome do diretório raiz deve ser dinâmico (variável `project_name`). |
| `workflows\landing_page_builder.md:29-38` | `index.html`, `css/`, `styles.css`, `js/`, `animations.js`, `scroll.js`, `magnetic.js`, `images/`, `assets/` | Path | Alto | Definir esses caminhos via variáveis de configuração, permitindo flexibilidade na estrutura do projeto por cliente. |
| `workflows\landing_page_builder.md:24` | `.tmp/lp_brief_<project_name>.md` | Path | Alto | Variável de configuração para o diretório temporário e nome de arquivo dinâmico. |
| `workflows\landing_page_builder.md:92` | `image_generation_pipeline.md` | Path | Alto | Lookup dinâmico de workflows por ID/nome em um registro central. |
| `workflows\landing_page_builder.md:104` | `deploy_site.md` | Path | Alto | Lookup dinâmico de workflows por ID/nome em um registro central. |
| `workflows\reels_com_ia.md:13`, `17`, `23`, `24`, `25`, `30`, `31`, `38`, `52`, `170` | `.tmp/` | Path | Alto | Variável de configuração global para o diretório temporário (`TMP_DIR`). |
| `workflows\reels_com_ia.md:13`, `29` | `video.mp4` | Path | Alto | Nome de arquivo dinâmico, baseado no input do usuário ou ID do vídeo. |
| `workflows\reels_com_ia.md:21` | `tools/fetch_youtube_info.py` | Path | Alto | Variável de configuração para o caminho da ferramenta ou lookup dinâmico de ferramentas. |
| `workflows\reels_com_ia.md:22` | `tools/create_reel.py` | Path | Alto | Variável de configuração para o caminho da ferramenta ou lookup dinâmico de ferramentas. |
| `workflows\reels_com_ia.md:23` | `yt-dlp` | Tool Name | Alto | Verificar se a ferramenta está no PATH do sistema. |
| `workflows\reels_com_ia.md:24` | `ffmpeg` | Tool Name | Alto | Verificar se a ferramenta está no PATH do sistema. |
| `workflows\reels_com_ia.md:29` | `mkdir -p .tmp` | Path | Alto | Usar variável de ambiente para o diretório temporário (`TMP_DIR`). |
| `workflows\reels_com_ia.md:30` | `.tmp/%(title)s.%(ext)s` | Path | Alto | Caminho de saída dinâmico, usando `TMP_DIR`. |
| `workflows\reels_com_ia.md:38` | `ffprobe -v quiet -show_entries format=duration -of csv=p=0 .tmp/video.mp4` | Path | Alto | Caminho do arquivo de vídeo deve usar `TMP_DIR` e nome de arquivo dinâmico. |
| `workflows\reels_com_ia.md:42` | `.tmp/config_reel.json` | Path | Alto | Caminho do arquivo de configuração deve usar `TMP_DIR`. |
| `workflows\reels_com_ia.md:52` | `"input": ".tmp/nome_do_video.mp4"` | Path | Alto | Caminho de input deve usar `TMP_DIR` e nome de arquivo dinâmico. |
| `workflows\reels_com_ia.md:53` | `"output": ".tmp/reel_final.mp4"` | Path | Alto | Caminho de output deve usar `TMP_DIR` e nome de arquivo dinâmico. |
| `workflows\reels_com_ia.md:83` | `python tools/create_reel.py .tmp/config_reel.json` | Path | Alto | Caminhos da ferramenta e do arquivo de configuração devem ser dinâmicos. |
| `workflows\reels_com_ia.md:87`, `170` | `.tmp/reel_final.mp4` | Path | Alto | Caminho do arquivo final deve usar `TMP_DIR`. |
| `workflows\reels_com_ia.md:135` | `.tmp/fonts/` | Path | Alto | Variável de configuração para o diretório de fontes, ou usar um gerenciador de fontes. |
| `workflows\research_niche.md:1` | `Mayara Farias (Nutrition)` | Cliente/Nicho | Alto | O workflow deve ser genérico. Nome do cliente e nicho devem ser passados como inputs ou configurados por contexto do cliente ativo. |
| `workflows\research_niche.md:26` | `Mayara` | Cliente | Alto | Substituir por uma variável do cliente ativo (ex: `client.name`). |
| `workflows\research_niche.md:34` | `python tools/search_youtube.py` | Path | Alto | Lookup dinâmico de ferramentas. |
| `workflows\research_niche.md:42` | `python tools/search_web.py "<topic> nutrition" --max 10 --region br-pt` | Niche/Domain, Language/Region | Alto | "nutrition" deve vir de uma variável de nicho do cliente. "br-pt" deve ser uma configuração de idioma/região por cliente. |
| `workflows\research_niche.md:46` | `--region br-pt` | Language/Region | Alto | "br-pt" deve ser uma configuração de idioma/região por cliente. |
| `workflows\research_niche.md:50` | `python tools/search_pubmed.py` | Path | Alto | Lookup dinâmico de ferramentas. |
| `workflows\research_niche.md:51` | `"<topic in English>"` | Language | Alto | A sugestão de usar inglês deve ser parte de uma estratégia de internacionalização, não hardcoded. |
| `workflows\research_niche.md:55`, `56` | `"nutritionist <topic>"`, `"nutritionist <topic> program"` | Niche/Domain | Alto | "nutritionist" deve ser derivado do tipo de cliente/papel. |
| `workflows\research_niche.md:90` | `.tmp/research_[topic-slug]_[date].md` | Path | Alto | Caminho de output deve usar uma variável para o diretório temporário. |
| `workflows\research_niche.md:92` | `.tmp/research_intermittent-fasting_2025-04-01.md` | Path | Alto | Exemplo de caminho de output, deve ser dinâmico. |
| `workflows\research_niche.md:135` | `.tmp/fonts/` | Path | Alto | Caminho para fontes deve ser configurável, ou usar um gerenciador de fontes. (Duplicado de reels_com_ia.md) |
| `workflows\session_router.md:10` | `clients/mayara/client.json` | Path | Alto | Caminho dinâmico para `client.json` do cliente ativo, usando uma variável `CLIENT_SLUG`. |
| `workflows\session_router.md:11` | `gemini/briefs/` | Path | Alto | Caminho dinâmico para outputs da AI, usando variável de configuração `AI_OUTPUTS_DIR`. |
| `workflows\session_router.md:14` | `clients/mayara/context/memoria/` | Path | Alto | Caminho dinâmico para contexto de memória, usando `CLIENTS_BASE_PATH` e `CLIENT_SLUG`. |
| `workflows\session_router.md:32` | `python tools/call_gemini_api.py` | Path | Alto | Lookup dinâmico de ferramentas. |
| `workflows\session_router.md:35` | `gemini/[briefs|research|drafts|audits]/` | Path | Alto | Subdiretórios dos outputs da AI devem ser dinâmicos ou configuráveis (ex: `f"{AI_OUTPUTS_DIR}/{type}/"`). |
| `workflows\session_router.md:36` | `--model gemini-2.5-flash` | Modelo de IA | Alto | Modelo de IA deve ser configurável por tarefa ou cliente. |
| `workflows\session_router.md:38` | `gemini-2.5-flash-lite` | Modelo de IA | Alto | Modelo de IA deve ser configurável por tarefa ou cliente. |
| `workflows\session_router.md:41-44` | `gemini/briefs/`, `gemini/research/`, `gemini/drafts/`, `gemini/audits/` | Path | Alto | Caminhos para subdiretórios dos outputs da AI devem ser dinâmicos. |
| `workflows\session_router.md:50` | `python tools/generate_images_api.py prompts.json --output images/` | Path | Alto | Caminho da ferramenta e diretório de output de imagens devem ser dinâmicos. |
| `workflows\session_router.md:50`, `51`, `55`, `56` | `images/` | Path | Alto | Caminho para diretório de imagens deve ser configurável. |
| `workflows\session_router.md:54` | `python tools/generate_images_manus.py prompts.json --output images/ --remove-bg` | Path | Alto | Caminho da ferramenta e diretório de output de imagens devem ser dinâmicos. |
| `workflows\session_router.md:61`, `62` | `gemini/` | Path | Alto | Caminho base dos outputs da AI deve ser configurável. |
| `workflows\session_router.md:64` | `clients/mayara/projects/` | Path | Alto | Caminho dinâmico para `projects` do cliente ativo. |
| `workflows\session_router.md:68`, `69` | `gemini/` | Path | Alto | Caminho base dos outputs da AI deve ser configurável. |
| `workflows\session_router.md:70` | `gemini/drafts/` | Path | Alto | Caminho para subdiretório de drafts deve ser dinâmico. |
| `workflows\session_router.md:70` | `clients/mayara/projects/` | Path | Alto | Caminho dinâmico para `projects` do cliente ativo. |
| `workflows\youtube_workflow_recommender.md:10` | `tools/fetch_youtube_info.py` | Path | Alto | Lookup dinâmico de ferramentas. |
| `workflows\youtube_workflow_recommender.md:31`, `33` | `workflows/` | Path | Alto | Caminho base para workflows deve ser configurável. |
| `workflows\youtube_workflow_recommender.md:46` | `workflows/nome_do_workflow.md` | Path | Alto | Exemplo de caminho de workflow, deve ser dinâmico. |
| `workflows\youtube_workflow_recommender.md:55` | `workflows/nome.md` | Path | Alto | Exemplo de caminho de workflow, deve ser dinâmico. |
| `workflows\youtube_workflow_recommender.md:55` | `workflows/` | Path | Alto | Caminho base para workflows deve ser configurável. |
| `docs\claude_code_structured_dev.md:32` | `references/spec.md` | Path | Alto | Caminho para arquivos de referência deve ser configurável (ex: `REFERENCES_DIR`). |
| `docs\claude_code_structured_dev.md:48` | `@references/spec.md` | Path | Alto | Caminho para arquivos de referência deve ser configurável. |
| `docs\claude_code_structured_dev.md:50` | `tasks/` | Path | Alto | Caminho para tarefas deve ser configurável (ex: `TASKS_DIR`). |
| `docs\claude_code_structured_dev.md:67` | `@tasks/<nome-da-tarefa>.md` | Path | Alto | Caminho para tarefas deve ser configurável. |
| `docs\claude_code_structured_dev.md:104` | `@tasks/<nome-da-tarefa>.md` | Path | Alto | Caminho para tarefas deve ser configurável. |
| `docs\claude_code_structured_dev.md:118` | `references/` | Path | Alto | Caminho para arquivos de referência deve ser configurável. |
| `docs\claude_code_structured_dev.md:121`, `122`, `123` | `architecture.md`, `design-system.md`, `spec.md` | Path | Alto | Nomes de arquivos de referência devem ser configuráveis. |
| `docs\claude_code_structured_dev.md:125` | `architecture.md` | Path | Alto | Nome de arquivo de referência deve ser configurável. |
| `docs\claude_code_structured_dev.md:156` | `architecture.md` | Path | Alto | Nome de arquivo de referência deve ser configurável. |
| `docs\supabase-schema.md:1` | `WAT Studio` | Nome de Cliente | Alto | Substituir por uma variável global de nome do produto/estúdio. |
| `docs\supabase-schema.md:4` | `gemini/research/2026-04-04_pesquise-padrões-de-multi-tenant-com-sup.md` | Path | Alto | Caminho para arquivos de pesquisa deve ser dinâmico. |
| `docs\supabase-schema.md:8-18` | `clients/<slug>/client.json`, `auth.users`, `context/negocio/*.md`, `context/memoria/voz_marca.md`, `context/memoria/preferencias.md`, `context/memoria/historico_temas.md`, `context/pesquisas/*.md`, `gemini/briefs/*.md`, `gemini/drafts/*.md`, `gemini/research/*.md`, `gemini/audits/*.md` | Path | Alto | Mapeamentos de caminhos locais devem usar variáveis de ambiente para raízes (ex: `CLIENTS_BASE_PATH`, `AI_OUTPUTS_DIR`). |
| `docs\supabase-schema.md:19` | `projects/reels/`, `projects/prototipos/` | Path | Alto | Mapeamentos de caminhos locais devem usar variáveis de ambiente para raízes. |
| `docs\supabase-schema.md:30` | `public.tenants` | Nome de Tabela | Alto | Nome da tabela deve ser configurável ou o esquema deve ser passado como parâmetro. |
| `docs\supabase-schema.md:43`, `45`, `52`, `60`, `71`, `77`, `84`, `91`, `102`, `112` | `public.profiles`, `public.tenants(id)`, `public.context_business`, `public.brand_voice`, `public.preferences`, `public.topic_history`, `public.research_notes`, `public.ai_outputs`, `public.projects`, `public.files` | Nome de Tabela | Alto | Nomes de tabelas devem ser configuráveis (ex: via ORM ou variáveis de configuração). |
| `docs\supabase-schema.md:95` | `'gemini-2.5-flash'` | Modelo de IA | Alto | Modelo de IA deve ser configurável por tarefa ou cliente. |
| `docs\supabase-schema.md:115`, `204`, `212` | `'wat-studio'` | Nome de Bucket | Alto | Nome do bucket de storage deve ser uma variável de ambiente ou configuração. |
| `docs\supabase-schema.md:140` | `public.my_tenant_id()` | Função SQL | Alto | O nome da função helper deve ser configurável. |
| `docs\supabase-schema.md:231` | `wat-studio/` | Nome de Bucket | Alto | Nome do bucket de storage deve ser uma variável de ambiente ou configuração. |
| `docs\supabase-schema.md:232` | `<tenant_slug>/` | Path | Alto | Placeholder que deve ser substituído pelo slug dinamicamente. |
| `docs\supabase-schema.md:233-235` | `reels/<project_id>/<filename>`, `prototipos/<project_id>/<filename>`, `campanha/<project_id>/<filename>` | Path | Alto | Padrões de caminho para storage devem ser configuráveis. |
| `docs\wat-studio-frontend-design.md:1` | `WAT Studio` | Nome de Cliente | Alto | Substituir por uma variável global de nome do produto/estúdio. |
| `docs\wat-studio-frontend-design.md:8` | `Mayara Farias, nutricionista` | Cliente/Nicho | Alto | Exemplo de cliente específico. O design deve ser agnóstico. |
| `docs\wat-studio-frontend-design.md:22-24` | `Browser → FastAPI (server.py) → Claude Code CLI → tools/*.py` | Arquitetura/Path | Alto | O fluxo e os caminhos internos devem ser parametrizados por variáveis de ambiente ou configuração. |
| `docs\wat-studio-frontend-design.md:28-48` | `workflows/`, `tools/`, `CLAUDE.md`, `frontend/`, `server.py`, `static/`, `index.html`, `style.css`, `app.js`, `clients/`, `<slug>/`, `context/`, `negocio/`, `conteudo/`, `memoria/`, `projects/`, `.env`, `client.json`, `docs/` | Path | Alto | A estrutura de diretórios deve ser parametrizada via variáveis de ambiente/configuração. |
| `docs\wat-studio-frontend-design.md:52` | `"Mayara Farias"` | Nome de Cliente | Alto | Exemplo de nome de cliente. O frontend deve carregar isso dinamicamente. |
| `docs\wat-studio-frontend-design.md:53` | `"mayara"` | Slug de Cliente | Alto | Exemplo de slug de cliente. O frontend deve carregar isso dinamicamente. |
| `docs\wat-studio-frontend-design.md:54` | `"nutrição"` | Niche/Domain | Alto | Exemplo de nicho. O frontend deve carregar isso dinamicamente. |
| `docs\wat-studio-frontend-design.md:55` | `"pesquisa", "youtube", "imagem", "landing_page"` | Nomes de Workflows | Alto | Lista de workflows deve ser carregada dinamicamente do `client.json` (já descrito). |
| `docs\wat-studio-frontend-design.md:56` | `"clients/mayara/context"` | Path | Alto | Exemplo de caminho de contexto. Deve ser dinâmico. |
| `docs\wat-studio-frontend-design.md:57` | `"clients/mayara/context/memoria"` | Path | Alto | Exemplo de caminho de memória. Deve ser dinâmico. |
| `docs\wat-studio-frontend-design.md:63-67` | `/client`, `/run`, `/history`, `/context`, `/memory/save` | Endpoint | Alto | Endpoints da API devem ser configuráveis via variáveis de ambiente/config. |
| `docs\wat-studio-frontend-design.md:65` | `.tmp/` | Path | Alto | Caminho para arquivos temporários. Deve ser configurável. |
| `docs\wat-studio-frontend-design.md:96` | `clients/<slug>/context/memoria/` | Path | Alto | Caminho para arquivos de memória. Deve ser configurável. |
| `docs\wat-studio-frontend-design.md:99-102` | `preferencias.md`, `historico_temas.md`, `voz_marca.md`, `notas_sessao.md` | Nomes de Arquivos | Alto | Nomes de arquivos de memória devem ser configuráveis ou descobertos dinamicamente. |
| `docs\wat-studio-frontend-design.md:108` | `client.json` | Path | Alto | O arquivo de configuração do cliente deve ser dinâmico. |
| `clients\mayara\client.json:2` | `"Mayara Farias"` | Nome de Cliente | Alto | Deve ser gerenciado via banco de dados ou painel administrativo para multi-tenancy. |
| `clients\mayara\client.json:3` | `"mayara"` | Slug de Cliente | Alto | Deve ser gerenciado via banco de dados ou painel administrativo para multi-tenancy. |
| `clients\mayara\client.json:4` | `"nutrição"` | Niche/Domain | Alto | Deve ser gerenciado via banco de dados ou painel administrativo para multi-tenancy. |
| `clients\mayara\client.json:6-10` | `"pesquisa"`, `"youtube"`, `"imagem"`, `"landing_page"`, `"reels"` | Nomes de Workflows | Alto | A lista de workflows ativos deve ser gerenciada via banco de dados ou painel administrativo. |
| `clients\mayara\client.json:11` | `"clients/mayara/context"` | Path | Alto | O caminho base dos clientes (`clients/`) e o slug (`mayara/`) devem ser variáveis. |
| `clients\mayara\client.json:12` | `"clients/mayara/context/memoria"` | Path | Alto | O caminho base dos clientes (`clients/`) e o slug (`mayara/`) devem ser variáveis. |
| `CLAUDE.md:9`, `11`, `27` | `workflows/`, `tools/` | Path | Alto | Caminhos base para workflows e tools devem ser configuráveis via variáveis de ambiente. |
| `CLAUDE.md:20` | `workflows/scrape_website.md` | Path | Alto | Exemplo de workflow, o nome deve ser dinâmico. |
| `CLAUDE.md:20` | `tools/scrape_single_site.py` | Path | Alto | Exemplo de ferramenta, o nome deve ser dinâmico. |
| `CLAUDE.md:28` | `.env` | Credencial | Alto | Já é um padrão, mas a referência explícita é um hardcode do nome do arquivo de credenciais. A parametrização deve ser via mecanismos de variáveis de ambiente. |
| `CLAUDE.md:46`, `73` | `.tmp/` | Path | Alto | Diretório temporário deve ser configurável via variável de ambiente (`TMP_DIR`). |
| `CLAUDE.md:47` | `tools/` | Path | Alto | Caminho base para ferramentas deve ser configurável. |
| `CLAUDE.md:48` | `workflows/` | Path | Alto | Caminho base para workflows deve ser configurável. |
| `CLAUDE.md:49` | `frontend/` | Path | Alto | Caminho base para frontend deve ser configurável. |
| `CLAUDE.md:50` | `server.py` | Path | Alto | Nome do arquivo do servidor frontend deve ser configurável. |
| `CLAUDE.md:51` | `static/` | Path | Alto | Caminho para assets estáticos deve ser configurável. |
| `CLAUDE.md:53` | `clients/` | Path | Alto | Caminho base para clientes deve ser configurável. |
| `CLAUDE.md:54` | `<slug>/` | Path | Alto | Placeholder para o slug do cliente. |
| `CLAUDE.md:55-60` | `context/`, `negocio/`, `conteudo/`, `pesquisas/`, `memoria/`, `projects/` | Path | Alto | Subdiretórios de cliente devem ser configuráveis. |
| `CLAUDE.md:61` | `client.json` | Path | Alto | Nome do arquivo de configuração do cliente deve ser configurável. |
| `CLAUDE.md:62` | `.env` | Credencial | Alto | Já é um padrão, mas a referência explícita é um hardcode do nome do arquivo de credenciais. A parametrização deve ser via mecanismos de variáveis de ambiente. |
| `CLAUDE.md:63` | `docs/` | Path | Alto | Caminho base para documentação deve ser configurável. |
| `CLAUDE.md:64` | `gemini/` | Path | Alto | Caminho base para outputs da AI deve ser configurável. |
| `CLAUDE.md:65` | `credentials.json`, `token.json` | Arquivo de Credencial | Alto | Nomes de arquivos de credenciais Google OAuth devem ser configuráveis. |
| `CLAUDE.md:70` | `~/.claude/` | Path | Alto | Caminho de infraestrutura do Claude Agent deve ser configurável (ex: `CLAUDE_HOME`). |
| `CLAUDE.md:72` | `client.json` | Path | Alto | Nome do arquivo de configuração do cliente deve ser configurável. |
| `CLAUDE.md:79` | `workflows/session_router.md` | Path | Alto | O caminho do workflow do router deve ser configurável. |
| `CLAUDE.md:80` | `clients/<slug>/client.json` | Path | Alto | Caminho dinâmico para `client.json`. |
| `CLAUDE.md:81` | `gemini/briefs/` | Path | Alto | Caminho dinâmico para outputs da AI. |
| `CLAUDE.md:82` | `clients/<slug>/context/memoria/` | Path | Alto | Caminho dinâmico para contexto de memória. |
| `start.bat:2` | `python frontend\server.py` | Path | Alto | O caminho para o servidor deve ser configurável (ex: variável `FRONTEND_SERVER_PATH`). |
| `start.bat:3` | `http://127.0.0.1:8000` | URL | Alto | O endereço e porta do servidor local devem ser configuráveis via variáveis de ambiente. |

### 2. Riscos MÉDIOS (Hardcodes que DEVEM ser parametrizados para flexibilidade e expansão, mas não quebram multi-tenancy imediatamente)

| Arquivo e Linha | Valor Hardcoded | Categoria | Risco | Como Parametrizar |
|---|---|---|---|---|
| `workflows\image_generation_pipeline.md:4` | `Nano Banana / Gemini` | Modelo de IA | Médio | Variável de configuração para o provedor de geração de imagens (ex: `IMAGE_GENERATION_PROVIDER`). |
| `workflows\image_generation_pipeline.md:15`, `39` | `Nano Banana Flow` | Nome de Cliente/Ferramenta | Médio | Tornar configurável se o nome da ferramenta manual pode mudar ou se outras ferramentas manuais forem adicionadas. |
| `workflows\image_generation_pipeline.md:23`, `31` | `Gemini API` | Modelo de IA | Médio | Variável de configuração para a API específica. |
| `workflows\image_generation_pipeline.md:26`, `32` | `Manus` | Modelo de IA | Médio | Variável de configuração para a API específica. |
| `workflows\image_generation_pipeline.md:47` | `5 images` | Limite Numérico | Médio | Variável de configuração (ex: `HIGH_VOLUME_THRESHOLD`). |
| `workflows\image_generation_pipeline.md:89` | `remove.bg` | URL/Ferramenta | Médio | Variável de configuração para o endpoint da API ou nome da ferramenta de remoção de fundo. |
| `workflows\landing_page_builder.md:42` | `https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js` | URL | Médio | As URLs de CDN devem ser configuráveis via variáveis de ambiente ou gerenciadas por um gerenciador de pacotes. |
| `workflows\landing_page_builder.md:43` | `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js` | URL | Médio | As URLs de CDN devem ser configuráveis via variáveis de ambiente ou gerenciadas por um gerenciador de pacotes. |
| `workflows\landing_page_builder.md:44` | `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js` | URL | Médio | As URLs de CDN devem ser configuráveis via variáveis de ambiente ou gerenciadas por um gerenciador de pacotes. |
| `workflows\landing_page_builder.md:54` | `data-animate`, `data-scroll` | Configuração/Atributos | Médio | Nomes de atributos HTML para animação devem ser configuráveis. |
| `workflows\landing_page_builder.md:60` | `duration: 800` | Limite Numérico | Médio | Duração da animação deve ser configurável. |
| `workflows\landing_page_builder.md:61` | `delay: anime.stagger(100)` | Limite Numérico | Médio | Atraso da animação deve ser configurável. |
| `workflows\landing_page_builder.md:62` | `easeOutExpo` | Configuração | Médio | Função de easing da animação deve ser configurável. |
| `workflows\landing_page_builder.md:67` | `.horizontal-track`, `.horizontal-section` | Configuração/Seletores | Médio | Nomes de seletores CSS devem ser configuráveis. |
| `workflows\landing_page_builder.md:68` | `x: () => -(document.querySelector(".horizontal-track").scrollWidth - window.innerWidth)` | Configuração/Lógica | Médio | Lógica específica de animação deve ser parametrizada se houver variações. |
| `workflows\landing_page_builder.md:71` | `pin: true` | Configuração | Médio | Opção de plugin GSAP deve ser configurável. |
| `workflows\landing_page_builder.md:72` | `scrub: 1` | Configuração | Médio | Opção de plugin GSAP deve ser configurável. |
| `workflows\landing_page_builder.md:80` | `.magnetic` | Configuração/Seletores | Médio | Nome do seletor CSS deve ser configurável. |
| `workflows\landing_page_builder.md:84` | `x * 0.3}px, ${y * 0.3}px` | Limite Numérico | Médio | Intensidade do efeito magnético deve ser configurável. |
| `workflows\reels_com_ia.md:4` | `Instagram/TikTok` | Plataforma | Médio | Plataformas alvo devem ser configuráveis. |
| `workflows\reels_com_ia.md:4`, `25` | `CapCut` | Nome de Ferramenta | Médio | Nome da ferramenta externa deve ser configurável. |
| `workflows\reels_com_ia.md:45` | `5s` | Limite Numérico | Médio | Padding de segurança para reel deve ser configurável. |
| `workflows\reels_com_ia.md:56` | `"content_offset": 5.0` | Limite Numérico | Médio | Offset de conteúdo padrão deve ser configurável. |
| `workflows\reels_com_ia.md:58-60` | `"w": 480, "h": 854, "x": 720, "y": 113` | Limite Numérico | Médio | Valores padrão de crop devem ser configuráveis. |
| `workflows\reels_com_ia.md:67`, `74` | `"type": "ctx"`, `"type": "kw"` | Configuração | Médio | Tipos de texto devem ser configuráveis (ex: lista de tipos permitidos). |
| `workflows\reels_com_ia.md:69`, `76` | `"white"`, `"#FF4422"` | Configuração | Médio | Cores padrão de texto devem ser configuráveis (ex: sistema de cores por tema). |
| `workflows\reels_com_ia.md:70`, `77` | `"y": 1555`, `"y": 1610` | Limite Numérico | Médio | Posição Y padrão para texto deve ser configurável. |
| `workflows\reels_com_ia.md:79` | `"size": 82` | Limite Numérico | Médio | Tamanho de fonte padrão deve ser configurável. |
| `workflows\reels_com_ia.md:88` | `"O vídeo tem 5s de margem no início e no fim. Abra no CapCut, apare onde quiser, adicione música trending e publique."` | Idioma | Médio | Deve ser internacionalizado se o sistema for usado em outros idiomas. |
| `workflows\reels_com_ia.md:108-110` | `1480–1520`, `1555–1650`, `1660–1750` | Limite Numérico | Médio | Zonas Y de texto devem ser configuráveis (ex: `TEXT_Y_ZONE_BOTTOM_SAFE`, `TEXT_Y_ZONE_KEYWORD`). |
| `workflows\reels_com_ia.md:115` | `Bebas Neue` | Fonte | Médio | Nome da fonte deve ser configurável (ex: sistema de tipografia). |
| `workflows\reels_com_ia.md:115` | `size 80–96` | Limite Numérico | Médio | Faixa de tamanho da fonte deve ser configurável. |
| `workflows\reels_com_ia.md:116` | `Montserrat Regular` | Fonte | Médio | Nome da fonte deve ser configurável (ex: sistema de tipografia). |
| `workflows\reels_com_ia.md:116` | `size 38–42` | Limite Numérico | Médio | Faixa de tamanho da fonte deve ser configurável. |
| `workflows\reels_com_ia.md:120` | `white` | Configuração | Médio | Cor padrão deve ser configurável. |
| `workflows\reels_com_ia.md:124-128` | `#FF4422`, `#C47A1E`, `#FF8800`, `#44CCFF`, `#FFE033` | Configuração | Médio | Cores hex devem ser configuráveis por tema ou cliente (ex: paleta de cores). |
| `workflows\reels_com_ia.md:170` | `1080x1920` | Limite Numérico | Médio | Resolução do vídeo vertical deve ser configurável. |
| `workflows\research_niche.md:19` | `8.000 caracteres` | Limite Numérico | Médio | Limite de caracteres para transcrição deve ser configurável. |
| `workflows\research_niche.md:35` | `--max 8` | Limite Numérico | Médio | Número máximo de resultados de busca deve ser configurável. |
| `workflows\research_niche.md:38` | `--max 5` | Limite Numérico | Médio | Número máximo de resultados de busca deve ser configurável. |
| `workflows\research_niche.md:42`, `46`, `51`, `55`, `56`, `60`, `61`, `66-69` | `--max 10`, `--max 8`, `--max 6`, `--max 5` | Limite Numérico | Médio | Números máximos de resultados de busca devem ser configuráveis. |
| `workflows\research_niche.md:46` | `--type news` | Configuração | Médio | Tipo de busca deve ser configurável. |
| `workflows\research_niche.md:51` | `--years 3` | Limite Numérico | Médio | Filtro de anos para PubMed deve ser configurável. |
| `workflows\research_niche.md:60`, `61` | `2025` | Ano | Médio | Ano hardcoded para pesquisa de tendências. Deve ser dinâmico ou configurável. |
| `workflows\research_niche.md:66-69` | `sbcbm.org.br`, `cfn.org.br`, `examine.com`, `healthline.com` | URL | Médio | Lista de sites especializados deve ser configurável. |
| `workflows\session_router.md:19-28` | `Gemini`, `Claude`, `Manus` | Modelo de IA | Médio | Nomes de modelos de IA devem ser configuráveis, por cliente ou tarefa. |
| `workflows\session_router.md:38` | `10 variações` | Limite Numérico | Médio | Limite para usar modelo 'lite' deve ser configurável. |
| `workflows\session_router.md:78` | `2 dias` | Limite Numérico | Médio | Validade do brief deve ser configurável. |
| `workflows\session_router.md:82` | `2 tentativas` | Limite Numérico | Médio | Número máximo de tentativas de redispatch deve ser configurável. |
| `workflows\youtube_workflow_recommender.md:19` | `8.000 caracteres` | Limite Numérico | Médio | Limite de caracteres para transcrição deve ser configurável. |
| `docs\claude_code_structured_dev.md:27`, `30` | `/spec` | Comando | Médio | Comandos do Claude Code devem ser configuráveis (ex: mapeados em uma config). |
| `docs\claude_code_structured_dev.md:45`, `48` | `/break` | Comando | Médio | Comandos do Claude Code devem ser configuráveis. |
| `docs\claude_code_structured_dev.md:64`, `67` | `/plan` | Comando | Médio | Comandos do Claude Code devem ser configuráveis. |
| `docs\claude_code_structured_dev.md:101`, `104` | `/execute` | Comando | Médio | Comandos do Claude Code devem ser configuráveis. |
| `docs\claude_code_structured_dev.md:150-153` | `/break`, `/plan`, `/execute` | Comando | Médio | Comandos do Claude Code devem ser configuráveis. |
| `docs\supabase-schema.md:34` | `'pilot'` | Configuração | Médio | Valor padrão para `plan` deve ser configurável (ex: `DEFAULT_TENANT_PLAN`). |
| `docs\supabase-schema.md:34` | `'pilot', 'starter', 'pro'` | Configuração | Médio | Lista de planos disponíveis deve ser configurável. |
| `docs\supabase-schema.md:47` | `'owner'` | Configuração | Médio | Valor padrão para `role` deve ser configurável (ex: `DEFAULT_PROFILE_ROLE`). |
| `docs\supabase-schema.md:47` | `'owner', 'member', 'admin'` | Configuração | Médio | Lista de roles disponíveis deve ser configurável. |
| `docs\supabase-schema.md:94` | `'brief','draft','research','audit'` | Configuração | Médio | Lista de tipos de AI output deve ser configurável. |
| `docs\supabase-schema.md:105` | `'reel','prototipo','landing_page','campanha','outro'` | Configuração | Médio | Lista de tipos de projeto deve ser configurável. |
| `docs\supabase-schema.md:106` | `'draft'` | Configuração | Médio | Valor padrão para `status` deve ser configurável (ex: `DEFAULT_PROJECT_STATUS`). |
| `docs\supabase-schema.md:106` | `'draft','review','approved','published'` | Configuração | Médio | Lista de status de projeto deve ser configurável. |
| `docs\wat-studio-frontend-design.md:113` | `#0A1810`, `#C9A96E`, `#6FA880` | Configuração | Médio | Cores CSS devem ser parte de um design system parametrizável. |
| `docs\wat-studio-frontend-design.md:114` | `Cormorant Garamond`, `DM Sans` | Configuração | Médio | Nomes de fontes devem ser parte de um design system parametrizável. |

### 3. Riscos BAIXOS (Hardcodes informativos, exemplos, ou de menor impacto para multi-tenancy/configuração)

| Arquivo e Linha | Valor Hardcoded | Categoria | Risco | Como Parametrizar |
|---|---|---|---|---|
| `workflows\image_generation_pipeline.md:23` | `Claude Code` | Nome de Cliente | Baixo | Referência ao orquestrador, pode ser uma variável global. |
| `workflows\image_generation_pipeline.md:95` | `Mateus Dias` | Nome | Baixo | Referência informativa. |
| `workflows\image_generation_pipeline.md:95` | `CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000` | Informativo | Baixo | Conteúdo informativo. |
| `workflows\image_generation_pipeline.md:96` | `PNG` | Formato de Arquivo | Baixo | Formato de arquivo, geralmente ditado pela ferramenta. |
| `workflows\landing_page_builder.md:4` | `Claude Code` | Nome de Cliente | Baixo | Referência ao orquestrador, pode ser uma variável global. |
| `workflows\landing_page_builder.md:4`, `16`, `17` | `Anime.js` | Nome de Ferramenta | Baixo | Pode ser parte de uma lista de bibliotecas de frontend configuráveis. |
| `workflows\landing_page_builder.md:4`, `16`, `17` | `GSAP` | Nome de Ferramenta | Baixo | Pode ser parte de uma lista de bibliotecas de frontend configuráveis. |
| `workflows\landing_page_builder.md:109` | `gsap.registerPlugin(ScrollTrigger)` | Configuração | Baixo | Chamada de biblioteca necessária, baixo risco. |
| `workflows\landing_page_builder.md:110` | `'ontouchstart' in window` | Configuração | Baixo | Verificação padrão para dispositivos touch, baixo risco. |
| `workflows\landing_page_builder.md:121` | `Mateus Dias` | Nome | Baixo | Referência informativa. |
| `workflows\landing_page_builder.md:121` | `CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000` | Informativo | Baixo | Conteúdo informativo. |
| `workflows\reels_com_ia.md:14` | `"alimentos que causam azia na gestação"` | Nicho/Domínio | Baixo | Exemplo de conteúdo, não crítico. |
| `workflows\reels_com_ia.md:15` | `"a parte onde ela lista os alimentos"` | Nicho/Domínio | Baixo | Exemplo de conteúdo, não crítico. |
| `workflows\reels_com_ia.md:54` | `"start_sec": 78.5` | Limite Numérico | Baixo | Exemplo de valor. |
| `workflows\reels_com_ia.md:55` | `"duration": 46` | Limite Numérico | Baixo | Exemplo de valor. |
| `workflows\reels_com_ia.md:62-64` | `[11.5, 16.0]`, `[23.0, 29.5]`, `[30.0, 40.5]` | Limite Numérico | Baixo | Exemplos de pulsos de zoom. |
| `workflows\reels_com_ia.md:75` | `"MOLHO DE TOMATE"` | Nicho/Domínio | Baixo | Exemplo de texto. |
| `workflows\reels_com_ia.md:94-96` | `1.78x`, `2.25x`, `2.84x` | Limite Numérico | Baixo | Exemplos de fatores de zoom. |
| `workflows\reels_com_ia.md:99` | `x = (1920 - w) / 2`, `y = (1080 - h) / 2` | Limite Numérico | Baixo | Fórmula de cálculo. |
| `workflows\reels_com_ia.md:99` | `1920`, `1080` | Limite Numérico | Baixo | Dimensões de vídeo constantes (full HD). |
| `workflows\reels_com_ia.md:133` | `"a diferenca"` | Idioma | Baixo | Exemplo de workaround para caracteres especiais. |
| `workflows\reels_com_ia.md:137` | `--format best` ou `--format mp4` | Configuração | Baixo | Opções de fallback, baixo risco. |
| `workflows\reels_com_ia.md:149-154` | `2026-04-02` | Data | Baixo | Datas de logs históricos. |
| `workflows\research_niche.md:3` | `YouTube`, `web`, `news`, `scientific studies` | Tipos de Fonte | Baixo | Lista de fontes, poderia ser configurável se houver muitas variações. |
| `workflows\research_niche.md:20` | `~30 seconds` | Limite Numérico | Baixo | Estimativa de tempo. |
| `workflows\research_niche.md:21` | `~2-3 minutes` | Limite Numérico | Baixo | Estimativa de tempo. |
| `workflows\research_niche.md:129` | `yt-dlp not found`, `pip install yt-dlp` | Erro/Comando | Baixo | Mensagem de erro e comando de instalação. |
| `workflows\research_niche.md:130` | `duckduckgo-search not installed`, `pip install duckduckgo-search` | Erro/Comando | Baixo | Mensagem de erro e comando de instalação. |
| `workflows\research_niche.md:136` | `"intermittent fasting women"`, `"jejum intermitente mulheres"` | Idioma/Nicho | Baixo | Exemplos de termos de pesquisa. |
| `workflows\research_niche.md:137` | `10-20s` | Limite Numérico | Baixo | Estimativa de tempo. |
| `workflows\research_niche.md:138` | `1-2 minutes` | Limite Numérico | Baixo | Estimativa de tempo. |
| `docs\architecture.md:9` | `src/` | Path | Baixo | Exemplo de diretório raiz. |
| `docs\architecture.md:10-18` | `pages/`, `<page-name>/`, `<behavior-name>/`, `index.tsx`, `hooks.ts`, `types.ts`, `components/`, `lib/`, `server/` | Path | Baixo | Componentes da estrutura de pastas de exemplo. |
| `docs\architecture.md:80` | `Button` | Nome de Componente | Baixo | Exemplo de nome de componente. |
| `docs\claude_code_structured_dev.md:4` | `4 etapas` | Limite Numérico | Baixo | Número de etapas. |
| `docs\claude_code_structured_dev.md:6` | `Deborah Folloni`, `Vibe Coding não funciona – Novo Workflow no Claude Code` | Nome/Informativo | Baixo | Referências informativas. |
| `docs\claude_code_structured_dev.md:79` | `Button` | Nome de Componente | Baixo | Exemplo de nome de componente. |
| `docs\supabase-schema.md:3` | `2026-04-04` | Data | Baixo | Data de geração. |
| `docs\supabase-schema.md:32` | `'mayara'`, `'joao'` | Cliente | Baixo | Exemplos de slugs de tenant. |
| `docs\supabase-schema.md:33` | `'nutrição'`, `'fisioterapia'` | Nicho/Domínio | Baixo | Exemplos de nichos. |
| `docs\supabase-schema.md:35` | `'{}'` | Configuração | Baixo | Default array vazio. |
| `docs\supabase-schema.md:36` | `TRUE` | Configuração | Baixo | Default boolean. |
| `docs\supabase-schema.md:37`, `38`, `48` | `NOW()` | Configuração | Baixo | Função SQL. |
| `docs\supabase-schema.md:55` | `'aquisicao', 'conversao', 'escalabilidade'` | Nicho/Domínio | Baixo | Exemplos de tópicos de negócio. |
| `docs\supabase-schema.md:63` | `1` | Limite Numérico | Baixo | Default version. |
| `docs\supabase-schema.md:65` | `0.0` | Limite Numérico | Baixo | Default confidence. |
| `docs\supabase-schema.md:97` | `CURRENT_DATE` | Configuração | Baixo | Função SQL. |
| `docs\supabase-schema.md:116` | `'mayara/reels/azia/v5.mp4'` | Path | Baixo | Exemplo de caminho de arquivo. |
| `docs\supabase-schema.md:126` | `ALTER TABLE public.tenants ENABLE ROW LEVEL SECURITY;` | Configuração | Baixo | Comandos SQL de segurança padrão. |
| `docs\supabase-schema.md:141`, `147` | `auth.uid()` | Função SQL | Baixo | Função interna do Supabase. |
| `docs\supabase-schema.md:145` | `CREATE POLICY "profiles_self"` | Nome de Política | Baixo | Nomes de políticas SQL. |
| `docs\supabase-schema.md:146` | `authenticated` | Role | Baixo | Role SQL. |
| `docs\supabase-schema.md:221` | `idx_context_business_tenant` | Nome de Índice | Baixo | Nomes de índices SQL. |
| `docs\wat-studio-frontend-design.md:2` | `2026-04-02` | Data | Baixo | Data de geração. |
| `docs\wat-studio-frontend-design.md:16` | `FastAPI`, `Python` | Nome de Ferramenta/Linguagem | Baixo | Nomes de tecnologias. |
| `docs\wat-studio-frontend-design.md:17` | `HTML + CSS + JS puro` | Tecnologias | Baixo | Nomes de tecnologias. |
| `docs\wat-studio-frontend-design.md:18` | `Claude Code CLI` | Nome de Ferramenta | Baixo | Nome da ferramenta. |
| `docs\wat-studio-frontend-design.md:19` | `EventSource` | Tecnologia | Baixo | Nome da tecnologia. |
| `docs\wat-studio-frontend-design.md:25` | `SSE streaming` | Tecnologia | Baixo | Nome da tecnologia. |
| `docs\wat-studio-frontend-design.md:71` | `3 zonas fixas` | Limite Numérico | Baixo | Número de zonas de UI. |
| `docs\wat-studio-frontend-design.md:86` | `3 passos` | Limite Numérico | Baixo | Número de passos do wizard. |
| `docs\wat-studio-frontend-design.md:119` | `v1` | Versão | Baixo | Tag de versão. |
| `CLAUDE.md:1` | `WAT framework` | Nome de Framework | Baixo | Nome do framework. |
| `CLAUDE.md:43` | `Google Sheets, Slides` | Nomes de Ferramentas | Baixo | Exemplos de serviços em nuvem. |
| `CLAUDE.md:68` | `superpowers/`, `gsd/`, `claude/` | Path | Baixo | Exemplos de nomes de pastas proibidas. |
| `requirements.txt:1-7` | `yt-dlp`, `ffmpeg-python`, `google-generativeai`, `duckduckgo-search`, `fastapi`, `uvicorn`, `python-dotenv` | Nome de Pacote | Baixo | Dependências do projeto. |
| `.gitignore:1-9` | `*.log`, `*.tmp`, `!.tmp/.gitkeep`, `__pycache__/`, `venv/`, `/.env`, `/credentials.json`, `/token.json`, `output.json` | Padrões de Arquivo/Pasta | Baixo | Entradas padrão do `.gitignore`. |
| `start.bat:4` | `start chrome http://127.0.0.1:8000` | Navegador | Baixo | Iniciar o Chrome é uma preferência de dev, pode ser parametrizado mas é baixo risco. |

---

<brief>
TAREFA: Auditoria completa de valores hardcoded em todos os arquivos do projeto.
ARQUIVOS LIDOS: 15 arquivos (workflows/*.md, frontend/*, docs/*.md, docs/*.html, clients/mayara/client.json, CLAUDE.md, .gitignore, requirements.txt, start.bat).
RESUMO: Foram identificadas 305 ocorrências de valores hardcoded. Destes, 126 foram classificados como ALTO risco, 92 como MÉDIO risco e 87 como BAIXO risco, para um cenário multi-tenant/multi-domínio. Os riscos altos incluem caminhos de arquivos/pastas, nomes de modelos de IA, credenciais e configurações específicas de cliente.
PRÓXIMO PASSO PARA O CLAUDE: Analisar este relatório e priorizar a parametrização dos itens de ALTO risco, começando pelos caminhos de arquivos/pastas e configurações de cliente, preferencialmente usando variáveis de ambiente ou arquivos de configuração centralizados.
</brief>