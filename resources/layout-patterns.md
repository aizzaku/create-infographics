# Layout Patterns — Aizfographics Design DNA
# Extracted from 175 real infographics via Claude Vision analysis
# Last updated: March 2026

## Layout Statistics

```
Aspect ratios:    portrait-tall (9:16) 50% | portrait-medium 22% | landscape 19% | square 10%
Primary columns:  2-col 49% | 1-col 32% | 3-col 12% | 4+ col 7%
Hero styles:      boxed 51% | split-layout 22% | full-bleed 19%
Card styles:      outlined 46% | filled 28% | flat 6%
Alignment:        left-aligned 89% — this is your universal rule
```

---

## Your Dominant Infographic Types

| Type | Count | % | Your Primary Format |
|------|-------|---|---------------------|
| **token-economics** | 61 | 35% | portrait-tall (9:16) |
| **game-overview** | 33 | 19% | portrait-tall or square |
| **ecosystem** | 26 | 15% | landscape (16:9) or portrait-tall |
| **crypto-explainer** | 21 | 12% | landscape (16:9) |
| **airdrop-guide** | 14 | 8% | landscape or portrait-tall |
| **nft-showcase** | 9 | 5% | square (1:1) or portrait |

---

## Layout Recipes by Type

### 1. TOKEN-ECONOMICS (35% of your work — your specialty)

**Target: 10+ content blocks. Archetype: Stacked Reference (default) or Flow Poster (if economy loop is the story).**

**Most common layout (portrait-tall):**
```
HEADER BAR
  └─ [logo left] [project name + chain badge right]

HERO TITLE + SUBTITLE (2 lines max)

STATS STRIP (3–4 col, full-width)
  └─ [Total Supply] [Token Price] [FDV] [Airdrop Pool]
  └─ Each stat: colored top border, 12px label, 20px value

CORE FEATURES (2-col bullet panel)
  └─ [icon] Feature name + 1-line bullet description
  └─ Use bullet_panel component, NOT feature cards

ALLOCATION SECTION (2-col asymmetric)
  ├─ LEFT (55%): Pie/donut chart with % labels on slices
  └─ RIGHT (45%): Allocation table
      └─ Category | Amount | % — compact (6px td padding)
      └─ Color dot matching pie slice color

  ↓ [arrow connector: "allocation → vesting schedule"]

VESTING TIMELINE (full-width)
  └─ Horizontal timeline: TGE → Month 3 → Month 6 → Month 12
  └─ Lock icons + progress bars + unlock % labels
  └─ 8px internal gap, 12px padding

ROUND DETAILS TABLE (full-width dense_table)
  └─ Round | Price | Allocation | Cliff | Vest Period | TGE %
  └─ Alternating row tint, 6px/10px td padding, 11px font

CALLOUT BOXES (2–3 col)
  └─ Key terms, staking APY, utility highlights
  └─ visible 2px colored left border, NOT ghost borders

FOOTER
```

**CSS Grid:**
```css
.token-layout {
  display: grid;
  grid-template-rows: auto auto auto auto auto auto auto auto auto;
  gap: 24px; /* section gap — NOT 48px */
}
.allocation-grid {
  display: grid;
  grid-template-columns: 55% 45%;
  gap: 12px;
  align-items: start;
}
/* Section spacing — tight within, clear between */
.section-inner { gap: 8px; }
.card-padding { padding: 12px 14px; } /* NOT 24-32px */
```

---

### 2. GAME-OVERVIEW (19% — your #2 type)

**Target: 10+ content blocks. Archetype: Stacked Reference (default) or Cheat Sheet (for comprehensive guides).**

**Common layout (portrait-tall or square):**
```
HEADER (logo left + game name + publisher badge right)

HERO SECTION (boxed or split-layout)
  └─ Game title (large Bebas Neue / Teko)
  └─ Character art or key visual on right
  └─ 2-3 key stat callouts on left

STATS / KEY METRICS BAR (3–4 col, full-width)
  └─ Players | Token Price | Reward Pool | Season
  └─ Colored top border per stat

GAME MECHANICS TABLE (full-width dense_table)
  └─ Mode | Description | Reward | Requirements
  └─ NOT feature cards — use a table with real specs

  ↓ [arrow connector: "mechanics → game loop"]

GAME LOOP / HOW TO PLAY (flow_with_arrows)
  └─ Numbered steps connected by arrows
  └─ Step 1 → Step 2 → Step 3 → Step 4
  └─ Each step: bordered node with action + outcome

CHARACTER / ITEM GRID (3-col, with images)
  └─ Small portrait + name + rarity badge + key stats
  └─ Compact: 12px padding, 11px font

MATERIALS / RESOURCES TABLE (dense_table)
  └─ Item | Source | Use | Drop Rate
  └─ Only if applicable

REWARDS TABLE (tier_comparison)
  └─ Tier | Requirements | Daily Reward | Boost
  └─ Gold/Silver/Bronze badge labels

FOOTER
```

