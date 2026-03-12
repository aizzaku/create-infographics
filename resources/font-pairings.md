# Font Pairings — Aizfographics Design DNA
# Extracted from 175 real infographics — cross-validated by Claude Vision + GPT-5.4
# Last updated: March 2026

## Key Statistics
- **100% of infographics use UPPERCASE labels** — this is your universal signature
- **Bebas Neue** used in 76/175 infographics (43%) — your dominant display font
- **Teko** confirmed in 23/175 (13%) — second condensed display, previously underdetected
- **Inter** used in 162/175 infographics (93%) — your near-universal body font
- **Heading style:** 90% uppercase, 7% mixed-case, 3% normal
- **Heading category:** 69% sans-serif, 27% display, 2% serif

> ℹ️ Font counts cross-validated by running both Claude Opus and GPT-5.4 vision analysis on the same 175 images. Where models disagreed, the GPT-5.4 reading is used as primary (scored avg quality 8.6 vs 7.5).

---

## Your Font Rules (Non-Negotiable)

1. **ALWAYS use UPPERCASE for section labels, stat labels, and category tags**
2. **Bebas Neue is your default display font** — use it unless the mood requires something else
3. **Inter is your default body font** — almost always the right choice
4. **Uppercase headings are your signature** — never title-case your main headers

---

## Your Core Display Fonts (Ranked by usage)

| Font | Used | Category | Best For |
|------|------|----------|---------|
| **Bebas Neue** | 76x | Condensed Sans | Token-economics, headers, labels |
| **Teko** | 23x | Condensed Sans | Tokenomics, esports, compact headings |
| **Montserrat** | 21x | Geometric Sans | Crypto-explainer, professional |
| **Orbitron** | 13x | Sci-Fi Display | Futuristic, DeFi, blockchain |
| **Rajdhani** | 5x | Condensed Sans | Gaming, technical, compact |
| **Bungee** | 6x | Block Display | Bold meme-coins, arcade feel |
| **Space Grotesk** | 4x | Geometric Sans | Web3, modern, clean |
| **Poppins** | 2x | Geometric Sans | Community, accessible |
| **Press Start 2P** | 7x | Pixel/Retro | NFT gaming, retro, arcade |
| **Cinzel Decorative** | 3x | Decorative Serif | NFT, luxury, legendary |

> ⚠️ **Demoted** (GPT-5.4 found 0 confirmed uses): `Bangers`, `Cinzel`, `Exo 2`, `Playfair Display`, `Impact`. These may be visually similar to fonts above — don't remove from your CSS kit but don't prioritise them.

### ✦ 2025/2026 Additions (Premium / Fresh)

| Font | Category | Best For |
|------|----------|---------|
| **Syne** | Geometric Display | Ultra-modern Web3, DeFi, tech startups |
| **Plus Jakarta Sans** | Premium Humanist Sans | Reports, ecosystem overviews, premium brands |
| **Outfit** | Clean Geometric Sans | Contemporary general use, accessible designs |
| **DM Sans** | Humanist Sans | Modern body alternative to Inter, startup feel |
| **Instrument Serif** | Elegant Serif | Editorial contrast, quote callouts, luxury NFT |

---

## Your Body Font (Almost Always the Same)

```
Inter — used in 93% of your infographics (162/175)
```
It's your workhorse. Clean, readable, universal. Only deviate for special projects:
- **DM Sans** — slightly softer, more startup-y alternative (use when Inter feels too corporate)
- **Plus Jakarta Sans** — premium feel, great for reports and polished brands
- **Open Sans** — accessibility-focused, for wider audience content
- **Exo 2** — when sci-fi/gaming feel extends to body text
- **Space Mono** — for data/numbers in tokenomics tables

---

## Tested Font Pairings (Your Actual Combinations)

### 1. BEBAS NEUE + INTER (Your Signature — 40%+ of work)
```css
--font-display: 'Bebas Neue', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Bebas+Neue:wght@400&Inter:wght@300;400;500;600;700`
- **Mood:** bold, professional, crypto-native
- **Use for:** token-economics, airdrop-guide, crypto-explainer

---

### 2. MONTSERRAT + INTER (Professional/Brand)
```css
--font-display: 'Montserrat', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Montserrat:wght@700;800;900&Inter:wght@400;500;600`
- **Mood:** professional, trustworthy, premium
- **Use for:** ecosystem, comparison, DeFi protocol

---

### 3. RAJDHANI + INTER (Gaming/Technical)
```css
--font-display: 'Rajdhani', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Rajdhani:wght@600;700&Inter:wght@400;500`
- **Mood:** gaming, technical, compact
- **Use for:** game-overview, stats-heavy layouts

