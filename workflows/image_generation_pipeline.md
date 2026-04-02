# Workflow: Image Generation Pipeline

## Objective

Generate images (illustrations, banners, assets) for landing pages and websites using Nano Banana / Gemini, automatically deciding which of the three routes to use based on cost, context, and required quality.

## Required Inputs

- `image_descriptions`: List of images to generate (description of each one)
- `style`: Desired visual style (e.g., flat illustration, 3D, minimalist, photorealistic)
- `remove_background`: `true` or `false` — whether images need a transparent background (PNG)
- `route`: `auto`, `flow`, `api`, or `manus` (see routes below)

## The Three Routes

### Route 1 — Flow (Free)
**When to use:** Personal projects, tests, prototypes, when there is no urgency
**How:** Access Nano Banana Flow, generate manually, download and save to `images/`
**Limitation:** Manual, cannot be automated via script

### Route 2 — Direct API (Paid, automated)
**When to use:** High volume of images, client project, automated pipeline
**How:** Claude Code calls the Gemini API directly to generate the images
**Cost:** Paid per API usage — always confirm with the user before triggering

### Route 3 — Via Manus (Paid, background removal included)
**When to use:** When you need illustrations without background (transparent PNG) ready to use
**How:** Claude Code sends tasks to Manus, which generates the images and delivers them with the background already removed
**Advantage:** Saves the background removal step — the PNG comes ready

## Tools

- `tools/generate_images_api.py` — Route 2: Gemini API call
- `tools/generate_images_manus.py` — Route 3: Manus integration

## Process

### Step 1 — Decide the route

If `route` is `auto`, use this decision logic:

```
remove_background = true?
  → Route 3 (Manus) — delivers ready transparent PNG

Volume > 5 images AND client project?
  → Route 2 (API) — automated and traceable

Otherwise?
  → Route 1 (Flow) — free, no setup
```

Confirm with the user before using any paid route (2 or 3).

### Step 2 — Prepare the prompts

For each image in `image_descriptions`, write a structured prompt:

```
[style], [object/scene description], [predominant color], [background],
[composition], no text, high quality
```

Example:
```
flat illustration, laptop with code on screen, blue and white tones,
white background, centered composition, no text, high quality
```

Save the prompts to `.tmp/image_prompts_<project_name>.json`.

### Step 3 — Execute the generation

**Route 1 (Flow — manual):**
Present the formatted prompts for the user to copy into Nano Banana Flow. Wait for the user to download and move to `images/`.

**Route 2 (API):**
```bash
python tools/generate_images_api.py .tmp/image_prompts_<project_name>.json --output images/
```

**Route 3 (Manus):**
```bash
python tools/generate_images_manus.py .tmp/image_prompts_<project_name>.json --output images/ --remove-bg
```

### Step 4 — Verify and apply

1. Confirm all files are in `images/`
2. Verify that PNGs with removed backgrounds have correct transparency
3. Apply the images in the project's HTML files, replacing the placeholders

## Outputs

- Image files in `images/` (PNG or WEBP)
- Background removed when `remove_background = true`
- Images correctly referenced in the project's HTML

## Edge Cases

| Situation | How to handle |
|---|---|
| Route 2 or 3 without credentials in `.env` | Stop. Report which variables are missing. Do not proceed. |
| Generated image does not match the request | Refine the prompt by adding more style and composition specificity. Try again. |
| Background not correctly removed by Manus | Process manually or use `remove.bg` API as fallback |
| User wants to use their own images | Skip generation. Move files to `images/` and proceed to Step 4. |
| Many images with high cost | Present cost estimate before executing. Wait for approval. |

## Video References

- Channel: Mateus Dias — "CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000"
- Route 3 (Manus) highlighted as the most practical for design — PNG without background already included
- Claude Code acts as orchestrator: triggers the task, waits, downloads and applies
