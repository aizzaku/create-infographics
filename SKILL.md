---
name: create-infographics
description: >
  Creates production-grade infographics as HTML, PNG, and PDF from any data or brief.
  Use when asked for an infographic, visual summary, one-pager, data visualization,
  or to convert tables, stats, timelines, or comparisons into a visual format.
  Also triggers on: "shareable graphic", "visual report", "poster" + data content,
  "one-pager", or any request where information should be presented as a designed image.
dependencies: playwright>=1.40.0
---

# Infographic Skill

Works in Claude Code and any agent with filesystem + bash access.

Two modes: **Interactive Builder** (preview each component live in the browser, iterate, then assemble) and **One-Shot** (generate the full polished infographic in one pass). Both produce the same final output: HTML + PNG + PDF.

---

## Non-Negotiable Rules

These apply to every infographic in every mode, no exceptions:

1. **Never fabricate data.** Only use statistics, figures, or facts explicitly provided in the input. Do not invent survey sizes, supporting stats, or contextual numbers — even plausible-sounding ones.
2. **No generic display fonts.** Never use Inter, Roboto, Arial, or Helvetica as the heading/display font. Use a distinctive display font (Bebas Neue, Syne, Teko, Outfit, Plus Jakarta Sans, Space Grotesk).
3. **No emojis as icons.** Use Phosphor Icons exclusively for all UI icons:
   ```html
   <script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
   ```
   Usage: `<i class="ph ph-rocket"></i>` · `<i class="ph-bold ph-shield-check"></i>` · `<i class="ph-fill ph-star"></i>`
4. **Brand color first.** If the user provides a hex color or logo, derive the palette from it — don't default to generic tech blue/purple.
5. **Honor explicit background requests.** If the user says "light background" or "no dark theme", use white/off-white. Default to dark only when the user doesn't specify.

---

## Platform Sizing

| Platform | Width | Height | CSS |
|----------|-------|--------|-----|
| Twitter/X | 1200px | 675px | `width:1200px; height:675px; overflow:hidden` |
| Instagram post | 1080px | 1080px | `width:1080px; height:1080px; overflow:hidden` |
| Instagram portrait | 1080px | 1350px | `width:1080px; height:1350px; overflow:hidden` |
| LinkedIn | 1200px | 627px | `width:1200px` |
| Pinterest | 1000px | 1500px | `width:1000px` |
| Website / default | 1100px | auto | `max-width:1100px` |

For PNG export, pass the matching `--width` flag: `python scripts/export.py --input x.html --output x --width 1200`

---

## Mode Detection

Classify the request before doing anything else.

### One-Shot signals → go to Mode B
- "create an infographic about X"
- User provides a complete data brief in one message
- "generate", "make me an infographic", "build this infographic"
- User says "assemble" or "finalize" after a builder session

### Interactive Builder signals → go to Mode A
- "show me each", "one by one", "piece by piece", "step by step", "let me iterate"
- Request for a **single** component: "show me a bar chart of X", "create a flow for Y"
- Incomplete or exploratory brief: "I'm not sure exactly what I want yet"
- "I want to refine as we go", "preview before finalizing"
- A `.infographic/{project}.json` state file already exists for this project

### When in doubt
Default to **Interactive Builder**. Ask: *"Want to build this piece-by-piece so you can preview and tweak each section in your browser, or generate the full infographic in one go?"*

---

## Mode A — Interactive Builder

### A1. Session Start & State Check

**Step 1 — Check for existing project:**
```
Look for: {cwd}/.infographic/{project_name}.json
```
- Found → load it, report approved count, ask to continue or restart
- Not found → ask for a project name (used for the state file and output filenames)

**Step 2 — Ensure the preview server is running:**
```bash
curl -s http://localhost:7783/__mtime__ > /dev/null 2>&1 || python scripts/preview_server.py &
```
Tell the user once: *"Preview server running at http://localhost:7783 — open it in your browser. It auto-refreshes on every render."*

Do not repeat this message on subsequent components.

