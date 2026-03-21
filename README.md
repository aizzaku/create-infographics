# create-infographics

A Claude Code skill for generating production-grade infographics as HTML, PNG, and PDF — built from a library of 175+ real designs.

Outputs match hand-crafted designer work: dense editorial layouts, distinctive typography, brand-derived palettes, and zero AI-generic aesthetics.

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

The CLI ([vercel-labs/skills](https://github.com/vercel-labs/skills)) installs to `.claude/skills/` or `~/.claude/skills/` automatically.

### Manual

```bash
# Global
git clone https://github.com/aizzaku/create-infographics ~/.claude/skills/create-infographics

# Project-local
git clone https://github.com/aizzaku/create-infographics .claude/skills/create-infographics
```

### PNG / PDF export (optional)

```bash
pip install playwright --break-system-packages
playwright install chromium --with-deps
```

---

## Usage

```
Create an infographic of our Q4 results using the data in q4.csv
```

```
Make a tokenomics breakdown — 35% community, 25% ecosystem, 20% team, 20% private. Brand color #00E5CC.
```

```
Build this piece by piece so I can preview each section before finalizing
```

---

## How It Works

**One-Shot** — provide a brief, receive finished HTML + PNG + PDF.

**Interactive Builder** — the skill decomposes the infographic into components, renders each to a live preview (`http://localhost:7783`), waits for approval, then assembles the final output. State persists to `.infographic/{project}.json` across interruptions.

### Output

| File | Use |
|------|-----|
| `{name}.html` | Self-contained, shareable, embeddable |
| `{name}.png` | 2x retina, ready for social / print |
| `{name}.pdf` | Print-ready, importable into Figma / Illustrator |

---

## Design System

Derived from 175 real infographics. Dense editorial style — cheat sheets, flow diagrams, data-packed tables, asymmetric layouts — not SaaS dashboards.

- **Typography** — Bebas Neue, Teko, Syne, Space Grotesk, Plus Jakarta Sans
- **Color** — Dark-first (`#0D0D0D`); brand color from user input; charts use primary color shades
- **Charts** — Inline SVG for allocation; Chart.js for line/bar/radar; CSS for progress bars and vesting strips
- **Icons** — Phosphor Icons exclusively
- **Spacing** — 8px grid; compact and comfortable density modes

### Templates

| Template | Use case |
|----------|----------|
| `token-economics` | Allocation, vesting, supply split |
| `token-flywheel` | Token utility loops and flywheel mechanics |
| `staking-yield` | Staking tiers, APY, reward flows |
| `airdrop-guide` | Claim steps, eligibility, vesting rules |
| `crypto-explainer` | Protocol explainer, how-it-works |
| `defi-protocol` | DeFi mechanics, liquidity flows |
| `whitepaper-overview` | Project summary, key pillars |
| `ecosystem` | Partner map, integration network |
| `game-overview` | Game features, mechanics, characters |
| `game-cheat-sheet` | Dense reference sheet for game systems |
| `game-event` | Event schedule, rewards, participation guide |
| `nft-showcase` | Collection breakdown, rarity, traits |
| `feature-roster` | Product features, team roster |
| `comparison` | A vs B, feature matrix |
| `data-story` | Stats-heavy, KPIs, survey results |
| `stats-poster` | Key numbers, metrics highlight |
| `listicle` | Ranked lists, top-N, tips |
| `modern-timeline` | Roadmap, milestones, history |
| `roadmap` | Phased roadmap with deliverables |
| `event-schedule` | Conference/event agenda |
| `how-it-works` | Numbered steps, process flows |
| `light-editorial` | Light-mode editorial layout |
| `dark-modern` | Dark-mode general purpose |
| `branded-minimal` | Minimal, brand-forward layout |

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
├── templates/                 # 24 reference HTML templates
├── examples/                  # PNG reference outputs for calibration
└── evals/                     # Automated quality evaluation suite
```

---

## Claude.ai (no CLI)

Upload `SKILL.md` to a Claude.ai Project as a knowledge file. PNG/PDF export requires running `scripts/export.py` locally after saving the HTML.

---

## Requirements

- Claude Code CLI, or any agent with filesystem and bash access
- Python 3.8+ (for export only)
- Playwright + Chromium (for export only)
