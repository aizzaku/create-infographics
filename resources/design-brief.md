# Design Brief — Intake Framework
# Maps brief questions to concrete design decisions

---

## The 5 Brief Questions

Run these before any mode detection or design work. Skip questions the user already answered in their message.

| # | Question | Acceptable Answers |
|---|----------|-------------------|
| 1 | **Brand color** | Hex code, logo URL, color name, or "none" |
| 2 | **Aesthetic direction** | A–F (see table below) |
| 3 | **Platform** | Twitter/X · Instagram · LinkedIn · Website · Print/Newsletter |
| 4 | **Hero insight** | "The one number or idea viewers must remember" |
| 5 | **Hard constraints** | Colors to avoid, tone requirements, must-haves / must-avoids |

If the user says "just do it" or skips: proceed with defaults (Dark/Editorial, LinkedIn, no brand color) and note all assumptions before building.

---

## Question 2 → Aesthetic Decision Mapping

| Option | Label | Background | Primary accent | Typography | Decoration |
|--------|-------|------------|---------------|------------|------------|
| A | Editorial/Clean | `#FAFAF9` or `#111111` | Muted single color | Serif headline + sans data | Minimal — whitespace does the work |
| B | Bold/Cyber | `#0D0D0D` | Neon (cyan, amber, lime) | Sans-serif, tight | Glows, gradients, scanlines — earned |
| C | Premium/Luxury | `#0A0A0A` | Gold `#C9A84C` or silver `#B0B7C3` | Serif + condensed sans | Thin borders, no clutter |
| D | Corporate/Trust | `#FFFFFF` or `#F4F6F8` | Brand blue / navy | Clean sans-serif | Light card shadows, no glows |
| E | Playful/Loud | `#F5F0E8` or vivid bg | Saturated multi-color | Rounded sans or display | Bold shapes, illustrations ok |
| F | Custom | User-defined | User-defined | Follow user spec | Follow user spec |

**Reduction pass strictness:**
- A, C, D → strict: strip all non-data decoration
- B, E → loose: brand identity earns its decoration
- F → match user intent

---

## Question 3 → Platform Decision Mapping

| Platform | Canvas size | Density | Safe zones |
|----------|-------------|---------|------------|
| Twitter/X | 1200 × 675px | Medium (5–8 data points) | 40px all sides |
| Instagram | 1080 × 1080px | Low–Medium (3–6 data points) | 48px all sides |
| LinkedIn | 1200 × 627px or 1080 × 1080px | Medium–High (6–10 data points) | 40px all sides |
| Website | 1200 × 800px+ (flexible) | High (up to 15 data points) | 32px all sides |
| Print/Newsletter | 800 × 1100px (A4-ish) | High | 48px all sides |

---

## Question 1 → Light/Dark Suitability

Determine whether a brand color suits light or dark backgrounds before committing.

```
1. Get the brand color hex (e.g., #0057B8)
2. Calculate relative luminance (or use the rule below):

   Light color (luminance > 0.4) → works better on DARK background
   Dark color (luminance < 0.2)  → works better on LIGHT background
   Mid-range (0.2–0.4)           → works on either — default to dark (our standard)

Quick heuristic:
   Bright / pastel / neon → dark background
   Navy / forest / burgundy → light background OR use as accent on dark
   Near-black → light background only
```

**When user provides no brand color:** default to the aesthetic direction's native background.

---

## Thesis Extraction

Extract a single declarative thesis from the user's data before designing anything.

### From raw numbers:

```
User gives: "Monthly active users: Jan 1.2M, Feb 1.4M, Mar 1.9M, Apr 2.6M"
→ Thesis: "User growth is accelerating, not just growing"
→ Hero stat: +117% growth, Jan–Apr
→ Supporting: month-over-month acceleration rate
```

### From a topic brief:

```
User says: "I want an infographic about our product launch"
→ Ask: "What's the one metric or outcome that makes this launch a success?"
→ Their answer becomes the hero stat
→ Everything else supports it
```

### Thesis formula:

