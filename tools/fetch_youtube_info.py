"""
fetch_youtube_info.py

Fetches YouTube video metadata and transcript.
Outputs a structured JSON summary to stdout.

Usage:
    python tools/fetch_youtube_info.py <youtube_url>

Dependencies:
    pip install youtube-transcript-api requests
"""

import sys
import json
import re
import requests

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled
except ImportError:
    print(json.dumps({"error": "Missing dependency. Run: pip install youtube-transcript-api requests"}))
    sys.exit(1)


def extract_video_id(url: str) -> str | None:
    """Extract YouTube video ID from various URL formats."""
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})",
        r"(?:embed\/)([0-9A-Za-z_-]{11})",
        r"(?:shorts\/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def fetch_metadata(url: str) -> dict:
    """Fetch video title and author via YouTube oEmbed (no API key needed)."""
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        resp = requests.get(oembed_url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return {
            "title": data.get("title", "Unknown Title"),
            "author": data.get("author_name", "Unknown Channel"),
        }
    except Exception as e:
        return {"title": "Unknown Title", "author": "Unknown Channel", "metadata_error": str(e)}


def fetch_transcript(video_id: str) -> dict:
    """
    Fetch transcript, preferring Portuguese then English.
    Returns the full text and language used.
    Compatible with youtube-transcript-api v1.x+
    """
    preferred = ["pt", "pt-BR", "en", "en-US", "en-GB"]

    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        # Try preferred languages first
        for lang in preferred:
            try:
                transcript = transcript_list.find_transcript([lang])
                fetched = transcript.fetch()
                entries = fetched.snippets if hasattr(fetched, "snippets") else list(fetched)
                text = " ".join(
                    e.text if hasattr(e, "text") else e["text"]
                    for e in entries
                )
                return {"text": text, "language": lang, "entry_count": len(entries)}
            except Exception:
                continue

        # Fall back to any available transcript
        for transcript in transcript_list:
            try:
                fetched = transcript.fetch()
                entries = fetched.snippets if hasattr(fetched, "snippets") else list(fetched)
                text = " ".join(
                    e.text if hasattr(e, "text") else e["text"]
                    for e in entries
                )
                return {"text": text, "language": transcript.language_code, "entry_count": len(entries)}
            except Exception:
                continue

        return {"text": "", "language": None, "error": "No fetchable transcript found"}

    except TranscriptsDisabled:
        return {"text": "", "language": None, "error": "Transcripts are disabled for this video"}
    except NoTranscriptFound:
        return {"text": "", "language": None, "error": "No transcript available"}
    except Exception as e:
        return {"text": "", "language": None, "error": str(e)}


def summarize_transcript(text: str, max_chars: int = 8000) -> str:
    """Trim transcript to a manageable size for the agent to analyze."""
    if len(text) <= max_chars:
        return text
    # Keep beginning and end, truncate middle
    half = max_chars // 2
    return text[:half] + "\n\n[... transcript trimmed for length ...]\n\n" + text[-half:]


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python tools/fetch_youtube_info.py <youtube_url>"}))
        sys.exit(1)

    url = sys.argv[1]
    video_id = extract_video_id(url)

    if not video_id:
        print(json.dumps({"error": f"Could not extract video ID from URL: {url}"}))
        sys.exit(1)

    metadata = fetch_metadata(url)
    transcript_data = fetch_transcript(video_id)

    result = {
        "video_id": video_id,
        "url": url,
        "title": metadata["title"],
        "author": metadata["author"],
        "transcript_language": transcript_data.get("language"),
        "transcript_entry_count": transcript_data.get("entry_count", 0),
        "transcript": summarize_transcript(transcript_data.get("text", "")),
        "transcript_error": transcript_data.get("error"),
    }

    if "metadata_error" in metadata:
        result["metadata_error"] = metadata["metadata_error"]

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
