## Mapa Completo do Projeto Mayara

### 1. Visão Geral do Projeto

*   **Cliente:** Mayara Farias, Nutricionista
*   **Nicho:** Nutrição, com foco em emagrecimento feminino, gestantes e pós-parto.
*   **Voz da Marca:** "Amiga Especialista" — Tom direto, humano, sem jargão técnico, usa contradição para engajar ("pão não engorda", "não é falta de vontade"). Não vende dieta, mas sim mudança de comportamento e entendimento do corpo. Oportunidade de se posicionar como a nutricionista "que não te culpa".
*   **Objetivo Principal:** Escalar a aquisição de clientes e otimizar a conversão, a retenção e a eficiência operacional, solidificando o posicionamento em nutrição comportamental.

---

### 2. O que existe (Contexto e Conhecimento Base)

*   **Contexto de Negócio:**
    *   **Aquisição:** Dependência de indicação, desalinhamento de posicionamento (sessão gratuita parece venda).
    *   **Conversão:** Alta taxa de no-show em sessões gratuitas, agendamento informal (WhatsApp), baixa taxa de conversão para consultas pagas (8 de 38 leads).
    *   **Gestão de Agenda:** No-shows e falta de comprometimento.
    *   **Modelo de Serviço:** Comparação implícita com "nutri tradicional" ou "dieta via WhatsApp", necessidade de definir diferencial real (comportamento vs. dieta).
    *   **Operação e Eficiência:** Gargalos de tempo em anamnese e cálculo de cardápio.
    *   **Posicionamento de Valor:** Percepção de "dieta personalizada" vs. realidade de "mudança de comportamento, entendimento, execução".
    *   **Retenção & Engajamento:** Problema central é a dificuldade de execução da dieta, não o conhecimento. 41 clientes ativos.
*   **Preferências da Mayara (para conteúdo):**
    *   **Reels:** 5s de padding no início/fim, texto no bottom third (y > 1480px), sem box de fundo (usar outline + shadow), fontes Bebas Neue + Montserrat.
    *   **Cenários de Gravação:** Quintal com piscina, áreas verdes, próxima à praia, consultório, cozinha.
    *   **Formato de Entrega:** Roteiros com cenário especificado, vídeo pronto para ajuste final no CapCut.
*   **Análise Competitiva:** Estudo de 4 perfis de nutricionistas de sucesso (@daianaparisato, @thiagobarros, @paulomuzy, @draoliviafernandes), identificando padrões (bio clara, produto próprio, destaques, contradição, identidade de método) e **gaps de mercado** para a Mayara: tom de amiga real, foco em comportamento alimentar, empoderamento sem culpa, nicho gestante/pós-parto e cenário de "vida boa".
*   **Insights sobre Vídeos YouTube:** Dicas de produção (zoom, câmera parada, arrumação, uso de fontes, cortes secos) e comunicação para vídeos impactantes.
*   **Histórico de Temas Pesquisados:** Registro de pesquisa sobre reels virais, 5 roteiros criados, e um reel editado.
*   **Configuração do Cliente (`client.json`):** Define `name: Mayara Farias`, `niche: nutrição`, e os workflows ativos `["pesquisa", "youtube", "imagem", "landing_page", "reels"]`.
*   **Prompt do Gemini:** Define o papel do Gemini como "Pesquisador e Destilador de Contexto" para leitura, pesquisa, geração de volume e auditoria de voz.

### 3. O que está pronto

*   **Roteiros de Reels:** 5 roteiros completos e formatados para Reels virais, prontos para gravação nos cenários da Mayara, com ganchos, desenvolvimento e CTAs claros. (Ex: "Você não precisa sofrer pra emagrecer", "Pão não engorda").
*   **Ferramenta `tools/create_reel.py`:** Script Python funcional para processar vídeos, aplicar crop, zoom e adicionar textos conforme as preferências da Mayara.
*   **Workflow `workflows/reels_com_ia.md`:** Processo detalhado para transformar vídeos existentes em reels verticais otimizados, utilizando a IA para o "trabalho pesado" e a Mayara para o ajuste fino no CapCut.
*   **Workflow `workflows/research_niche.md`:** Processo completo para conduzir pesquisas multi-fonte (YouTube, Web, Notícias, PubMed) sobre temas de nutrição, gerando relatórios consolidados.
*   **Workflow `workflows/session_router.md`:** Workflow mestre para orquestração de tarefas, roteando entre Gemini, Claude e Manus com base na natureza da tarefa.
*   **Workflow `workflows/youtube_workflow_recommender.md`:** Processo para analisar vídeos do YouTube e recomendar workflows relevantes para o conteúdo.
*   **Workflow `workflows/image_generation_pipeline.md`:** Processo para gerar imagens (ilustrações, banners) via Nano Banana / Gemini ou Manus, com opções de custo e remoção de fundo.
*   **Workflow `workflows/landing_page_builder.md`:** Processo para criar landing pages animadas e de alto valor comercial usando Claude como orquestrador, Anime.js e GSAP.
*   **Brief Executivo de Negócio:** Um resumo conciso e detalhado dos desafios de negócio da Mayara, gerado pelo Gemini.

### 4. O que está incompleto / Em construção

*   **Campanha de Captação de Pacientes (v1):** O projeto foi criado, mas todas as suas peças estão marcadas como "🔲 Criar":
    *   3 Roteiros de Reels (Atração, Prova, Oferta).
    *   Formulário de triagem (3 perguntas).
    *   Mensagem de resposta para DM.
