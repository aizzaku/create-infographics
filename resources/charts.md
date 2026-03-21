# Chart & Data Visualization System — Aizfographics
# Last updated: March 2026

## When to Use What

| Chart Type | Method | When |
|-----------|--------|------|
| Pie (full) | Inline SVG | Token allocation, any % breakdown ≤ 8 segments |
| Horizontal bar | Pure CSS | Vesting schedule, comparative bars, allocation strips |
| Vertical bar | Chart.js | Multi-period comparisons, time-series bars |
| Line chart | Chart.js | Price over time, growth curves, trend lines |
| Radar / Spider | Chart.js | Game character stats, feature comparisons |
| Progress bar | Pure CSS | Unlock progress, single metric completion |
| **Waffle chart** | **Pure HTML/CSS** | **% of total — more memorable than pie, editorial feel** |
| **Slope chart** | **Inline SVG** | **Before/after comparison, two-point change** |
| **Annotated bar** | **Inline SVG** | **Bar chart with callout on hero data point + benchmark line** |
| **Proportional circles** | **Inline SVG** | **Compare magnitudes where area = value (3–6 items)** |
| **Dot plot** | **Inline SVG** | **Distribution, individual data points, avoiding bar bias** |

**Rule:** Use CSS/SVG for anything static and allocation-based. Use Chart.js only when the data is dynamic or the chart type genuinely requires it. Never add Chart.js just for a bar chart you could build in CSS.

---

## 1. SVG Pie Chart (Token Allocation — Your Most-Used)

This is the central chart in 35% of your infographics. Build it inline as SVG so it works in PNG/PDF with zero dependencies.

**No donut hole. Full solid wedges.**

### Color Rule

**Never use arbitrary rainbow colors.** Two options, in priority order:

1. **Primary shades (preferred):** Derive all segment colors from HSL shades of the brand primary.
   Example for amber `#F5A623` (HSL 37°, 91%, 55%):
   ```
   Shade 1 (lightest): hsl(37, 85%, 70%)  → #F7C26B
   Shade 2 (primary):  hsl(37, 91%, 55%)  → #F5A623  ← fullest
   Shade 3:            hsl(37, 76%, 40%)  → #C4841A
   Shade 4 (darkest):  hsl(37, 75%, 27%)  → #7A5211
   ```
   Spread evenly across lightness — always enough contrast between adjacent segments.

2. **Brand complementary (max 2–3 hues):** Only if the brand has defined secondary/accent colors. Never invent colors not in the brand palette. Never exceed 3 distinct hues total — fill remaining segments with shades.

### How SVG Pie Wedges Work

Each segment is a filled `<path>` wedge from the center:
```
M cx cy          — move to center
L x1 y1          — line to arc start point
A r r 0 [large-arc] 1 x2 y2   — arc to end point (clockwise)
Z                — close back to center
```

Point on circle at angle θ (0° = right, increases clockwise in SVG):
```
x = cx + r * cos(θ * π/180)
y = cy + r * sin(θ * π/180)
```

