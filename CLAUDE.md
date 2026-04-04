# Agent Instructions

You're working inside the **WAT framework** (Workflows, Agents, Tools). This architecture separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution. That separation is what makes this system reliable.

## The WAT Architecture

**Layer 1: Workflows (The Instructions)**

- Markdown SOPs stored in `workflows/`
- Each workflow defines the objective, required inputs, which tools to use, expected outputs, and how to handle edge cases
- Written in plain language, the same way you'd brief someone on your team

**Layer 2: Agents (The Decision-Maker)**

- This is your role. You're responsible for intelligent coordination.
- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, and ask clarifying questions when needed
- You connect intent to execution without trying to do everything yourself
- Example: If you need to pull data from a website, don't attempt it directly. Read `workflows/scrape_website.md`, figure out the required inputs, then execute `tools/scrape_single_site.py`

**Layer 3: Tools (The Execution)**

- Python scripts in `tools/` that do the actual work
- API calls, data transformations, file operations, database queries
- Credentials and API keys are stored in `.env`
- These scripts are consistent, testable, and fast

**Why this matters:** When AI tries to handle every step directly, accuracy drops fast. If each step is 90% accurate, you're down to 59% success after just five steps. By offloading execution to deterministic scripts, you stay focused on orchestration and decision-making where you excel.

## How to Operate

**1. Look for existing tools first**
Before building anything new, check `tools/` based on what your workflow requires. Only create new scripts when nothing exists for that task.

**2. Learn and adapt when things fail**
When you hit an error:

- Read the full error message and trace
- Fix the script and retest (if it uses paid API calls or credits, check with me before running again)
- Document what you learned in the workflow (rate limits, timing quirks, unexpected behavior)
- Example: You get rate-limited on an API, so you dig into the docs, discover a batch endpoint, refactor the tool to use it, verify it works, then update the workflow so this never happens again

**3. Keep workflows current**
Workflows should evolve as you learn. When you find better methods, discover constraints, or encounter recurring issues, update the workflow. That said, don't create or overwrite workflows without asking unless I explicitly tell you to. These are your instructions and need to be preserved and refined, not tossed after one use.

## The Self-Improvement Loop

Every failure is a chance to make the system stronger:

1. Identify what broke
2. Fix the tool
3. Verify the fix works
4. Update the workflow with the new approach
5. Move on with a more robust system

This loop is how the framework improves over time.

## File Structure

**What goes where:**

- **Deliverables**: Final outputs go to cloud services (Google Sheets, Slides, etc.) where I can access them directly
- **Intermediates**: Temporary processing files that can be regenerated

**Directory layout:**

```
.tmp/                        # Temporary files (scraped data, intermediate exports). Regenerated as needed.
tools/                       # Python scripts for deterministic execution
workflows/                   # Markdown SOPs defining what to do and how
frontend/                    # Web interface (FastAPI + HTML/JS)
  server.py                  # FastAPI backend
  static/                    # index.html, style.css, app.js
clients/                     # One folder per client — isolated context and projects
  <slug>/
    context/                 # Knowledge and business rules for this client
      negocio/               # Business context
      conteudo/              # Content style and tone
      pesquisas/             # Research notes
      memoria/               # Persistent memory across sessions (preferencias, historico, voz_marca)
    projects/                # Client deliverables and active projects
    client.json              # Client metadata: name, slug, active workflows, paths
    .env                     # Client-specific API keys (NEVER store secrets anywhere else)
docs/                        # Design specs and documentation (flat — no subfolders by tool or plugin)
gemini/                      # Gemini sandbox — read/write only by call_gemini_api.py
credentials.json, token.json # Google OAuth (gitignored)
```

**Folder hygiene rules (non-negotiable):**
- NEVER create folders named after tools, plugins, or frameworks inside this project (`superpowers/`, `gsd/`, `claude/`, etc.)
- `docs/` is flat — specs and references go directly in `docs/`, no nested tool folders
- Plugin and skill infrastructure lives in `~/.claude/` — never bleeds into project directories
- If a skill or workflow tries to create a tool-specific subfolder, override it and use the correct project path instead

**Active client:** When operating via the WAT Studio frontend, read `client.json` from the active client folder to know which context to load, which workflows are available, and where to persist memory.

**Core principle:** Local files are just for processing. Anything the client needs to see or use lives in cloud services. Everything in `.tmp/` is disposable.

## Session Protocol

**At the start of any client session:**
1. Read `workflows/session_router.md` — always first, before anything else
2. Read `clients/<slug>/client.json` to identify context paths, active workflows, and metadata
3. Check `gemini/briefs/` for a recent brief (same day) before reading raw context files
4. Read all files in `clients/<slug>/context/memoria/` only if no current Gemini brief exists

**At the end of any client session:**
1. Update the relevant memory files with new learnings, preferences, or decisions
2. Document any tool/environment gotchas in the relevant workflow's Edge Cases — not here

**Environment and tool gotchas belong in workflow Edge Cases sections, not in this file.**

## Bottom Line

You sit between what I want (workflows) and what actually gets done (tools). Your job is to read instructions, make smart decisions, call the right tools, recover from errors, and keep improving the system as you go.

Stay pragmatic. Stay reliable. Keep learning.

---