```
[Subject] [verb] [insight] — proven by [hero stat].
```

Examples:
- "Remote work increases output — 23% productivity gain over office baseline."
- "DeFi adoption is driven by yield, not ideology — 78% of users entered during high-APY windows."
- "Engagement peaks early and fast — 60% of campaign impressions occur in the first 6 hours."

**If no clear thesis is extractable:** present two candidates and ask the user which direction to build toward.

---

## Tone → Palette Mapping

Map the communication tone to a color palette before touching the design system.

| Tone | Signal words | Primary palette | Accent | Avoid |
|------|-------------|-----------------|--------|-------|
| **Authoritative** | "proves", "data shows", "according to" | Deep navy or black | Single neutral accent | Bright neon, pastels |
| **Alarming / Urgent** | "crisis", "risk", "warning", "drops" | Dark background | Red `#E53935` or amber `#FFB300` | Blues and greens (calm colors) |
| **Optimistic / Growth** | "growth", "opportunity", "up", "record" | Dark or light | Green `#00C853` or brand color | Reds, oranges |
| **Friendly / Community** | "join", "together", "community", "guide" | Light warm bg | Brand color, rounded forms | Heavy glows, corporate coldness |
| **Premium / Exclusive** | "launch", "unveil", "limited", "milestone" | Near-black | Gold or silver | Saturated neons |
| **Analytical / Neutral** | "breakdown", "analysis", "comparison" | Dark or light | Single muted accent | Multi-color palettes |

---

## Audience Sophistication → Density & Vocabulary

Adjust how much you explain and how many data points to include based on who's reading.

| Audience | Signals | Density | Labels | Vocabulary |
|----------|---------|---------|--------|------------|
| **General public** | "explain to anyone", "share on Twitter", no jargon in brief | Low (3–5 points) | Full descriptive labels | Plain language, no acronyms |
| **Industry-savvy** | Domain terms used naturally in brief, LinkedIn | Medium (6–9 points) | Short labels with context | Industry terms ok, define unusual ones |
| **Expert / Insider** | Technical metrics, API/protocol data, academic brief | High (10–14 points) | Terse, precise labels | Full domain vocabulary, no hedging |
| **Executive** | "board deck", "investor update", "one-pager" | Very low (1–3 hero stats) | Bold callouts, no footnotes | Business outcomes only |

---

## Skip-Brief Defaults

When the user skips all or part of the brief, apply these defaults silently and state assumptions before building.

| Question skipped | Default assumption |
|------------------|--------------------|
| Brand color | No brand color — use aesthetic palette only |
| Aesthetic | B (Bold/Cyber) — this skill's native style |
| Platform | LinkedIn (1200 × 627px) |
| Hero insight | Extract from data or ask one targeted question |
| Hard constraints | None — full creative latitude |

**How to communicate defaults:**

> "No brief provided — proceeding with: Bold/Cyber aesthetic, LinkedIn format, no brand color. Hero insight extracted as: [X]. Building now."

Don't ask again. State and proceed.

---

## Brief → Design Decision Checklist

After collecting the brief, map answers to decisions explicitly. Do this in your head or as a one-line statement before building.

```
Brief:
  Brand color: #FF6B35
  Aesthetic: B (Bold/Cyber)
  Platform: Twitter/X (1200×675)
  Hero insight: "Response time cut by 40%"
  Constraints: avoid blue, keep it technical

Design decisions:
  Background: #0D0D0D (dark, Cyber default)
  Primary accent: #FF6B35 (brand — luminance check: bright → works on dark ✓)
  Secondary accent: amber #FFB300 (warm pair to brand orange, avoids blue ✓)
  Canvas: 1200×675px, 40px safe zone
  Typography: tight sans-serif (Cyber), tabular-nums on all stat values
  Hero stat: "40% faster" — dominate 35-40% of canvas (Typographic Hero archetype)
  Tone: Authoritative (data proof) + Premium (technical audience)
  Reduction: loose (Cyber style earns decoration)
```

This mapping step takes 30 seconds and prevents design drift.
