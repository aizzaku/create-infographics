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

```css
:root {
  /* 8px grid */
  --space-1: 8px;
  --space-2: 16px;
  --space-3: 24px;
  --space-4: 32px;
  --space-5: 40px;
  --space-6: 48px;
  --space-8: 64px;

  /* Compact mode (53% of your work) */
  --section-padding: 32px 40px;
  --card-padding: 16px 20px;
  --grid-gap: 12px;

  /* Comfortable mode (47% of your work) */
  --section-padding-lg: 48px 56px;
  --card-padding-lg: 24px 28px;
  --grid-gap-lg: 16px;
}
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
  padding: 16px 24px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  margin-bottom: 24px;
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

## Composition Rules (from 175 designs)

```
left-aligned dominant    — 155/175 (89%) ← YOUR RULE
top-to-bottom flow       — dominant
asymmetric balance       — most common
moderate negative space  — most common
```

**Rule:** Always left-align your content. Your entire body of work is left-to-left-aligned. Only center small hero titles.
