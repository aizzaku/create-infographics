# Copy & Headlines Guide — Aizfographics
# Last updated: March 2026

## The Core Rule
Infographics are not articles. Every word competes for space. **Cut 40% of whatever you write first.** Lead with the number, not the explanation.

---

## Stat Formatting Rules

### Numbers — How to Display Them
Always format large numbers for scannability. Never show raw unformatted digits.

| Raw value | ❌ Wrong | ✅ Right |
|-----------|---------|---------|
| 1,000,000,000 | 1000000000 | **1B** |
| 69,000,000,000 | 69000000000 | **69B** |
| 500,000,000 | 500,000,000 | **500M** |
| 1,500,000 | 1500000 | **1.5M** |
| 0.000123 | 0.000123 | **$0.0001** |
| 157,432 | 157432 | **157K** |
| 45.7% | 45.70% | **45.7%** |
| $12,000,000 | $12,000,000 | **$12M** |

### Labeling Stats
- Label always UPPERCASE, below the number
- Use the shortest unambiguous label possible

```
✅ TOTAL SUPPLY      ❌ Total Token Supply
✅ AIRDROP POOL      ❌ Total Tokens for Airdrop
✅ TGE PRICE         ❌ Token Price at TGE Launch
✅ FDV               ❌ Fully Diluted Valuation
✅ STAKING APY       ❌ Annual Percentage Yield
```

### Currency Conventions
- Always prefix with `$` for USD values
- Crypto price: use 4 sig figs max → `$0.0234` not `$0.023400`
- Billions: `$1.2B` | Millions: `$3.4M` | Thousands: `$56K`

---

## Headline Formulas

### Rule: UPPERCASE + Verb-First or Noun-Phrase
Your signature is ALL-CAPS headlines. Structure matters too:

**Type A — Verb-first (action, how-it-works, airdrop)**
```
HOW [PROJECT] WORKS
CLAIM YOUR [TOKEN] AIRDROP
STAKE, EARN, REPEAT
PLAY. EARN. OWN.
```

**Type B — Noun phrase (token-economics, stats, reports)**
```
[PROJECT] TOKENOMICS
THE [PROJECT] ECOSYSTEM
Q4 2025 HIGHLIGHTS
[PROJECT] × [PARTNER] INTEGRATION
```

**Type C — Mission statement (product launch, profile)**
```
THE FUTURE OF [CATEGORY]
[PROJECT]: REDEFINING [THING]
[STAT] [UNIT]. [BOLD CLAIM].
```

### Subtitle Rules
- Subtitles are NOT uppercase — sentence case or title case
- Max 12 words
- Complement the headline — don't repeat it

```
✅ Headline: BYBIT × AVAIL INTEGRATION
   Subtitle: Seamless cross-chain bridging, live February 2026

❌ Headline: BYBIT × AVAIL INTEGRATION
   Subtitle: THE BYBIT AND AVAIL INTEGRATION IS NOW LIVE  ← redundant + wrong case
```

---

## Per-Component Word Budgets

Strict limits. Exceed these and the infographic becomes a document.

| Component | Title | Body | Labels |
|-----------|-------|------|--------|
| **Hero title** | 3–6 words | — | — |
| **Hero subtitle** | — | 8–12 words | — |
| **Stat card** | — | — | 1–3 words UPPERCASE |
| **Feature card title** | 2–4 words | — | — |
| **Feature card body** | — | 15–25 words MAX | — |
| **Timeline node** | 2–4 words | 8–15 words | Date/quarter |
| **Comparison row** | 2–3 words | — | 1–2 words per cell |
| **Footer** | — | 5–15 words | — |
| **Callout/alert** | 2–4 words | 10–20 words | — |
| **Badge/tag** | 1–2 words | — | — |

**If your feature card body exceeds 25 words, you're writing an article, not an infographic. Cut it.**

---

## Color-Coded Keyword Highlighting

One of your signature techniques (from airdrop-guide layout patterns):

Key terms within body text should be wrapped in a colored `<span>`:
```html
<p class="card-body">
  Hold a minimum of
  <span class="highlight">500 $TKN</span>
  in your wallet before the
  <span class="highlight">March 31st</span>
  snapshot date.
</p>
```

