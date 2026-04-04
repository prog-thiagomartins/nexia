# Workflow: Niche Research — [CLIENT_NAME] ([CLIENT_NICHE])

## Objective

Conduct multi-source research on a topic in the women's [CLIENT_NICHE] niche.
Generates a consolidated report in `.tmp/` with insights from YouTube, web, news, and scientific studies.

## Required Inputs

- `topic`: What to research (e.g., "intermittent fasting for women", "low carb protocol 2025")
- `depth`: **Quick** (metadata only) or **Deep** (includes video transcripts)
- `output_format`: Format of the final report (see options below)

---

## STEP 0 — Mandatory questions before starting

**ALWAYS ask before running any tool:**

> **1. Research depth:**
> - **Quick**: fetches titles, snippets, and links — result in ~30 seconds
> - **Deep**: extracts transcripts from top YouTube videos — result in ~2-3 minutes, much more content
>
> **2. Format of the generated material:**
> - **Executive summary**: synthesis of the main insights, ready to use
> - **Full report**: raw data + analysis — useful for consulting sources later
> - **Content briefing**: focused on ideas for posts, videos, or materials for [CLIENT_NAME]
> - **Benchmarking**: analysis focused on competitors and positioning

Wait for the response before continuing.

---

## STEP 1 — Execute searches (in parallel)

Run all 4 searches **simultaneously**:

### 1a. YouTube
```bash
# Quick mode
python tools/search_youtube.py "<topic>" --max 8

# Deep mode
python tools/search_youtube.py "<topic>" --max 5 --transcripts
```

### 1b. General Web (articles, blogs, [CLIENT_NICHE] sites)
```bash
python tools/search_web.py "<topic> [CLIENT_NICHE]" --max 10 --region ${CLIENT_REGION:-br-pt}
```

### 1c. Recent news
```bash
python tools/search_web.py "<topic>" --max 8 --type news --region ${CLIENT_REGION:-br-pt}
```

### 1d. Scientific studies (PubMed)
```bash
# Use English terms for best results
python tools/search_pubmed.py "<topic in English>" --max 6 --years 3
```

### Additional searches by research type

**If competitor benchmarking:**
```bash
python tools/search_youtube.py "[CLIENT_ROLE] <topic>" --max 10
python tools/search_web.py "[CLIENT_ROLE] <topic> program" --max 10
```

**If trends:**
```bash
python tools/search_web.py "<topic> trend 2025" --max 10 --type news
python tools/search_youtube.py "<topic> 2025" --max 8
```

**If searching specific sites:**
```bash
# Examples of specialized sites:
python tools/search_web.py "<topic>" --site sbcbm.org.br --max 5
python tools/search_web.py "<topic>" --site cfn.org.br --max 5
python tools/search_web.py "<topic>" --site examine.com --max 5
python tools/search_web.py "<topic>" --site healthline.com --max 5
```

---

## STEP 2 — Consolidation and analysis

With results from all 4 sources, analyze and synthesize:

### For all formats, identify:
1. **Main subtopics**: What is being most discussed about this topic?
2. **Content angles**: What different approaches do creators use?
3. **Data and numbers**: Statistics, percentages, results mentioned
4. **Frequently asked questions**: What do people want to know?
5. **Content gaps**: What is not being covered well?

### If Benchmarking, add:
6. **Identified competitors**: Name, channel, positioning
7. **What they do well**: Observed strengths
8. **Possible differentiation**: Where [CLIENT_NAME] can stand out

### If Scientific Studies, add:
9. **Evidence found**: Level of evidence (systematic review > RCT > observational studies)
10. **Current consensus**: What does science say in a consolidated way?
11. **Controversies**: Where is there scientific debate?

---

## STEP 3 — Report generation

Save the report to `.tmp/research_[topic-slug]_[date].md`.

**Name example:** `.tmp/research_intermittent-fasting_2025-04-01.md`

### Report template

```markdown
# Research: [Topic]
**Date:** [date]
**Depth:** [Quick/Deep]
**Sources consulted:** YouTube ([N] videos) · Web ([N] results) · News ([N]) · PubMed ([N] studies)

---

## Executive Summary
[3-5 bullets with the most important insights]

---

## YouTube — What is being said

### Top Videos Found
| Title | Channel | Views | Link |
|--------|-------|-------|------|

### Main Messages
[Synthesis of what creators are saying — extracted from transcripts if Deep mode]

---

## Web & News — Trends and Context

### Relevant Articles
[List with title + snippet + link of the most relevant ones]

### What is trending
[Identified trends]

---

## Science — What studies say

### PubMed Articles
| Title | Authors | Year | Journal | Link |
|--------|---------|-----|---------|------|

### Scientific Consensus
[Synthesis of what the evidence points to]

---

## Content Ideas for [CLIENT_NAME]
[5-10 ideas for posts, videos, or materials based on the research]

---

## Complete Sources
[Links to everything found, organized by category]
```

---

## Error Handling

| Error | Action |
|------|------|
| `yt-dlp not found` | `pip install yt-dlp` and try again |
| `duckduckgo-search not installed` | `pip install duckduckgo-search` and try again |
| `No results in PubMed` | Translate query to English and try more general terms |
| `Transcript unavailable` | Record in the report and use title/description only |
| `Timeout` | Try with a smaller `--max` or split the research into subtopics |

---

## Notes and Learnings

- PubMed returns better results with English terms (e.g., "intermittent fasting women" instead of "jejum intermitente mulheres")
- `yt-dlp` can take 10-20s per video when fetching transcripts in Deep mode
- DuckDuckGo may be temporarily blocked after many searches — wait 1-2 minutes if this occurs
- For benchmarking, adding the specialty name to the term helps (e.g., "[CLIENT_ROLE] intermittent fasting")
