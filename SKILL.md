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

Creates information-dense visual infographics that look hand-crafted — not AI-generated. Output: HTML (interactive) + PNG (retina) + PDF.

---

## Non-Negotiable Rules

These apply to every infographic, no exceptions:

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

## Workflow

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
  --font-display: 'Bebas Neue', sans-serif; /* or your chosen display font */
  --font-body: 'Inter', sans-serif;
  --text-hero: clamp(48px, 6vw, 80px);
  --text-h1: clamp(28px, 3.5vw, 42px);
  --text-h2: clamp(18px, 2vw, 24px);
  --text-body: clamp(13px, 1.4vw, 16px);
  --text-stat: clamp(32px, 4vw, 56px);
}
```

### Step 3 — Build

Single self-contained HTML file. Required `<head>` elements:

```html
<!-- Google Fonts — replace with your chosen pair -->
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<!-- Phosphor Icons — required for all UI icons -->
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
<!-- Chart.js — only include if building bar/line/radar charts -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

Rules:
- All CSS inline — no external stylesheets
- Use CSS custom properties at `:root` for all colors, fonts, spacing
- 8px grid (section padding: 48–64px vertical, card padding: 24–32px, gaps: 16–24px)
- Charts: inline SVG for donut/pie (no CDN). Chart.js `<canvas>` for bar/line/radar (renders correctly in Playwright)
- No lorem ipsum, no placeholder text, no fabricated data

For detailed component styling (borders, shadows, decorative effects), see `resources/style-details.md`.

### Step 4 — Export

```bash
pip install playwright --break-system-packages -q && playwright install chromium --with-deps
python scripts/export.py --input {html_file} --output {name} --width {W} --scale 2
```

`--serve` is on by default — Google Fonts and Phosphor Icons CDN load correctly. Produces `{name}.png` and `{name}.pdf`.

---

## Quality Check

Before delivering, verify:
- [ ] No fabricated data — every number and figure came from the input
- [ ] Display font is NOT Inter, Roboto, Arial, or Helvetica
- [ ] Phosphor Icons CDN loaded — no emojis anywhere as icons
- [ ] Canvas width matches platform (if user specified one)
- [ ] All input data is represented — nothing omitted
- [ ] Single self-contained HTML file
- [ ] Background mode matches user's request (or dark by default)

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
