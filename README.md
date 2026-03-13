# create-infographics

A Claude Code skill for generating production-grade infographics as HTML, PNG, and PDF — built from a library of 175+ real designs.

Outputs are indistinguishable from hand-crafted designer work: distinctive typography, brand-derived palettes, proper visual hierarchy, and zero AI-generic aesthetics.

---

## Installation

### Via npx (recommended)

**Project-local** (this project only):
```bash
npx skills add aizzaku/create-infographics
```

**Global** (available in all projects):
```bash
npx skills add aizzaku/create-infographics -g
```

The CLI ([vercel-labs/skills](https://github.com/vercel-labs/skills)) installs to `.claude/skills/` or `~/.claude/skills/` automatically. Claude Code discovers the skill on next launch — no restart or registration needed.

### Manual

```bash
# Global
git clone https://github.com/aizzaku/create-infographics ~/.claude/skills/create-infographics

# Project-local
git clone https://github.com/aizzaku/create-infographics .claude/skills/create-infographics
```

### PNG / PDF export (optional)

The HTML output works standalone in any browser. To also generate PNG and PDF files, install Playwright:

```bash
pip install playwright --break-system-packages
playwright install chromium --with-deps
```

---

## Usage

Trigger the skill naturally in Claude Code:

```
Create an infographic of our Q4 results using the data in q4.csv
```

```
Make a tokenomics breakdown infographic — 35% community, 25% ecosystem, 20% team, 20% private sale. Brand color #00E5CC.
```

```
Build this piece by piece so I can preview each section before finalizing
```

The skill detects whether you want a one-shot output or an interactive build session where you approve each component before assembly.

---

## How It Works

### Two modes

**One-Shot** — provide a complete brief and receive the finished HTML + PNG + PDF in one pass.

**Interactive Builder** — the skill decomposes the infographic into individual components, renders each to a live browser preview (`http://localhost:7783`), waits for your approval or revision notes, then assembles all approved components into the final output. State is persisted to `.infographic/{project}.json` so sessions survive interruptions.

### Output

Every run produces three files:

| File | Use |
|------|-----|
| `{name}.html` | Self-contained, shareable, embeddable |
| `{name}.png` | 2x retina, ready for social / print |
| `{name}.pdf` | Print-ready, importable into Figma / Illustrator |

---

## Design System

The skill carries a full design system derived from 175 real infographics:

- **Typography** — Bebas Neue, Teko, Syne, Space Grotesk, Plus Jakarta Sans (never Inter/Roboto as display)
- **Color** — Dark-first (`#0D0D0D` default); brand color derived from user input; tokenomics charts use primary color shades, not rainbow palettes
- **Charts** — Inline SVG for pie/allocation charts; Chart.js for line/bar/radar; pure CSS for progress bars and vesting strips
- **Icons** — Phosphor Icons exclusively; no emojis as UI elements
- **Spacing** — 8px grid throughout; compact (53%) and comfortable (47%) density modes

### Supported archetypes

| Archetype | Use case |
|-----------|----------|
| `token-economics` | Crypto allocation, vesting, supply split |
| `listicle` | Ranked lists, top-N, tips |
| `how-it-works` | Numbered steps, process flows |
| `comparison` | A vs B, feature matrix |
| `data-story` | Stats-heavy, KPIs, survey results |
| `timeline` | Roadmap, milestones, history |
| `ecosystem` | Partner map, integration network |
| `game-overview` | Game features, characters, mechanics |
| `airdrop-guide` | Claim steps, eligibility, vesting rules |

---

## Project Structure

```
create-infographics/
├── SKILL.md                   # Agent instructions and execution logic
├── scripts/
│   ├── export.py              # Playwright PNG/PDF export
│   └── preview_server.py      # Local auto-refresh preview server
├── resources/
│   ├── charts.md              # SVG/CSS/Chart.js component templates
│   ├── color-palettes.md      # Curated palette library
│   ├── style-details.md       # Design DNA: borders, shadows, spacing
│   ├── layout-patterns.md     # Layout recipes per archetype
│   ├── font-pairings.md       # Tested Google Font combinations
│   ├── platform-sizes.md      # Canvas dimensions for social platforms
│   └── copy-guide.md          # Text formatting and length rules
├── templates/                 # Reference HTML per archetype
├── examples/                  # PNG reference outputs for calibration
└── evals/                     # Automated quality evaluation suite
```

---

## Claude.ai (no CLI)

Upload `SKILL.md` to a Claude.ai Project as a knowledge file. Claude will follow the instructions and generate the HTML. PNG/PDF export requires running `scripts/export.py` locally after saving the HTML output.

---

## Requirements

- Claude Code CLI, or any agent with filesystem and bash access
- Python 3.8+ (for export only)
- Playwright + Chromium (for export only)