---

### 3. ECOSYSTEM (15% — partner/collaboration type)

**Target: 12+ content blocks. Archetype: Stacked Reference (default) or Hub & Spoke (if one platform is the center).**

**Common layout (landscape 16:9 or portrait-tall):**
```
BRANDED HEADER STRIP
  └─ [Logo left] [chain/platform badges right]
  └─ Full-width bar, 2px bottom border in accent color

TITLE + HERO STAT STRIP
  └─ Bold headline (uppercase, large)
  └─ Stat strip: Partners | Chains | TVL | Users

  ↓ [section pill: "INTEGRATIONS" / "DEPLOYMENTS" / "DEFI"]

CATEGORY SECTIONS (repeat per category)
  └─ Pill-badge section header (background: primary color)
  └─ 3-col partner grid (denser than v3)
      └─ [logo] [PARTNER NAME] [category pill]
      └─ 12px padding, 11px font — NOT generous card spacing

FEATURED INTEGRATIONS TABLE (dense_table, full-width)
  └─ Partner | Category | Integration Type | Status | Chain
  └─ More informative than logo grid alone

  ↓ [section pill: "PRODUCTS / SERVICES"]

PRODUCTS SECTION
  └─ 2–3 col grid: product name + 2-bullet description
  └─ Sub-categories as pill headers within section

GOVERNANCE / UTILITY BULLET PANEL
  └─ bordered_section with bullet list

FOOTER (attribution + source date)
```

---

### 4. CRYPTO-EXPLAINER (12% — educational type)

**Target: 9+ content blocks. Archetype: Flow Poster (default for protocol/economy) or Stacked Reference (for feature breakdowns).**

**Common layout (landscape 16:9):**
```
BRAND HEADER STRIP
  └─ Logo + project name + subtitle/topic

HERO CONCEPT + KEY STAT STRIP
  └─ Large concept title (2 lines max)
  └─ Stat strip: 3–4 KPIs (TVL, APY, Users, etc.)

HOW IT WORKS (flow_with_arrows, horizontal or vertical)
  └─ Step 1 → Step 2 → Step 3 → Step 4
  └─ Each node: bordered box, title + 1-line bullet
  └─ Arrows between nodes (mandatory — not optional)

COMPARISON TABLE (dense_table, full-width)
  └─ Protocol A vs B, or feature matrix, or before/after
  └─ Color-coded column headers

  ↓ [arrow connector: "comparison → economy flow"]

ECONOMY / FEE FLOW (flow_with_arrows or flywheel)
  └─ Where does value go? fees → treasury → buyback → burn
  └─ Arrow connectors with % labels

KEY PROPERTIES (bullet_panel, 2-col)
  └─ Bullet list: features, rules, conditions
  └─ NOT paragraph descriptions

CALLOUT BOXES (key terms, glossary)
  └─ Visible 2px left-border, NOT ghost borders

FOOTER
```

---

### 5. AIRDROP-GUIDE (8% — action-focused type)

**Target: 9+ content blocks. Archetype: Cheat Sheet (default — this is the most "pocket guide" type) or Stacked Reference.**

