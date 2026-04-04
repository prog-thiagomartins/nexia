"""
search_web.py

Busca na web usando DuckDuckGo (sem API key necessária).
Suporta busca geral, notícias e busca restrita a sites específicos.

Usage:
    python tools/search_web.py "<query>" [--max 10] [--type text|news] [--site exemplo.com]

Options:
    --max N         Número de resultados (padrão: 10)
    --type          Tipo de busca: "text" (padrão) ou "news"
    --site          Restringe resultados a um domínio específico (ex: pubmed.ncbi.nlm.nih.gov)
    --region        Região para resultados (padrão: br-pt para Brasil/Português)

Output:
    JSON com lista de resultados: título, url, snippet, fonte, data (se notícia)

Dependencies:
    pip install duckduckgo-search
"""

import sys
import json
import argparse

def search_web(
    query: str,
    max_results: int = 10,
    search_type: str = "text",
    site: str = None,
    region: str = "br-pt",
) -> dict:
    """Busca na web via DuckDuckGo."""
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        return {"error": "duckduckgo-search não instalado. Execute: pip install duckduckgo-search"}

    # Adiciona filtro de site na query se especificado
    full_query = f"site:{site} {query}" if site else query

    results = []

    try:
        with DDGS() as ddgs:
            if search_type == "news":
                raw = list(ddgs.news(full_query, region=region, max_results=max_results))
                for item in raw:
                    results.append({
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "snippet": item.get("body", ""),
                        "source": item.get("source", ""),
                        "published": item.get("date", ""),
                        "type": "news",
                    })
            else:
                raw = list(ddgs.text(full_query, region=region, max_results=max_results))
                for item in raw:
                    results.append({
                        "title": item.get("title", ""),
                        "url": item.get("href", ""),
                        "snippet": item.get("body", ""),
                        "source": item.get("href", "").split("/")[2] if item.get("href") else "",
                        "type": "web",
                    })

        return {
            "query": full_query,
            "type": search_type,
            "region": region,
            "total_found": len(results),
            "results": results,
        }

    except Exception as e:
        return {"error": str(e), "query": full_query}


def main():
    parser = argparse.ArgumentParser(description="Busca na web via DuckDuckGo")
    parser.add_argument("query", help="Termo de busca")
    parser.add_argument("--max", type=int, default=10, help="Número de resultados")
    parser.add_argument("--type", choices=["text", "news"], default="text", dest="search_type")
    parser.add_argument("--site", help="Restringir a um domínio específico")
    parser.add_argument("--region", default="br-pt", help="Região (padrão: br-pt)")
    args = parser.parse_args()

    result = search_web(
        args.query,
        max_results=args.max,
        search_type=args.search_type,
        site=args.site,
        region=args.region,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