```css
.highlight {
  color: var(--primary);
  font-weight: 600;
}
/* or with background tint: */
.highlight-bg {
  background: rgba(var(--primary-rgb), 0.15);
  color: var(--primary);
  padding: 1px 5px;
  border-radius: 3px;
  font-weight: 600;
}
```

Limit: **max 2 highlights per paragraph**. More than that loses the emphasis effect.

---

## Disclaimers & Source Citations

### Footer Disclaimer (Always Include)
```
This infographic is for informational purposes only and does not constitute financial advice.
```
Or shorter:
```
Not financial advice. DYOR.
```

### Source Citation Format
```
Source: [Platform/Report Name], [Month Year]
Data: [Source URL shortened] • @[handle]
```

CSS treatment:
```css
.disclaimer {
  font-family: var(--font-body);
  font-size: 10px;
  color: var(--muted);
  opacity: 0.6;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1.4;
}
```

---

## Badge & Tag Copy

Badges create urgency and context. Rules:
- **1–2 words maximum**
- **ALL CAPS**
- Never use complete sentences

```
✅ LIVE NOW     SEASON 2     BETA     NEW     Q1 2026
✅ FREE MINT    LIMITED      SOLD OUT  V2 LAUNCH
❌ NOW AVAILABLE TO USERS
❌ Currently in beta testing
```

---

## Body Copy Rules — Bullets Over Paragraphs

### Rule: Bullet points, not paragraphs
Body text inside any card, panel, or callout box must be bullet points — never prose paragraphs. The only paragraph allowed in an entire infographic is 1–2 sentences in the hero intro.

```
✅ Inside a card:
• Earns 8% APY on staked tokens
• 30-day lock period after deposit
• Compounding every 24 hours

❌ Inside a card:
"Users who stake their tokens will earn an 8% annual percentage yield
on their deposited assets, with a 30-day lock period that applies
after each deposit, and rewards that compound every 24 hours."
```

### Rule: One fact per line
Never wrap explanations into multi-sentence bullet points. Each bullet = one fact, one condition, one number.

```
✅ One fact per bullet:
• Min stake: 500 $TKN
• Lock period: 30 days
• APY: 8% (compounding daily)

❌ Multi-sentence bullet:
• Users must stake at least 500 $TKN tokens and maintain the lock
  for 30 days to earn the 8% APY, which compounds every day.
```

### Rule: Sentence fragments, not full sentences
Use the shortest phrase that conveys the fact. Drop articles ("the", "a"), drop "users can", drop "this allows":

```
✅ Fragment style:
• Daily rate based on Temperature factor
• 3 egg types: Common, Rare, Legendary
• Snapshot: March 31, 2026

❌ Full sentence style:
• The daily rate is calculated based on the Temperature nurturing factor.
• There are 3 types of eggs available: Common, Rare, and Legendary.
• The snapshot will take place on March 31, 2026.
```

### Rule: Inline token coloring — always color `$TOKEN` names
Token names mentioned inline in any body text must be wrapped in an accent `<span>`. This is a core signature of the designer's style.

```html
✅ Colored token reference:
<li>Hold <span class="highlight">500 $TKN</span> before snapshot</li>
<li>Earn <span class="highlight">$ARENA</span> + <span class="highlight">$ENERGY</span> daily</li>

❌ Uncolored token reference:
<li>Hold 500 $TKN before snapshot</li>
```

Limit: max 2 highlights per bullet. Token names always get colored — limit other highlights to key numbers only.

---

## Common Mistakes to Avoid

| ❌ Don't | ✅ Do Instead |
|---------|-------------|
| "The total token supply is 1 billion" | **1B TOTAL SUPPLY** |
| "Users can earn rewards by staking" | **STAKE & EARN** |
| "This is not financial advice and you should always do your own research before investing" | **Not financial advice. DYOR.** |
| Mixed case section labels: "Token Allocation" | **TOKEN ALLOCATION** |
| Abbreviation without context: "TVL: $2.4M" | **$2.4M TVL** (number first) |
| Generic tag: "Feature" | **NEW** or **LIVE** |
| Paragraph inside a card | Bullet list, one fact per line |
| "The daily rate is based on the Temperature factor" | "Daily rate based on Temperature factor" |
| Uncolored `$TOKEN` in body text | `<span class="highlight">$TOKEN</span>` |
