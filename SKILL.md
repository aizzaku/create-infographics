---
name: create-infographics
description: >
  Creates production-grade infographics as HTML, PNG, and PDF from any data or brief.
  Use when asked for an infographic, visual summary, one-pager, data visualization,
  or to convert tables, stats, timelines, or comparisons into a visual format.
  Also triggers on: "shareable graphic", "visual report", "poster" + data content,
  "one-pager", or any request where information should be presented as a designed image.
  Crypto and Web3 triggers: tokenomics, token distribution, token economics, vesting schedule,
  allocation breakdown, airdrop guide, airdrop infographic, ecosystem map, ecosystem overview,
  ecosystem infographic, protocol explainer, game overview, game infographic, NFT showcase,
  how-it-works diagram, comparison chart, pricing graphic, listicle graphic.
  Also triggers on: "make a graphic for", "design a visual for", "create a visual",
  "turn this into an infographic", "visualize this data", "make this shareable".
dependencies: playwright>=1.40.0
---

# Infographic Skill

Works in Claude Code and any agent with filesystem + bash access.

Two modes: **Interactive Builder** (preview each component live in the browser, iterate, then assemble) and **One-Shot** (generate the full polished infographic in one pass). Both produce the same final output: HTML + PNG + PDF.

---

## Designer DNA

These infographics are **dense editorial reference material** — closer to a game cheat sheet or crypto research poster than a website. Built across 175 pieces, the signature is: maximum information density organized by strong visual hierarchy, not whitespace.

**The #1 failure mode is producing something that looks like a dark-mode SaaS landing page.** If your output has: uniform card grids, generous breathing room, paragraph descriptions, no arrows/connectors, and could pass as a Next.js marketing page — you have failed. Start over.

**The success state looks like:** A piece someone would screenshot, save to their phone, and reference later. Dense with data. Sections connected by arrows showing how concepts relate. Bullet points, not paragraphs. Tables with real data. Each section structurally different from the last. Bold borders framing content areas. Multiple content types on one canvas — tables next to flow diagrams next to stat callouts next to bullet lists.

### Anti-Frontend Checklist (run before delivery)

Before delivering ANY infographic, verify it does NOT exhibit these frontend-design anti-patterns:

- ❌ **Uniform card grids** — If every section uses the same N-column card grid, redesign. Each section should use a different layout structure.
- ❌ **Paragraph descriptions** — Body text inside components should be bullet points, not paragraphs. One line per fact. The only paragraph allowed is a 1-2 sentence intro in the hero.
- ❌ **Generous whitespace within sections** — Whitespace separates SECTIONS from each other. Within a section, content is packed tight. If you can fit more information without it looking chaotic, you should.
- ❌ **Isolated sections** — Sections should connect to each other visually. Use arrows, flow lines, or shared color coding to show how Section A's output feeds into Section B.
- ❌ **All same component type** — If 3+ sections all use "feature cards", replace at least one with a table, flow diagram, bullet list, or stat callout. Variety is mandatory.
- ❌ **No tables** — If the data has any comparison, specs, rates, tiers, or requirements, it should be in a table. Tables are the designer's primary data structure.
- ❌ **Ghost borders** — Borders should be visible. Use `rgba(primary, 0.3)` minimum, or solid colored borders. `rgba(255,255,255,0.08)` is invisible and looks like a frontend component.

**Background**: Near-black by default. The true signature range is `#060606`–`#090909` — closer to pure black than `#0A0A0A`–`#0D0D0D`. Both ends are valid, but prefer the darker end. Some pieces use medium-dark `#1a1a1a`–`#1d1d1d` (still dark, but noticeably lighter than near-black) — valid for strategy guides and flow-diagram-heavy pieces. **Light mode exceptions**: game event guides, quest cheat sheets, and bounty/pocket guides often use white/light-gray backgrounds — this is correct, not a mistake. "Whitepaper" or "report" context does NOT mean light mode unless the piece is clearly guide/educational style.

**Signature palette**: When no brand color is given, the default is project/brand-driven. Palette is almost always mixed temperature — warm + cool accent together (75% of pieces). The true defaults:
- Background: `#060606`–`#090909` near-black
- Default warm accent: **amber `#E99A00`** family (`#E99A00`–`#F6A615`) — the most common recurring primary color
- Default cool complement: teal/green (`#00E88A`, `#2ED5D7`, `#11C59A`) or blue (`#29B7FF`) — these appear far more than cyan `#00FFFF`
- Pink/magenta (`#F59AC3`, `#A764F6`) is type-specific (crypto-explainer), not a universal default
- Multiple accents can coexist on one dark infographic — mixed palette is the norm

**Display font**: All-caps, heavy weight, condensed. True hierarchy by usage across 175 pieces:
- **Bebas Neue** — 76 uses (43%), the dominant signature font
- **Teko** — 23 uses (13%), condensed, slightly wider than Bebas
- **Orbitron** — 13 uses (7%), techno/sci-fi; use for token-economics and game-overview
- **Press Start 2P** — 8 uses (5%), pixel/retro; use exclusively for pixel/retro game pieces
- **Bungee** — 6 uses (3%), bold, wide, high-energy
- **Montserrat ExtraBold/Black** — when display and body font should match
- Barlow Condensed — acceptable alternative (2 uses); not the signature

Section headers are ALWAYS all-caps. Never use Plus Jakarta Sans, Syne, Outfit, or Space Grotesk as the display font — these feel like generic frontend design, not this designer's work.

**Layout pattern**: Stacked named sections top-to-bottom. Each section gets a bold all-caps header, then its content beneath. This is the dominant structure in 13 of 15 example pieces — it maps to the **Stacked Reference** archetype. The other 4 archetypes (Flow Poster, Hub & Spoke, Stat Poster, Cheat Sheet) are secondary options — only reach for them when the stacked-sections pattern genuinely doesn't fit.

**Signature components** (use these first):
- **Full-width section separator bands** — solid dark-filled full-width bars spanning the canvas, containing the section label in all-caps. Not just a text header — a full background-colored strip. This is the dominant section-divider pattern.
- **Numbered section headers with icon prefix** — diamond `◆` or colored circle prefix before section number + name (e.g., `◆1 OVERVIEW`). Common in game guides and mechanic breakdowns.
- Bold all-caps section headers with color accent or number prefix
- Colored rounded-rectangle **border** containers (border, not fill) grouping related content
- **Vertical flow diagrams with labeled arrows** — process nodes (rectangular, colored fill) connected by thin directional arrows. Arrows ALWAYS carry text labels (action names, percentages, token names). Never unlabeled arrows in a flow diagram.
- **Branch/split flow nodes** — diamond or condition nodes where flow diverges into parallel paths, with each path labeled
- **Swim-lane architecture diagrams** — horizontal labeled bands (e.g., "AUCTIONEER LAYER" / "STRATEGY LAYER") with flow nodes inside them. Used for two-tier protocol architectures.
- **Hierarchical tree diagrams** — branching node structure (1 root → 5 columns → 3–4 levels deep). Used for crafting trees, skill trees, dependency maps.
- **Character/NFT card grid** — tight grid of small cards, each with pixel art / character image + name + colored stat bars. Standard for game-overview and ecosystem pieces.
- **Tag cloud / pill grid** — irregular rows of rounded-rectangle category pills. Used in guides and event posters to show scope/coverage.
- Flywheel/economy loop diagrams: rectangular nodes → arrows → circular cycle
- Colored pill/badge labels for tokens, tiers, rewards
- Data tables with colored cell highlights or row accents
- **Blockchain chain color-coding** (multi-chain protocols): Ethereum = blue `#627EEA`, Arbitrum = orange `#E87030`, Solana = purple `#9945FF`, BNBChain = yellow `#F3BA2F`, Base = dark blue `#0052FF`. When a protocol lists supported chains, apply these colors to the chain identifier cells.
- Inline token coloring: `$TOKEN` names in body text get their accent color
- **Neon glow / box-shadow on accent elements** (57% of pieces) — standard especially for ecosystem (73%), crypto-explainer (69%), game-overview (60%), and token-economics (53%) types
- **Outer canvas border** — thin 1–2px solid accent-colored border around the entire infographic canvas. Common in game pieces. Implemented as `body { outline: 2px solid var(--primary); }` or a wrapping container border.

