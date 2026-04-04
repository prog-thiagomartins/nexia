Aqui está o inventário completo do projeto Mayara, conforme sua solicitação:

## INVENTÁRIO DO PROJETO MAYARA

### Workflows

*   **Image Generation Pipeline**: Gera imagens (ilustrações, banners, assets) para landing pages e websites, com seleção automatizada da rota (Flow, Direct API, Manus) baseada em custo, contexto e qualidade.
*   **Landing Page Builder**: Cria landing pages animadas de alto valor comercial usando Claude Code como orquestrador, com Anime.js e GSAP para animações.
*   **Reels com IA — Reel Vertical a partir de Vídeo Existente**: Transforma vídeos horizontais em reels verticais otimizados para Instagram/TikTok, com textos de impacto, zoom dinâmico e entrega pronta para ajuste final no CapCut.
*   **Niche Research — Mayara Farias (Nutrition)**: Conduz pesquisa multi-fontes (YouTube, web, notícias, estudos científicos) sobre um tópico no nicho de nutrição feminina e gera um relatório consolidado.
*   **Session Router (Master)**: O primeiro workflow a ser lido em qualquer sessão, que define quem executa o quê (Gemini ou Claude) e como despachar cada tipo de tarefa.
*   **YouTube → Workflow Recommender**: Analisa um vídeo do YouTube e recomenda workflows relevantes (existentes ou novos) com base no conteúdo apresentado.

### Tools

*   `tools/generate_images_api.py`: Chama a API Gemini diretamente para gerar imagens.
*   `tools/generate_images_manus.py`: Envia tarefas para Manus para gerar imagens e entregá-las com o fundo já removido.
*   `tools/fetch_youtube_info.py`: Extrai título, canal e transcrição com timestamps de um vídeo do YouTube.
*   `tools/create_reel.py`: Gera reels verticais via ffmpeg, aplicando crop, zoom dinâmico e textos.
*   `yt-dlp`: Baixa vídeos do YouTube.
*   `ffmpeg`: Processa e manipula arquivos de vídeo.
*   `CapCut`: (Ferramenta do Usuário) Usado para ajustes manuais finais (aparar, adicionar música) nos reels gerados.
*   Claude Code: O principal orquestrador do projeto, conectando a intenção às execuções das tarefas.
*   `Anime.js`: Biblioteca JavaScript para animações de entrada, contadores e efeitos de texto em páginas web.
*   `GSAP`: Biblioteca JavaScript para animações avançadas como scroll horizontal, efeitos de mouse magnético e parallax em páginas web.
*   `tools/search_youtube.py`: Realiza buscas no YouTube, obtendo metadados de vídeos e, opcionalmente, transcrições.
*   `tools/search_web.py`: Realiza buscas gerais na web (artigos, blogs) e de notícias.
*   `tools/search_pubmed.py`: Busca estudos científicos no PubMed.
*   `tools/call_gemini_api.py`: Despacha tarefas (leitura de contexto, pesquisa, geração de conteúdo, auditoria de voz) para a API Gemini.

### Resumo do CLAUDE.md

O `CLAUDE.md` descreve a arquitetura WAT (Workflows, Agents, Tools), onde Claude (o Agente) orquestra tarefas lendo workflows em Markdown e executando scripts Python. O documento enfatiza a separação entre raciocínio da IA e execução determinística para garantir a confiabilidade, detalha como operar (priorizando ferramentas existentes, aprendendo com falhas, mantendo workflows atualizados), define um ciclo de autoaperfeiçoamento para tratamento de erros, especifica a estrutura de arquivos do projeto e estabelece um protocolo de sessão para carregar contexto do cliente e atualizar a memória.

### Padrões de Comportamento Recorrentes

1.  **Adesão à Arquitetura WAT**: Forte ênfase na separação entre o raciocínio da IA (Claude) e a execução determinística (Ferramentas/scripts Python) através de Workflows bem definidos para garantir confiabilidade e escalabilidade.
2.  **Abordagem Cliente-Centrada**: O sistema é projetado em torno de clientes específicos (ex: Mayara), com pastas dedicadas para contexto, projetos e preferências (`clients/<slug>/`).
3.  **Orquestração e Delegação**: Claude atua primariamente como orquestrador, delegando subtarefas específicas a modelos de IA especializados (Gemini, Manus) ou a scripts determinísticos (ferramentas Python, `ffmpeg`, `yt-dlp`).
4.  **Priorização de Ferramentas Existentes**: Instrução clara para sempre buscar e utilizar ferramentas existentes antes de criar novas.
5.  **Ciclo de Autoaperfeiçoamento**: Um processo definido para aprender com falhas (identificar, corrigir, verificar, atualizar workflow) para aprimorar continuamente o sistema.
6.  **Protocolo de Carregamento de Contexto**: Uma sequência padronizada para carregar o contexto no início de cada sessão, começando pelo `session_router.md`.
7.  **Confirmação de Serviços Pagos**: Instrução explícita para sempre confirmar com o usuário antes de acionar qualquer rota paga (ex: API de Geração de Imagens, Manus, pesquisas de alto custo).
8.  **Localização e Descarte de Outputs**: Distinção clara entre arquivos temporários descartáveis (`.tmp/`) e entregáveis finais persistentes para o cliente (`clients/<slug>/projects/` ou serviços em nuvem), com outputs do Gemini restritos à pasta `gemini/`.
9.  **Ajustes Finais Manuais pelo Usuário**: Vários workflows (ex: `reels_com_ia.md`) geram outputs "prontos para ajuste final" pelo usuário em softwares específicos (CapCut), reconhecendo o valor do toque humano em processos criativos (ex: padding de 5s).
10. **Desenvolvimento Mobile-First**: No `landing_page_builder.md`, há uma regra explícita de garantir que a página funcione bem em dispositivos móveis antes de aplicar qualquer animação.
11. **Especificação de Idioma para Ferramentas**: Reconhecimento de que algumas ferramentas (ex: pesquisa no PubMed) retornam melhores resultados com termos em inglês.
12. **Tratamento Cauteloso de Caracteres Especiais/Caminhos**: Preocupação recorrente com caracteres especiais (`:`, `ç`, `ã`) e caminhos com espaços que podem quebrar comandos `ffmpeg`, indicando a necessidade de sanitização de entradas ou considerações ambientais robustas.

<brief>
TAREFA: Inventariar workflows, tools, CLAUDE.md e padrões de comportamento do projeto Mayara.
ARQUIVOS LIDOS: 10 arquivos (6 workflows, CLAUDE.md, 3 arquivos de memória do cliente).
RESUMO: O inventário detalha 6 workflows, 14 ferramentas (incluindo as de usuário e bibliotecas), um resumo conciso das instruções para o Claude, e 12 padrões de comportamento recorrentes, como a adesão à arquitetura WAT e o foco no cliente.
PRÓXIMO PASSO PARA O CLAUDE: Utilizar este inventário como base de conhecimento para futuras interações e execuções de tarefas no projeto Mayara.
</brief>