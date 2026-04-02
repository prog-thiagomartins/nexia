"""
create_reel.py

Transforma um trecho de vídeo horizontal em reel vertical (9:16) com:
- Crop e zoom de aproximação
- Zoom dinâmico sincronizado com momentos-chave
- Textos em dois pesos: Bebas Neue (impacto) + Montserrat (contexto)
- Outline + sombra nos textos (sem box)
- Padding de 5s no início e fim para edição manual no CapCut

Usage:
    python tools/create_reel.py <config.json>

Config JSON esperado:
{
  "input":      "caminho/para/video.mp4",
  "output":     ".tmp/reel_output.mp4",
  "start_sec":  78.5,        // início do trecho (com 5s de padding)
  "duration":   46,          // duração total (conteúdo + 5s padding em cada ponta)
  "content_offset": 5.0,     // onde o conteúdo real começa (após o padding)
  "crop": {
    "w": 480, "h": 854,      // área a cortar do original (define o zoom)
    "x": 720, "y": 113       // posição do crop (use centro da imagem)
  },
  "zoom_pulses": [           // janelas de zoom dinâmico (relativo ao vídeo, já com offset)
    [11.5, 16.0],
    [23.0, 29.5],
    [30.0, 40.5]
  ],
  "texts": [
    {
      "type":    "kw",       // "kw" = keyword (Bebas Neue) | "ctx" = contexto (Montserrat)
      "text":    "MOLHO DE TOMATE",
      "color":   "#FF4422",
      "y":       1610,
      "t_start": 11.5,
      "t_end":   18.0,
      "size":    82
    }
  ]
}

Dependencies:
    pip install (nenhuma — usa apenas ffmpeg no PATH)
    Fontes: baixadas automaticamente se não encontradas em .tmp/fonts/
"""

import sys, json, os, subprocess, urllib.request, re
from pathlib import Path

# ─── DIRETÓRIO DE FONTES ────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent.parent
FONTS_DIR  = BASE_DIR / ".tmp" / "fonts"
FONTS_DIR.mkdir(parents=True, exist_ok=True)

FONT_BEBAS = FONTS_DIR / "bebas_neue.ttf"
FONT_MONT  = FONTS_DIR / "montserrat_regular.ttf"

GFONT_URLS = {
    "bebas_neue":          "https://fonts.googleapis.com/css2?family=Bebas+Neue",
    "montserrat_regular":  "https://fonts.googleapis.com/css2?family=Montserrat:wght@400",
}

def ensure_font(dest: Path, family_key: str):
    """Baixa a fonte do Google Fonts se não existir localmente."""
    if dest.exists():
        return
    print(f"  Baixando fonte: {dest.name}...")
    url = GFONT_URLS[family_key]
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    css = urllib.request.urlopen(req).read().decode()
    urls = re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+\.ttf)\)", css)
    if not urls:
        raise RuntimeError(f"Fonte não encontrada: {family_key}")
    urllib.request.urlretrieve(urls[0], dest)
    print(f"  OK: {dest}")

def ffmpeg_path(p: Path) -> str:
    """Converte Path para formato que o ffmpeg aceita no Windows."""
    return str(p).replace("\\", "/").replace("C:/", "C\\:/")

# ─── ZOOM ───────────────────────────────────────────────────────────────────
def zoom_pulse(t_in, t_out, amp=0.10):
    mid  = (t_in + t_out) / 2
    up   = f"min(1,max(0,(t-{t_in:.1f})/{(mid-t_in):.1f}))"
    down = f"min(1,max(0,({t_out:.1f}-t)/{(t_out-mid):.1f}))"
    return f"{amp}*min({up},{down})"

# ─── TEXTO ───────────────────────────────────────────────────────────────────
def make_text(item: dict, bebas_path: str, mont_path: str) -> str:
    font  = bebas_path if item["type"] == "kw" else mont_path
    size  = item.get("size", 88 if item["type"] == "kw" else 40)
    color = item.get("color", "white")
    bw    = 4 if item["type"] == "kw" else 2
    sw    = 3 if item["type"] == "kw" else 2
    return (
        f"drawtext=text='{item['text']}':fontfile='{font}':fontsize={size}"
        f":fontcolor={color}:x=(w-text_w)/2:y={item['y']}"
        f":enable='between(t,{item['t_start']},{item['t_end']})'"
        f":borderw={bw}:bordercolor=black"
        f":shadowx={sw}:shadowy={sw}:shadowcolor=black@0.7"
    )

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/create_reel.py <config.json>")
        sys.exit(1)

    cfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    ensure_font(FONT_BEBAS, "bebas_neue")
    ensure_font(FONT_MONT,  "montserrat_regular")

    bebas = ffmpeg_path(FONT_BEBAS)
    mont  = ffmpeg_path(FONT_MONT)

    # Crop + scale vertical
    c    = cfg["crop"]
    vf_parts = [
        f"crop={c['w']}:{c['h']}:{c['x']}:{c['y']}",
        "scale=1080:1920",
    ]

    # Zoom dinâmico
    if cfg.get("zoom_pulses"):
        Z = "1+" + "+".join(f"({zoom_pulse(a,b)})" for a,b in cfg["zoom_pulses"])
        vf_parts += [
            f"scale=w='1080*({Z})':h='1920*({Z})':eval=frame",
            "crop=w=1080:h=1920:x=(iw-1080)/2:y=(ih-1920)/2",
        ]

    # Textos
    for item in cfg.get("texts", []):
        vf_parts.append(make_text(item, bebas, mont))

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(cfg["start_sec"]),
        "-t",  str(cfg["duration"]),
        "-i",  cfg["input"],
        "-vf", ",".join(vf_parts),
        "-c:v", "libx264", "-preset", "fast", "-crf", "21",
        "-c:a", "aac", "-b:a", "128k",
        cfg["output"],
    ]

    print(f"Gerando reel...")
    print(f"  Input  : {cfg['input']}")
    print(f"  Output : {cfg['output']}")
    print(f"  Trecho : {cfg['start_sec']}s + {cfg['duration']}s (padding 5s em cada ponta)")

    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        print(f"  OK -> {cfg['output']}")
    else:
        print("ERRO ffmpeg:\n", r.stderr[-3000:])
        sys.exit(1)

if __name__ == "__main__":
    main()