---

### 4. ORBITRON + INTER (Sci-Fi/DeFi)
```css
--font-display: 'Orbitron', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Orbitron:wght@600;700;800&Inter:wght@400;500`
- **Mood:** futuristic, sci-fi, DePIN
- **Use for:** blockchain infrastructure, DeFi, technical protocols

---

### 5. PRESS START 2P + INTER (Pixel/Retro Gaming)
```css
--font-display: 'Press Start 2P', monospace;
--font-body: 'Inter', sans-serif;
--font-mono: 'VT323', monospace;
```
- **Load:** `Press+Start+2P&Inter:wght@400;500&VT323`
- **Mood:** retro-gaming, pixel art, nostalgic
- **Use for:** NFT gaming, arcade-style, pixel art projects

---

### 6. TEKO + INTER (Esports / Tokenomics) ✦ Confirmed
```css
--font-display: 'Teko', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Teko:wght@500;600;700&Inter:wght@400;500;600`
- **Mood:** esports, bold, condensed, athletic
- **Use for:** token-economics, airdrop-guide, any layout needing a wide uppercase headline that's more compact than Bebas Neue

---

### 7. BUNGEE + INTER (Arcade / Bold Block)
```css
--font-display: 'Bungee', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Bungee&Inter:wght@400;500;600`
- **Mood:** bold, arcade, street-poster, meme-adjacent
- **Use for:** meme tokens, community airdrop guides, any project channel arcade/retro energy

---

### 8. BANGERS + INTER (Meme/Bold)
```css
--font-display: 'Bangers', cursive;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Bangers&Inter:wght@400;500;600`
- **Mood:** playful, meme, loud, bold
- **Use for:** meme tokens, community, fun airdrop guides

---

### 9. CINZEL + INTER (Fantasy/NFT Luxury)
```css
--font-display: 'Cinzel Decorative', serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Cinzel+Decorative:wght@700;900&Inter:wght@400;500`
- **Mood:** fantasy, mystical, premium tier
- **Use for:** NFT showcase, character profiles, legendary rarity

---

### 10. SPACE GROTESK + INTER (Modern Web3)
```css
--font-display: 'Space Grotesk', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Space+Grotesk:wght@600;700&Inter:wght@400;500`
- **Mood:** modern, clean, web3-native
- **Use for:** ecosystem overviews, protocol explainers

---

### 11. SYNE + DM SANS (Ultra-Modern Web3 / Tech) ✦ New
```css
--font-display: 'Syne', sans-serif;
--font-body: 'DM Sans', sans-serif;
```
- **Load:** `Syne:wght@600;700;800&DM+Sans:ital,opsz,wght@0,9..40,300..500;1,9..40,400`
- **Mood:** cutting-edge, bold, startup energy, 2025 premium
- **Use for:** DeFi protocols, tech launches, modern ecosystem maps

---

### 12. PLUS JAKARTA SANS (Premium Report / Brand) ✦ New
```css
--font-display: 'Plus Jakarta Sans', sans-serif; /* 800 weight */
--font-body: 'Plus Jakarta Sans', sans-serif;    /* 400–500 weight */
```
- **Load:** `Plus+Jakarta+Sans:wght@400;500;600;700;800`
- **Mood:** polished, premium, trustworthy, editorial
- **Use for:** quarterly reports, team profiles, funding announcements, investor decks

---

### 13. OUTFIT + INTER (Clean Contemporary) ✦ New
```css
--font-display: 'Outfit', sans-serif;
--font-body: 'Inter', sans-serif;
```
- **Load:** `Outfit:wght@600;700;800&Inter:wght@400;500`
- **Mood:** accessible, contemporary, friendly-professional
- **Use for:** community guides, product launches, general-purpose infographics

---

## Typography Constants (Always Apply)

```css
:root {
  /* Always uppercase for labels and section headers */
  --text-transform-label: uppercase;
  --letter-spacing-label: 0.08em;
  --letter-spacing-hero: 0.02em;

  /* Your type scale */
  --text-hero: clamp(36px, 5vw, 64px);   /* Main title — Bebas Neue */
  --text-h1: clamp(22px, 3vw, 36px);     /* Section headers */
  --text-h2: clamp(16px, 2vw, 22px);     /* Card titles */
  --text-body: clamp(13px, 1.4vw, 15px); /* Body — Inter */
  --text-caption: clamp(10px, 1vw, 12px);/* Labels — UPPERCASE */
  --text-stat: clamp(28px, 4vw, 48px);   /* Big numbers — Bebas Neue */
  --text-mono: clamp(11px, 1.2vw, 13px); /* Data/addresses — mono */
}
```
