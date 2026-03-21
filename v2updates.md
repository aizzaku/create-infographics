# create-infographics v2 — Full Update Scope

All changes required to transform the skill from a template-filling tool into a design-intelligence system that produces world-class, editorially-driven infographics.

---

## SKILL.md Changes

### 1. Mandatory Design Brief (5 questions before mode selection)
Replace the soft "confirm design constants" in Mode A and remove the absent intake in Mode B with a unified design brief that runs *before* mode detection.

Questions to ask:
1. **Brand color** — hex code, logo URL, or "none"
2. **Aesthetic direction** — pick one:
   - A) Editorial/Clean — typographic, whitespace-first, NYT/Economist feel
   - B) Bold/Cyber — neon, dark, glows, futuristic energy
   - C) Premium/Luxury — dark + gold/silver, refined, exclusive
   - D) Corporate/Trust — light backgrounds, professional, institutional
   - E) Playful/Loud — saturated, energetic, community-feel
   - F) Custom — user describes their own
3. **Platform** — Twitter/X | Instagram | LinkedIn | Website | Print/Newsletter
4. **The #1 insight** — "What's the one number or idea viewers must remember?"
5. **Hard constraints** — colors to avoid, tone requirements, must-haves, must-avoids

Rules for the brief:
- Run it before any mode detection or design work
- If user already answered some (e.g., gave a hex in the initial message), skip those — don't re-ask
- If user says "just do it" or skips, proceed with defaults but note the assumptions
- Map answers to design decisions explicitly before building (see `resources/design-brief.md`)

---

### 2. Thesis-First Architecture
After the brief, before any design work, Claude must state the infographic's thesis:

> "Thesis: [single declarative sentence that this infographic proves]"
> "Hero stat: [the one number that proves it]"
> "Supporting points: [2–4 secondary data points that build the argument]"

This step is non-negotiable. If the user hasn't provided a clear thesis, surface one from their data or ask. Every design decision flows from here.

---

### 3. Visual Concept Declaration
After thesis, before building, name the aesthetic direction in 3 words and describe the compositional approach:

> "Visual concept: 'ELECTRIC RESTRAINT' — one dominant amber stat commanding 40% of the canvas, sparse supporting data orbiting it. Dark field, single accent color, no decoration."

This creates accountability. Each infographic should have a distinct concept, not a recycled template.

---

### 4. Data → Layout Derivation (not template-first)
Add a step that maps the data structure to the right chart type before picking a layout:

| Data task | Chart type |
|---|---|
| Compare categories | Horizontal bar (sorted descending) |
| Show trend over time (≤5 series) | Line chart with direct labels |
| Show trend over time (many series) | Small multiples |
| Part-of-whole (2–3 segments) | Pie or donut |
| Part-of-whole (many segments) | Stacked bar, sorted |
| Single number with context | Hero stat + comparison bar |
| Before/after comparison | Slope chart |
| % of total, memorable visual | Waffle chart (10×10 grid) |
| Distribution | Dot plot or histogram |
| Correlation | Scatterplot with annotated outliers |
| Process/flow | Annotated flowchart |
| Geographic | Choropleth (out of scope unless SVG map provided) |

Rule: derive layout from data type. Never start from a template and fill it.

---

### 5. Annotation-First Principle (Replace legends)
All labels go directly on the chart. No legends unless the chart has 5+ series.

- Bar chart: value label at end of each bar
- Line chart: label at the end of each line
- Pie/donut: percentage + label inside or callout line outside
- Stat cards: label directly below the number
- Flow diagrams: labels inline, not in a separate key

Add callout lines for annotations on key data points (highlight outliers, trend breaks, thresholds).

---

### 6. Reduction Pass (New final step before delivery)
After assembly, run a reduction pass — strip everything that doesn't encode data:

Checklist:
- [ ] Remove gridlines that aren't needed for reading values
- [ ] Remove axis tick marks where direct labels exist
- [ ] Replace decorative icons with whitespace or remove entirely
- [ ] Check: does every color choice encode something? If not, make it gray
- [ ] Remove border/glow on any element that is already separated by whitespace
- [ ] Cut any text that repeats what the visual already shows
- [ ] Check data-to-ink ratio: is decoration competing with data?

Note: This pass applies more strictly to Editorial/Corporate styles. Bold/Cyber style earns its decoration through brand identity. Use judgment.

---

### 7. Animated HTML Preview (Interactive Builder only)
The live browser preview should use CSS animations — they don't affect PNG export but make the review experience feel premium.

Required animations for each component type:
- **Stat numbers**: count up from 0 to final value on load (use JS counter, 800ms)
- **Bar charts**: bars animate from 0 to value (width transition, 600ms ease-out)
- **Progress bars**: fill sweeps from left with glow trail (600ms)
- **Feature cards**: stagger-fade in (opacity 0→1, translateY 12px→0, 80ms delay per card)
- **Line charts**: draw path from left to right (SVG stroke-dasharray animation)
- **Flow diagrams**: nodes fade in sequentially

These animations appear in the browser preview only — the export script captures the final rendered state (post-animation).

