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

**Most common layout (portrait-tall):**
```
HEADER BAR
  └─ [logo left] [project name right]

STATS STRIP (3-col)
  └─ [Total Supply] [Token Price] [FDV / Market Cap]

CENTRAL PIE CHART
  └─ Large donut chart, project logo centered inside
  └─ % labels with colored segments

ALLOCATION BREAKDOWN (2-col asymmetric)
  ├─ LEFT: 3 stacked allocation blocks
  │   └─ [Airdrop / Community] [Ecosystem Fund] [Team/Advisors]
  └─ RIGHT: 2-3 stacked allocation blocks
      └─ [Private Sale] [Public Sale / IDO]

VESTING TIMELINE (full-width)
  └─ Horizontal timeline with lock icons
  └─ Progress bars showing unlock schedule
  └─ Month/quarter labels

FOOTER DISCLAIMER BAR
  └─ Small text, muted, left-aligned
```

**CSS Grid:**
```css
.token-layout {
  display: grid;
  grid-template-rows: auto auto 1fr auto auto;
  gap: 20px;
}
.allocation-grid {
  display: grid;
  grid-template-columns: 1fr 300px 1fr;  /* left | chart | right */
  gap: 16px;
  align-items: start;
}
```

---

### 2. GAME-OVERVIEW (19% — your #2 type)

**Common layout (portrait-tall or square):**
```
HERO SECTION (boxed or split-layout)
  └─ Game title (large Bebas Neue)
  └─ Character art or key visual on right
  └─ 2-3 key benefit bullets on left

STATS / KEY METRICS BAR (3-4 col)
  └─ Players | Token Price | Reward Pool | Season

FEATURE CARDS (2×3 or 3×2 grid)
  └─ [icon] + [title] + [1-2 line description]
  └─ Outlined cards with glow on hover

GAME MECHANICS / HOW TO PLAY
  └─ Numbered steps or flow diagram
  └─ Arrows connecting steps

REWARDS & TOKENOMICS
  └─ Simple allocation bar or pie chart
  └─ Key reward types highlighted

FOOTER
  └─ Logo + social links + season info
```

---

### 3. ECOSYSTEM (15% — partner/collaboration type)

**Common layout (landscape 16:9 or portrait-tall):**
```
DUAL LOGO HEADER
  └─ [Brand A Logo] ←→ [Brand B Logo]
  └─ Thin separator or "×" between logos

TITLE + DESCRIPTION BLOCK
  └─ Bold headline (left-aligned, uppercase)
  └─ 2-3 sentence description
  └─ Optional date/event badge

FLOW DIAGRAM or INTEGRATION MAP
  └─ Central hub (or arrow diagram)
  └─ Connected nodes/boxes
  └─ Benefit labels on arrows

2-COL PARTNER DETAILS
  ├─ LEFT: About Brand A (bullet list)
  └─ RIGHT: About Brand B or shared benefits

TIER SYSTEM or ACCESS LEVELS
  └─ Horizontal row of tier badges (I, II, III)
  └─ Color-coded by value

CTA FOOTER BAR
  └─ Single line: "Learn more at [url]"
```

---

### 4. CRYPTO-EXPLAINER (12% — educational type)

**Common layout (landscape 16:9):**
```
HEADER (left-aligned, branded)
  └─ Logo + project name
  └─ Subtitle/topic line

CONCEPT FLOW (horizontal)
  └─ Step 1 → Step 2 → Step 3
  └─ Arrow connectors (straight or curved)
  └─ Icon above each step, description below

DETAIL SECTION (2-col)
  ├─ LEFT: Expanded explanation of steps
  └─ RIGHT: Supporting stats or benefits card

BENEFIT BADGES
  └─ 3-5 horizontal gradient pills
  └─ Labeled: "Faster", "Cheaper", "Decentralized"

FOOTER
  └─ Logo + URL + disclaimer
```

---

### 5. AIRDROP-GUIDE (8% — action-focused type)

**Common layout (landscape 16:9):**
```
BOLD HEADLINE BANNER (left-aligned uppercase)
  └─ "HOW TO CLAIM YOUR [TOKEN] AIRDROP"
  └─ Date/deadline badge (right-aligned)

ELIGIBILITY / REQUIREMENTS (single-col bullet list)
  └─ 4-6 items with colored keyword highlights
  └─ e.g., "Hold [X] tokens in wallet"
  └─ Color-code key terms with accent color

VESTING VISUALIZATION (full-width)
  └─ Horizontal progress bar with segments
  └─ Percentages labeled on each segment
  └─ Timeline markers (TGE, Month 3, Month 6, etc.)

TOKEN SUMMARY (bottom stat row)
  └─ 3-4 key numbers: total airdrop, per wallet, unlock date

FOOTER
  └─ Warning/disclaimer in muted text
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

### 7. MODULAR CARD GRID (used across ALL types)

This is your most reused component:

**2-col card grid:**
```
┌─────────────────┬─────────────────┐
│  [icon] Title   │  [icon] Title   │
│  Description    │  Description    │
│  line 1-2       │  line 1-2       │
└─────────────────┴─────────────────┘
┌─────────────────┬─────────────────┐
│  [icon] Title   │  [icon] Title   │
│  Description    │  Description    │
└─────────────────┴─────────────────┘
```

```css
.card-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}
.card-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}
@media (max-width: 600px) {
  .card-grid-2, .card-grid-3 { grid-template-columns: 1fr; }
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
  padding: 16px 20px;
  background: var(--bg-secondary);
  text-align: left;
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
  font-size: var(--text-caption);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 4px;
}
```
