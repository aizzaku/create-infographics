# v2 Progress Tracker

Read this file at the start of every session. Update it after completing each item.

---

## Status Key
- `[ ]` Not started
- `[~]` In progress
- `[x]` Complete

---

## SKILL.md Changes

- [x] **1. Mandatory Design Brief** — Add 5-question intake before mode detection. Remove the soft "confirm design constants" from Mode A. If user pre-answered any questions in their message, skip those.
- [x] **2. Thesis-First Architecture** — After brief, before design: state thesis + hero stat + supporting points. Non-negotiable step.
- [x] **3. Visual Concept Declaration** — After thesis, name the aesthetic in 3 words + describe compositional approach.
- [x] **4. Data → Layout Derivation** — Add data-type-to-chart-type mapping table. Instruction: derive layout from data, never start from template.
- [x] **5. Annotation-First Principle** — All labels go directly on charts. No legends unless 5+ series. Add callout line guidance.
- [x] **6. Reduction Pass** — New final step before delivery. Checklist in skill. Note: applies strictly to Editorial/Corporate, loosely to Bold/Cyber.
- [x] **7. Animated HTML Preview** — Add CSS/JS animation guidance for Interactive Builder preview. Per component type: stat counter, bar animate, card stagger, etc.
- [x] **8. New Composition Archetypes** — Add 5 archetypes to the component vocabulary: Typographic Hero, Diagonal Split, Editorial Asymmetric, Full-Bleed Data, Center-Stage Monument.
- [x] **9. Mode 3: Guided Creative** — New mode: brief → thesis+concept → 2 composition options → user picks → one-shot build. Add trigger signals to Mode Detection section.

---

## Resource File Changes

- [x] **10. `resources/design-brief.md` (NEW)** — Full intake framework: question→decision mappings, thesis extraction, tone→palette mapping, audience→density guidance, skip-brief defaults.
- [x] **11. `resources/style-details.md` — Atmospheric Depth** — Add: inline SVG grain filter, gradient mesh background, scanline overlay, paper texture, glassmorphism accent panels.
- [x] **12. `resources/style-details.md` — Annotation System** — Add: direct label CSS, callout line technique, insight callout box, threshold/benchmark line.
- [x] **13. `resources/style-details.md` — Premium Typography** — Add: tabular-nums, minor third scale, weight-based hierarchy, letter-spacing rules.
- [x] **14. `resources/style-details.md` — Reduction Pass Examples** — Add: before/after for gridline removal, legend→label conversion, decoration removal.
- [x] **15. `resources/layout-patterns.md` — Unconventional Archetypes** — Add CSS grid implementations for all 5 new archetypes.
- [x] **16. `resources/charts.md` — Custom SVG Charts** — Add: waffle chart, slope chart, annotated bar, proportional circles, dot plot. Each with full HTML/CSS/SVG template.

---

## Completion Summary
16 / 16 v2 items complete ✓ ALL DONE

---

## V4 Dense Editorial Overhaul (2026-03-20)

**Scope**: Full rewrite of all 16 existing templates + 8 new crypto-specific templates = 24 templates total

### Status

- [x] **Scope 5A — Core crypto template rewrites** (5 templates): `ecosystem.html`, `airdrop-guide.html` rewritten; `token-flywheel.html`, `staking-yield.html`, `defi-protocol.html` created
- [x] **Scope 5B — New crypto templates** (8 templates): `roadmap.html`, `stats-poster.html`, `whitepaper-overview.html`, `game-event.html`, `game-cheat-sheet.html`, `comparison.html` (rewrite), `how-it-works.html` (rewrite), `nft-showcase.html` (rewrite)
- [x] **Scope 5C — Generic template rewrites** (8 templates): `listicle.html`, `feature-roster.html`, `modern-timeline.html`, `dark-modern.html`, `data-story.html`, `event-schedule.html`, `branded-minimal.html`, `light-editorial.html`
- [x] **Scope 5D — SKILL.md update**: Updated content type enum in Step 2 + added full Template Registry section (24 templates × use cases + selection guide table)

### V4 CSS Standards (applied to all 24 templates)

```css
/* Dense table */
.dense-table { font-size: 12px; }
.dense-table td { padding: 7px 12px; vertical-align: middle; font-weight: 500; }
.dense-table tbody tr:nth-child(odd) td { background: rgba(255,255,255,0.02); }
.dense-table thead tr { background: rgba(var(--primary-rgb),0.07); }
.dense-table thead th { font-size: 9px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; }

/* Bullet panel */
.bullet-panel li::before { content: '▸'; color: var(--primary); font-size: 9px; flex-shrink: 0; }
.bullet-panel li { font-size: 11.5px; font-weight: 500; gap: 7px; line-height: 1.4; }

/* Arrow connector */
.arrow-connector { display: flex; align-items: center; gap: 10px; padding: 10px 48px 20px; }
.arrow-line { flex: 1; height: 1px; background: linear-gradient(to right, transparent, rgba(var(--primary-rgb),0.4), transparent); }
.arrow-icon { padding: 4px 12px; border-radius: 3px; background: rgba(var(--primary-rgb),0.08); border: 1px solid rgba(var(--primary-rgb),0.22); }

/* Stat strip */
.stat-box::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: var(--primary); }
.stat-val { font-family: 'Bebas Neue', sans-serif; font-size: 28px; }

/* Section label */
.section-label { display: flex; align-items: center; gap: 14px; padding: 0 48px 12px; }
.section-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }
```

