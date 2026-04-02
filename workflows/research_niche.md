# Workflow: Pesquisa de Nicho — Mayara Farias (Nutrição)

## Objetivo

Realizar pesquisa multi-fonte sobre um tema do nicho de nutrição para mulheres.
Gera um relatório consolidado em `.tmp/` com insights de YouTube, web, notícias e estudos científicos.

## Inputs Necessários

- `tema`: O que pesquisar (ex: "jejum intermitente para mulheres", "protocolo low carb 2025")
- `profundidade`: **Rápido** (só metadados) ou **Profundo** (inclui transcrições de vídeos)
- `formato_output`: Formato do relatório final (ver opções abaixo)

---

## PASSO 0 — Perguntas obrigatórias antes de iniciar

**SEMPRE pergunte antes de executar qualquer tool:**

> **1. Profundidade da pesquisa:**
> - **Rápido**: busca títulos, snippets e links — resultado em ~30 segundos
> - **Profundo**: extrai transcrições dos top vídeos do YouTube — resultado em ~2-3 minutos, muito mais conteúdo
>
> **2. Formato do material gerado:**
> - **Resumo executivo**: síntese dos principais insights, pronto para usar
> - **Relatório completo**: raw data + análise — útil para consultar fontes depois
> - **Briefing de conteúdo**: focado em ideias para posts, vídeos ou materiais da Mayara
> - **Benchmarking**: análise focada em concorrentes e posicionamento

Aguarde a resposta antes de continuar.

---

## PASSO 1 — Execução das buscas (em paralelo)

Execute as 4 buscas **simultaneamente**:

### 1a. YouTube
```bash
# Modo Rápido
python tools/search_youtube.py "<tema>" --max 8

# Modo Profundo
python tools/search_youtube.py "<tema>" --max 5 --transcripts
```

### 1b. Web Geral (artigos, blogs, sites de nutrição)
```bash
python tools/search_web.py "<tema> nutrição" --max 10 --region br-pt
```

### 1c. Notícias recentes
```bash
python tools/search_web.py "<tema>" --max 8 --type news --region br-pt
```

### 1d. Estudos científicos (PubMed)
```bash
# Use termos em inglês para melhores resultados
python tools/search_pubmed.py "<tema em inglês>" --max 6 --years 3
```

### Buscas adicionais por tipo de pesquisa

**Se for benchmarking de concorrentes:**
```bash
python tools/search_youtube.py "nutricionista <tema>" --max 10
python tools/search_web.py "nutricionista <tema> programa" --max 10
```

**Se for tendências:**
```bash
python tools/search_web.py "<tema> tendência 2025" --max 10 --type news
python tools/search_youtube.py "<tema> 2025" --max 8
```

**Se for busca em sites específicos:**
```bash
# Exemplos de sites especializados:
python tools/search_web.py "<tema>" --site sbcbm.org.br --max 5
python tools/search_web.py "<tema>" --site cfn.org.br --max 5
python tools/search_web.py "<tema>" --site examine.com --max 5
python tools/search_web.py "<tema>" --site healthline.com --max 5
```

---

## PASSO 2 — Consolidação e análise

Com os resultados das 4 fontes, analise e sintetize:

### Para todos os formatos, identifique:
1. **Principais subtemas**: O que está sendo mais discutido sobre esse tema?
2. **Ângulos de conteúdo**: Quais abordagens diferentes os criadores usam?
3. **Dados e números**: Estatísticas, percentuais, resultados mencionados
4. **Dúvidas frequentes**: O que as pessoas querem saber?
5. **Gaps de conteúdo**: O que não está sendo coberto bem?

### Se for Benchmarking, adicione:
6. **Concorrentes identificados**: Nome, canal, posicionamento
7. **O que eles fazem bem**: Pontos fortes observados
8. **Diferenciação possível**: Onde a Mayara pode se destacar

### Se for Estudos Científicos, adicione:
9. **Evidências encontradas**: Nível de evidência (revisão sistemática > RCT > estudos observacionais)
10. **Consenso atual**: O que a ciência diz de forma consolidada?
11. **Controvérsias**: Onde há debate científico?

---

## PASSO 3 — Geração do relatório

Salve o relatório em `.tmp/research_[tema-slug]_[data].md`.

**Exemplo de nome:** `.tmp/research_jejum-intermitente_2025-04-01.md`

### Template do relatório

```markdown
# Pesquisa: [Tema]
**Data:** [data]  
**Profundidade:** [Rápido/Profundo]  
**Fontes consultadas:** YouTube ([N] vídeos) · Web ([N] resultados) · Notícias ([N]) · PubMed ([N] estudos)

---

## Resumo Executivo
[3-5 bullets com os insights mais importantes]

---

## YouTube — O que está sendo dito

### Top Vídeos Encontrados
| Título | Canal | Views | Link |
|--------|-------|-------|------|

### Principais Mensagens
[Síntese do que os criadores estão dizendo — extraída das transcrições se modo Profundo]

---

## Web & Notícias — Tendências e Contexto

### Artigos Relevantes
[Lista com título + snippet + link dos mais relevantes]

### O que está em alta
[Tendências identificadas]

---

## Ciência — O que os estudos dizem

### Artigos do PubMed
| Título | Autores | Ano | Journal | Link |
|--------|---------|-----|---------|------|

### Consenso Científico
[Síntese do que a evidência aponta]

---

## Ideias de Conteúdo para a Mayara
[5-10 ideias de posts, vídeos, ou materiais baseadas na pesquisa]

---

## Fontes Completas
[Links de tudo que foi encontrado, organizados por categoria]
```

---

## Tratamento de Erros

| Erro | Ação |
|------|------|
| `yt-dlp não encontrado` | `pip install yt-dlp` e tentar novamente |
| `duckduckgo-search não instalado` | `pip install duckduckgo-search` e tentar novamente |
| `Nenhum resultado no PubMed` | Traduzir query para inglês e tentar termos mais gerais |
| `Transcript indisponível` | Registrar no relatório e usar apenas título/descrição |
| `Timeout` | Tentar com `--max` menor ou dividir a pesquisa em subtemas |

---

## Notas e Aprendizados

- PubMed retorna melhores resultados com termos em inglês (ex: "intermittent fasting women" em vez de "jejum intermitente mulheres")
- `yt-dlp` pode demorar 10-20s por vídeo ao buscar transcrições no modo Profundo
- DuckDuckGo pode ser bloqueado temporariamente após muitas buscas — aguardar 1-2 minutos se ocorrer
- Para benchmarking, adicionar o nome da especialidade ao termo ajuda (ex: "nutricionista jejum intermitente")