**Common layout (landscape 16:9 or portrait-tall):**
```
BRAND HEADER
  └─ Logo + project name + "AIRDROP GUIDE" label

HERO WITH KEY STATS
  └─ Headline: "HOW TO CLAIM YOUR [TOKEN] AIRDROP"
  └─ Stat strip: Total Allocation | TGE % | Snapshot Date | Deadline

OVERVIEW (bordered_section with bullet summary)
  └─ 4–6 bullets: what, who qualifies, when, how much
  └─ Visible 2px border — NOT ghost border

ELIGIBILITY TABLE (dense_table — the main content)
  └─ Tier | Requirement | Allocation | % of Pool
  └─ Color-coded tier badges (Gold/Silver/Bronze)
  └─ 65% of airdrop guides have this table — it's mandatory

  ↓ [arrow connector: "eligibility → claim steps"]

CLAIM STEPS (step_process, full-width)
  └─ 1 → 2 → 3 → 4 numbered steps with arrows
  └─ Step: Connect Wallet → Check Eligibility → Claim → Stake
  └─ Each step: bordered node + action + outcome bullet

VESTING SCHEDULE TABLE (dense_table)
  └─ Phase | Date | % Unlock | Cumulative %
  └─ NOT just a progress bar — an actual table with dates

  ↓ [vesting progress bar below table for visual reference]

PLAYER REQUIREMENTS BULLET PANEL
  └─ What you need to hold/do before snapshot
  └─ bullet_panel component with checkmarks

REWARD BREAKDOWN TABLE
  └─ Reward type | Amount | Condition | Lock period

FOOTER (warning/disclaimer)
```

---

### 6. NFT-SHOWCASE (5% — collectible type)

**Common layout (square 1:1 or portrait):**
```
HEADER BAR (logo + project name)

HERO (split-layout)
  ├─ LEFT (60%): NFT artwork / character / item
  │   └─ With rarity badge overlay
  └─ RIGHT (40%): Key attributes
      └─ Trait tags (rarity, faction, class)
      └─ Stats list

DATA TABLE (full-width)
  └─ Tier columns: Common | Rare | Epic | Legendary
  └─ Color-coded headers matching tier colors
  └─ Row data: supply, drop rate, power level

FACTION / CATEGORY ICONS
  └─ Horizontal row, centered
  └─ Small icons with labels below

FOOTER ATTRIBUTION
  └─ Small, muted
```

---

### 7. DENSE SPACING REFERENCE (apply across ALL types)

**The core spacing rule:** Whitespace separates SECTIONS from each other. Within a section, content is packed tight.

```
Between major sections:   24–32px gap + horizontal rule or colored border
Within sections (items):  8–12px gap
Card / panel padding:     12–16px (NOT 24–32px — that's frontend spacing)
Section header to body:   8–12px
Body font size:           11–13px for dense content, 14px max
Table cell padding:       6px 10px (NOT 12px 16px)
```

**Dense card grid (when cards are needed — use sparingly):**
```
┌───────────────┬───────────────┐
│ [icon] Title  │ [icon] Title  │
│ • bullet 1    │ • bullet 1    │
│ • bullet 2    │ • bullet 2    │
└───────────────┴───────────────┘
```

```css
/* Use bullet_panel instead of feature cards wherever possible */
.bullet-panel-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}
.bullet-panel {
  padding: 12px 14px;
  border: 1.5px solid rgba(var(--primary-rgb), 0.3);
  border-radius: 6px;
  background: rgba(var(--primary-rgb), 0.04);
}
.bullet-panel ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.bullet-panel li {
  font-size: 12px;
  line-height: 1.4;
  color: var(--text-secondary);
  padding-left: 14px;
  position: relative;
}
.bullet-panel li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary);
}
/* Dense card grid — only when icons/visuals are needed */
.card-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px; /* NOT 16px+ */
}
.card-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}
.card {
  padding: 12px 14px; /* NOT 20-24px */
  font-size: 12px;
}
```

**Warning:** If you have 3+ card-grid sections in a row, you're producing a SaaS landing page. Replace at least one section with a `dense_table` or `flow_with_arrows`.

---

---

## Composition Archetype CSS Implementations

CSS grid implementations for the 5 archetypes defined in SKILL.md. These map to the designer's actual structural patterns.

---

### ARCHETYPE 1: Stacked Reference (DEFAULT — 70%+ of pieces)

Dense top-to-bottom sections. Each section is structurally different from the previous. The backbone of almost every infographic.

```
┌────────────────────────────────────────┐
│  HEADER BAR                            │
├────────────────────────────────────────┤
│  HERO / TITLE + STAT STRIP             │
├────────────────────────────────────────┤
│  SECTION A (e.g. 2-col bullet panels)  │
├──────────────────────────────────── ── ┤  ← thin hr or colored border
│  SECTION B (e.g. pie chart + table)    │
├────────────────────────────────────────┤
│  SECTION C (e.g. flow diagram)         │
├────────────────────────────────────────┤
│  SECTION D (e.g. dense data table)     │
├────────────────────────────────────────┤
│  FOOTER                                │
└────────────────────────────────────────┘
```

