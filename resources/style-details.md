# Style Details — Aizfographics Design DNA
# Extracted from 175 real infographics via Claude Vision analysis
# Last updated: March 2026

## The Big Picture

| Property | Your Dominant Choice | Frequency |
|----------|---------------------|-----------|
| Background | Dark (`#0D0D0D`) | 99% |
| Border radius | Rounded (8-16px) | 58% |
| Card border | Solid-thin | 62% |
| Spacing | Compact/Comfortable | 53%/47% |
| Glow effects | YES | 75% |
| Gradient overlays | YES | 40% |
| Uppercase labels | ALWAYS | 100% |
| Has logos | YES | 95% |

---

## Border Radius

Your measured border radius distribution across 175 designs:

```
rounded (8-16px)     — 101 designs (58%) ← YOUR DEFAULT
slight (2-4px)       — 68 designs  (39%)
very-rounded (20px+) — 3 designs   (2%)  ← pills only
sharp (0px)          — 3 designs   (2%)  ← rarely
```

**Rule:** Use `8-12px` for cards and containers. Use `4-6px` for smaller elements like tags and badges. Use `50%` only for circular stat badges.

```css
:root {
  --radius-card: 10px;     /* feature cards */
  --radius-small: 4px;     /* tags, badges, table rows */
  --radius-badge: 20px;    /* pill-shaped labels */
  --radius-circle: 50%;    /* stat bubbles, avatars */
}
```

---

## Card Border Style

```
solid-thin border     — 108 designs (62%) ← YOUR DEFAULT
none                  — 46 designs  (26%)
gradient-border       — 12 designs  (7%)  ← premium/special
glow border           — 9 designs   (5%)  ← important cards
```

**Default card border:**
```css
.card {
  border: 1px solid rgba(255, 255, 255, 0.12);
}
/* or with accent color: */
.card {
  border: 1px solid rgba(var(--primary-rgb), 0.3);
}
```

**Gradient border (for special/featured cards):**
```css
.card-featured {
  border: 1px solid transparent;
  background-clip: padding-box;
  position: relative;
}
.card-featured::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  z-index: -1;
}
```

---

## Shadows & Glow Effects

**Glow effects used in 75% of your designs** — this is a core signature:

```
uses glow effects       — 131/175 (75%)
uses gradient overlays  — 70/175  (40%)
uses glassmorphism      — rare (< 5%)
```

### Your Glow System

```css
/* Standard neon glow — most common */
.glow-primary {
  box-shadow: 0 0 20px rgba(var(--primary-rgb), 0.4),
              0 0 40px rgba(var(--primary-rgb), 0.2);
}

/* Subtle glow — for cards */
.glow-card {
  box-shadow: 0 0 12px rgba(var(--primary-rgb), 0.25);
}

/* Text glow — for stat numbers and headers */
.glow-text {
  text-shadow: 0 0 20px rgba(var(--primary-rgb), 0.6),
               0 0 40px rgba(var(--primary-rgb), 0.3);
}

/* No glow — for tables and dense layouts */
.no-glow {
  box-shadow: none;
}
```

### Top Glow Colors (Use these first)
```
#F5A623  (amber)    — 7 designs
#FFD700  (gold)     — 6 designs
#00D4FF  (cyan)     — 8 designs
#E63946  (red)      — 4 designs
#FF69B4  (pink)     — 3 designs
#00E5A0  (emerald)  — 3 designs
#7CFC00  (lime)     — 3 designs
#9B5DE5  (purple)   — 2 designs
```

---

## Spacing System (8px Grid)

Your measured spacing density:
```
compact     — 92 designs (53%)
comfortable — 82 designs (47%)
tight       — rare (< 1%)
```

**Editorial-dense style = compact mode only.** The 47% "comfortable" applies to stat posters and single-focus pieces only — NOT to token-economics, game-overview, or ecosystem infographics. Use the dense defaults below.

