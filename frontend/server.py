"""
WAT Studio — FastAPI backend
Wraps Claude Code CLI and exposes SSE streaming to the browser.

Run from the project root:
    uvicorn frontend.server:app --reload --port 8000
"""

import asyncio
import json
import os
import re
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ─── Paths ───────────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent.parent          # workflows/
STATIC_DIR = Path(__file__).parent / "static"
TMP_DIR = ROOT / ".tmp"

ALLOWED_WORKFLOWS = {"pesquisa", "youtube", "imagem", "landing_page", "reels"}
ALLOWED_CLIENTS   = re.compile(r"^[a-z0-9_-]{1,64}$")

def get_client_slug() -> str:
    slug = os.environ.get("WAT_CLIENT", "mayara")
    if not ALLOWED_CLIENTS.match(slug):
        raise ValueError(f"Invalid client slug: {slug!r}")
    return slug

def client_dir(slug: str | None = None) -> Path:
    return ROOT / "clients" / (slug or get_client_slug())

def client_json(slug: str | None = None) -> Path:
    return client_dir(slug) / "client.json"

# ─── App ─────────────────────────────────────────────────────────────────────

app = FastAPI(title="WAT Studio", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# ─── Models ──────────────────────────────────────────────────────────────────

class RunPayload(BaseModel):
    type: str
    workflow: str | None = None
    inputs: dict | None = None
    message: str | None = None

class MemorySavePayload(BaseModel):
    content: str

# ─── Prompt building ─────────────────────────────────────────────────────────

WORKFLOW_TEMPLATES: dict[str, str] = {
    "pesquisa": (
        "Read workflows/research_niche.md carefully. "
        "Research topic: {tema}. Depth: {depth}. Format: {format}. "
        "Follow the workflow steps exactly."
    ),
    "youtube": (
        "Read workflows/youtube_workflow_recommender.md carefully. "
        "Analyse YouTube for topic: {tema}. "
        "Follow the workflow steps exactly."
    ),
    "imagem": (
        "Read workflows/image_generation_pipeline.md carefully. "
        "Generate image — prompt: {prompt}, style: {style}, format: {format}. "
        "Follow the workflow steps exactly."
    ),
    "landing_page": (
        "Read workflows/landing_page_builder.md carefully. "
        "Build landing page — product: {produto}, audience: {publico}, tone: {tom}. "
        "Follow the workflow steps exactly."
    ),
    "reels": (
        "Read workflows/reels_com_ia.md carefully. "
        "Create reel — topic: {tema}, duration: {duracao}, style: {estilo}. "
        "Follow the workflow steps exactly."
    ),
}

def _safe_str(value: object) -> str:
    """Convert any input value to a plain string, stripping shell-sensitive chars."""
    text = str(value)
    # Remove characters that could affect prompt parsing
    return re.sub(r"[`$\\]", "", text)[:500]

def build_prompt(payload: RunPayload, client_data: dict) -> str:
    context_path = client_data.get("context_path", f"clients/{get_client_slug()}/context")
    memory_path  = client_data.get("memory_path",  f"clients/{get_client_slug()}/context/memoria")

    header = (
        f"You are working for client: {client_data.get('name', 'Unknown')}. "
        f"Their niche: {client_data.get('niche', 'general')}. "
        f"Load their context from: {context_path}/ "
        f"Load their persistent memory from: {memory_path}/ "
        f"---\n"
    )

    if payload.type == "chat":
        message = _safe_str(payload.message or "")
        return header + message

    if payload.type == "workflow":
        workflow = payload.workflow or ""
        if workflow not in ALLOWED_WORKFLOWS:
            return header + "Unknown workflow."
        template = WORKFLOW_TEMPLATES[workflow]
        safe_inputs = {k: _safe_str(v) for k, v in (payload.inputs or {}).items()}
        try:
            instruction = template.format(**safe_inputs)
        except KeyError:
            instruction = template
        return header + instruction

    return header + "How can I help?"

# ─── Claude Code streaming ────────────────────────────────────────────────────

async def stream_claude(prompt: str):
    """
    Spawn claude CLI using create_subprocess_exec (no shell — injection-safe).
    The prompt is passed as a single positional argument, never through sh -c.
    Yields Server-Sent Events lines.
    """
    # create_subprocess_exec passes args as a list directly to execvp —
    # no shell expansion occurs, making this safe regardless of prompt content.
    try:
        proc = await asyncio.create_subprocess_exec(
            "claude", "--print", prompt,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(ROOT),
        )
    except FileNotFoundError:
        yield "data: [ERRO] Claude Code CLI não encontrado. Execute: npm install -g @anthropic-ai/claude-code\n\n"
        return

    assert proc.stdout is not None

    async for raw_line in proc.stdout:
        text = raw_line.decode("utf-8", errors="replace")
        escaped = text.replace("\n", "\\n")
        yield f"data: {escaped}\n\n"

    await proc.wait()

    if proc.returncode != 0:
        assert proc.stderr is not None
        err = (await proc.stderr.read()).decode("utf-8", errors="replace").replace("\n", "\\n")
        yield f"data: [ERRO] {err}\n\n"

    yield "data: [DONE]\n\n"

# ─── Routes ──────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/static/index.html")


@app.get("/client")
async def get_client():
    path = client_json()
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"client.json not found at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


@app.get("/history")
async def get_history(limit: int = 20):
    TMP_DIR.mkdir(exist_ok=True)
    files = sorted(
        [f for f in TMP_DIR.iterdir() if f.suffix == ".md"],
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )[:limit]
    return [
        {
            "filename": f.name,
            "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
            "size_kb": round(f.stat().st_size / 1024, 1),
        }
        for f in files
    ]


@app.get("/context")
async def get_context():
    memory_dir = client_dir() / "context" / "memoria"
    if not memory_dir.exists():
        return []
    return sorted(f.name for f in memory_dir.iterdir() if f.suffix == ".md")


@app.post("/memory/save")
async def memory_save(payload: MemorySavePayload):
    memory_dir = client_dir() / "context" / "memoria"
    memory_dir.mkdir(parents=True, exist_ok=True)
    notes_file = memory_dir / "notas_sessao.md"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    content   = payload.content.strip()[:2000]          # cap at 2000 chars
    entry     = f"\n## {timestamp}\n{content}\n"

    with open(notes_file, "a", encoding="utf-8") as fh:
        fh.write(entry)

    return {"saved": True, "file": str(notes_file)}


@app.post("/run")
async def run(payload: RunPayload):
    if payload.type not in {"workflow", "chat"}:
        raise HTTPException(status_code=400, detail="type must be 'workflow' or 'chat'")
    if payload.type == "workflow" and payload.workflow not in ALLOWED_WORKFLOWS:
        raise HTTPException(status_code=400, detail=f"Unknown workflow: {payload.workflow}")

    path = client_json()
    if not path.exists():
        raise HTTPException(status_code=404, detail="client.json not found")

    client_data = json.loads(path.read_text(encoding="utf-8"))
    prompt = build_prompt(payload, client_data)

    return StreamingResponse(
        stream_claude(prompt),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
