"""
Exporta os slides de um carrossel HTML do visual companion em PNGs 1080x1350px
(resolução oficial Instagram 4:5), prontos pra postar.

Uso:
    python tools/exportar_slides_carrossel.py <arquivo-html> <pasta-saida>

Exemplo:
    python tools/exportar_slides_carrossel.py \
        ".superpowers/brainstorm/956-.../content/carrossel-dia2-v21.html" \
        "Campanhas/essencia/carrosseis/dia2-export/"

Saída: slide-01.png, slide-02.png, ..., slide-XX.png
"""

import sys
import os
from pathlib import Path
from playwright.sync_api import sync_playwright


IG_WIDTH = 1080
IG_HEIGHT = 1350   # 4:5 Instagram feed

# Template foi desenhado em 540px (max-width do .ig-wrap).
# Renderizamos direto em 1080x1350 (tamanho nativo do feed Instagram) e
# aplicamos zoom 2x via CSS para manter fontes/elementos proporcionais.
# Assim a imagem original (que já é de alta res) não sofre upscale borrado.
ZOOM = IG_WIDTH / 540  # = 2


def exportar(html_path: str, out_dir: str):
    html_path = Path(html_path).resolve()
    out_dir = Path(out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    file_url = html_path.as_uri()
    print(f"Lendo: {file_url}")
    print(f"Saída: {out_dir}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 540, "height": 675},
            device_scale_factor=2,  # 540x675 * 2 = 1080x1350 (tamanho nativo IG)
        )
        page = context.new_page()
        page.goto(file_url, wait_until="networkidle")

        # Espera fontes do Google Fonts carregarem
        page.wait_for_timeout(2000)
        page.evaluate("document.fonts.ready")

        # Injeta CSS pra o slide ocupar viewport inteiro (sem frame ou legend)
        page.add_style_tag(content="""
            body { margin: 0 !important; padding: 0 !important; background: white !important; }
            h2, h3.page-title, .subtitle, .legend-below, .ig-dots, .ig-counter, .ig-nav { display: none !important; }
            /* zoom 2x escala fontes e elementos sem borrar a imagem original (que sobe 1:1) */
            .ig-wrap { max-width: none !important; margin: 0 !important; }
            .ig-frame {
                width: 100vw !important; height: 100vh !important;
                aspect-ratio: unset !important;
                border-radius: 0 !important;
                box-shadow: none !important;
            }
        """)
        page.wait_for_timeout(500)

        slides = page.query_selector_all(".ig-slide")
        total = len(slides)
        print(f"Encontrados {total} slides. Exportando…")

        for i in range(total):
            # Ativa apenas o slide i (remove active dos outros, adiciona no i)
            page.evaluate(f"""
                document.querySelectorAll('.ig-slide').forEach((s, idx) => {{
                    s.classList.toggle('active', idx === {i});
                    s.style.opacity = idx === {i} ? '1' : '0';
                }});
            """)
            # Espera transição
            page.wait_for_timeout(400)

            out_file = out_dir / f"slide-{i+1:02d}.png"
            # Screenshot do frame (não da página inteira)
            frame = page.query_selector(".ig-frame")
            if frame:
                frame.screenshot(path=str(out_file))
            else:
                page.screenshot(path=str(out_file), clip={"x": 0, "y": 0, "width": IG_WIDTH, "height": IG_HEIGHT})
            print(f"  ✓ {out_file.name}")

        browser.close()

    print(f"\nPronto! {total} slides em {out_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python exportar_slides_carrossel.py <arquivo.html> <pasta-saida>")
        sys.exit(1)
    exportar(sys.argv[1], sys.argv[2])