```css
:root {
  /* 8px grid */
  --space-1: 8px;
  --space-2: 16px;
  --space-3: 24px;
  --space-4: 32px;

  /* Editorial-dense defaults (use for ALL multi-section infographics) */
  --section-gap: 24px;        /* gap BETWEEN major sections */
  --section-padding: 14px 16px; /* padding WITHIN a section container */
  --card-padding: 12px 14px;  /* padding inside cards/panels — NOT 24-32px */
  --grid-gap: 8px;            /* gap between items within a section */
  --grid-gap-md: 10px;        /* medium gap for 2-col layouts */

  /* Comfortable mode — only for stat posters / single-metric pieces */
  --section-padding-lg: 20px 24px;
  --card-padding-lg: 16px 20px;
  --grid-gap-lg: 14px;
}
```

**The most common spacing mistake:** Using `24-32px` card padding and `48-64px` section gaps. These are frontend/dashboard values. The designer's infographics use `12-16px` card padding and `24-32px` section gaps.

**Spacing rules summary:**
```
Between major sections:   24–32px + thin rule or colored border
Within sections (items):  8–12px gap
Card / panel padding:     12–16px
Section header to body:   8–12px
Table cell padding:       6px 10px
Body font size:           11–13px for dense content, 14px max
```

---

## Decorative Elements & Backgrounds

### Background Texture (39% of designs have texture)
```
solid (clean)           — 136 designs (78%)
gradient                — 22 designs  (13%)
image-overlay           — 16 designs  (9%)
has texture/pattern     — 69 designs  (39%)  ← adds subtle depth
```

**Subtle texture overlay (most common in your work):**
```css
.infographic {
  /* Subtle noise — very common in your designs */
  background-image: url("data:image/svg+xml,...");
  /* OR */
  background: linear-gradient(
    135deg,
    #0D0D0D 0%,
    #0F1525 50%,
    #0D0D0D 100%
  );
}
```

### Geometric Shapes (used in many gaming infographics)
Common shapes in your work: circles, hexagons, abstract curves, soft blobs, rectangles, pixel-blocks

```css
/* Radial gradient blob — common background accent */
.bg-blob {
  position: absolute;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(245, 166, 35, 0.15) 0%, transparent 70%);
  filter: blur(40px);
  pointer-events: none;
}
```

---

## Logo Treatment (95% of your infographics have logos)

Your logo placement patterns:
- **Dual logo lockup** (left brand + right partner) — very common for collab infographics
- **Left-aligned header** — standard single brand
- **Header bar** — logo in a distinct top strip separated from content

```css
.logo-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  border-bottom: 1px solid rgba(var(--primary-rgb), 0.25); /* visible colored border — NOT ghost border */
  margin-bottom: 16px;
}

.logo-header img {
  height: 32px;
  width: auto;
}
```

---

## Progress Bars (45/175 designs — 26%)

Very common in tokenomics (vesting schedules, allocation bars):

```css
.progress-container {
  width: 100%;
  height: 8px;
  background: rgba(255,255,255,0.1);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 4px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  box-shadow: 0 0 8px rgba(var(--primary-rgb), 0.5);
}
```

---

## Dense Table (Primary Data Component)

Tables are the designer's #1 data format — more common than charts. Every infographic with comparisons, specs, rates, tiers, or requirements should have one.

```css
.dense-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11.5px;
  line-height: 1.4;
}

.dense-table thead tr {
  background: rgba(var(--primary-rgb), 0.12);
  border-bottom: 1.5px solid rgba(var(--primary-rgb), 0.3);
}

.dense-table th {
  padding: 6px 10px;
  text-align: left;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--primary);
}

.dense-table td {
  padding: 6px 10px;       /* NOT 12px 16px — that's frontend padding */
  color: var(--text-secondary);
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

/* Alternating row tint */
.dense-table tbody tr:nth-child(even) {
  background: rgba(255,255,255,0.02);
}

.dense-table tbody tr:hover {
  background: rgba(var(--primary-rgb), 0.04);
}

/* Left-accent for first column (chain/tier identifier) */
.dense-table td:first-child {
  font-weight: 600;
  color: var(--text-primary);
}
```