*   **Métricas de Conversão:** A necessidade de "MAPEAR MÉTRICAS MELHOR" para a conversão de agendamentos gratuitos em consultas pagas.
*   **Escalabilidade:** O arquivo `clients\mayara\context\negocio\Escalabilidade.md` está vazio, indicando que este pilar de negócio ainda não foi detalhado.
*   **Voz da Marca:** As seções "Palavras e expressões que ela usa" e "Palavras e expressões que ela evita" no `voz_marca.md` estão vazias e precisam ser preenchidas.

### 5. Tools e Workflows Existentes e suas Funções

#### Tools

*   `tools/call_gemini_api.py`: Orquestrador para chamadas à API do Gemini para pesquisa, resumo de contexto, geração de conteúdo em massa e auditoria de voz.
*   `tools/create_reel.py`: Processa um vídeo para formato vertical, adiciona zoom dinâmico e textos na tela (com fontes, cores, outline e sombra) baseado em um config JSON.
*   `tools/fetch_youtube_info.py`: Extrai título, autor e transcrição de vídeos do YouTube.
*   `tools/generate_images_api.py`: Gera imagens utilizando a API do Gemini.
*   `tools/generate_images_manus.py`: Envia tarefas para o serviço Manus para geração de imagens (incluindo remoção de fundo).
*   `tools/search_pubmed.py`: Realiza buscas de artigos científicos no PubMed.
*   `tools/search_web.py`: Realiza buscas gerais na web (artigos, blogs, notícias).
*   `tools/search_youtube.py`: Realiza buscas de vídeos no YouTube, com opção de extrair transcrições.
*   **Dependências externas:** `yt-dlp` e `ffmpeg` (para processamento de vídeo).

#### Workflows

*   `workflows/image_generation_pipeline.md`: **Função:** Gerar imagens (ilustrações, banners, assets) para uso em landing pages e outros materiais, oferecendo rotas otimizadas (manual, API, ou com remoção de fundo via Manus) com base em necessidades e custo.
*   `workflows/landing_page_builder.md`: **Função:** Construir landing pages animadas e responsivas de alto valor comercial, utilizando Claude para orquestração e Anime.js/GSAP para efeitos visuais e interativos.
*   `workflows/reels_com_ia.md`: **Função:** Automatizar a conversão de vídeos existentes (YouTube ou local) em reels verticais para Instagram/TikTok, aplicando crop, zoom, e textos de impacto, entregando um produto semi-acabado para ajuste final da Mayara no CapCut.
*   `workflows/research_niche.md`: **Função:** Conduzir pesquisas aprofundadas sobre tópicos de nutrição em diversas fontes (YouTube, Web, Notícias, Estudos Científicos), consolidando insights para guiar a criação de conteúdo e estratégias.
*   `workflows/session_router.md`: **Função:** Atuar como o "cérebro" do projeto, direcionando cada tipo de tarefa (leitura, pesquisa, geração de imagens, codificação, etc.) para a ferramenta ou modelo de IA mais adequado (Gemini, Claude, Manus), garantindo o uso eficiente dos recursos.
*   `workflows/youtube_workflow_recommender.md`: **Função:** Analisar o conteúdo de um vídeo do YouTube para identificar seu tema e técnicas, e então recomendar workflows existentes ou sugerir a criação de novos que sejam relevantes para o aprendizado ou aplicação da Mayara.

### 6. Próximos Passos Óbvios

1.  **Concluir e Lançar a Campanha de Captação (v1):**
    *   Priorizar a criação dos 3 roteiros de Reels de Atração, Prova e Oferta.
    *   Desenvolver o formulário de triagem e a mensagem de resposta para DM.
    *   Utilizar o workflow `reels_com_ia.md` para criar e otimizar os vídeos dos reels.
2.  **Aprofundar as Métricas de Conversão:** Implementar um sistema para mapear detalhadamente as métricas de agendamento gratuito, comparecimento e fechamento de consultas pagas, incluindo a origem dos no-shows.
3.  **Desenvolver a Estratégia de Escalabilidade:** Preencher o arquivo `Escalabilidade.md` com um plano claro de como Mayara pode crescer além da indicação.
4.  **Refinar a Voz da Marca:** Coletar exemplos de "Palavras e expressões que ela usa" e "Palavras e expressões que ela evita" para completar o `voz_marca.md`, garantindo maior consistência na comunicação.
5.  **Comunicar o Diferencial de Valor:** Com base na análise competitiva e no brief de negócio, articular e comunicar ativamente o posicionamento da Mayara como a "amiga especialista que não te culpa" e seu foco em nutrição comportamental.
6.  **Otimizar Operações Internas:** Investigar e propor soluções (automação, templates, ferramentas) para os gargalos de tempo na anamnese e cálculo de cardápio.
7.  **Considerar Landing Page para Campanha:** Avaliar se uma landing page (usando `landing_page_builder.md`) poderia otimizar a conversão da campanha de captação, em vez de depender apenas de formulários de DM.

---
<brief>
TAREFA: Devolver um mapa completo do projeto Mayara.
ARQUIVOS LIDOS: 23 arquivos de contexto, memória, negócio, pesquisas, projetos, tools, workflows e briefs.
RESUMO: O mapa detalha o contexto de negócio da Mayara, sua voz de marca, preferências, análises competitivas, e o status de seus projetos. Apresenta uma lista exaustiva de workflows e tools existentes com suas funções, e identifica o que está pronto, incompleto ou em construção, culminando em uma lista clara de próximos passos.
PRÓXIMO PASSO PARA O CLAUDE: Agora que o mapa completo do projeto foi entregue, o Claude pode usar esta visão consolidada para priorizar as próximas ações, focando em dar andamento aos itens "incompletos/em construção" e seguir os "próximos passos óbvios".
</brief>