```css
.stacked-reference-layout {
  display: flex;
  flex-direction: column;
  gap: 0; /* sections manage their own separation */
}

.stacked-section {
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.stacked-section:last-child {
  border-bottom: none;
}

.section-header {
  font-family: var(--font-display);
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--primary);
  margin-bottom: 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(var(--primary-rgb), 0.3);
}

.section-body {
  display: flex;
  flex-direction: column;
  gap: 8px; /* tight internal gap */
}
```

---

### ARCHETYPE 2: Flow Poster

Central flow diagram dominates the canvas. Arrows show how entities, tokens, or processes connect. Supporting data panels above/below.

```
┌────────────────────────────────────────┐
│  HEADER + STATS STRIP                  │
├────────────────────────────────────────┤
│                                        │
│  ┌──────┐  →  ┌──────┐  →  ┌──────┐  │
│  │ Node │     │ Node │     │ Node │  │
│  │  A   │     │  B   │     │  C   │  │
│  └──────┘     └──────┘     └──────┘  │
│       ↓              ↓               │
│  ┌──────┐       ┌──────┐             │
│  │ Node │  ←──  │ Node │             │
│  │  D   │       │  E   │             │
│  └──────┘       └──────┘             │
│                                        │
├────────────────────────────────────────┤
│  SUPPORTING DATA TABLE / BULLET PANEL  │
├────────────────────────────────────────┤
│  FOOTER                                │
└────────────────────────────────────────┘
```

```css
.flow-poster-layout {
  display: grid;
  grid-template-rows: auto 1fr auto auto;
  gap: 0;
  min-height: 100%;
}

.flow-canvas {
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.flow-row {
  display: flex;
  align-items: center;
  gap: 0;
  width: 100%;
  justify-content: center;
}

.flow-node {
  flex: 1;
  max-width: 160px;
  padding: 12px 14px;
  border: 1.5px solid rgba(var(--primary-rgb), 0.4);
  border-radius: 8px;
  background: rgba(var(--primary-rgb), 0.06);
  font-size: 12px;
}

.flow-node-title {
  font-family: var(--font-display);
  font-size: 13px;
  color: var(--primary);
  text-transform: uppercase;
  margin-bottom: 4px;
}

.flow-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  color: var(--primary);
  font-size: 16px;
  flex-shrink: 0;
}

.flow-connector-down {
  width: 2px;
  height: 24px;
  background: var(--primary);
  margin: 0 auto;
  position: relative;
}

.flow-connector-down::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: -3px;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 6px solid var(--primary);
}
```

---

### ARCHETYPE 3: Hub & Spoke

Central entity with radiating connections. The hub (logo, token, platform) owns the center. Spokes radiate outward to category nodes.

```
┌────────────────────────────────────────┐
│  HEADER                                │
├────────────────────────────────────────┤
│                                        │
│    [Node]    [Node]    [Node]          │
│       ↘        ↓        ↙             │
│    [Node] ←─[HUB]─→ [Node]           │
│       ↗        ↑        ↖             │
│    [Node]    [Node]    [Node]          │
│                                        │
├────────────────────────────────────────┤
│  CATEGORY DETAIL PANELS (2-3 col)      │
├────────────────────────────────────────┤
│  FOOTER                                │
└────────────────────────────────────────┘
```

```css
.hub-spoke-layout {
  display: grid;
  grid-template-rows: auto 1fr auto auto;
  gap: 0;
  min-height: 100%;
}

.spoke-canvas {
  position: relative;
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 300px;
}

.hub-node {
  position: relative;
  z-index: 2;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 2px solid var(--primary);
  background: rgba(var(--primary-rgb), 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(var(--primary-rgb), 0.3);
}

/* Spoke nodes: use absolute positioning around hub */
.spoke-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  width: 100%;
}

.spoke-node {
  padding: 10px 12px;
  border: 1px solid rgba(var(--primary-rgb), 0.3);
  border-radius: 6px;
  background: rgba(var(--primary-rgb), 0.04);
  font-size: 11px;
  text-align: center;
}
```

---

### ARCHETYPE 4: Stat Poster

One or a few oversized numbers dominate. Everything else is minimal and orbits the stat. Bold, immediate, screenshot-worthy.