**Usage rules:**
- Use `font-size: 11-12px` — never 14px+ in table cells
- Row count: 4–10 rows is optimal; 12+ rows → consider splitting
- Always pair with a section header using `.section-pill` or underlined header
- For tier tables (Gold/Silver/Bronze), add colored left-border on first cell

---

## Composition Rules (from 175 designs)

```
left-aligned dominant    — 155/175 (89%) ← YOUR RULE
top-to-bottom flow       — dominant
asymmetric balance       — most common
moderate negative space  — most common
```

**Rule:** Always left-align your content. Your entire body of work is left-to-left-aligned. Only center small hero titles.

---

## Atmospheric Depth Techniques (inline, no external files)

These techniques add tactile depth without external assets. All are self-contained HTML/CSS/SVG.

### Noise Grain — SVG feTurbulence Filter

Adds film grain that makes flat color fields feel physical. Works cross-browser.

```html
<!-- Place once in the HTML, invisible -->
<svg style="position:absolute;width:0;height:0">
  <defs>
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
      <feBlend in="SourceGraphic" mode="overlay" result="blend"/>
      <feComposite in="blend" in2="SourceGraphic" operator="in"/>
    </filter>
  </defs>
</svg>
```

```css
/* Apply to the infographic container */
.infographic::after {
  content: '';
  position: absolute;
  inset: 0;
  filter: url(#grain);
  opacity: 0.04;          /* 3–6%: subtle. Above 8% it becomes noise */
  pointer-events: none;
  border-radius: inherit;
}
```

**When to use:** Editorial, Premium/Luxury, Corporate. Skip for Bold/Cyber (glow already adds depth).

---

### Gradient Mesh Background

Layered radial gradients simulate a photographic gradient mesh. No images needed.

```css
.infographic {
  background-color: #0D0D0D;
  background-image:
    radial-gradient(ellipse 80% 60% at 20% 10%, rgba(var(--primary-rgb), 0.12) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 80%, rgba(var(--secondary-rgb), 0.08) 0%, transparent 50%),
    radial-gradient(ellipse 100% 80% at 50% 50%, rgba(255,255,255,0.02) 0%, transparent 70%);
}
```

**Tuning:**
- 3 layers is the sweet spot. More = muddy.
- Keep opacity low (0.06–0.15). The mesh is felt, not seen.
- Anchor one gradient to where the hero stat lives.

---

### Scanline Overlay — Cyber Aesthetic

Classic CRT scanline effect for Bold/Cyber infographics.

```css
.infographic::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.12) 2px,
    rgba(0, 0, 0, 0.12) 4px
  );
  pointer-events: none;
  z-index: 1;
}
```

**When to use:** Bold/Cyber only. Pair with neon accent colors and dark backgrounds.
**Do not use** on Editorial or Corporate styles — it reads as distressed/broken.

---

### Paper Texture — Editorial Aesthetic

SVG filter that simulates natural paper for editorial and newsletter aesthetics.

```html
<svg style="position:absolute;width:0;height:0">
  <defs>
    <filter id="paper">
      <feTurbulence type="turbulence" baseFrequency="0.04" numOctaves="5" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="2" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
</svg>
```

```css
.infographic {
  background-color: #F5F0E8;     /* warm off-white for editorial */
  filter: url(#paper);
}
/* Or apply only to background layer, not content */
.bg-paper {
  position: absolute;
  inset: 0;
  background: #F5F0E8;
  filter: url(#paper);
  opacity: 0.6;
}
```

**When to use:** Editorial/Clean, Print/Newsletter output. Gives a handcrafted, trusted feel.

---

### Glassmorphism Accent Panels

Use sparingly — one or two panels maximum. Never the entire background.

```css
.glass-panel {
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 12px;
}

/* Colored glass — accent/highlight variant */
.glass-accent {
  background: rgba(var(--primary-rgb), 0.08);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(var(--primary-rgb), 0.2);
  border-radius: 12px;
}
```