**Logos are nearly universal** (95% of pieces, 166/175). Always incorporate the project logo — typically placed top-left or centered in the hero header, with the parent company/chain logo top-right. Never omit a logo when the user references a named project.

**Images are standard** (78%, 136/175): game character art, game screenshots, NFT visuals, protocol diagrams. When the user references a game or NFT project, expect to incorporate imagery.

**Decorative style — Editorial poster, not frontend UI:**
- **Thick section borders** — Major content areas get visible colored borders (`2px solid rgba(primary, 0.4)` or thicker). Not ghost borders. The border IS the section separator.
- **Horizontal rules between sections** — Full-width `1px solid rgba(255,255,255,0.15)` or colored accent rules between major sections.
- **Underlined section headers** — Section titles often have a colored underline or bottom border, not just text. Some headers sit inside colored pill badges.
- **Neon glow on key elements** — `box-shadow` glow on accent-colored elements (57% of pieces). The glow IS the accent — it draws the eye.
- **Decorative background geometry** — Radial gradient orbs in corners (`rgba(primary, 0.07)`), subtle geometric shapes. Background is NOT flat — it has depth.
- No SVG grain/noise textures. No heavy scanlines. The decoration is structural (borders, glows, geometry), not texture-based.

**Density: VERY DENSE.** This is the defining characteristic. Target 8–15 distinct content blocks per portrait-medium (1080×1440) canvas. A "content block" is a table, chart, stat callout, bullet list, flow diagram, or callout box. If your infographic has fewer than 6 content blocks on a portrait canvas, you are too sparse.

**Density by canvas size:**
- Portrait-medium (1080×1440): 8–15 content blocks
- Portrait-tall (1080×1920): 12–20 content blocks
- Landscape (1200×675): 4–8 content blocks
- Square (1080×1080): 5–10 content blocks

