# Chart & Data Visualization System — Aizfographics
# Last updated: March 2026

## When to Use What

| Chart Type | Method | When |
|-----------|--------|------|
| Donut / Pie | Inline SVG | Token allocation, any % breakdown ≤ 8 segments |
| Horizontal bar | Pure CSS | Vesting schedule, comparative bars, allocation strips |
| Vertical bar | Chart.js | Multi-period comparisons, time-series bars |
| Line chart | Chart.js | Price over time, growth curves, trend lines |
| Radar / Spider | Chart.js | Game character stats, feature comparisons |
| Progress bar | Pure CSS | Unlock progress, single metric completion |

**Rule:** Use CSS/SVG for anything static and allocation-based. Use Chart.js only when the data is dynamic or the chart type genuinely requires it. Never add Chart.js just for a bar chart you could build in CSS.

---

## 1. SVG Donut Chart (Token Allocation — Your Most-Used)

This is the central chart in 35% of your infographics. Build it inline as SVG so it works in PNG/PDF with zero dependencies.

### How SVG Stroke-Dasharray Works
- Circle circumference = `2 × π × r` — for r=80: **502.65**
- Each segment: `dasharray = "portion_of_502 rest_of_502"` and `dashoffset = -cumulative_offset`

### Template (4-segment example)

```html
<div class="chart-donut-wrapper">
  <svg viewBox="0 0 200 200" width="280" height="280" class="chart-donut">
    <!-- Track (background ring) -->
    <circle cx="100" cy="100" r="80"
      fill="none"
      stroke="rgba(255,255,255,0.06)"
      stroke-width="28"/>

    <!-- Segment 1: Community/Airdrop — e.g. 35% = 175.9 of 502.65 -->
    <circle cx="100" cy="100" r="80"
      fill="none"
      stroke="#F5A623"
      stroke-width="28"
      stroke-dasharray="175.9 326.75"
      stroke-dashoffset="0"
      stroke-linecap="butt"
      transform="rotate(-90 100 100)"/>

    <!-- Segment 2: Ecosystem Fund — e.g. 25% = 125.66 of 502.65 -->
    <circle cx="100" cy="100" r="80"
      fill="none"
      stroke="#00E5A0"
      stroke-width="28"
      stroke-dasharray="125.66 376.99"
      stroke-dashoffset="-175.9"
      stroke-linecap="butt"
      transform="rotate(-90 100 100)"/>

    <!-- Segment 3: Team — e.g. 20% = 100.53 -->
    <circle cx="100" cy="100" r="80"
      fill="none"
      stroke="#00D4FF"
      stroke-width="28"
      stroke-dasharray="100.53 402.12"
      stroke-dashoffset="-301.56"
      stroke-linecap="butt"
      transform="rotate(-90 100 100)"/>

    <!-- Segment 4: Private Sale — e.g. 20% = 100.53 -->
    <circle cx="100" cy="100" r="80"
      fill="none"
      stroke="#E63946"
      stroke-width="28"
      stroke-dasharray="100.53 402.12"
      stroke-dashoffset="-402.12"
      stroke-linecap="butt"
      transform="rotate(-90 100 100)"/>

    <!-- Center logo/text -->
    <circle cx="100" cy="100" r="52" fill="#0D0D0D"/>
    <!-- Place project logo here via <image> or abbreviation text -->
    <text x="100" y="96" text-anchor="middle"
      font-family="'Bebas Neue', sans-serif"
      font-size="14" fill="#8B8B8B" letter-spacing="1">TOKEN</text>
    <text x="100" y="114" text-anchor="middle"
      font-family="'Bebas Neue', sans-serif"
      font-size="22" fill="#FFFFFF">$TKN</text>
  </svg>

  <!-- Legend -->
  <div class="chart-legend">
    <div class="legend-item">
      <span class="legend-dot" style="background:#F5A623;"></span>
      <span class="legend-label">COMMUNITY / AIRDROP</span>
      <span class="legend-pct">35%</span>
    </div>
    <div class="legend-item">
      <span class="legend-dot" style="background:#00E5A0;"></span>
      <span class="legend-label">ECOSYSTEM FUND</span>
      <span class="legend-pct">25%</span>
    </div>
    <div class="legend-item">
      <span class="legend-dot" style="background:#00D4FF;"></span>
      <span class="legend-label">TEAM & ADVISORS</span>
      <span class="legend-pct">20%</span>
    </div>
    <div class="legend-item">
      <span class="legend-dot" style="background:#E63946;"></span>
      <span class="legend-label">PRIVATE SALE</span>
      <span class="legend-pct">20%</span>
    </div>
  </div>
</div>
```

### CSS

```css
.chart-donut-wrapper {
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

### Segment Calculator

Given total circumference = 502.65 (r=80):
```
dasharray_length = percentage / 100 * 502.65
dashoffset       = -(sum of all previous segments' dasharray_lengths)
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