Start angle: **−90°** (12 o'clock). Add each segment's degrees (`pct/100 * 360`) to advance.
`large-arc-flag` = `1` if segment > 50%, else `0`.

### Segment Calculator

```
segment_degrees  = percentage / 100 * 360
start_angle      = -90 + (sum of all previous segments' degrees)
end_angle        = start_angle + segment_degrees
x1 = 100 + 90 * cos(start_angle * π/180)
y1 = 100 + 90 * sin(start_angle * π/180)
x2 = 100 + 90 * cos(end_angle * π/180)
y2 = 100 + 90 * sin(end_angle * π/180)
large-arc-flag   = segment_degrees > 180 ? 1 : 0
```

### Template (4-segment example — amber primary shades)

Segments: Community 35%, Ecosystem 25%, Team 20%, Private Sale 20%

```html
<div class="chart-pie-wrapper">
  <svg viewBox="0 0 200 200" width="280" height="280" class="chart-pie">
    <!-- Thin separator gaps between segments via stroke -->
    <circle cx="100" cy="100" r="90" fill="#0D0D0D" stroke="none"/>

    <!-- Segment 1: Community/Airdrop — 35% → 126° → start -90°, end 36° -->
    <!-- x1=100.0,y1=10.0 → x2=172.8,y2=152.9 -->
    <path d="M 100 100 L 100.0 10.0 A 90 90 0 0 1 172.8 152.9 Z"
      fill="#F7C26B" stroke="#0D0D0D" stroke-width="1.5"/>

    <!-- Segment 2: Ecosystem Fund — 25% → 90° → start 36°, end 126° -->
    <!-- x2=47.1,y2=172.8 -->
    <path d="M 100 100 L 172.8 152.9 A 90 90 0 0 1 47.1 172.8 Z"
      fill="#F5A623" stroke="#0D0D0D" stroke-width="1.5"/>

    <!-- Segment 3: Team — 20% → 72° → start 126°, end 198° -->
    <!-- x2=14.4,y2=72.2 -->
    <path d="M 100 100 L 47.1 172.8 A 90 90 0 0 1 14.4 72.2 Z"
      fill="#C4841A" stroke="#0D0D0D" stroke-width="1.5"/>

    <!-- Segment 4: Private Sale — 20% → 72° → start 198°, end 270° → closes to 100,10 -->
    <path d="M 100 100 L 14.4 72.2 A 90 90 0 0 1 100.0 10.0 Z"
      fill="#7A5211" stroke="#0D0D0D" stroke-width="1.5"/>
  </svg>

  <!-- Legend -->
  <div class="chart-legend">
    <div class="legend-item">
      <span class="legend-dot" style="background:#F7C26B;"></span>
      <span class="legend-label">COMMUNITY / AIRDROP</span>
      <span class="legend-pct">35%</span>
    </div>
    <div class="legend-item">
      <span class="legend-dot" style="background:#F5A623;"></span>
      <span class="legend-label">ECOSYSTEM FUND</span>
      <span class="legend-pct">25%</span>
    </div>
    <div class="legend-item">
      <span class="legend-dot" style="background:#C4841A;"></span>
      <span class="legend-label">TEAM & ADVISORS</span>
      <span class="legend-pct">20%</span>
    </div>
    <div class="legend-item">
      <span class="legend-dot" style="background:#7A5211;"></span>
      <span class="legend-label">PRIVATE SALE</span>
      <span class="legend-pct">20%</span>
    </div>
  </div>
</div>
```

### CSS

```css
.chart-pie-wrapper {
  display: flex;
  align-items: center;
  gap: 32px;
  justify-content: center;
}

.chart-legend {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 200px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.legend-label {
  font-family: var(--font-body);
  font-size: var(--text-caption);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  flex: 1;
}

.legend-pct {
  font-family: var(--font-display);
  font-size: 18px;
  color: var(--text);
}
```

---

## 2. CSS Horizontal Bar Chart (Vesting / Allocation Strips)

Use for vesting schedules, side-by-side allocation comparisons, and ranked lists.

```html
<div class="bar-chart">
  <div class="bar-row">
    <div class="bar-label">COMMUNITY</div>
    <div class="bar-track">
      <div class="bar-fill" style="width: 35%; background: #F5A623;">
        <span class="bar-pct">35%</span>
      </div>
    </div>
    <div class="bar-value">350M</div>
  </div>
  <div class="bar-row">
    <div class="bar-label">ECOSYSTEM</div>
    <div class="bar-track">
      <div class="bar-fill" style="width: 25%; background: #00E5A0;">
        <span class="bar-pct">25%</span>
      </div>
    </div>
    <div class="bar-value">250M</div>
  </div>
  <!-- repeat -->
</div>
```

```css
.bar-chart { display: flex; flex-direction: column; gap: 10px; }

.bar-row {
  display: grid;
  grid-template-columns: 140px 1fr 80px;
  align-items: center;
  gap: 12px;
}

.bar-label {
  font-family: var(--font-body);
  font-size: var(--text-caption);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  text-align: right;
}

.bar-track {
  height: 10px;
  background: rgba(255,255,255,0.07);
  border-radius: 5px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 4px;
  box-shadow: 0 0 8px rgba(255,255,255,0.15);
  transition: width 0.8s ease;
}

.bar-pct {
  font-size: 9px;
  font-family: var(--font-mono);
  color: rgba(255,255,255,0.7);
  white-space: nowrap;
}

.bar-value {
  font-family: var(--font-body);
  font-size: var(--text-caption);
  color: var(--text);
  text-transform: uppercase;
}
```

---

## 3. Chart.js — Complex Charts via CDN

Use Chart.js when you need: line charts (price/growth), vertical bar charts (multi-period), or radar charts (game stats). Load via CDN in `<head>`:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

Always use `<canvas>` elements (NOT divs). Chart.js renders to canvas, which Playwright screenshots correctly.

### Line Chart Template

```html
<div class="chart-container" style="position:relative; height:240px;">
  <canvas id="lineChart"></canvas>
</div>

<script>
const ctx = document.getElementById('lineChart').getContext('2d');
new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q1 \'26'],
    datasets: [{
      label: 'Price (USD)',
      data: [0.001, 0.0034, 0.0028, 0.0089, 0.012],
      borderColor: '#F5A623',
      backgroundColor: 'rgba(245,166,35,0.08)',
      borderWidth: 2,
      pointBackgroundColor: '#F5A623',
      pointRadius: 4,
      fill: true,
      tension: 0.4,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#1A1A1A',
        borderColor: 'rgba(255,255,255,0.1)',
        borderWidth: 1,
        titleColor: '#F5A623',
        bodyColor: '#FFFFFF',
      }
    },
    scales: {
      x: {
        grid: { color: 'rgba(255,255,255,0.05)' },
        ticks: { color: '#8B8B8B', font: { family: 'Inter', size: 11 } }
      },
      y: {
        grid: { color: 'rgba(255,255,255,0.05)' },
        ticks: { color: '#8B8B8B', font: { family: 'Inter', size: 11 } }
      }
    }
  }
});
</script>
```

### Radar Chart Template (Game Stats)

```html
<div class="chart-container" style="position:relative; height:280px; max-width: 320px; margin: 0 auto;">
  <canvas id="radarChart"></canvas>
</div>

<script>
new Chart(document.getElementById('radarChart'), {
  type: 'radar',
  data: {
    labels: ['ATTACK', 'DEFENSE', 'SPEED', 'MAGIC', 'STAMINA', 'LUCK'],
    datasets: [{
      data: [85, 72, 91, 60, 78, 55],
      borderColor: '#00E5A0',
      backgroundColor: 'rgba(0,229,160,0.12)',
      borderWidth: 2,
      pointBackgroundColor: '#00E5A0',
      pointRadius: 4,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      r: {
        min: 0, max: 100,
        grid: { color: 'rgba(255,255,255,0.08)' },
        angleLines: { color: 'rgba(255,255,255,0.08)' },
        pointLabels: {
          color: '#8B8B8B',
          font: { family: 'Inter', size: 10 }
        },
        ticks: { display: false }
      }
    }
  }
});
</script>
```

---

## 4. Pure CSS Progress Bar (Vesting Timeline)

For single-metric unlock progress — no JS needed.

```html
<div class="vesting-bar">
  <div class="vesting-label-row">
    <span>TGE — 10% UNLOCKED</span>
    <span>MONTH 12 — 100%</span>
  </div>
  <div class="progress-track">
    <div class="progress-fill" style="width: 35%;"></div>
    <!-- Milestone markers -->
    <div class="progress-marker" style="left: 10%;" title="TGE"></div>
    <div class="progress-marker" style="left: 25%;" title="3M"></div>
    <div class="progress-marker" style="left: 50%;" title="6M"></div>
    <div class="progress-marker" style="left: 75%;" title="9M"></div>
  </div>
  <div class="vesting-milestones">
    <span>TGE</span><span>3M</span><span>6M</span><span>9M</span><span>12M</span>
  </div>
</div>
```

```css
.vesting-bar { width: 100%; }

.vesting-label-row {
  display: flex;
  justify-content: space-between;
  font-size: var(--text-caption);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
}

.progress-track {
  position: relative;
  height: 10px;
  background: rgba(255,255,255,0.07);
  border-radius: 5px;
  overflow: visible;
}

.progress-fill {
  height: 100%;
  border-radius: 5px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  box-shadow: 0 0 10px rgba(var(--primary-rgb), 0.4);
}

.progress-marker {
  position: absolute;
  top: -3px;
  width: 2px;
  height: 16px;
  background: rgba(255,255,255,0.2);
  transform: translateX(-50%);
}

.vesting-milestones {
  display: flex;
  justify-content: space-between;
  font-size: 10px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 6px;
}
```

---

## 5. Waffle Chart (% of Total — Pure HTML/CSS)

A 10×10 grid of 100 squares. Fill N squares to show N%. More memorable and honest than a pie chart for single-percentage stories.

**Key rule:** Use `--fill-count` CSS custom property to control how many squares are colored. No JS required.

```html
<div class="waffle-chart-wrapper">
  <div class="waffle-grid" style="--fill-count: 63;">
    <!-- 100 squares — generate with a loop or paste manually -->
    <!-- squares 1–63 get the accent color via nth-child CSS -->
  </div>
  <div class="waffle-legend">
    <div class="waffle-stat">63%</div>
    <div class="waffle-label">OF SUPPLY LOCKED</div>
    <div class="waffle-detail">630M / 1B tokens</div>
  </div>
</div>
```

**Generate 100 squares (copy-paste or template loop):**
```html
<!-- Inside .waffle-grid: repeat this 100 times -->
<span class="waffle-cell"></span>
```

```css
.waffle-chart-wrapper {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.waffle-grid {
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  gap: 3px;
  width: 200px;
  height: 200px;
}

.waffle-cell {
  background: rgba(255,255,255,0.08);
  border-radius: 2px;
  aspect-ratio: 1;
}

/* Fill the first N cells using :nth-child — set via inline --fill-count */
/* Since CSS can't use custom props in :nth-child, use JS to add a class instead: */
.waffle-cell.filled {
  background: var(--primary);
  box-shadow: 0 0 4px rgba(var(--primary-rgb), 0.4);
}

/* For animation — stagger fill in */
.waffle-cell.filled {
  animation: waffleFill 0.4s ease both;
  animation-delay: calc(var(--i) * 8ms);
}

@keyframes waffleFill {
  from { transform: scale(0.2); opacity: 0; background: var(--primary); }
  to   { transform: scale(1);   opacity: 1; }
}

.waffle-legend {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.waffle-stat {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 6vw, 3.5rem);
  font-weight: 800;
  color: var(--primary);
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.waffle-label {
  font-size: var(--text-caption);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
}

.waffle-detail {
  font-size: var(--text-caption);
  color: var(--muted);
  margin-top: 0.5rem;
}
```

**JS snippet to add `.filled` classes and stagger animation:**
```js
document.querySelectorAll('.waffle-grid').forEach(grid => {
  const count = parseInt(getComputedStyle(grid).getPropertyValue('--fill-count')) || 0;
  grid.querySelectorAll('.waffle-cell').forEach((cell, i) => {
    if (i < count) {
      cell.classList.add('filled');
      cell.style.setProperty('--i', i);
    }
  });
});
```

---

## 6. Slope Chart (Before/After — Inline SVG)

Two columns of labeled points connected by lines. Color-codes positive change (green/accent) vs negative change (red/muted). Best for 3–8 items.

**Coordinate system:** SVG viewBox `0 0 400 300`. Left column x=80, right column x=320. Y positions spread evenly between 40 and 260.

```html
<div class="slope-chart-wrapper">
  <svg viewBox="0 0 400 320" class="slope-svg">
    <!-- Column headers -->
    <text x="80"  y="18" class="slope-col-label" text-anchor="middle">2023</text>
    <text x="320" y="18" class="slope-col-label" text-anchor="middle">2024</text>

    <!-- Column axis lines -->
    <line x1="80"  y1="28" x2="80"  y2="292" class="slope-axis"/>
    <line x1="320" y1="28" x2="320" y2="292" class="slope-axis"/>

    <!-- Item: Bitcoin — up (positive) -->
    <!-- left y=60, right y=40 -->
    <line x1="80" y1="60" x2="320" y2="40" class="slope-line positive"/>
    <circle cx="80"  cy="60" r="5" class="slope-dot positive"/>
    <circle cx="320" cy="40" r="5" class="slope-dot positive"/>
    <text x="72"  y="64" class="slope-label-left">BTC</text>
    <text x="72"  y="56" class="slope-value-left">$42K</text>
    <text x="328" y="44" class="slope-label-right">BTC</text>
    <text x="328" y="36" class="slope-value-right">$98K ↑</text>

    <!-- Item: Solana — up -->
    <!-- left y=120, right y=90 -->
    <line x1="80" y1="120" x2="320" y2="90" class="slope-line positive"/>
    <circle cx="80"  cy="120" r="5" class="slope-dot positive"/>
    <circle cx="320" cy="90"  r="5" class="slope-dot positive"/>
    <text x="72"  y="124" class="slope-label-left">SOL</text>
    <text x="72"  y="116" class="slope-value-left">$105</text>
    <text x="328" y="94"  class="slope-label-right">SOL</text>
    <text x="328" y="86"  class="slope-value-right">$190 ↑</text>

    <!-- Item: Terra — down (negative) -->
    <!-- left y=180, right y=240 -->
    <line x1="80" y1="180" x2="320" y2="240" class="slope-line negative"/>
    <circle cx="80"  cy="180" r="5" class="slope-dot negative"/>
    <circle cx="320" cy="240" r="5" class="slope-dot negative"/>
    <text x="72"  y="184" class="slope-label-left">LUNA</text>
    <text x="72"  y="176" class="slope-value-left">$12</text>
    <text x="328" y="244" class="slope-label-right">LUNA</text>
    <text x="328" y="236" class="slope-value-right">$0.01 ↓</text>
  </svg>
</div>
```

```css
.slope-chart-wrapper {
  width: 100%;
  max-width: 480px;
}

.slope-svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.slope-col-label {
  font-family: var(--font-body);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  fill: var(--muted);
}

.slope-axis {
  stroke: rgba(255,255,255,0.08);
  stroke-width: 1;
}

.slope-line {
  stroke-width: 2;
  fill: none;
}
.slope-line.positive { stroke: var(--primary); opacity: 0.8; }
.slope-line.negative { stroke: #ef4444; opacity: 0.7; }

.slope-dot { fill: var(--bg-primary); stroke-width: 2; }
.slope-dot.positive { stroke: var(--primary); }
.slope-dot.negative { stroke: #ef4444; }

/* Left labels — right-aligned to the left axis */
.slope-label-left {
  font-family: var(--font-body);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  fill: var(--muted);
  text-anchor: end;
}
.slope-value-left {
  font-family: var(--font-display);
  font-size: 11px;
  fill: var(--text-secondary);
  text-anchor: end;
}

/* Right labels — left-aligned from the right axis */
.slope-label-right {
  font-family: var(--font-body);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  fill: var(--muted);
  text-anchor: start;
}
.slope-value-right {
  font-family: var(--font-display);
  font-size: 11px;
  fill: var(--text-secondary);
  text-anchor: start;
}
.slope-value-right.positive { fill: var(--primary); }
.slope-value-right.negative { fill: #ef4444; }
```

---

## 7. Annotated Bar Chart (SVG — Hero Bar + Benchmark)

SVG horizontal bar chart with: one highlighted hero bar, callout annotation, and a benchmark/threshold line. No Chart.js dependency.

**ViewBox:** `0 0 500 280`. Bars start at x=120 (label area). Max bar width = 340px (to x=460). Y positions: 8 rows × 32px each, starting y=40.

```html
<svg viewBox="0 0 500 300" class="annotated-bar-svg">
  <!-- Title -->
  <text x="120" y="18" class="abar-title">STAKING APY BY PROTOCOL</text>

  <!-- Benchmark line at 45% of 340 = x=273 -->
  <line x1="273" y1="22" x2="273" y2="268" class="benchmark-line"/>
  <text x="276" y="30" class="benchmark-label">AVG 18%</text>

  <!-- Row 1: Lido — hero bar (highlighted) — 72% → width=245 -->
  <text x="112" y="50" class="abar-label hero-label">LIDO</text>
  <rect x="120" y="38" width="245" height="20" rx="3" class="abar-fill hero-fill"/>
  <text x="370" y="52" class="abar-value hero-value">72%</text>

  <!-- Callout annotation for hero bar -->
  <!-- SVG line from bar end to annotation box -->
  <line x1="365" y1="48" x2="400" y2="70" class="callout-line"/>
  <rect x="398" y="60" width="90" height="28" rx="4" class="callout-box"/>
  <text x="443" y="71" class="callout-text" text-anchor="middle">TOP APY</text>
  <text x="443" y="82" class="callout-subtext" text-anchor="middle">+4× AVERAGE</text>

  <!-- Row 2: Rocket Pool — 45% → width=153 -->
  <text x="112" y="90" class="abar-label">ROCKET POOL</text>
  <rect x="120" y="78" width="153" height="20" rx="3" class="abar-fill"/>
  <text x="278" y="92" class="abar-value">45%</text>

  <!-- Row 3: Frax — 31% → width=105 -->
  <text x="112" y="130" class="abar-label">FRAX</text>
  <rect x="120" y="118" width="105" height="20" rx="3" class="abar-fill"/>
  <text x="230" y="132" class="abar-value">31%</text>

  <!-- Row 4: Ankr — 18% → width=61 -->
  <text x="112" y="170" class="abar-label">ANKR</text>
  <rect x="120" y="158" width="61" height="20" rx="3" class="abar-fill"/>
  <text x="186" y="172" class="abar-value">18%</text>

  <!-- Row 5: StakeWise — 12% → width=41 -->
  <text x="112" y="210" class="abar-label">STAKEWISE</text>
  <rect x="120" y="198" width="41" height="20" rx="3" class="abar-fill"/>
  <text x="166" y="212" class="abar-value">12%</text>
</svg>
```

```css
.annotated-bar-svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.abar-title {
  font-family: var(--font-body);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  fill: var(--muted);
}

.abar-label {
  font-family: var(--font-body);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  fill: var(--text-secondary);
  text-anchor: end;
  dominant-baseline: middle;
}
.abar-label.hero-label { fill: var(--text-primary); font-weight: 600; }

.abar-fill {
  fill: rgba(255,255,255,0.10);
}
.abar-fill.hero-fill {
  fill: var(--primary);
  filter: drop-shadow(0 0 6px rgba(var(--primary-rgb), 0.5));
}

.abar-value {
  font-family: var(--font-display);
  font-size: 11px;
  fill: var(--text-secondary);
  dominant-baseline: middle;
}
.abar-value.hero-value {
  fill: var(--primary);
  font-weight: 700;
  font-size: 13px;
}

/* Benchmark line */
.benchmark-line {
  stroke: rgba(255,255,255,0.2);
  stroke-width: 1;
  stroke-dasharray: 4 3;
}
.benchmark-label {
  font-family: var(--font-body);
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  fill: var(--muted);
}

/* Callout annotation */
.callout-line {
  stroke: var(--primary);
  stroke-width: 1;
  opacity: 0.5;
}
.callout-box {
  fill: rgba(var(--primary-rgb), 0.12);
  stroke: var(--primary);
  stroke-width: 0.75;
  stroke-opacity: 0.4;
}
.callout-text {
  font-family: var(--font-display);
  font-size: 9px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  fill: var(--primary);
}
.callout-subtext {
  font-family: var(--font-body);
  font-size: 8px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  fill: var(--text-secondary);
}
```

---

## 8. Proportional Circles (SVG — Area = Value)

Compare 3–6 magnitudes using circles where area (not radius) represents the value. Use `r = sqrt(value / π) * scale`. Labels inside or below.

**Rule:** Calculate radius as `r = sqrt(value) * k` where k is a constant that fits the canvas. This ensures area is proportional to value.

**ViewBox:** `0 0 500 220`. Arrange circles left-to-right, largest to smallest.

```html
<svg viewBox="0 0 520 240" class="prop-circles-svg">
  <!-- Title -->
  <text x="260" y="16" class="pcircle-title" text-anchor="middle">MARKET CAP COMPARISON ($B)</text>

  <!--
    Values: BTC=800, ETH=350, SOL=85, BNB=60, ADA=15
    Scale k=0.28: r = sqrt(value) * 0.28 * some_factor
    Use: r = sqrt(value / maxValue) * maxRadius
    maxValue=800, maxRadius=90 → r_btc=90, r_eth=59.5, r_sol=29.3, r_bnb=24.6, r_ada=12.3

    Center y=130 (radius area). X positions spaced by radius sums + gap=16
    BTC: cx=100, ETH: cx=229, SOL: cx=322, BNB: cx=373, ADA: cx=415
  -->

  <!-- BTC — r=90, cx=100, cy=130 -->
  <circle cx="100" cy="130" r="90" class="pcircle c1"/>
  <text x="100" y="125" class="pcircle-label" text-anchor="middle">BTC</text>
  <text x="100" y="141" class="pcircle-value" text-anchor="middle">$800B</text>

  <!-- ETH — r=60, cx=229, cy=130 -->
  <circle cx="229" cy="130" r="60" class="pcircle c2"/>
  <text x="229" y="125" class="pcircle-label" text-anchor="middle">ETH</text>
  <text x="229" y="141" class="pcircle-value" text-anchor="middle">$350B</text>

  <!-- SOL — r=29, cx=322, cy=145 (bottom-aligned for visual interest) -->
  <circle cx="322" cy="175" r="29" class="pcircle c3"/>
  <text x="322" y="172" class="pcircle-label small" text-anchor="middle">SOL</text>
  <text x="322" y="183" class="pcircle-value small" text-anchor="middle">$85B</text>

  <!-- BNB — r=24, cx=374, cy=175 -->
  <circle cx="374" cy="175" r="24" class="pcircle c4"/>
  <text x="374" y="172" class="pcircle-label small" text-anchor="middle">BNB</text>
  <text x="374" y="183" class="pcircle-value small" text-anchor="middle">$60B</text>

  <!-- ADA — r=12, cx=414, cy=175 -->
  <circle cx="414" cy="175" r="12" class="pcircle c5"/>
  <!-- label below for small circles -->
  <text x="414" y="197" class="pcircle-label small" text-anchor="middle">ADA</text>
  <text x="414" y="207" class="pcircle-value small" text-anchor="middle">$15B</text>
</svg>
```

```css
.prop-circles-svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.pcircle-title {
  font-family: var(--font-body);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  fill: var(--muted);
}

/* Color each circle with primary shades */
.pcircle { opacity: 0.9; }
.pcircle.c1 { fill: var(--primary); }
.pcircle.c2 { fill: hsl(from var(--primary) h s calc(l - 12%)); opacity: 0.8; }
.pcircle.c3 { fill: hsl(from var(--primary) h s calc(l - 24%)); opacity: 0.75; }
.pcircle.c4 { fill: hsl(from var(--primary) h s calc(l - 34%)); opacity: 0.7; }
.pcircle.c5 { fill: hsl(from var(--primary) h s calc(l - 42%)); opacity: 0.65; }

/* Fallback explicit shades if CSS relative color syntax unsupported: */
/* .c2 { fill: #C4841A; } .c3 { fill: #9A6614; } etc. — derive from brand primary */

.pcircle-label {
  font-family: var(--font-body);
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  fill: var(--bg-primary);
  /* fills over the circle — ensure contrast */
}
.pcircle-label.small { font-size: 9px; }

.pcircle-value {
  font-family: var(--font-display);
  font-size: 12px;
  font-weight: 700;
  fill: var(--bg-primary);
  font-variant-numeric: tabular-nums;
}
.pcircle-value.small { font-size: 9px; }
```

**Radius calculation helper (run mentally or in a comment):**
```
maxValue = largest data point
maxRadius = 90  (or fit to canvas)
r_i = sqrt(value_i / maxValue) * maxRadius
```

---

## 9. Dot Plot (SVG — Distribution / Individual Points)

Shows individual data points on a linear scale. Less misleading than bars for distributions. Editorial and clean. Best for 8–40 points.

**Orientation:** Horizontal axis (value scale), dots at y positions per category. Use jitter (random y offset within band) if many overlapping points.

```html
<svg viewBox="0 0 500 200" class="dot-plot-svg">
  <!-- Title -->
  <text x="20" y="16" class="dp-title">VALIDATOR UPTIME DISTRIBUTION (%)</text>

  <!-- Axis line -->
  <line x1="20" y1="160" x2="480" y2="160" class="dp-axis"/>

  <!-- Axis ticks + labels: 0, 25, 50, 75, 100 -->
  <!-- scale: value * 4.6 + 20 = x (0→20, 100→480) -->
  <line x1="20"  y1="158" x2="20"  y2="164" class="dp-tick"/>
  <text x="20"  y="175" class="dp-tick-label" text-anchor="middle">0%</text>
  <line x1="135" y1="158" x2="135" y2="164" class="dp-tick"/>
  <text x="135" y="175" class="dp-tick-label" text-anchor="middle">25%</text>
  <line x1="250" y1="158" x2="250" y2="164" class="dp-tick"/>
  <text x="250" y="175" class="dp-tick-label" text-anchor="middle">50%</text>
  <line x1="365" y1="158" x2="365" y2="164" class="dp-tick"/>
  <text x="365" y="175" class="dp-tick-label" text-anchor="middle">75%</text>
  <line x1="480" y1="158" x2="480" y2="164" class="dp-tick"/>
  <text x="480" y="175" class="dp-tick-label" text-anchor="middle">100%</text>

  <!-- Category: Top Validators (y=60) -->
  <text x="15" y="64" class="dp-cat-label" text-anchor="end">TOP TIER</text>
  <!-- Points at: 99.8, 99.5, 99.1, 98.7, 98.2, 97.6 → x = val*4.6+20 -->
  <circle cx="479" cy="60" r="5" class="dp-dot hero"/>  <!-- 99.8% — hero -->
  <circle cx="477" cy="54" r="4" class="dp-dot"/>  <!-- 99.5 -->
  <circle cx="476" cy="66" r="4" class="dp-dot"/>  <!-- 99.1 -->
  <circle cx="474" cy="58" r="4" class="dp-dot"/>  <!-- 98.7 -->
  <circle cx="472" cy="64" r="4" class="dp-dot"/>  <!-- 98.2 -->
  <circle cx="469" cy="56" r="4" class="dp-dot"/>  <!-- 97.6 -->

  <!-- Category: Mid Validators (y=110) -->
  <text x="15" y="114" class="dp-cat-label" text-anchor="end">MID TIER</text>
  <circle cx="400" cy="108" r="4" class="dp-dot mid"/>  <!-- 82% -->
  <circle cx="385" cy="114" r="4" class="dp-dot mid"/>  <!-- 79% -->
  <circle cx="373" cy="106" r="4" class="dp-dot mid"/>  <!-- 77% -->
  <circle cx="360" cy="112" r="4" class="dp-dot mid"/>  <!-- 74% -->
  <circle cx="345" cy="108" r="4" class="dp-dot mid"/>  <!-- 71% -->
  <circle cx="330" cy="116" r="4" class="dp-dot mid"/>  <!-- 68% -->
  <circle cx="312" cy="104" r="4" class="dp-dot mid"/>  <!-- 64% -->

  <!-- Median annotation line -->
  <line x1="365" y1="30" x2="365" y2="150" class="dp-median-line"/>
  <text x="368" y="38" class="dp-annotation">MEDIAN</text>
  <text x="368" y="48" class="dp-annotation-val">75%</text>
</svg>
```

```css
.dot-plot-svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.dp-title {
  font-family: var(--font-body);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  fill: var(--muted);
}

.dp-axis {
  stroke: rgba(255,255,255,0.15);
  stroke-width: 1;
}

.dp-tick {
  stroke: rgba(255,255,255,0.15);
  stroke-width: 1;
}

.dp-tick-label {
  font-family: var(--font-body);
  font-size: 9px;
  fill: var(--muted);
  letter-spacing: 0.04em;
}

.dp-cat-label {
  font-family: var(--font-body);
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  fill: var(--muted);
  dominant-baseline: middle;
}

.dp-dot {
  fill: rgba(255,255,255,0.25);
  stroke: none;
}
.dp-dot.hero {
  fill: var(--primary);
  filter: drop-shadow(0 0 4px rgba(var(--primary-rgb), 0.6));
  r: 6;
}
.dp-dot.mid {
  fill: rgba(255,255,255,0.15);
}

/* Median / reference line */
.dp-median-line {
  stroke: rgba(255,255,255,0.25);
  stroke-width: 1;
  stroke-dasharray: 3 3;
}

.dp-annotation {
  font-family: var(--font-body);
  font-size: 8px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  fill: var(--muted);
}

.dp-annotation-val {
  font-family: var(--font-display);
  font-size: 10px;
  font-weight: 600;
  fill: var(--text-secondary);
  font-variant-numeric: tabular-nums;
}
```