### Session Notes
- 2026-03-20: V4 scope confirmed. User requested full overhaul: rewrite 16 existing + add 8 new crypto-specific = 24 templates total. Core problem: outputs looked like dark-mode SaaS landing pages. Fix: Dense Editorial standard with 8+ content blocks per template, 3+ different component types, tight spacing, visible borders, mandatory arrows/connectors.
- 2026-03-20: V4 complete. All 24 templates written with V4 Dense Editorial CSS standards. SKILL.md updated with expanded content type classification and full Template Registry.
- 2026-03-20: Reference image analysis complete. Vision agent analyzed 12 real portfolio pieces. Key corrections applied to SKILL.md Designer DNA and style-details.md: (1) full-width section separator bands are the dominant section-divider pattern; (2) arrow labels are mandatory — every flow arrow must carry text; (3) branch/split flow nodes are common; (4) swim-lane architecture diagrams; (5) character card grid (5-col, portrait + stat bars) is the game-overview signature component; (6) hierarchical tree diagrams for cheat sheets; (7) blockchain chain color table (ETH=#627EEA, ARB=#E87030, SOL=#9945FF, BNB=#F3BA2F, Base=#0052FF); (8) outer canvas border on game pieces; (9) light mode is CORRECT for game event guides + quest cheat sheets + bounty pocket guides. CSS patterns added to style-details.md for all 8 new component types.

---

## Session Notes
_Append notes here as work progresses. Include any decisions made, patterns discovered, or scope changes._

- 2026-03-16: v2 scope defined. 16 items across SKILL.md + 3 resource files + 1 new resource file.
- 2026-03-16: Item 1 complete. Added Design Brief section before Mode Detection in SKILL.md. Removed Mode A Step 3 "Confirm design constants". Added `brief` object to state schema. Renumbered Mode B steps (now 5 total).
- 2026-03-16: Item 2 complete. Added "Thesis-First Architecture" global section between Design Brief and Mode Detection. Updated Mode A A2 to reference thesis as the component hierarchy anchor. Added Mode B Step 2 "Define Thesis" and renumbered subsequent steps (now 6 total).
- 2026-03-16: Item 3 complete. Added "Visual Concept Declaration" global section after Thesis-First Architecture. Updated Mode A A2 to state the concept before showing the plan. Added Mode B Step 3 "Declare Visual Concept" and renumbered subsequent steps (now 7 total: Brief → Thesis → Concept → Classify → Design System → Build → Export).
- 2026-03-16: Item 4 complete. Added "Data → Layout Derivation" global section after Visual Concept Declaration with 12-row data-task-to-chart-type mapping table and the core rule: data → chart type → layout → component plan. Updated Mode A A2 and Mode B Step 4 to reference the derivation step.
- 2026-03-16: Item 5 complete. Added "Annotation-First Principle" global section between Data→Layout Derivation and Mode Detection. Per-chart-type label placement table, legend exception rule (5+ series only), callout line guidance (SVG lines + insight callout box), and threshold/benchmark line pattern. Added annotation-first check to Quality Check checklist.
- 2026-03-17: Item 6 complete. Added "Reduction Pass" global section between Annotation-First Principle and Mode Detection. 7-item checklist + per-aesthetic strictness table (strict for Editorial/Corporate, loose for Bold/Cyber). Wired into Mode A A6 as Step 3 (moved export to Step 4, Live Editor to Step 5). Wired into Mode B as new Step 7 (export renumbered to Step 8). Added reduction pass check to Quality Check checklist.
- 2026-03-17: Item 7 complete. Added "Animation guidelines for preview (browser only)" within Mode A A3. 6-row component table (stat counter, bar chart, progress bar, feature cards, line chart, flow diagram) with duration/easing specs. Four inline implementation patterns: JS count-up, CSS bar transition, card stagger with setTimeout, SVG stroke-dasharray draw. Added export note: animations run in browser only, PNG/PDF captures final state.
- 2026-03-17: Item 8 complete. Added "Composition Archetypes" global section between Data→Layout Derivation and Annotation-First Principle. 5-archetype table (Typographic Hero, Diagonal Split, Editorial Asymmetric, Full-Bleed Data, Center-Stage Monument) with descriptions and when-to-use guidance. Wired into Mode A A2 (name archetype in plan for 3+ components) and Mode B Step 4 (choose archetype explicitly before building, references layout-patterns.md for CSS grid implementations).
- 2026-03-17: Item 10 complete. Created resources/design-brief.md with: 5 brief questions + decision mappings, aesthetic→design system table, platform→canvas/density table, brand color light/dark suitability heuristic, thesis extraction formulas, tone→palette mapping table, audience sophistication→density/vocabulary table, skip-brief defaults, and a brief→design decision checklist example.
- 2026-03-17: Items 11–14 complete. Added four new sections to resources/style-details.md: Atmospheric Depth Techniques (SVG grain, gradient mesh, scanlines, paper texture, glassmorphism), Annotation System (direct labels, callout lines, insight callout box, benchmark line), Premium Typography (tabular-nums, minor-third scale, weight hierarchy, letter-spacing rules), and Reduction Pass Examples (before/after for gridlines, legend→label, decoration).
- 2026-03-17: Items 15–16 complete. Added "Unconventional Composition Archetypes" section to layout-patterns.md with full CSS grid implementations for all 5 archetypes (Typographic Hero, Diagonal Split, Editorial Asymmetric, Full-Bleed Data, Center-Stage Monument). Added 5 custom SVG chart templates to charts.md (waffle chart, slope chart, annotated bar, proportional circles, dot plot), each with full HTML/SVG markup + CSS + usage notes. Updated "When to Use What" table to include all 5 new types. v2 complete.
- 2026-03-17: Item 9 complete. Added "Guided Creative signals → go to Mode C" block to Mode Detection (4 trigger phrases). Updated "When in doubt" message to mention the third option. Added full Mode C section (6 steps: Design Brief → Thesis+Concept → Present Two Options → User Selects → One-Shot Build → Export) with required output format for the two-option presentation and a selection routing table.
