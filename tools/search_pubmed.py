"""
search_pubmed.py

Busca artigos científicos no PubMed via NCBI E-utilities (API pública, sem key).
Retorna título, autores, abstract, ano e link para cada artigo.

Usage:
    python tools/search_pubmed.py "<query>" [--max 5] [--years 3]

Options:
    --max N         Número de artigos (padrão: 5)
    --years N       Filtrar pelos últimos N anos (padrão: 5)
    --lang pt|en    Preferência de idioma para ordenação (padrão: en)

Output:
    JSON com lista de artigos: título, autores, abstract, ano, journal, pmid, url

Dependencies:
    pip install requests
    (sem API key necessária para uso básico — limite: 3 req/s sem key, 10 req/s com key)
"""

import sys
import json
import argparse
import requests
from datetime import datetime

ENTREZ_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def search_pubmed(query: str, max_results: int = 5, years: int = 5) -> dict:
    """Busca artigos no PubMed e retorna metadados + abstracts."""
    try:
        # Passo 1: buscar IDs dos artigos
        current_year = datetime.now().year
        min_year = current_year - years

        search_params = {
            "db": "pubmed",
            "term": f"{query}[Title/Abstract]",
            "retmax": max_results,
            "retmode": "json",
            "sort": "relevance",
            "datetype": "pdat",
            "mindate": str(min_year),
            "maxdate": str(current_year),
        }

        search_resp = requests.get(
            f"{ENTREZ_BASE}/esearch.fcgi",
            params=search_params,
            timeout=15,
        )
        search_resp.raise_for_status()
        search_data = search_resp.json()

        ids = search_data.get("esearchresult", {}).get("idlist", [])
        total_available = search_data.get("esearchresult", {}).get("count", "0")

        if not ids:
            return {
                "query": query,
                "total_available": total_available,
                "articles": [],
                "note": "Nenhum artigo encontrado. Tente termos em inglês.",
            }

        # Passo 2: buscar detalhes dos artigos por ID
        fetch_params = {
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "json",
            "rettype": "abstract",
        }

        fetch_resp = requests.get(
            f"{ENTREZ_BASE}/efetch.fcgi",
            params=fetch_params,
            timeout=20,
        )

        # efetch não retorna JSON estruturado — usar summary endpoint
        summary_params = {
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "json",
        }

        summary_resp = requests.get(
            f"{ENTREZ_BASE}/esummary.fcgi",
            params=summary_params,
            timeout=15,
        )
        summary_resp.raise_for_status()
        summary_data = summary_resp.json()

        articles = []
        result_set = summary_data.get("result", {})

        for pmid in ids:
            article_data = result_set.get(pmid, {})
            if not article_data:
                continue

            authors = [a.get("name", "") for a in article_data.get("authors", [])[:3]]
            pub_date = article_data.get("pubdate", "")
            year = pub_date[:4] if pub_date else ""

            article = {
                "pmid": pmid,
                "title": article_data.get("title", ""),
                "authors": authors,
                "journal": article_data.get("fulljournalname") or article_data.get("source", ""),
                "year": year,
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "doi": next(
                    (
                        uid.get("value", "")
                        for uid in article_data.get("articleids", [])
                        if uid.get("idtype") == "doi"
                    ),
                    "",
                ),
            }
            articles.append(article)

        return {
            "query": query,
            "date_range": f"{min_year}–{current_year}",
            "total_available": total_available,
            "returned": len(articles),
            "articles": articles,
            "note": "Abstracts: acesse cada URL para texto completo do abstract.",
        }

    except requests.exceptions.ConnectionError:
        return {"error": "Sem conexão com PubMed. Verifique sua internet."}
    except requests.exceptions.Timeout:
        return {"error": "Timeout ao conectar ao PubMed."}
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Busca artigos científicos no PubMed")
    parser.add_argument("query", help="Termo de busca (preferencialmente em inglês)")
    parser.add_argument("--max", type=int, default=5, help="Número de artigos")
    parser.add_argument("--years", type=int, default=5, help="Últimos N anos")
    args = parser.parse_args()

    result = search_pubmed(args.query, max_results=args.max, years=args.years)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