**Rules:**
- Requires something behind it (gradient mesh, image) to be visible. Against solid black it's invisible.
- Max 2 glass panels per infographic.
- Good for: callout boxes, hero stat containers, quote cards.
- **Do not** glass the entire background or use for standard data cards.

---

## Annotation System

Labels live on the chart. Legends are a last resort.

### Direct Label CSS

Position labels at chart endpoints rather than in a separate legend.

```css
/* End-of-bar label */
.bar-label {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 11px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  white-space: nowrap;
}

/* End-of-line label (SVG) */
.line-label {
  font-size: 11px;
  font-weight: 500;
  fill: var(--primary);
  dominant-baseline: middle;
}

/* Inside donut/pie label */
.pie-label {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 24px;
  text-align: center;
}
```

**Placement rules by chart type:**
| Chart type | Label position |
|---|---|
| Horizontal bar | Right end of bar, vertically centered |
| Vertical bar | Top of bar, centered |
| Line chart | End of line, right-aligned |
| Pie/donut | Inside segment or callout line outside |
| Stat cards | Below number, uppercase |

---

### Callout Line Technique

Use SVG lines to point from annotation text to data points.

```html
<!-- SVG callout: line + annotation text -->
<svg class="callout-layer" style="position:absolute;inset:0;pointer-events:none;overflow:visible">
  <!-- Line from data point to annotation -->
  <line x1="240" y1="80" x2="320" y2="50"
        stroke="rgba(255,255,255,0.4)" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- Dot at data point -->
  <circle cx="240" cy="80" r="3" fill="var(--primary)"/>
  <!-- Annotation text -->
  <text x="324" y="54" font-size="10" fill="rgba(255,255,255,0.7)" font-family="inherit">
    Peak: Mar 2024
  </text>
</svg>
```

**CSS alternative (pseudo-element for simple cases):**
```css
.data-annotation {
  position: absolute;
  padding: 4px 8px;
  font-size: 10px;
  color: rgba(255, 255, 255, 0.65);
}
.data-annotation::before {
  content: '';
  position: absolute;
  left: -20px;
  top: 50%;
  width: 16px;
  height: 1px;
  background: rgba(255, 255, 255, 0.3);
}
```

---

### Insight Callout Box

A highlighted annotation block for major insights — left border accent, muted background.

```css
.insight-callout {
  border-left: 3px solid var(--primary);
  background: rgba(var(--primary-rgb), 0.06);
  padding: 10px 14px;
  border-radius: 0 6px 6px 0;
  font-size: 12px;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.8);
}

.insight-callout .insight-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary);
  margin-bottom: 4px;
}
```

```html
<div class="insight-callout">
  <div class="insight-label">Key Insight</div>
  Revenue grew 3× faster in markets where onboarding took under 2 minutes.
</div>
```

---

### Threshold / Benchmark Line

Horizontal reference line with a label — shows target, average, or industry benchmark.

```html
<!-- SVG benchmark line -->
<svg style="position:absolute;inset:0;pointer-events:none;overflow:visible">
  <line x1="0" y1="120" x2="600" y2="120"
        stroke="rgba(255,255,255,0.25)" stroke-width="1" stroke-dasharray="6,4"/>
  <text x="4" y="115" font-size="9" fill="rgba(255,255,255,0.5)"
        font-family="inherit" text-anchor="start">
    Industry avg: 42%
  </text>
</svg>
```

```css
/* CSS alternative for horizontal bar charts */
.benchmark-line {
  position: absolute;
  left: 0;
  right: 0;
  top: var(--benchmark-pct);   /* set via inline style */
  height: 1px;
  background: rgba(255, 255, 255, 0.25);
  border-top: 1px dashed rgba(255, 255, 255, 0.25);
}
.benchmark-label {
  position: absolute;
  top: -14px;
  left: 4px;
  font-size: 9px;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
```

---

## Premium Typography

### Tabular Numbers

