"""
search_youtube.py

Busca vídeos no YouTube por query e retorna metadados + transcrições opcionais.
Usa yt-dlp para busca (sem API key). Para transcrições, chama fetch_youtube_info.py.

Usage:
    python tools/search_youtube.py "<query>" [--max 5] [--transcripts]

Options:
    --max N         Número de resultados (padrão: 5)
    --transcripts   Busca transcrições dos vídeos encontrados (mais lento)

Output:
    JSON com lista de vídeos: título, canal, url, visualizações, data, duração
    Se --transcripts: inclui transcript de cada vídeo

Dependencies:
    pip install yt-dlp
"""

import sys
import json
import subprocess
import argparse
import os

def search_youtube(query: str, max_results: int = 5, fetch_transcripts: bool = False) -> dict:
    """Busca vídeos no YouTube usando yt-dlp."""
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                f"ytsearch{max_results}:{query}",
                "--dump-json",
                "--no-download",
                "--flat-playlist",
                "--no-warnings",
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode != 0 and not result.stdout.strip():
            return {"error": f"yt-dlp falhou: {result.stderr.strip()}"}

        videos = []
        for line in result.stdout.strip().splitlines():
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                video = {
                    "title": data.get("title", ""),
                    "channel": data.get("uploader") or data.get("channel", ""),
                    "url": data.get("url") or f"https://www.youtube.com/watch?v={data.get('id', '')}",
                    "video_id": data.get("id", ""),
                    "views": data.get("view_count"),
                    "duration": data.get("duration"),
                    "upload_date": data.get("upload_date", ""),
                    "description_snippet": (data.get("description") or "")[:300],
                }
                videos.append(video)
            except json.JSONDecodeError:
                continue

        if fetch_transcripts and videos:
            tool_dir = os.path.dirname(os.path.abspath(__file__))
            fetch_script = os.path.join(tool_dir, "fetch_youtube_info.py")
            for video in videos:
                try:
                    tr = subprocess.run(
                        ["python", fetch_script, video["url"]],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )
                    info = json.loads(tr.stdout)
                    video["transcript"] = info.get("transcript", "")
                    video["transcript_language"] = info.get("transcript_language", "")
                    video["transcript_error"] = info.get("transcript_error", "")
                except Exception as e:
                    video["transcript_error"] = str(e)

        return {"query": query, "total_found": len(videos), "videos": videos}

    except FileNotFoundError:
        return {"error": "yt-dlp não encontrado. Instale com: pip install yt-dlp"}
    except subprocess.TimeoutExpired:
        return {"error": "Timeout ao buscar no YouTube. Tente uma query mais específica."}
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Busca vídeos no YouTube")
    parser.add_argument("query", help="Termo de busca")
    parser.add_argument("--max", type=int, default=5, help="Número de resultados (padrão: 5)")
    parser.add_argument("--transcripts", action="store_true", help="Buscar transcrições")
    args = parser.parse_args()

    result = search_youtube(args.query, max_results=args.max, fetch_transcripts=args.transcripts)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