---

### 8. New Composition Archetypes
Add to the layout vocabulary. These are in addition to the existing component grid system.

| Archetype | Description | When to use |
|---|---|---|
| **Typographic Hero** | One massive number/word dominates 35–45% of canvas. Everything else orbits it. | Single-stat story, KPI announcement |
| **Diagonal Split** | Canvas divided diagonally. Brand color floods one half, dark/light on other. | Comparison, before/after, partnerships |
| **Editorial Asymmetric** | 3+1 column layout — wide chart area + narrow annotation rail. Like a magazine spread. | Data-heavy, analysis-focused |
| **Full-Bleed Data** | Chart or visualization bleeds edge-to-edge. Copy overlaid with contrast panel. | Dramatic visual, report cover |
| **Center-Stage Monument** | Single insight, centered, symmetrical, given full architectural weight. Generous whitespace. | Award, milestone, premium announcement |

These should be offered as options during Mode B's layout step and Mode A's plan step.

---

### 9. Mode 3: Guided Creative (New mode)
A premium UX path for users who want creative input without micromanaging components.

Flow:
1. Run design brief (as above)
2. Claude presents the thesis + visual concept
3. Claude shows 2 composition options (different archetypes) with brief descriptions — no code yet
4. User picks one (or says "neither, try X")
5. Claude builds the full infographic in one shot, using the chosen direction
6. Export as usual

Triggers for Mode 3:
- "Help me figure out the design" / "I'm not sure what style I want"
- "Give me options" / "show me two approaches"
- User brief is rich but visual direction is unclear

---

## Resource File Changes

### `resources/design-brief.md` (NEW FILE)
Full intake framework — what questions map to what design decisions.

Contents:
- The 5 brief questions with decision mappings
- How to extract a thesis from raw data
- How to determine light vs. dark suitability from brand colors
- Tone → palette mapping (authoritative, friendly, alarming, optimistic)
- Audience sophistication → density/vocabulary guidance
- What to do when user skips the brief

---

### `resources/style-details.md` — Add sections:

**A. Atmospheric Depth Techniques (inline, no external files)**
- Noise grain via inline SVG `<feTurbulence>` filter (cross-browser)
- Gradient mesh background (layered CSS radial gradients)
- Scanline overlay for cyber aesthetic (repeating CSS linear-gradient)
- Paper texture for editorial aesthetic (SVG filter with contrast + brightness)
- Glassmorphism accent panels (backdrop-filter: blur — use sparingly as accents)

**B. Annotation System**
- Direct label CSS patterns (positioned at chart endpoints)
- Callout line technique (SVG line + text, or CSS ::before pseudo-element)
- Insight callout box (left-border accent, muted background)
- Threshold/benchmark line with label

**C. Premium Typography Details**
- `font-variant-numeric: tabular-nums` on all numbers (prevents column jitter)
- Minor third type scale (1.25 ratio) for harmonious sizing
- Weight-based hierarchy (not just size): 300 context / 400 data / 500 labels / 700 headers / 800 hero stats
- Tight letter-spacing on large numbers (-0.02em), loose on small caps labels (0.03em)

**D. Reduction Pass Examples**
- Before/after showing gridline removal
- Before/after showing legend → direct label conversion
- Before/after showing decoration removal

---

### `resources/layout-patterns.md` — Add section:

**Unconventional Composition Archetypes**
Full CSS grid implementations for each of the 5 new archetypes:
- Typographic Hero grid
- Diagonal Split (clip-path technique)
- Editorial Asymmetric (3+1 columns with annotation rail)
- Full-Bleed Data (position absolute overlay technique)
- Center-Stage Monument (centered, generous whitespace)

---

### `resources/charts.md` — Add sections:

**Custom SVG Charts (alternatives to Chart.js)**

A. **Waffle chart** — 10×10 grid of squares, fill N squares for N%
   - More memorable than a pie chart
   - Pure HTML/CSS (no JS required)
   - Template with CSS custom property for fill count

B. **Slope chart** — before/after with connecting lines
   - Two columns of labeled points, lines connecting them
   - Color-codes winners (green) vs losers (red)
   - SVG-based

C. **Annotated bar chart** — SVG bars with callout annotations
   - Highlighted/colored single bar for the hero data point
   - Callout line from bar to annotation text
   - Benchmark line with label

D. **Proportional circles** — area represents value
   - Use area (not radius) for accurate perception
   - Overlapping allowed for dramatic effect
   - Label inside or below

E. **Dot plot** — individual data points, shows distribution
   - Less misleading than a bar chart for certain data
   - Clean, editorial feel

---

## Non-Goals (explicitly out of scope for v2)
- Interactive/clickable charts (infographics are static artifacts)
- Geographic maps (out of scope without SVG map assets)
- Animation in exported PNG/PDF (only in browser preview)
- React/Vue components (HTML/CSS only per existing approach)
- Changing the export pipeline (Playwright is fine as-is)
- Changing the state persistence system (already solid)
- Removing the existing design DNA (color palettes, font pairings — keep and extend)