Prevents column jitter when numbers change or animate. Apply to all numeric elements.

```css
/* Apply globally to numbers */
.stat-number,
.table-cell,
.bar-value,
.chart-label {
  font-variant-numeric: tabular-nums;
  font-feature-settings: "tnum" 1;  /* fallback for older browsers */
}
```

---

### Minor Third Type Scale (1.25 ratio)

Harmonious size progression. Pick a base (12–14px for dense layouts, 16px for spacious).

```css
:root {
  --text-base: 13px;             /* base for compact infographics */

  --text-xs:   10px;             /* base × 0.79 — footnotes, data labels */
  --text-sm:   11px;             /* base × 0.87 — secondary labels */
  --text-md:   13px;             /* base — body, table cells */
  --text-lg:   16px;             /* base × 1.25 — section headers */
  --text-xl:   20px;             /* base × 1.56 — card titles */
  --text-2xl:  25px;             /* base × 1.95 — subsection hero */
  --text-3xl:  32px;             /* base × 2.44 — section hero stat */
  --text-hero: 56px;             /* base × 4.3  — primary hero stat */
}
```

---

### Weight-Based Hierarchy

Size alone is weak. Pair size changes with weight changes for clear signal.

```css
/* Context / supporting copy */
.text-context  { font-weight: 300; opacity: 0.6; }

/* Data values, cell content */
.text-data     { font-weight: 400; }

/* Chart labels, category names */
.text-label    { font-weight: 500; text-transform: uppercase; }

/* Headers, section titles */
.text-header   { font-weight: 700; }

/* Hero stat — the one number */
.text-hero     { font-weight: 800; }
```

---

### Letter-Spacing Rules

```css
/* Large numbers — tighten for mass, presence */
.stat-number,
.text-hero {
  letter-spacing: -0.02em;
}

/* Small caps labels — open up for legibility */
.text-label,
.category-label {
  letter-spacing: 0.06em;
  text-transform: uppercase;
  font-size: var(--text-xs);
  font-weight: 600;
}

/* Body text — natural tracking */
.text-body {
  letter-spacing: 0;
}

/* Subtitle / descriptor lines */
.text-descriptor {
  letter-spacing: 0.02em;
  font-weight: 400;
  opacity: 0.65;
}
```

**Rule summary:**
- Hero stats and large numbers: `-0.02em`
- All-caps small labels: `+0.04em` to `+0.08em`
- Body text: `0` (never touch it)

---

## Reduction Pass Examples

These before/after examples illustrate the reduction pass described in SKILL.md.

### Example A — Gridline Removal

**Before:** 5 horizontal gridlines behind bars, tick marks on Y-axis, light gray background grid
```css
/* BEFORE — visual noise */
.chart-grid {
  background-image: repeating-linear-gradient(
    0deg, rgba(255,255,255,0.08) 0px, rgba(255,255,255,0.08) 1px,
    transparent 1px, transparent 40px
  );
}
.axis-tick { display: block; }
```

**After:** Direct value labels on each bar replace the need for gridlines
```css
/* AFTER — gridlines and ticks removed */
.chart-grid { background: none; }
.axis-tick  { display: none; }

/* Value labels do the work instead */
.bar-value-label {
  position: absolute;
  right: 8px;
  font-size: 11px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}
```

**What changed:** Reader can still get the value from the label. The gridlines encoded nothing the label doesn't already encode.

---

### Example B — Legend → Direct Label Conversion

**Before:** Separate color legend box below chart with 4 colored squares + text
```html
<!-- BEFORE — wasted space, requires eye travel -->
<div class="legend">
  <span class="legend-dot" style="background:#00D4FF"></span> Product A
  <span class="legend-dot" style="background:#F5A623"></span> Product B
</div>
```

**After:** Labels placed at the end of each line/bar
```html
<!-- AFTER — annotation at point of interest -->
<svg>
  <!-- line path ... -->
  <text x="580" y="42" fill="#00D4FF" font-size="11" font-weight="600">Product A</text>
  <!-- line path ... -->
  <text x="580" y="78" fill="#F5A623" font-size="11" font-weight="600">Product B</text>
</svg>
```

