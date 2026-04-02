# Workflow: Reels com IA — Reel Vertical a partir de Vídeo Existente

## Objetivo

Transformar um vídeo horizontal (YouTube, gravação própria) em reel vertical otimizado para Instagram/TikTok, com textos de impacto, zoom dinâmico e entrega pronta para ajuste final no CapCut.

**Filosofia:** IA faz o trabalho pesado (crop, zoom, fontes, timing). Humano faz o ajuste fino (apara início/fim, adiciona música, publica).

---

## Inputs Necessários

| Input | Descrição | Exemplo |
|---|---|---|
| `video_url` | URL do YouTube ou caminho local | `https://youtube.com/watch?v=...` |
| `tema` | O que o reel vai comunicar | `"alimentos que causam azia na gestação"` |
| `trecho` | Qual parte do vídeo usar (texto livre) | `"a parte onde ela lista os alimentos"` |

---

## Ferramentas

- `tools/fetch_youtube_info.py` — baixa transcrição com timestamps
- `tools/create_reel.py` — gera o reel via ffmpeg (crop, zoom, textos)
- `yt-dlp` — download do vídeo (deve estar no PATH)
- `ffmpeg` — processamento de vídeo (deve estar no PATH)
- **CapCut** — ajuste final pelo usuário (apara início/fim, adiciona música)

---

## Processo

### Passo 1 — Analisar o vídeo

```bash
python tools/fetch_youtube_info.py <youtube_url>
```

Leia a transcrição com timestamps e identifique:
- Qual trecho é mais valioso (dica prática, lista, contradição)
- O timestamp exato de início e fim do conteúdo útil
- As frases de impacto para virar texto na tela

### Passo 2 — Baixar o vídeo

```bash
mkdir -p .tmp
yt-dlp -o ".tmp/%(title)s.%(ext)s" <youtube_url>
```

### Passo 3 — Montar o config JSON

Crie `.tmp/config_reel.json` com a estrutura abaixo.

**Regra de padding:** sempre adicione 5s antes e 5s depois do conteúdo útil. O usuário apara no CapCut. Nunca tente acertar o corte exato — isso custa mais tempo do que vale.

```json
{
  "input":           ".tmp/nome_do_video.mp4",
  "output":          ".tmp/reel_final.mp4",
  "start_sec":       78.5,
  "duration":        46,
  "content_offset":  5.0,
  "crop": {
    "w": 480, "h": 854,
    "x": 720, "y": 113
  },
  "zoom_pulses": [
    [11.5, 16.0],
    [23.0, 29.5],
    [30.0, 40.5]
  ],
  "texts": [
    {
      "type":    "ctx",
      "text":    "vai te dar mais azia",
      "color":   "white",
      "y":       1555,
      "t_start": 11.5,
      "t_end":   18.0
    },
    {
      "type":    "kw",
      "text":    "MOLHO DE TOMATE",
      "color":   "#FF4422",
      "y":       1610,
      "t_start": 11.5,
      "t_end":   18.0,
      "size":    82
    }
  ]
}
```

### Passo 4 — Gerar o reel

```bash
python tools/create_reel.py .tmp/config_reel.json
```

A tool baixa as fontes automaticamente se necessário.

### Passo 5 — Entregar para ajuste final

Entregue o arquivo `.tmp/reel_final.mp4` ao usuário com instruções:

> "O vídeo tem 5s de margem no início e no fim. Abra no CapCut, apare onde quiser, adicione música trending e publique."

---

## Parâmetros de Crop (referência)

| Situação | crop.w | crop.h | crop.x | crop.y | Zoom final |
|---|---|---|---|---|---|
| Câmera próxima (close-up) | 608 | 1080 | 656 | 0 | 1.78x |
| Câmera média (padrão) | 480 | 854 | 720 | 113 | 2.25x |
| Câmera distante | 380 | 676 | 770 | 202 | 2.84x |

> **Como calcular:** `x = (1920 - w) / 2`, `y = (1080 - h) / 2`

---

## Posicionamento dos Textos (referência)

Sempre use o **bottom third** — texto no meio do frame cobre o rosto.

| Zona | y aproximado | Uso |
|---|---|---|
| Bottom safe (início) | 1480–1520 | Contexto acima do keyword |
| Bottom keyword | 1555–1650 | Palavra de impacto |
| Bottom extra | 1660–1750 | Segunda linha de keyword |

---

## Tipografia

| Elemento | Fonte | Estilo | Quando usar |
|---|---|---|---|
| **Keyword** | Bebas Neue | Bold, colorida, size 80–96 | Palavra central do momento |
| **Contexto** | Montserrat Regular | Branca, size 38–42 | Frase de suporte acima do keyword |

Baixadas automaticamente pelo script. Sem box de fundo — use `borderw` (outline) + `shadowcolor`.

---

## Cores recomendadas por tema

| Alimento/Tema | Cor hex |
|---|---|
| Tomate / perigo | `#FF4422` |
| Chocolate / prazer | `#C47A1E` |
| Gordura / frituras | `#FF8800` |
| Condimentos / azul | `#44CCFF` |
| Hook / destaque | `#FFE033` |
| Neutro | `white` |

---

## Edge Cases

| Situação | Como lidar |
|---|---|
| Texto com `:` ou `,` | Remover ou substituir por `-` ou `\` — o ffmpeg quebra com esses caracteres no drawtext |
| Texto com `ç`, `ã`, `é` | Usar versão sem acento (ex: `"a diferenca"`) — pode causar falha no Windows |
| Fontes não baixam | Copiar manualmente para `.tmp/fonts/` e apontar o path no config |
| `yt-dlp` falha no download | Tentar `--format best` ou `--format mp4` como fallback |
| Pessoa aparece fora do centro | Ajustar `crop.x` para deslocar horizontalmente. Cada pixel = 1px no original |
| Início com fala cortada | Adicionar mais padding (`start_sec` mais cedo, aumentar `duration`) |
| ffmpeg "Error opening output" no Windows | Verificar paths: evitar espaços e caracteres especiais. Usar `.tmp/` como diretório de trabalho |

---

## Outputs

- `reel_final.mp4` em `.tmp/` — vertical 1080x1920, com textos e zoom
- Pronto para abrir no CapCut e finalizar

---

## Aprendizados (atualizar sempre)

| Data | Aprendizado |
|---|---|
| 2026-04-02 | Arial é genérica demais — Bebas Neue + Montserrat são as fontes certas para reels virais |
| 2026-04-02 | Box de fundo no texto parece legenda de filme — usar outline + shadow no lugar |
| 2026-04-02 | Tentar acertar o corte exato custa mais do que vale — padding de 5s é a solução certa |
| 2026-04-02 | Caracteres especiais (`:`, `ç`, `ã`) quebram o drawtext do ffmpeg no Windows — evitar ou escapar |
| 2026-04-02 | Texto no meio do frame cobre o rosto — sempre usar bottom third (y > 1480) |
| 2026-04-02 | Paths com espaços e acentos no Windows quebram o ffmpeg — usar `.tmp/` sem acentos como área de trabalho |
