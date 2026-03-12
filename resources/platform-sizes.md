# Platform Size Guide — Aizfographics
# Last updated: March 2026

## Quick Reference

| Platform | Width | Height | Aspect | export.py --width |
|----------|-------|--------|--------|-------------------|
| **Twitter/X card** | 1200 | 675 | 16:9 | `--width 1200` |
| **Twitter/X portrait** | 1080 | 1350 | 4:5 | `--width 1080` |
| **Instagram post** | 1080 | 1080 | 1:1 | `--width 1080` |
| **Instagram portrait** | 1080 | 1350 | 4:5 | `--width 1080` |
| **Instagram story** | 1080 | 1920 | 9:16 | `--width 1080` |
| **LinkedIn post** | 1200 | 627 | ~2:1 | `--width 1200` |
| **LinkedIn article** | 1200 | 800 | 3:2 | `--width 1200` |
| **Pinterest** | 1000 | 1500 | 2:3 | `--width 1000` |
| **TikTok thumbnail** | 1080 | 1920 | 9:16 | `--width 1080` |
| **General / default** | 1100 | auto | auto | `--width 1100` |

> **Note:** For height, the export script auto-measures document height. You control width via `--width`. For fixed-aspect platforms (Instagram story, TikTok), use the fixed-height CSS below.

---

## Layout & Font Adjustments Per Platform

### Twitter/X (Most Common)
- **Optimal:** 1200×675 (16:9 landscape) — renders full-width in feed
- Portrait (1080×1350) also works and gets 20% more screen space
- Font sizes: use default clamp values — they're calibrated for 1100px, scale proportionally at 1200px
- **Safe zone:** keep critical content 60px inset from all edges (Twitter crops previews)

```css
/* Twitter 16:9 fixed height */
.infographic {
  width: 1200px;
  height: 675px;
  overflow: hidden; /* strict fixed height */
}
```

---

### Instagram Post (1:1 Square)
- 1080×1080 is the golden size
- Grid layouts work better than single-column for square format
- Hero should be compact — 1:1 has no room for a tall hero block
- Increase base font sizes by ~10% vs default (closer viewing distance on mobile)

```css
/* Instagram square fixed canvas */
.infographic {
  width: 1080px;
  height: 1080px;
  overflow: hidden;
  padding: 48px;
}
/* Increase body text for mobile readability */
:root {
  --text-body: clamp(15px, 1.6vw, 18px);
  --text-caption: clamp(12px, 1.2vw, 14px);
}
```

---

### Instagram Story / TikTok (9:16 Vertical)
- 1080×1920 — your natural format (50% of your work is portrait-tall)
- This is where your design DNA shines — full-bleed dark vertical
- Keep text away from top 150px and bottom 250px (UI chrome overlap)
- Use larger hero text — story format allows big bold display

```css
/* Story / TikTok canvas */
.infographic {
  width: 1080px;
  min-height: 1920px;
  padding: 150px 56px 250px; /* safe zones */
}
```

---

### LinkedIn
- 1200×627 for feed posts (standard horizontal)
- More professional audience → use report/ecosystem type palettes
- Text-heavy content works better here than anywhere else
- Slightly increase body text weight (LinkedIn app renders at smaller size)

```css
/* LinkedIn canvas */
.infographic {
  width: 1200px;
  height: 627px;
  overflow: hidden;
}
```

---

### Pinterest
- 2:3 portrait (1000×1500) — tall content performs best
- Pinterest users read carefully → more text is acceptable
- Always include a URL or watermark — Pinterest repins strip metadata

---

## Font Size Scaling by Platform

Your default type scale is calibrated at **1100px width**. When changing width:

| Platform | Width | Scale Factor | --text-body override |
|----------|-------|-------------|---------------------|
| Pinterest | 1000px | 0.91x | `clamp(12px, 1.4vw, 14px)` |
| Default | 1100px | 1.0x | default |
| Twitter/LinkedIn | 1200px | 1.09x | default (auto-scales) |
| Instagram square | 1080px | mobile-viewed → boost | `clamp(15px, 1.6vw, 18px)` |

---

## Watermark / Attribution Rule by Platform

| Platform | Recommendation |
|----------|---------------|
| Twitter/X | Footer URL: small, bottom-left |
| Instagram | Watermark: semi-transparent overlay, bottom-right corner |
| LinkedIn | Footer with company handle + date |
| Pinterest | URL prominently in middle or footer — always visible |
| TikTok | Top-right small watermark (bottom is covered by UI) |

---

## export.py Commands by Platform

```bash
# Twitter 16:9
python scripts/export.py -i infographic.html -o output/twitter -f png --width 1200

# Instagram Square
python scripts/export.py -i infographic.html -o output/instagram -f png --width 1080

# Instagram Story / TikTok
python scripts/export.py -i infographic.html -o output/story -f png --width 1080

# LinkedIn
python scripts/export.py -i infographic.html -o output/linkedin -f png --width 1200

# Pinterest
python scripts/export.py -i infographic.html -o output/pinterest -f png --width 1000

# All formats, default width
python scripts/export.py -i infographic.html -o output/infographic -f all --width 1100
```