**When to revert:** 5+ series where end-labels would collide. Only then use a compact legend (12px text, colored squares).

---

### Example C — Decoration Removal

**Before:** Card with gradient border glow, drop shadow, background pattern, and decorative icon
```css
/* BEFORE — everything is shouting */
.card {
  border: 1px solid transparent;
  background: linear-gradient(#0D0D0D, #0D0D0D) padding-box,
              linear-gradient(135deg, var(--primary), var(--secondary)) border-box;
  box-shadow: 0 0 30px rgba(var(--primary-rgb), 0.5), 0 8px 32px rgba(0,0,0,0.4);
  background-image: url("data:image/svg+xml,...");  /* pattern */
}
.card-icon { font-size: 32px; margin-bottom: 8px; }  /* decorative only */
```

**After:** Separation by whitespace. No glow if cards are already in a grid.
```css
/* AFTER — structure creates hierarchy, not decoration */
.card {
  border: 1px solid rgba(255, 255, 255, 0.10);
  box-shadow: none;
  background: rgba(255, 255, 255, 0.03);
}
/* icon removed — heading already identifies the card */
```

**Decision rule:** If two elements are separated by 16px+ of whitespace, they don't need a border AND a glow AND a shadow. Pick one separation signal. Usually: border alone is enough.

---

## Reference Image Patterns (Vision Analysis — 12 real pieces)

These patterns were directly observed across the designer's portfolio. Add to signature component vocabulary.

### Full-Width Section Separator Bands

The most common section-divider pattern. NOT just a text label — a full-width solid-background strip containing the section number and title.

```css
.section-band {
  width: 100%;
  background: #111520;  /* slightly lighter than page bg */
  border-top: 1px solid rgba(255,255,255,0.08);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding: 8px 48px;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}
.section-band-num {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 11px;
  color: var(--primary);
  letter-spacing: 1px;
}
/* Optional diamond prefix */
.section-band-num::before { content: '◆ '; color: var(--primary); }
.section-band-title {
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--text-muted);
}
.section-band-line {
  flex: 1;
  height: 1px;
  background: var(--border);
}
```

### Vertical Flow Diagram with Labeled Arrows

Process flow (DEPOSIT → CLAIM → SWAP → REDEEM). Nodes are rectangular colored boxes; arrows carry text labels. Always include percentage and token labels on arrows.

```css
.flow-diagram-v { display: flex; flex-direction: column; align-items: center; gap: 0; }
.flow-node-v {
  background: var(--primary);
  color: #000;
  font-family: 'Bebas Neue', sans-serif;
  font-size: 16px;
  letter-spacing: 1.5px;
  padding: 10px 32px;
  border-radius: 4px;
  min-width: 180px;
  text-align: center;
  position: relative;
}
.flow-node-v.secondary { background: rgba(var(--primary-rgb),0.1); color: var(--text); border: 1px solid rgba(var(--primary-rgb),0.3); }
.flow-node-v.branch { background: #1a1a2a; color: var(--text-muted); border: 1px dashed rgba(255,255,255,0.2); min-width: 220px; }
.flow-arrow-v {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: 4px 0;
}
.flow-arrow-v-line { width: 2px; height: 16px; background: rgba(var(--primary-rgb),0.4); }
.flow-arrow-v-head { width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 7px solid rgba(var(--primary-rgb),0.6); }
.flow-arrow-v-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: rgba(var(--primary-rgb),0.7);
  position: absolute;
  right: -90px;
  top: 50%;
  transform: translateY(-50%);
  white-space: nowrap;
}
/* Branch split: two paths side by side */
.flow-branch-row { display: flex; gap: 24px; align-items: flex-start; }
.flow-branch-path { display: flex; flex-direction: column; align-items: center; gap: 0; }
```

### Character Card Grid (Game)