**Step 3 — Confirm design constants** (ask only what isn't known yet):
- Platform (Twitter/X, Instagram, LinkedIn, website — default: website)
- Brand color or palette preference (default: AMBER DARK)
- Light or dark background (default: dark)

**Step 4 — Initialize state file:**
```json
{
  "version": "1.0",
  "project": "project-name",
  "created": "ISO-8601",
  "updated": "ISO-8601",
  "metadata": {
    "platform": "website",
    "palette_name": "AMBER DARK",
    "bg": "#0D0D0D",
    "primary": "#E99A00",
    "secondary": "#E8943A",
    "font_display": "Bebas Neue",
    "font_body": "Inter"
  },
  "plan": [],
  "components": []
}
```
Write to `{cwd}/.infographic/{project_name}.json`.

---

### A2. Plan the Components

Before building anything, decompose the infographic into individual components and show the plan:

```
I'll break this into 4 components:

1. 📊 Bar chart — weekly hours (remote vs. office)
2. 🔄 Flow diagram — remote hiring process (5 steps)
3. 🎯 Stat callout — 3 KPIs: cost savings, satisfaction, retention
4. 📈 Line chart — productivity trend 2020–2025

Starting with #1. Ready?
```

Get an explicit go-ahead before starting. Write the plan to `state.plan[]`.

**Component type vocabulary:**

| Type | Visual | Use when |
|------|--------|----------|
| `bar_chart` | Horizontal or vertical bars | Comparisons, rankings, allocations |
| `line_chart` | Line over time | Trends, growth, price history |
| `pie_chart` | SVG full pie (no hole) | % breakdown, token allocation |
| `radar_chart` | Spider/radar | Multi-axis comparisons, game stats |
| `stat_callout` | Large number + label | KPIs, key metrics, hero stats |
| `flow_diagram` | Boxes + arrows | Process, steps, how-it-works |
| `timeline` | Horizontal or vertical milestones | Roadmap, history |
| `comparison_table` | Side-by-side columns | A vs B, feature matrix |
| `ecosystem_map` | Hub-and-spoke | Partner network, integrations |
| `progress_bars` | CSS bars | Vesting, unlock schedules |
| `feature_cards` | Icon + title + body | Benefits, features, explainers |

---

### A3. Render Component to Browser Preview

For each component, write a **full self-contained HTML file** to `.infographic/.preview.html`. The preview server watches this file and the browser tab auto-reloads.

**The preview file must be a complete HTML document** (not a fragment) — it loads in a real browser tab, not a sandbox:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{Component Label} — Preview</title>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
  <!-- Add Chart.js only if this component uses it -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script> -->
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0D0D0D;         /* or the project bg color */
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 48px;
    }
    .component-wrapper {
      width: 100%;
      max-width: 900px;            /* generous but not full-canvas width */
    }
    /* All component CSS inline here using project palette vars */
    :root {
      --bg: #0D0D0D;
      --primary: #E99A00;
      --secondary: #E8943A;
      --text: #FFFFFF;
      --muted: #8B8B8B;
      --border: rgba(255,255,255,0.1);
    }
  </style>
</head>
<body>
  <div class="component-wrapper">
    <!-- Component HTML here — full fidelity, with gradients, glows, shadows -->
  </div>
</body>
</html>
```

Preview components use **full design fidelity** — gradients, box-shadows, glows, all of it. This is a real browser, not an iframe sandbox, so nothing is restricted.

After writing the file, tell the user:
> "Component rendered — check your browser tab."

Then immediately ask:
> "Does this look right? Say **approve** to lock it in, or tell me what to change."

---

### A4. Approval Gate

| User says | Action |
|-----------|--------|
| `approve` / `looks good` / `next` / `perfect` / `✓` / `yes` | Save verbatim HTML to state, move to next component |
| Any correction or change request | Re-write `.infographic/.preview.html` only — **do NOT write to state** |
| `skip` | Mark `status: "skipped"`, move to next |
| `start over` / `scrap this` | Mark `status: "rejected"`, re-render from scratch |
| `assemble` / `finalize` / `build it` / `done` | Trigger assembly → A6 |

**Never write a component to state until the user explicitly approves it.** Revision cycles happen in the browser — state is only locked, approved markup.

---

### A5. State Persistence

After each approval, write the component to the state file immediately:

```json
{
  "id": "bar-chart-hours",
  "type": "bar_chart",
  "label": "Weekly hours worked",
  "status": "approved",
  "approved_at": "ISO-8601",
  "html": "<!-- verbatim full body content of the approved preview -->"
}
```

The `html` field stores **the exact markup of the approved component** — the full inner content, not a description, not a re-generation. Copy it verbatim from the preview file.

Confirm to the user after each write:
> "✓ Bar chart locked in. (1/4 approved) — Moving to the flow diagram."

**On session resume** (returning to a project with an existing state file): load the state, report what's approved, continue from where the plan left off.

---

### A6. Assembly

Triggered when the user says `assemble`, `finalize`, `build it`, or `done`.

**Step 1 — Confirm scope:**
```
Ready to assemble. Here's what I'll include:

✓ Bar chart — weekly hours (approved)
✓ Flow diagram — hiring process (approved)
✓ Stat callout — 3 KPIs (approved)
⏭ Line chart — productivity (skipped)

Building now...
```

**Step 2 — Build the full HTML:**
- Load all `approved` components from state
- Place their `html` content **verbatim** — do not regenerate, do not modify
- Wrap in the full design system shell:
  - Branded header: project name + platform badge
  - Footer: disclaimer + source attribution
  - Section padding, grid layout, background, full palette
  - Decorative elements (glows, background blobs, noise texture)
- Use `metadata` from state for all design tokens

**Assembly layout rules:**
- 1 component → centered full-width
- 2 components → 2-col or stacked depending on types
- 3+ components → use archetype layout from `resources/layout-patterns.md`
- Platform sizing overrides layout when specified (see Platform Sizing table)

**Step 3 — Write and export:**
```bash
# Write assembled HTML to:
{cwd}/.infographic/{project_name}.html