```
┌────────────────────────────────────────┐
│  HEADER (logo + context label)         │
│                                        │
│         ████████████████               │
│              $4.2M                     │  ← hero stat (40% of canvas height)
│         TOTAL RAISED                   │
│                                        │
│  ┌─────────┬─────────┬─────────┐       │
│  │ 1,240   │  92%    │  14 days│       │
│  │investors│ sold    │ to close│       │
│  └─────────┴─────────┴─────────┘       │
│                                        │
│  FOOTER                                │
└────────────────────────────────────────┘
```

```css
.stat-poster-layout {
  display: grid;
  grid-template-rows: auto 1fr auto auto;
  gap: 0;
  min-height: 100%;
}

.stat-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem 1.5rem;
  gap: 8px;
}

.hero-number {
  font-family: var(--font-display);
  font-size: clamp(4rem, 18vw, 10rem);
  font-weight: 800;
  line-height: 0.9;
  letter-spacing: -0.04em;
  color: var(--primary);
  text-align: center;
  font-variant-numeric: tabular-nums;
  text-shadow: 0 0 40px rgba(var(--primary-rgb), 0.4);
}

.hero-label {
  font-family: var(--font-display);
  font-size: 14px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.supporting-stat-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 1px;
  background: rgba(255,255,255,0.06);
  width: 100%;
  border-top: 1px solid rgba(255,255,255,0.08);
}

.supporting-stat {
  padding: 10px 14px;
  background: var(--bg-secondary);
  text-align: center;
}

.supporting-value {
  font-family: var(--font-display);
  font-size: 18px;
  color: var(--text-primary);
}

.supporting-label {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--muted);
  margin-top: 2px;
}
```

---

### ARCHETYPE 5: Cheat Sheet

Maximum density. Multiple section types mixed freely. Reads like a reference document you'd screenshot and save. Tables, bullets, flows, images — all on one canvas.

```
┌────────────────────────────────────────┐
│  HEADER                                │
├──────────────────────┬─────────────────┤
│  SECTION A           │  SECTION B      │
│  (pill tags grid)    │  (bullet list)  │
├──────────────────────┴─────────────────┤
│  ↓ FLOW CONNECTOR (labeled arrow)      │
├────────────────────────────────────────┤
│  SECTION C  │  SECTION D  │ SECTION E  │
│  (tier badges)│ (criteria) │ (process) │
├─────────────┴─────────────┴────────────┤
│  SECTION F (full-width tier table)     │
├────────────────────────────────────────┤
│  FOOTER / CTA                          │
└────────────────────────────────────────┘
```

```css
.cheat-sheet-layout {
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* Mixed-width row: two panels side by side */
.cheat-row-2col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Three-panel row */
.cheat-row-3col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Full-width section */
.cheat-row-full {
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Flow connector between sections */
.section-connector {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px 0;
  gap: 8px;
  color: var(--muted);
  font-size: 11px;
}

.section-connector::before,
.section-connector::after {
  content: '';
  flex: 1;
  height: 1px;
  background: rgba(var(--primary-rgb), 0.2);
}

/* Pill/tag grid (e.g. content ideas) */
.pill-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.content-pill {
  padding: 4px 10px;
  border: 1px solid rgba(var(--primary-rgb), 0.4);
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text-secondary);
  background: rgba(var(--primary-rgb), 0.06);
}
```

---

## Stats Bar / KPI Strip (74/175 = 42%)

Your stats bars typically show 3-5 metrics:
```
┌──────────────┬──────────────┬──────────────┐
│  69 Billion  │   $0.0001    │  $6.9M FDV   │
│  Total Supply│  Token Price │  Fully Diluted│
└──────────────┴──────────────┴──────────────┘
```

**Common stat fields in your work:**
- Token supply / Max supply
- Token price (TGE or current)  
- FDV / Market cap
- Airdrop pool size
- Player count / Active wallets
- Staking APY

```css
.stats-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1px;
  background: rgba(255,255,255,0.06);
  border-radius: var(--radius-card);
  overflow: hidden;
}
.stat-item {
  padding: 10px 14px; /* Dense: NOT 16px 20px */
  background: var(--bg-secondary);
  text-align: left;
  border-top: 2px solid var(--primary); /* signature colored top border */
}
.stat-value {
  font-family: var(--font-display);
  font-size: var(--text-stat);
  color: var(--primary);
  line-height: 1;
  text-transform: uppercase;
}
.stat-label {
  font-family: var(--font-body);
  font-size: 10px; /* Dense: NOT var(--text-caption) which may be larger */
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 3px;
}
```