Tight 5-column grid for character/NFT rosters. Each card: portrait image + name + stat bars.

```css
.char-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 2px; }
.char-card { background: var(--bg3); border: 1px solid var(--border); overflow: hidden; }
.char-portrait { width: 100%; aspect-ratio: 1; object-fit: cover; display: block; }
.char-name { font-size: 9px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; padding: 5px 8px 4px; color: #fff; }
.char-stats { padding: 0 8px 8px; display: flex; flex-direction: column; gap: 3px; }
.char-stat-row { display: flex; align-items: center; gap: 5px; }
.char-stat-label { font-size: 7px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; color: var(--text-muted); width: 28px; flex-shrink: 0; }
.char-stat-bar { flex: 1; height: 4px; background: rgba(255,255,255,0.08); border-radius: 2px; overflow: hidden; }
.char-stat-fill { height: 100%; border-radius: 2px; }
```

### Swim-Lane Architecture Diagram

Two-tier (or multi-tier) horizontal labeled bands showing protocol layers.

```css
.swim-diagram { border: 1px solid var(--border); overflow: hidden; }
.swim-lane { display: grid; grid-template-columns: 80px 1fr; min-height: 80px; border-bottom: 1px solid var(--border); }
.swim-lane:last-child { border-bottom: none; }
.swim-label {
  background: rgba(var(--primary-rgb),0.08);
  border-right: 1px solid rgba(var(--primary-rgb),0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  writing-mode: vertical-rl;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--primary);
}
.swim-content {
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
```

### Blockchain Chain Color Tokens

Always apply these when rendering multi-chain protocol data:

```css
.chain-eth   { --chain-color: #627EEA; } /* Ethereum  — blue   */
.chain-arb   { --chain-color: #E87030; } /* Arbitrum  — orange */
.chain-sol   { --chain-color: #9945FF; } /* Solana    — purple */
.chain-bnb   { --chain-color: #F3BA2F; } /* BNBChain  — yellow */
.chain-base  { --chain-color: #0052FF; } /* Base      — blue   */
.chain-poly  { --chain-color: #8247E5; } /* Polygon   — violet */
.chain-avax  { --chain-color: #E84142; } /* Avalanche — red    */
.chain-op    { --chain-color: #FF0420; } /* Optimism  — red    */

.chain-badge {
  background: rgba(var(--chain-color-rgb),0.12);
  border: 1px solid rgba(var(--chain-color-rgb),0.3);
  color: var(--chain-color);
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 2px;
}
/* Table row left-border per chain */
.chain-row-eth td:first-child { border-left: 3px solid #627EEA; }
.chain-row-arb td:first-child { border-left: 3px solid #E87030; }
.chain-row-sol td:first-child { border-left: 3px solid #9945FF; }
.chain-row-bnb td:first-child { border-left: 3px solid #F3BA2F; }
.chain-row-base td:first-child { border-left: 3px solid #0052FF; }
```

### Outer Canvas Border

Thin accent border framing the entire infographic canvas (common in game pieces):

```css
/* On body or a wrapping .canvas div */
body {
  outline: 2px solid var(--primary);
  outline-offset: -2px;
}
/* Or as a pseudo-element for more control */
.canvas::before {
  content: '';
  position: fixed;
  inset: 0;
  border: 2px solid var(--primary);
  pointer-events: none;
  z-index: 999;
}
```

### Section Header Pill Badge (Ecosystem style)

Used heavily in ecosystem infographics — section label inside a colored pill with glow:

```css
.section-pill {
  display: inline-flex;
  align-items: center;
  background: rgba(var(--primary-rgb),0.1);
  border: 1px solid rgba(var(--primary-rgb),0.35);
  box-shadow: 0 0 8px rgba(var(--primary-rgb),0.25);
  color: var(--primary);
  font-family: 'Bebas Neue', sans-serif;
  font-size: 13px;
  letter-spacing: 2px;
  padding: 4px 16px;
  border-radius: 4px;
  margin-bottom: 14px;
}
```