# Export PNG + PDF + SVG (for Figma / Illustrator / Affinity):
python scripts/export.py --input .infographic/{project_name}.html --output .infographic/{project_name} --width {W} --scale 2
```

SVG export requires Inkscape or pdf2svg. If neither is installed, the script prints install instructions and notes that the PDF can be dragged directly into Figma as a fallback.

**Step 4 — Offer the Live Editor Block** (see bottom of this file).

---

## Mode B — One-Shot Infographic

### Step 1 — Read and classify

Identify the input type and pick a content archetype:

| Archetype | Use when |
|-----------|----------|
| **listicle** | ranked list, top-N, tips |
| **how-it-works** | numbered steps, process, workflow |
| **comparison** | A vs B, side-by-side columns |
| **data-story** | stats-heavy, KPIs, survey results |
| **timeline** | roadmap, milestones, history |
| **token-economics** | crypto allocation, vesting, supply split |
| **ecosystem** | partner map, integration network |
| **game-overview** | game features, characters, mechanics |
| **airdrop-guide** | claim steps, eligibility, vesting rules |

For charts, see `resources/charts.md`. For layout recipes per archetype, see `resources/layout-patterns.md`.

---

### Step 2 — Design system

**Your default display fonts (pick one, don't repeat across consecutive runs):**
- `Bebas Neue` — condensed, bold, all-caps labels (your dominant font, 76/175 infographics)
- `Teko` — condensed, gaming/esports/tokenomics (23/175)
- `Syne` — ultra-modern, DeFi, tech startups
- `Plus Jakarta Sans` — premium humanist, reports, ecosystems
- `Outfit` — contemporary general use, accessible
- `Space Grotesk` — Web3, clean, modern

**Body font:** Inter (93% of your infographics — your standard).

**Your signature palette defaults** (use when no brand color is given):

| Palette | Background | Accent | Use for |
|---------|-----------|--------|---------|
| Default dark | `#0D0D0D` | `#E99A00` (amber) | Most infographics |
| Cyber teal | `#0D0D0F` | `#00E5CC` | Web3, DeFi, tech |
| Deep navy | `#0A1628` | `#4F9EFF` | Crypto, gaming |
| Editorial light | `#F7F4EF` | brand color | When user requests light mode |

For the full curated palette library, see `resources/color-palettes.md`.

**Typography scale:**
```css
:root {
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'Inter', sans-serif;
  --text-hero: clamp(48px, 6vw, 80px);
  --text-h1: clamp(28px, 3.5vw, 42px);
  --text-h2: clamp(18px, 2vw, 24px);
  --text-body: clamp(13px, 1.4vw, 16px);
  --text-stat: clamp(32px, 4vw, 56px);
}
```

---

### Step 3 — Build

Single self-contained HTML file. Required `<head>` elements:

```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
<!-- Chart.js — only include if building bar/line/radar charts -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

Rules:
- All CSS inline — no external stylesheets
- Use CSS custom properties at `:root` for all colors, fonts, spacing
- 8px grid (section padding: 48–64px vertical, card padding: 24–32px, gaps: 16–24px)
- Charts: inline SVG for pie (no CDN, no donut hole). Chart.js `<canvas>` for bar/line/radar
- No lorem ipsum, no placeholder text, no fabricated data

For detailed component styling, see `resources/style-details.md`.

---

### Step 4 — Export

```bash
pip install playwright --break-system-packages -q && playwright install chromium --with-deps
python scripts/export.py --input {html_file} --output {name} --width {W} --scale 2
```

Produces `{name}.png`, `{name}.pdf`, and `{name}.svg` (SVG requires Inkscape or pdf2svg — script prints install instructions if missing, and notes the PDF can be dropped into Figma directly as a fallback).

---

## Quality Check

Before delivering in either mode, verify:
- [ ] No fabricated data — every number came from the input
- [ ] Display font is NOT Inter, Roboto, Arial, or Helvetica
- [ ] Phosphor Icons CDN included — no emojis as icons
- [ ] Canvas width matches platform (if user specified one)
- [ ] All input data is represented — nothing omitted
- [ ] Background mode matches request (dark by default)
- [ ] **Builder only:** assembled HTML uses verbatim approved component markup

---

## Live Editor Block

After delivering, always offer this for easy no-code revisions:

> "Here are the editable variables. Update any values and paste back to me:"
> ```json
> {
>   "theme": { "primary_color": "current hex", "background_mode": "dark | light" },
>   "content": { "title": "current text", "subtitle": "current text", "footer": "current text" }
> }
> ```

Apply changes immediately and re-run export when the user pastes it back.