**Spacing rules:**
- Between major sections: 24–32px gap + a thin horizontal rule or colored border
- Within sections (between items): 8–12px gap
- Card/panel internal padding: 12–16px (NOT 24–32px — that's frontend spacing)
- Section header to content: 8–12px
- Body font size: 11–13px for dense content, 14px max for comfortable

**Content format hierarchy (prefer formats higher in the list):**
1. **Tables** — for any comparison, specs, rates, tiers, requirements, costs, stats
2. **Bullet lists** — for features, rules, steps, conditions, requirements
3. **Flow diagrams with arrows** — for processes, token flows, economy loops, how-it-works
4. **Stat callouts** — for key numbers, oversized hero stats
5. **Badges/pills** — for categories, tiers, status, chain identifiers
6. **Paragraphs** — LAST RESORT. Only for 1-2 sentence hero intros. Never inside cards/panels.

The designer's infographics read like structured data, not prose. When in doubt, use a table or bullet list.

**Arrows & connectors (71% of pieces):**
Arrows are a signature element — they show how concepts, tokens, fees, or processes flow between sections. They are NOT optional decoration.

When to use arrows:
- Token/fee flows: show where money goes (fees → treasury → buyback → burn)
- Process steps: connect numbered steps with directional arrows
- Economy loops: circular flows (stake → earn → reinvest → stake)
- Section connections: show that Section A's output feeds Section B

CSS arrow patterns:
```css
/* Arrow connector between flow boxes */
.arrow-right {
  display: flex; align-items: center; justify-content: center;
  width: 40px; color: var(--primary); font-size: 18px;
}
/* Use Phosphor: <i class="ph-bold ph-arrow-right"></i> */

/* Vertical connector line between sections */
.connector-down {
  width: 2px; height: 32px; margin: 0 auto;
  background: var(--primary);
  position: relative;
}
.connector-down::after {
  content: ''; position: absolute; bottom: -4px; left: -3px;
  border-left: 4px solid transparent; border-right: 4px solid transparent;
  border-top: 6px solid var(--primary);
}

/* Flow diagram row */
.flow-row { display: flex; align-items: center; gap: 0; }
.flow-node {
  flex: 1; padding: 12px 14px;
  border: 1.5px solid rgba(var(--primary-rgb), 0.4);
  border-radius: 8px; background: rgba(var(--primary-rgb), 0.06);
}
```

**Rule:** If the infographic explains a process, economy, or flow — arrows are mandatory. If there are 3+ related sections — at least one connector arrow should show the relationship.

---

## Non-Negotiable Rules

These apply to every infographic in every mode, no exceptions:

1. **Never fabricate data.** Only use statistics, figures, or facts explicitly provided in the input. Do not invent survey sizes, supporting stats, or contextual numbers — even plausible-sounding ones.
2. **No generic display fonts.** Never use Inter, Roboto, Arial, Helvetica, Plus Jakarta Sans, Syne, or Outfit as the display/heading font. Use Bebas Neue, Teko, Orbitron, Bungee, or Rajdhani.
3. **No emojis as icons.** Use Phosphor Icons exclusively for all UI icons:
   ```html
   <script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
   ```
   Usage: `<i class="ph ph-rocket"></i>` · `<i class="ph-bold ph-shield-check"></i>` · `<i class="ph-fill ph-star"></i>`
4. **Brand color first.** If the user provides a hex color or logo, derive the palette from it — don't default to generic tech blue/purple.
5. **Dark mode is the default.** Use near-black background (`#060606`–`#090909`) unless the user explicitly requests light mode. "Whitepaper", "report", "institutional" — none of these override dark mode.

---

## Platform Sizing

**Default when no platform specified: portrait-medium (3:4, ~1080×1440px).** This is the most common format in the body of work (41% of 175 pieces). Use it unless the user specifies a platform.

| Platform | Width | Height | CSS |
|----------|-------|--------|-----|
| **Portrait-medium (default)** | **1080px** | **1440px** | `width:1080px; margin:0 auto; height:1440px; overflow:hidden` |
| Twitter/X | 1200px | 675px | `width:1200px; margin:0 auto; height:675px; overflow:hidden` |
| Instagram post | 1080px | 1080px | `width:1080px; margin:0 auto; height:1080px; overflow:hidden` |
| Instagram portrait | 1080px | 1350px | `width:1080px; margin:0 auto; height:1350px; overflow:hidden` |
| LinkedIn | 1200px | 627px | `width:1200px; margin:0 auto` |
| Pinterest | 1000px | 1500px | `width:1000px; margin:0 auto` |
| Website | 1100px | auto | `max-width:1100px; margin:0 auto` |

For PNG export, pass the matching `--width` flag: `python scripts/export.py --input x.html --output x --width 1200`

---

## Design Brief (Run First — Before Everything Else)

Before mode detection or any design work, collect the design brief. Run this as a single message with all unanswered questions.

**3 questions to ask:**

1. **Brand** — project name, logo URL or hex color (or "none")
2. **Platform** — Twitter/X | Instagram | Default (portrait 1080×1440)
3. **Key insight** — the one number or fact viewers must remember (or "extract from data")

**Rules:**
- Run before any mode detection or design work
- If the user already answered a question in their initial message, skip it — don't re-ask
- If the user says "just do it", "skip", or doesn't answer, proceed with defaults and note the assumptions

**Defaults when skipped:**
- Brand → signature palette: amber `#E99A00` + teal/blue complement on `#070707`–`#090909`
- Platform → portrait-medium (1080×1440)
- Key insight → extract the most striking number from the data

---

## Layout Intent (Before Building)

Before building, state in one sentence:
- The layout archetype you're using (from the 5 archetypes above)
- The dominant component type (what takes the most canvas space)
- The information density target (how many content blocks)

**Example:** "Stacked Reference layout, dominated by a dense allocation table and vesting timeline, targeting 10 content blocks on portrait-medium."

State this before Step 2 in Mode B and before showing the component plan in Mode A.

---

## Data → Layout Derivation

Before choosing a layout or picking component types, map the data structure to the appropriate visual format. Derive the layout from the data — never start from a template and fill it.

| Data type | Designer's solution |
|-----------|-------------------|
| Allocation / breakdown | Pie chart (SVG) + allocation table with % bars |
| Comparison (A vs B) | Dense comparison table with colored column headers |
| Process / flow | Flow diagram with arrow connectors |
| Stats / KPIs | Stat strip (full-width, 3–4 KPIs) or oversized stat callout |
| Timeline / schedule | Horizontal segmented timeline or vertical milestone list |
| Requirements / conditions | Bullet panel with checkmarks or icons |
| Tiers / levels | Tier comparison table with badge labels |
| Economy / loop | Flywheel diagram with arrows |
| Partner list / directory | Dense grid (3-col) with logo + name + category pill |

**Rule:** Look at what the data *does* (breaks down, compares, flows, lists) — the visual format follows from that. Then the layout follows from the format.

---

## Composition Archetypes

After mapping data to chart type, choose the overall canvas architecture. These archetypes are derived from the designer's actual 175-piece body of work — they describe how the real pieces are structured, not abstract design-school concepts. They apply to the full canvas, not individual components.

| Archetype | Description | When to use | Example references |
|-----------|-------------|-------------|--------------------|
| **Stacked Reference** | Dense top-to-bottom sections, each structurally different from the last. **This is the DEFAULT (70%+ of pieces).** | Token-economics, game-overview, whitepaper overview, any dense multi-topic content | `tokenomics_overview.png`, `game_whitepaper_overview.png` |
| **Flow Poster** | Central flow diagram (vertical or circular) with supporting data panels above/below or on sides. Arrows dominate the canvas. | Token economy flows, how-it-works explainers, strategy overviews | `token_ecosystem_flow.png`, `double_token_strategy_flywheel_flow.png` |
| **Hub & Spoke** | Central entity (logo, token, platform) with radiating connections to surrounding nodes. Hub owns 30–40% of canvas. | Ecosystem maps, integration networks, game economy hubs | `nft_ecosystem_overview.png` |
| **Stat Poster** | Oversized numbers/stats dominate the canvas. Minimal supporting text. Bold, immediate impact. Everything else orbits the number. | Sale stats, KPI announcements, single-metric stories | `stats.png` |
| **Cheat Sheet** | Dense multi-section reference with mixed layouts per section — tables, bullets, flow diagrams, images all on one canvas. Most editorial. | Pocket guides, game guides, airdrop guides, comprehensive overviews | `pocket_guide.png`, `farming_game_mode_mechanic_overview.png` |

**Rules:**
- **Stacked Reference is the default** — use it unless the content clearly calls for something else
- Offer these archetypes as options during Mode A's plan step (A2) and Mode B's layout derivation step (Step 4)
- The layout intent declaration should name the chosen archetype before building
- For 1-stat stories where the number is the entire message, use Stat Poster
- For CSS grid implementations of each archetype, see `resources/layout-patterns.md`

### Section Variety Rule (MANDATORY)

Every infographic with 4+ sections MUST use at least 3 different component types across its sections. This prevents the "uniform card grid" anti-pattern.

**Acceptable section variety:**
- ✅ Hero stat strip → Bullet panel → Flow diagram with arrows → Dense table → Callout boxes
- ✅ Hero → Pie chart + allocation list → Vesting timeline → Dense table → Footer
- ✅ Hero → 2-col bullet panels → Full-width comparison table → Step process → Footer

**Anti-pattern (reject):**
- ❌ Hero → 3-col feature cards → 3-col feature cards → 3-col feature cards → Footer
- ❌ Hero → Callout boxes → Callout boxes → Callout boxes → Footer

If you catch yourself repeating the same component type 3+ times in a row, stop and redesign those sections.

---

## Annotation-First Principle (Labels on Charts, Not in Legends)

All labels go directly on the chart. No separate legend unless the chart has 5+ series.

**Per chart type:**

| Chart type | Label placement |
|------------|----------------|
| Bar chart | Value label at the end of each bar (inside or outside, high-contrast) |
| Line chart | Series label at the rightmost endpoint of each line |
| Pie/donut | Percentage + category label inside the slice, or callout line outside for small slices |
| Stat cards | Label directly below/above the number — never in a separate caption block |
| Flow diagrams | Labels inline on nodes/arrows — no separate key |
| Progress bars | Percentage at the end of the fill, label above or inline |

**Legend exception:** Only use a legend when there are 5+ series and direct labeling would cause overlap. Even then, place the legend immediately adjacent to the chart — never in a footer or sidebar.

**Callout lines for key annotations:**

Use a callout line to highlight outliers, trend breaks, or threshold values:
- SVG line from the data point to a text annotation offset by 20–40px
- Annotation text: short, declarative ("Peak adoption", "+180% YoY", "Threshold")
- Line style: `stroke: var(--primary); stroke-width: 1; stroke-dasharray: 4 3` for secondary callouts; solid for the primary insight
- Insight callout box: left-border accent (`border-left: 3px solid var(--primary)`), muted background (`background: rgba(255,255,255,0.06)`), tight padding

**Threshold/benchmark lines:**

When data has a reference value (average, target, previous period):
- Draw a horizontal line across the chart at the threshold value
- Label it inline at the right edge: `"Avg: 42%"` or `"Target"`
- Style: dashed, muted color (`opacity: 0.5`) so it recedes behind the data

**Rule:** Every label that explains a data point must live next to that data point. Viewers should never have to look away from the chart to understand what they're seeing.

---

## Reduction Pass (Final Step Before Delivery)

After building — before exporting — strip everything that doesn't encode data. This is the difference between a good infographic and a great one.

**Checklist:**

- [ ] Remove gridlines that aren't needed for reading values
- [ ] Remove axis tick marks where direct labels already exist
- [ ] Replace decorative icons with whitespace, or remove entirely
- [ ] Does every color choice encode something? If not, make it gray
- [ ] Remove border/glow on any element already separated by whitespace
- [ ] Cut any text that repeats what the visual already shows
- [ ] Check data-to-ink ratio: is decoration competing with data?

**Style guidance:**

| Aesthetic | Reduction strictness |
|-----------|---------------------|
| Designer signature dark (default) | **Loose** — dense information is the point; colored borders, neon accents, and multi-color labeling all serve the style. Remove axis clutter and redundant text, but do not reduce density. |
| Editorial/Clean | Strict — every element must justify its existence |
| Corporate/Trust | Strict — remove decoration, preserve structure |
| Premium/Luxury | Moderate — decoration earns its place through refinement |
| Bold/Cyber | Loose — glows and texture serve the brand identity; don't strip them |
| Playful/Loud | Loose — saturation and energy are the point |

**Rule:** Remove axis clutter, redundant labels, and unjustified blank space. Do NOT reduce information density — this designer's work is dense and that is intentional. Whitespace separates *sections*, not content within sections.

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

### Guided Creative signals → go to Mode C
- "help me figure out the design" / "I'm not sure what style I want"
- "give me options" / "show me two approaches" / "show me two directions"
- "what would look best?" / "what do you recommend?"
- User brief is rich in content but visual direction is unclear or absent
- User expresses uncertainty about aesthetic, layout, or composition

### When in doubt
Default to **Interactive Builder**. Ask: *"Want to build this piece-by-piece so you can preview and tweak each section in your browser, generate the full infographic in one go, or should I show you two design directions to choose from first?"*

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

**Step 3 — Initialize state file:**
```json
{
  "version": "1.0",
  "project": "project-name",
  "created": "ISO-8601",
  "updated": "ISO-8601",
  "brief": {
    "brand_color": "#E99A00",
    "aesthetic": "Bold/Cyber",
    "platform": "website",
    "top_insight": "The one number or idea viewers must remember",
    "hard_constraints": ""
  },
  "metadata": {
    "platform": "website",
    "palette_name": "AMBER DARK",
    "bg": "#0D0D0D",
    "primary": "#E99A00",
    "secondary": "#E8943A",
    "font_display": "Bebas Neue",
    "font_body": "Montserrat"
  },
  "plan": [],
  "components": []
}
```
Write to `{cwd}/.infographic/{project_name}.json`.

---

### A2. Plan the Components

State the **Layout Intent** (see Layout Intent above) before showing the component plan. The archetype and density target anchor the session.

Apply the **Data → Layout Derivation** table to map each data element to its visual format before choosing components. The key insight should map to the most visually dominant component.

For 3+ components, also choose a **Composition Archetype** (see Composition Archetypes above) that governs how components are arranged on the canvas. Name it in the plan and note why it fits. Show the plan:

```
I'll break this into 4 components:

1. 📊 Bar chart — weekly hours (remote vs. office)
2. 🔄 Flow diagram — remote hiring process (5 steps)
3. 🎯 Stat callout — 3 KPIs: cost savings, satisfaction, retention
4. 📈 Line chart — productivity trend 2020–2025

Starting with #1. Ready?
```

If the content type maps to one of the 5 type playbooks (`token-economics`, `crypto-explainer`, `game-overview`, `ecosystem`, `airdrop-guide`), state it explicitly in the plan — e.g. "Applying Token-Economics Playbook" — and use that playbook's color system and component defaults throughout the session.

Get an explicit go-ahead before starting. Write the plan to `state.plan[]`.

**Component type vocabulary:**

**PRIMARY components (use these first — they produce dense editorial output):**

| Type | Visual | Use when | CSS ref |
|------|--------|----------|---------|
| `bullet_panel` | Bordered panel with compact bullet list inside | Features, rules, conditions, requirements — **DEFAULT for text content** — prefer over feature_cards always | See CSS below |
| `dense_table` | Compact table with colored row accents, td padding 6px 10px, font 11–12px | Specs, rates, requirements, comparisons — the designer's **PRIMARY data format** (see EGG HATCHING, BORPA) | See CSS below |
| `flow_with_arrows` | Boxes connected by directional arrows, horizontal or vertical | Token flows, fee flows, process steps, economy loops — **mandatory when content describes a process** | See CSS below |
| `stat_strip` | Full-width row of 3–4 KPIs with colored top borders, always at canvas top | KPI summaries, hero stat bars | See CSS below |
| `bordered_section` | Panel with 2px colored border (left accent or full) containing mixed content | Major content groupings — replaces naked card grids | See CSS below |
| `step_process` | Numbered steps with connector line or arrow between them | How-to-claim, how-to-play, onboarding flows | See CSS below |
| `tier_comparison` | Multi-column table/grid with tier badges (Gold/Silver/Bronze or equivalent) | Reward tiers, rarity levels, subscription levels | See CSS below |
| `labeled_diagram` | Central visual (chart/image/logo) with labeled callout lines or surrounding nodes | Token distribution, game mechanics hub, ecosystem overview | — |

**SUPPORTING components (use alongside primary — don't let these dominate):**

| Type | Visual | Use when |
|------|--------|----------|
| `section_block` | Bold all-caps header + content beneath | **Default container for everything** — wrap all content in named sections |
| `flywheel_loop` | Rectangular nodes → directional arrows → circular back to start | Token economies, fee loops, incentive cycles — designer's signature diagram |
| `flow_diagram` | Boxes + arrows, top-to-bottom or left-to-right | Process, steps, how-it-works — use `flow_with_arrows` for simpler linear flows |
| `stat_callout` | Large number + label | KPIs, key metrics, oversized hero stats |
| `token_pill` | Inline `$TOKEN` name colored with accent | Token name callouts within any text or table |
| `bar_chart` | Horizontal or vertical bars | Comparisons, rankings, allocations |
| `line_chart` | Line over time | Trends, growth, price history |
| `pie_chart` | SVG full pie (no hole) | % breakdown, token allocation |
| `radar_chart` | Spider/radar | Multi-axis comparisons, game stats |
| `timeline` | Horizontal or vertical milestones | Roadmap, history |
| `comparison_table` | Side-by-side columns | A vs B, feature matrix |
| `ecosystem_map` | Hub-and-spoke | Partner network, integrations |
| `progress_bars` | CSS bars | Vesting, unlock schedules |
| `icon_list` | Icon + title + 1-line description (renamed from `feature_cards`) | Benefits, features — **use sparingly**: 3+ in a row looks like a SaaS landing page. Prefer `bullet_panel` or `dense_table` instead. Never use as the primary repeating component. |

---

### Component CSS Patterns

Copy-paste ready. All use CSS vars, match designer density targets. Use these as starting points — adapt colors to project palette.

**`bullet_panel` — Bordered panel with compact bullet list**
```css
.bullet-panel {
  border: 1.5px solid rgba(var(--primary-rgb), 0.35);
  border-radius: 8px;
  padding: 14px 16px;
  background: rgba(var(--primary-rgb), 0.04);
}
.bullet-panel h4 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary);
  margin-bottom: 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(var(--primary-rgb), 0.2);
}
.bullet-panel ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.bullet-panel li {
  font-size: 12px;
  line-height: 1.45;
  color: var(--text);
  padding-left: 14px;
  position: relative;
}
.bullet-panel li::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: var(--primary);
  font-size: 10px;
}
```

**`dense_table` — Compact reference table (the designer's primary data format)**
```css
.dense-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11.5px;
}
.dense-table th {
  background: rgba(var(--primary-rgb), 0.15);
  color: var(--primary);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 6px 10px;
  text-align: left;
  border-bottom: 1.5px solid rgba(var(--primary-rgb), 0.3);
}
.dense-table td {
  padding: 5px 10px;
  color: var(--text);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  line-height: 1.4;
}
.dense-table tr:nth-child(even) td {
  background: rgba(255,255,255,0.03);
}
.dense-table tr:hover td {
  background: rgba(var(--primary-rgb), 0.06);
}
/* Accent cell for highlighted values */
.dense-table .accent { color: var(--primary); font-weight: 600; }
```

**`flow_with_arrows` — Horizontal flow nodes with arrow connectors**
```css
.flow-row {
  display: flex;
  align-items: center;
  gap: 0;
}
.flow-node {
  flex: 1;
  padding: 10px 14px;
  border: 1.5px solid rgba(var(--primary-rgb), 0.4);
  border-radius: 8px;
  background: rgba(var(--primary-rgb), 0.06);
  text-align: center;
}
.flow-node .label {
  font-size: 11px;
  font-weight: 700;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.flow-node .sub {
  font-size: 10.5px;
  color: var(--muted);
  margin-top: 3px;
}
.flow-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  flex-shrink: 0;
  color: var(--primary);
  font-size: 16px;
}
/* Vertical connector with arrowhead */
.connector-down {
  width: 2px;
  height: 28px;
  margin: 0 auto;
  background: var(--primary);
  position: relative;
}
.connector-down::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: -3px;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 6px solid var(--primary);
}
/* Usage: <div class="flow-row"><div class="flow-node">...</div><div class="flow-arrow">→</div><div class="flow-node">...</div></div> */
```

**`stat_strip` — Full-width KPI row with colored top borders**
```css
.stat-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* or repeat(3, 1fr) */
  gap: 10px;
  margin-bottom: 24px;
}
.stat-item {
  border-top: 3px solid var(--primary);
  background: rgba(var(--primary-rgb), 0.07);
  border-radius: 0 0 6px 6px;
  padding: 12px 14px;
  text-align: center;
}
.stat-item .number {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 28px;
  color: var(--primary);
  line-height: 1;
}
.stat-item .label {
  font-size: 10px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 4px;
}
```

**`bordered_section` — Visible-border content panel**
```css
/* Left-accent variant (most common) */
.bordered-section {
  border-left: 3px solid var(--primary);
  background: rgba(var(--primary-rgb), 0.04);
  border-radius: 0 8px 8px 0;
  padding: 14px 16px;
  margin-bottom: 16px;
}
/* Full-border variant */
.bordered-section-full {
  border: 2px solid rgba(var(--primary-rgb), 0.3);
  border-radius: 8px;
  padding: 14px 16px;
  background: rgba(var(--primary-rgb), 0.04);
}
.bordered-section h3 {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--primary);
  margin-bottom: 10px;
}
```

**`step_process` — Numbered steps with connector line**
```css
.step-list {
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
}
.step-list::before {
  content: '';
  position: absolute;
  left: 15px;
  top: 30px;
  bottom: 16px;
  width: 2px;
  background: rgba(var(--primary-rgb), 0.25);
}
.step-item {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  padding: 0 0 14px 0;
  position: relative;
}
.step-num {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--primary);
  color: #000;
  font-size: 12px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}
.step-content .title {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 3px;
}
.step-content .desc {
  font-size: 11px;
  color: var(--muted);
  line-height: 1.45;
}
```

**`tier_comparison` — Tier badge table**
```css
.tier-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11.5px;
}
.tier-badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.05em;
}
.tier-badge.gold   { background: rgba(255,215,0,0.2);  color: #FFD700; border: 1px solid rgba(255,215,0,0.4); }
.tier-badge.silver { background: rgba(192,192,192,0.2); color: #C0C0C0; border: 1px solid rgba(192,192,192,0.4); }
.tier-badge.bronze { background: rgba(205,127,50,0.2);  color: #CD7F32; border: 1px solid rgba(205,127,50,0.4); }
/* Swap colors for project-specific tiers (e.g. Diamond/Platinum/Gold) */
```

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
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
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

**Animation guidelines for preview (browser only):**

Add entrance animations to every preview component. They run in the browser only — the export script captures the post-animation final state, so PNG/PDF output is unaffected.

| Component type | Animation | Duration / easing |
|----------------|-----------|-------------------|
| Stat numbers | Count up from 0 to final value via JS counter | 800ms, ease-out |
| Bar charts | Bars animate from 0 to full width/height | 600ms, ease-out |
| Progress bars | Fill sweeps left-to-right with a glow trail at the leading edge | 600ms, ease-out |
| Feature cards | Stagger-fade in: `opacity 0→1` + `translateY 12px→0`, 80ms delay per card | 300ms per card |
| Line charts | Path draws left-to-right via `stroke-dasharray` / `stroke-dashoffset` | 900ms, ease-in-out |
| Flow diagrams | Nodes fade in sequentially, 100ms delay per node | 250ms per node |

**Implementation patterns:**

```html
<!-- Stat counter (JS) -->
<script>
function animateCount(el, target, duration) {
  const start = performance.now();
  const update = (now) => {
    const t = Math.min((now - start) / duration, 1);
    const ease = 1 - Math.pow(1 - t, 3); // ease-out cubic
    el.textContent = Math.round(ease * target).toLocaleString();
    if (t < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
document.querySelectorAll('[data-count]').forEach(el => {
  animateCount(el, parseInt(el.dataset.count), 800);
});
</script>
<!-- Usage: <span data-count="74">0</span> -->

<!-- Bar chart (CSS transition) -->
<style>
.bar { width: 0; transition: width 600ms ease-out; }
</style>
<script>
requestAnimationFrame(() => {
  document.querySelectorAll('.bar').forEach(b => b.style.width = b.dataset.width);
});
</script>
<!-- Usage: <div class="bar" data-width="74%"></div> -->

<!-- Feature card stagger (CSS) -->
<style>
.card { opacity: 0; transform: translateY(12px); transition: opacity 300ms ease, transform 300ms ease; }
</style>
<script>
document.querySelectorAll('.card').forEach((card, i) => {
  setTimeout(() => { card.style.opacity = 1; card.style.transform = 'none'; }, i * 80);
});
</script>

<!-- SVG line draw -->
<style>
.chart-path {
  stroke-dasharray: var(--path-length);
  stroke-dashoffset: var(--path-length);
  animation: drawLine 900ms ease-in-out forwards;
}
@keyframes drawLine { to { stroke-dashoffset: 0; } }
</style>
<script>
document.querySelectorAll('.chart-path').forEach(path => {
  const len = path.getTotalLength();
  path.style.setProperty('--path-length', len);
});
</script>
```

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
  - Section padding, grid layout, background, full palette
  - **Footer is the default** (present in 60% of pieces). Include a small attribution/logo strip at the bottom unless the user explicitly says to omit it. Footer content: small project logo + chain/platform mark + one-line tagline.
  - Decorative elements (glows, background blobs, noise texture)
- Use `metadata` from state for all design tokens

**Assembly layout rules:**
- 1 component → centered full-width
- 2 components → 2-col or stacked depending on types
- 3+ components → use archetype layout from `resources/layout-patterns.md`
- Platform sizing overrides layout when specified (see Platform Sizing table)

**Step 3 — Reduction Pass:**

Run the **Reduction Pass** (see above) on the assembled HTML before exporting. Apply strictness based on the aesthetic declared in the brief.

**Step 4 — Write and export:**
```bash
# Write assembled HTML to:
{cwd}/.infographic/{project_name}.html

# Export PNG + PDF + SVG (for Figma / Illustrator / Affinity):
python scripts/export.py --input .infographic/{project_name}.html --output .infographic/{project_name} --width {W} --scale 2
```

SVG export requires Inkscape or pdf2svg. If neither is installed, the script prints install instructions and notes that the PDF can be dragged directly into Figma as a fallback.

**Step 5 — Offer the Live Editor Block** (see bottom of this file).

---

## Mode B — One-Shot Infographic

### Step 1 — Brief

Run the **Design Brief** (see above) if not already answered. 3 questions: brand, platform, key insight. Skip any already answered.

---

### Step 2 — Classify + Archetype + Layout Intent

In three sentences:

1. **Content type** — identify which playbook type applies or the closest generic archetype. **Crypto/Web3 playbooks:** `token-economics`, `crypto-explainer`, `game-overview`, `ecosystem`, `airdrop-guide`, `token-flywheel`, `staking-yield`, `defi-protocol`, `roadmap`, `stats-poster`, `whitepaper-overview`, `game-event`, `game-cheat-sheet`. **Generic archetypes:** `listicle`, `feature-roster`, `modern-timeline`, `dark-modern`, `data-story`, `event-schedule`, `branded-minimal`, `light-editorial`, `how-it-works`, `comparison`, `nft-showcase`. If a playbook type applies, state it — e.g. "Content type: token-economics → applying Token-Economics Playbook." For all types, use the corresponding reference template from the Template Registry.
2. **Composition archetype** — choose from Stacked Reference (default), Flow Poster, Hub & Spoke, Stat Poster, Cheat Sheet. Default to Stacked Reference unless the content strongly implies another.
3. **Layout intent** — state archetype + dominant component + density target per the **Layout Intent** format above.

Apply the **Data → Layout Derivation** table to map each data element to its visual format. For CSS grid implementations of each archetype, see `resources/layout-patterns.md`.

---

### Step 3 — Build

Single self-contained HTML file. Required `<head>` elements:

```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
<!-- Chart.js — only include if building bar/line/radar charts -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

**Display fonts (175-piece hierarchy):** Bebas Neue (43%, default) · Teko (13%) · Orbitron (7%, tech/game) · Press Start 2P (5%, pixel only) · Bungee (3%). Never use Syne, Plus Jakarta Sans, Outfit, or Space Grotesk.

**Body font:** Montserrat (standard). Inter as fallback.

**Signature palette defaults:**

| Palette | Background | Primary | Secondary | Use for |
|---------|-----------|---------|-----------|---------|
| **Signature dark (default)** | `#060606`–`#090909` | `#E99A00` amber | teal `#00E88A` or blue `#29B7FF` | Most infographics |
| Deep navy dark | `#0A1628` | `#00E5CC` teal | `#E99A00` amber | DeFi, Web3 protocols |
| Pure black neon | `#000000` | `#A764F6` purple | `#F4BC2F` gold | Crypto-explainer |
| Editorial light | `#F7F4EF` | brand color | — | Only when explicitly requested |

For the full palette library, see `resources/color-palettes.md`.

**Typography scale:**
```css
:root {
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'Montserrat', sans-serif;
  --text-hero: clamp(48px, 6vw, 80px);
  --text-h1: clamp(28px, 3.5vw, 42px);
  --text-h2: clamp(18px, 2vw, 24px);
  --text-body: clamp(13px, 1.4vw, 16px);
  --text-stat: clamp(32px, 4vw, 56px);
}
```

Rules:
- All CSS inline — no external stylesheets
- Use CSS custom properties at `:root` for all colors, fonts, spacing
- Section padding: 24–32px vertical, card padding: 12–16px, gaps: 8–12px within sections
- Charts: inline SVG for pie (no CDN, no donut hole). Chart.js `<canvas>` for bar/line/radar
- No lorem ipsum, no placeholder text, no fabricated data
- **Footer by default** — small attribution/logo strip at the bottom. Omit only if the user explicitly says to.

For detailed component styling, see `resources/style-details.md`.

---

### Step 4 — Quality Check

Run the **Anti-Frontend Checklist** (see Designer DNA above) on the built HTML:
- [ ] No uniform card grids — at least 3 different component types used
- [ ] No paragraph descriptions — all body text is bullet points
- [ ] Tight spacing — card padding 12–16px, body font 11–13px
- [ ] Visible borders — not ghost borders
- [ ] Arrows/connectors present if content describes a process or flow
- [ ] At least one table if data has comparisons, specs, or rates
- [ ] Content block count meets density target from Layout Intent

Then run the **Reduction Pass** (see above) — remove gridlines, redundant labels, and unjustified blank space. Do NOT reduce information density.

---

### Step 5 — Export

```bash
pip install playwright --break-system-packages -q && playwright install chromium --with-deps
python scripts/export.py --input {html_file} --output {name} --width {W} --scale 2
```

Produces `{name}.png`, `{name}.pdf`, and `{name}.svg` (SVG requires Inkscape or pdf2svg — script prints install instructions if missing).

---

## Mode C — Guided Creative

A premium UX path for users who want creative direction without micromanaging components. The key difference from Mode B: Claude shows two composition options *before writing any code*, lets the user choose, then builds in one shot.

### Step 1 — Design Brief

Run the **Design Brief** (see above) if not already collected. This mode requires the brief — if the user skips it, use defaults and proceed, but note the assumptions.

---

### Step 2 — Classify + Layout Intent

Apply the **Data → Layout Derivation** table to understand the content. Identify the content type (playbook type or generic archetype) and extract the key insight from the data. This informs the two options you'll present.

---

### Step 3 — Present Two Composition Options

Present two distinct composition approaches — **no code, no HTML yet**. Each option gets:
- A short name (can be 2-3 words)
- The composition archetype it uses
- A one-sentence description of the structure and dominant component
- Why it fits this data

Use two **different** archetypes from: Stacked Reference, Flow Poster, Hub & Spoke, Stat Poster, Cheat Sheet.

**Required format:**

```
Here are two directions for this infographic:

**Option A — 'DENSE REFERENCE'** (Stacked Reference)
Top-to-bottom stacked sections, each structurally different — allocation table, vesting timeline, bullet panel, dense data table. Every section earns its space with different content format. This works because the data has 4+ distinct topics that each need their own visual treatment.

**Option B — 'ECONOMY FLOW'** (Flow Poster)
Central flow diagram showing how tokens move through the system, with supporting tables above and below. Arrows dominate — fees, rewards, and burns are shown as directional flows. This works because the core story is a circular token economy, and the flow IS the infographic.

Which direction do you want? (Or describe a different approach and I'll build it.)
```

Rules:
- Two options only — decision fatigue kills momentum
- Options must be genuinely different, not variations of the same layout
- Each option must have a clear rationale tied to the specific data
- Do not start building until the user selects

---

### Step 4 — User Selects Direction

| User says | Action |
|-----------|--------|
| "Option A" / "A" / "first one" | Build using Option A's archetype and concept |
| "Option B" / "B" / "second one" | Build using Option B's archetype and concept |
| "Neither" / "try X instead" | Acknowledge, propose a third option or ask one clarifying question, then build |
| No preference / "you pick" | Choose the option with the strongest rationale for this data, name the choice, build |

---

### Step 5 — One-Shot Build

Build the full infographic using the chosen direction. Follow Mode B Steps 2–4 (classify + layout intent, build, quality check). The composition archetype from the chosen option constrains all layout decisions — apply it literally throughout.

---

### Step 6 — Export

```bash
python scripts/export.py --input {html_file} --output {name} --width {W} --scale 2
```

Then offer the **Live Editor Block** (see below).

---

## Quality Check

Before delivering in either mode, verify:
- [ ] No fabricated data — every number came from the input
- [ ] Display font is NOT Inter, Roboto, Arial, or Helvetica
- [ ] Phosphor Icons CDN included — no emojis as icons
- [ ] Canvas width matches platform (if user specified one)
- [ ] All input data is represented — nothing omitted
- [ ] Background mode matches request (dark by default)
- [ ] Footer included by default (omit only if user explicitly requested no footer)
- [ ] **Annotation-first:** all chart labels are directly on the chart — no legend unless 5+ series
- [ ] **Reduction pass run:** gridlines, redundant text, and unjustified decoration removed (strictness scaled to aesthetic)
- [ ] **Builder only:** assembled HTML uses verbatim approved component markup
- [ ] If a type-specific playbook exists, was it followed? (color system, font pair, component defaults)
- [ ] Is a logo present? (95% of pieces have one — omit only if user explicitly said no logo)
- [ ] For token-economics: does it include a vesting timeline or allocation visual?
- [ ] For ecosystem: are partner entries in a dense grid with category pills?
- [ ] For airdrop-guide: is there an eligibility table and a step-process section?

**Density & Editorial Quality (run these last — they catch the most common failures):**
- [ ] **Content block count:** Does the piece have at least 6 content blocks? (8+ for portrait-medium, 12+ for portrait-tall) A content block is a table, stat callout, bullet panel, flow diagram, chart, or callout box.
- [ ] **Section variety:** Are at least 3 different component types used across sections? If 3+ sections use the same type (e.g., all callout boxes), replace one with a table or bullet panel.
- [ ] **Arrow/connectors present:** If the content describes a process, economy, flow, or loop — are there directional arrow connectors? If not, add them.
- [ ] **Tables present:** If the data has comparisons, specs, tiers, rates, or requirements — is there a dense table? Tables are the primary data format.
- [ ] **Bullet points, not paragraphs:** Is all body text inside components formatted as bullet lists (not multi-sentence paragraphs)?
- [ ] **Visible borders:** Are section borders actually visible? `rgba(255,255,255,0.08)` ghost borders fail this check. Minimum: `rgba(primary, 0.25)`.
- [ ] **Tight spacing:** Is card/panel padding 12–16px (not 24–32px)? Is body font 11–13px (not 14–16px)? Is gap between items 8–12px?

---

### Common Failure Modes

If you catch yourself producing any of these patterns, stop and fix before delivering:

1. **The SaaS Landing Page** — Uniform 3-column card grids, generous whitespace, paragraph descriptions, no tables or arrows. Looks like a Next.js marketing page. Fix: Replace card grids with bullet panels + dense tables. Add arrow connectors between sections.

2. **The Dashboard** — Clean, minimal, data-sparse. Looks like a Stripe or Linear dashboard widget. Too much empty space, too few content blocks. Fix: Pack more content. Use smaller fonts (11–13px body). Tighten spacing. Add more sections.

3. **The Slide Deck** — Each section is a "slide" with one big idea and lots of empty space around it. Fix: Merge sparse sections. Increase density within each section. Use mixed layouts — not the same layout for every section.

4. **The Component Demo** — Every section uses the same component type (all callout boxes, or all feature cards, or all icon lists). Fix: Apply the Section Variety Rule — at least 3 different component types across 4+ sections.

5. **The Floating Islands** — Sections have no visual connection to each other. Each section is isolated with no arrows, connectors, or shared color coding showing relationships. Fix: Add directional arrow connectors between related sections. Use consistent color coding to show linked concepts.

---

## Type Playbooks

For the 5 major infographic types, these playbooks override the generic design system defaults in Step 5. When the content archetype maps to one of these types, apply the playbook's color system, font pair, and component defaults instead of the signature dark defaults.

---

### Token-Economics

**Data foundation:** 62/175 pieces (35% of all work)

**Color system:**
- Primary: amber `#E99A00`–`#F6A615` (warm, crypto-native, high urgency)
- Secondary: blue `#29B7FF` or grey `#4C5A6A` (cool contrast)
- Background: `#070707`–`#090909` solid (48%) or gradient (21%) or image-overlay (18%)
- Temperature: mixed warm+cool (60%), pure warm (26%)

**Typography:**
- Display: Bebas Neue (40%) · Orbitron (16%) · Teko (16%)
- Body: Montserrat (65%) · Avenir Next (19%)
- Type scale: comfortable (large stats, medium labels)

**Hero style:** full-bleed (50%) or split-layout (35%)
- Full-bleed: oversized heading dominates upper third, stats strip below
- Split: left text/stats, right pie chart or vesting graphic

**Standard component set (by prevalence in 62 pieces):**
- Callout box: 73% — always for key allocation facts
- Stats bar (3 KPIs): 55% — Total Supply / Initial Price / FDV or TGE stats
- Progress/vesting bars: 50% — segmented horizontal unlock timeline
- Footer: 56% — attribution + logo strip
- Timeline: 45% — vesting schedule (often horizontal)
- Feature cards (outlined): 40%
- Comparison/allocation table: 27%

**Glow:** moderate (53%). Geometric shapes: heavy (87%). Density: compact (81%).
**Border radius:** rounded 8–16px (39%) or slight 2–4px (32%).
**Card style:** outlined (40%), flat (26%).

**Signature layout pattern:**
Top hero (logo + oversized title + 3-stat strip) → allocation section (pie chart or segmented bar) → vesting timeline graphic (TGE lock icon + monthly blocks + endpoint %) → callout boxes for key terms → small footer

**CSS vars:**
```css
--bg: #080808; --primary: #E99A00; --secondary: #29B7FF; --text: #FFFFFF; --muted: #8B8B8B
```
**Font pair:** Bebas Neue (display) + Montserrat (body)

**Reference template:** `templates/token-economics.html`

---

### Crypto-Explainer

**Data foundation:** 29/175 pieces (17% of all work)

**Color system:**
- Primary: pink `#F59AC3` / `#F39AC6` or purple `#A764F6` (most common for this type)
- Alternatives: teal `#11C59A`, green `#4BF3B2`, amber `#F6A91A`
- Secondary: yellow/gold `#F4BC2F` or blue `#4DA0F8`
- Background: solid (45%), gradient (21%), image-overlay (21%)
- Temperature: mixed (69%), cool-dominant (21%)
- Saturation: vibrant (93%)

**Typography:**
- Display: Bebas Neue (38%) · Montserrat Bold/Black (21%) · Space Grotesk (10%) · Bungee (7%)
- Body: Montserrat (41%) · Avenir Next (24%) · Inter (21%)

**Hero style:** full-bleed (62%), split-layout (24%)

**Standard component set (by prevalence in 29 pieces):**
- Callout box: 83% — highest of all types, always present
- Footer: 59%
- Feature cards (outlined 45%, filled 31%)
- Numbered list: 24% — eligibility steps or how-to-claim
- Timeline/steps: 31%
- Comparison table: 21%

**Glow:** heavy (69%). Gradient overlays: very heavy (72%). Geometric: 93%.
**Border radius:** rounded 8–16px (59%). Density: compact (66%), comfortable (31%).
**Card style:** outlined (45%), filled (31%).

**Signature layout pattern:**
Brand header with project logo → full-bleed hero concept section with large callout → flow diagram or process cards (often with curved arrows, neon glows on key nodes) → optional comparison or numbered steps → footer

**CSS vars:**
```css
--bg: #080808; --primary: #A764F6; --secondary: #F4BC2F; --glow: rgba(167,100,246,0.3); --text: #FFFFFF; --muted: #8B8B8B
```
**Font pair:** Bebas Neue (display) + Montserrat (body)

**Reference template:** `templates/crypto-explainer.html`

---

### Game-Overview

**Data foundation:** 25/175 pieces (14% of all work)

**Color system:**
- Primary: amber/gold `#F6A91A` / `#F2BC42` (55%) OR vibrant purple `#A94CFF` / `#C24BFF` (24%)
- Secondary: complementary contrast — green `#4FE112` with amber, OR gold with purple
- Background: solid (56%), image-overlay (20%) — often uses actual game art as background
- Temperature: mixed (100%). Saturation: vibrant (96%).

**Typography — two sub-variants:**
- Standard game: Bebas Neue (48%) / Teko (12%) display · Montserrat (52%) body
- Pixel/retro game: Press Start 2P (20%) display · VT323 body · IBM Plex Mono for stats
  - Use pixel fonts when the game has retro/pixel/8-bit aesthetic
  - Use sharp (0px) border radius for pixel games, rounded for standard

**Hero style:** full-bleed (48%), split-layout (32%), boxed (16%)
- Full-bleed: game background image + title overlay, logos anchored to edges
- Split: character portrait left + metadata right (character card pattern)

**Standard component set (by prevalence in 25 pieces):**
- Feature cards (outlined 56%, filled 36%): very common
- Callout box: 64%
- Comparison table: 40% — character stats, rarity matrix, item comparison
- Footer: 52%
- Progress bars: 16% — character stats, game progression
- Timeline: 16%

**Glow:** 60%. Decorative BG elements (game art): 68%. Geometric: 68%.
**Border radius:** rounded 8–16px (60%), sharp 0px (12% for pixel games).
**Density:** compact (76%).

**Signature layout pattern:**
Game-art hero header with logo lockup → character profiles (portrait + rarity + ability grid) or game feature sections → stats comparison matrix → mechanics/economy overview → footer

**Character card grid pattern:** Game infographics frequently use a `display: grid; grid-template-columns: repeat(5, 1fr)` tight card grid — each card has a character/NFT portrait image at top, name label, and 2–4 colored horizontal stat bars beneath. Stat bars use `height: 6px; border-radius: 2px; background: var(--stat-color)` with a percentage fill. Cards have no gap or minimal 2px gap to pack tight.

**Light mode sub-variant:** Game event guides, quest cheat sheets, and bounty pocket guides in this designer's portfolio frequently use white/light backgrounds (#ffffff or #f4f5f8). If the content type is an event guide, quest walkthrough, or bounty guide — light mode is the right default for that sub-type.

**Special rule:** When user provides a game name, research the aesthetic (pixel vs 3D vs fantasy vs sci-fi) and select the appropriate font variant. Never use Bebas Neue for a pixel game.

**CSS vars:**
```css
--bg: #070707; --primary: #F6A91A; --secondary: #A94CFF; --glow: rgba(246,169,26,0.25); --text: #FFFFFF; --muted: #8B8B8B
```
**Font pair:** Bebas Neue (display) + Montserrat (body). For pixel games: Press Start 2P (display) + VT323 (body).

**Reference template:** `templates/game-overview.html`

---

### Ecosystem

**Data foundation:** 22/175 pieces (13% of all work)

**Color system:**
- Primary: teal/green `#00E88A` (most common) or `#2ED5D7` (teal-blue) or red `#D94A4B`
- Secondary: purple `#B98AFF` / `#8B45D9` or complementary accent
- Background: solid (50%), gradient (18%), image-overlay (18%)
- Temperature: mixed (82%). Saturation: vibrant (82%).

**Typography:**
- Display: Bebas Neue (55%) · Teko (14%) · Orbitron (9%)
- Body: Montserrat (77%) — heaviest Montserrat concentration of any type

**Hero style:** full-bleed (59%), boxed (36%)
- Usually includes: section label ("ECOSYSTEM OVERVIEW") as header pill, project logo, chain/platform badge

**Standard component set (by prevalence in 22 pieces):**
- Badges/tags: 100% — category pills on every partner entry
- Footer: 77% — highest footer usage of all types; always attribution
- Callout box: 50%
- Feature cards (outlined 59%): common
- Comparison/partner table: 36%

**Glow:** heavy (73%) — neon border glow on section headers. Gradient: 68%. Geometric: 82%.
**Border radius:** rounded (55%), slight (41%).
**Density:** compact (82%) — densest type; logo grids packed tight.

**Signature layout pattern:**
Branded header strip (logo left, chain/platform right) → section header pills (e.g. "INTEGRATIONS", "DEPLOYMENTS", "PARTNERS") → per-section: 3-column logo grid with partner name + category tag + one-line description → featured partner comparison table → small footer with attribution

**Special rule:** Ecosystem pieces are directory-style — dense logo rosters are the core content. Use `display: grid; grid-template-columns: repeat(3, 1fr)` for partner grids. Each entry: small logo + uppercase partner name + category pill. Section headers always use the pill/badge style with a teal neon glow.

**CSS vars:**
```css
--bg: #080808; --primary: #00E88A; --secondary: #B98AFF; --glow: rgba(0,232,138,0.2); --text: #FFFFFF; --muted: #8B8B8B
```
**Font pair:** Bebas Neue (display) + Montserrat (body).

**Reference template:** `templates/ecosystem.html`

---

### Airdrop-Guide

**Data foundation:** 17/175 pieces (10% of all work)

**Color system:**
- Primary: amber `#E79A00`–`#F0A11A` (dominant, high urgency)
- Secondary: blue `#61B8FF` / `#4DA5F0` / `#10D7F4` — amber + blue is the signature split for this type
- Background: solid (71%), image-overlay (24%)
- Temperature: mixed (94%). Saturation: vibrant (94%).

**Typography:**
- Display: Bebas Neue (47%) · Montserrat Bold/Black (24%) · Teko (18%)
- Body: Montserrat (41%) · Avenir Next (29%) · Inter (18%)

**Hero style:** full-bleed (47%), boxed (35%)

**Standard component set (by prevalence in 17 pieces):**
- Footer: 82% — near-universal
- Comparison/eligibility table: 65% — the primary data structure for this type
- Stats bar: 41%
- Callout box: 41%
- Timeline (horizontal steps): 35% — numbered claim steps
- Progress bars: 24% — vesting unlock
- Numbered list: 24% — eligibility steps or how-to-claim

**Glow:** moderate (41%). Geometric: 71%.
**Border radius:** mixed (35%), rounded 8-16px (35%), slight (29%).
**Card style:** outlined (41%), none (24%).
**Density:** compact (76%).

**Signature layout pattern:**
Hero with key airdrop stats (total allocation, TGE %, eligibility snapshot) → eligibility/tier comparison table (who qualifies, how much) → horizontal step process (numbered: connect wallet → check eligibility → claim → stake) → vesting mini-chart (TGE % + linear unlock over N months) → footer

**Special rule:** Airdrop guides have the highest comparison table prevalence of all types (65%). The table is almost always the main content. Use amber for earned/unlocked values, blue for locked/future values — this amber+blue value split is the type signature.

**CSS vars:**
```css
--bg: #080808; --primary: #E79A00; --secondary: #61B8FF; --text: #FFFFFF; --muted: #8B8B8B
```
**Font pair:** Bebas Neue (display) + Montserrat (body).

**Reference template:** `templates/airdrop-guide.html`

---

## Live Editor Block

After delivering, always offer this for easy no-code revisions:

> "Here are the editable variables. Update any values and paste back to me:"
> ```json
> {
>   "theme": { "primary_color": "current hex", "background_mode": "dark | light" },
>   "content": { "title": "current text", "subtitle": "current text" }
> }
> ```

Apply changes immediately and re-run export when the user pastes it back.

---

## Template Registry

All 24 reference templates in `templates/`. Each is a fully-built V4 Dense Editorial example — use as a starting point and substitute real content for `{{PLACEHOLDER}}` variables. Every template shares the same V4 CSS standards: 12px dense tables, `▸` bullet panels, arrow connectors, stat strips with 2px top-border accents, and Bebas Neue + Montserrat font pairing.

### Crypto / Web3 Templates

| Template | File | Primary Color | Best For |
|----------|------|---------------|----------|
| **Token Economics** | `token-economics.html` | Amber `#E99A00` | Allocation pie, vesting schedule, supply breakdown |
| **Crypto Explainer** | `crypto-explainer.html` | Purple `#A764F6` | Protocol explainers, how-it-works for DeFi/Web3 concepts |
| **Game Overview** | `game-overview.html` | Gold `#F6A91A` | GameFi launch posters, character rosters, tokenomics |
| **Ecosystem Map** | `ecosystem.html` | Green `#00E88A` | Partner directories, protocol integrations, chain ecosystems |
| **Airdrop Guide** | `airdrop-guide.html` | Amber `#E79A00` | Eligibility criteria, tier tables, claim steps, vesting |
| **Token Flywheel** | `token-flywheel.html` | Green `#00E88A` | Value accrual loops, fee→buyback→burn cycles |
| **Staking & Yield** | `staking-yield.html` | Blue `#00C9FF` | APY breakdown, staking tiers, yield source flow |
| **DeFi Protocol** | `defi-protocol.html` | Cyan `#4ECBFF` | Protocol mechanics, fee structures, risk matrices |
| **Project Roadmap** | `roadmap.html` | Purple `#B98AFF` | Phase cards, milestone tables, delivery timelines |
| **Stats Poster** | `stats-poster.html` | Amber `#E79A00` | Dominant single-stat hero, period-over-period tables |
| **Whitepaper Overview** | `whitepaper-overview.html` | Cyan `#4ECBFF` | Technical summaries, problem/solution, competitor comparisons |
| **Game Event** | `game-event.html` | Red `#FF6B6B` | Tournament schedules, prize tiers, participation guides |
| **Game Cheat Sheet** | `game-cheat-sheet.html` | Green `#00E88A` | Quick-ref class/resource tables, combat/economy tips |

### Generic Templates

| Template | File | Primary Color | Best For |
|----------|------|---------------|----------|
| **NFT Showcase** | `nft-showcase.html` | Teal `#1AA8B8` | Rarity tiers, trait distribution, collection stats |
| **How It Works** | `how-it-works.html` | Amber `#E99A00` | Step-flow explainers, mechanics breakdowns |
| **Comparison** | `comparison.html` | Cyan `#00D4FF` vs Red `#FF4D6A` | A vs B head-to-head with winner highlights |
| **Listicle** | `listicle.html` | Amber `#FFD166` | Ranked lists with scoring criteria, top-N formats |
| **Feature Roster** | `feature-roster.html` | Green `#00E88A` | Product feature cards, feature matrix, pricing tiers |
| **Modern Timeline** | `modern-timeline.html` | Purple `#B98AFF` | History/roadmap with done/active/planned track |
| **Dark Modern** | `dark-modern.html` | Cyan `#4ECBFF` | General-purpose dark overview with data panels |
| **Data Story** | `data-story.html` | Green `#00E88A` | KPI-dominant with horizontal bar charts, period tables |
| **Event Schedule** | `event-schedule.html` | Red `#FF6B6B` | Conference/event day columns, speaker grid, session table |
| **Branded Minimal** | `branded-minimal.html` | Amber `#E99A00` | Brand-forward with pullquote, gradient accent bar |
| **Light Editorial** | `light-editorial.html` | Blue `#1A4FD6` | Light-mode reports, editorial research, press-ready output |

### Template Selection Guide

| User says... | Use template |
|-------------|--------------|
| "tokenomics", "vesting", "allocation" | `token-economics.html` |
| "how does X protocol work", "explainer" | `crypto-explainer.html` or `how-it-works.html` |
| "game overview", "NFT game" | `game-overview.html` |
| "ecosystem", "partner map", "integrations" | `ecosystem.html` |
| "airdrop", "claim guide", "eligibility" | `airdrop-guide.html` |
| "flywheel", "value loop", "tokenomics cycle" | `token-flywheel.html` |
| "staking", "yield", "APR", "rewards" | `staking-yield.html` |
| "DeFi protocol", "liquidity", "AMM" | `defi-protocol.html` |
| "roadmap", "milestones", "Q1/Q2" | `roadmap.html` or `modern-timeline.html` |
| "stats", "numbers", "metrics poster" | `stats-poster.html` or `data-story.html` |
| "whitepaper", "technical overview" | `whitepaper-overview.html` |
| "tournament", "game event", "prizes" | `game-event.html` |
| "cheat sheet", "quick reference", "tips" | `game-cheat-sheet.html` |
| "NFT collection", "rarity", "traits" | `nft-showcase.html` |
| "compare X vs Y", "versus" | `comparison.html` |
| "top 10", "best", "ranked list" | `listicle.html` |
| "product features", "pricing", "plans" | `feature-roster.html` |
| "timeline", "history", "milestones" | `modern-timeline.html` |
| "data story", "report", "dashboard" | `dark-modern.html` or `data-story.html` |
| "event", "conference", "schedule" | `event-schedule.html` |
| "brand", "one-pager", "deck" | `branded-minimal.html` |
| "light mode", "report", "editorial" | `light-editorial.html` |
