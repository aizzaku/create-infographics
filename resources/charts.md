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
