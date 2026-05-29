---
title: Agency State — Brand Guidelines
date: 2026-05-12
version: 2.9
status: active
---

# Agency State — Brand Guidelines

**URL:** agencystate.ai
**Tagline:** In-stack AI for marketers.

This is the system of truth for Agency State's visual language. When you build a new page or component, build from this document.

Novel variations live in a page's own CSS. Don't elevate a pattern to this guide just because it appeared twice — repetition alone isn't evidence it belongs in the system. The default answer to "should we add this to the guide?" is **no**. When the temptation arises, push back: surface the question, name the tradeoff, and only update if explicit agreement is reached. Codifying a mistake or a one-off is worse than leaving it out.

For voice, copy, and positioning decisions, see `brand-platform.md`.

---

## Logo

### Wordmark (primary mark)

- `agencystate`, rendered from outlined SVG paths, set as a single string with no space between words
- "agency" in bold (700) and "state" in regular (400) — the weight shift is the visual identity and must always be preserved
- Always lowercase
- Production asset: `assets/wordmark-black-on-white.svg` in the public `agency-state` repo
- This is the default form of the brand mark — used in site navigation, footer, documents, decks, email signatures

### Monogram icon

- A rounded square with a star (representing *state*) positioned at the right edge — the star exiting the square. The visual statement: *state* (the second word) acts on its own *agency* (the first word's secondary meaning, the capacity to act). The buyer sees themselves in the mark — a marketing builder exiting the institutional frame to do their best work.
- Monochromatic — dark mark on light background, or light mark on dark background, per the broader logo color rule. Default is dark on light.
- Corner radius: 8px at standard size (scale proportionally).
- Use as favicon, social avatar, and app icon only — not combined with the wordmark into a lockup in production.
- Replaces the *as* monogram (lowercase a/s on a rounded square), retired in v2.8 — the lowercase letterforms didn't read at small sizes.

### Full logo (reserved)

The full lockup — monogram icon + wordmark + tagline — exists for brand-introduction contexts (press kits, slide title pages). It is not the default form. In everyday use, the wordmark stands alone.

### Tagline

- "In-stack AI for marketers." in sentence case, regular weight (400), default letter spacing
- Sits below the wordmark, left-aligned with the wordmark start
- Use when the tagline adds context the surrounding copy doesn't already provide (e.g., logo lockups, social bios, slide decks). Omit on pages where the headline and body copy already do the positioning work.

---

## Typography

### Primary typeface: Inter

- Source: Google Fonts — https://fonts.google.com/specimen/Inter
- License: Open Font License (free for all uses)
- Why: clean, highly legible sans-serif with excellent weight range, optimized for screens, professional without being decorative

### Weights used

| Weight | Value | Usage |
|--------|-------|-------|
| Light | 300 | Body copy, secondary text, captions |
| Regular | 400 | Monogram "s", tagline, small UI labels |
| Bold | 700 | Monogram "a", headings, emphasis, CTAs |

**Three weights.** Body copy runs light (300) for visual restraint; headings and emphasis are bold (700). The monogram preserves the original 700/400 contrast. Avoid medium and semibold — they muddy the step between light and bold.

The production wordmark is outlined SVG (`assets/wordmark-black-on-white.svg` in the public `agency-state` repo), so its weight relationship is locked in paths and doesn't depend on loaded font weights.

### Type scale — brand ranges

Use these as guardrails when designing new text roles.

| Element | Size | Weight | Case | Letter spacing |
|---------|------|--------|------|----------------|
| Wordmark | outlined SVG | n/a | lowercase | n/a |
| Monogram letters | 24px (reference) | 700/400 | lowercase | default |
| Tagline | 14px (reference) | 400 | sentence case | default |
| H1 headings | 36–72px | 700 | sentence case | −0.03em |
| H2 headings | 24–32px | 700 | sentence case | default |
| H3 headings | 18–24px | 700 | sentence case | default |
| Body text | 16–19px | 300 | sentence case | default |
| Secondary body | 14–16px | 300 | sentence case | default |
| Labels/captions | 12–14px | 600–700 | uppercase | 0.04–0.06em |

All sizes are reference values. Scale proportionally for different applications.

### Type scale — production implementations

These are the exact specs used in production. Use these — don't pick new values.

| Role | font-size | weight | line-height | letter-spacing | notes |
|------|-----------|--------|-------------|----------------|-------|
| Hero — statement | `clamp(2.5rem, 6.5vw, 4.75rem)` | 700 | 1.02 | −0.03em | Cohort/welcome pages |
| Hero — tagline | `clamp(1.875rem, 4vw, 3rem)` | 300 | 1.1 | −0.025em | Umbrella/personal-statement pages; max-width 24ch |
| Hero — services | `clamp(2rem, 4.5vw, 3.5rem)` | 300 | 1.1 | −0.03em | Services/offer pages; max-width 18ch |
| Section heading | `clamp(1.75rem, 3.25vw, 2.5rem)` | 700 | 1.05 | −0.028em | §2, §3 section h2s (cohort/welcome) |
| Section heading — services | `clamp(1.75rem, 3.25vw, 2.5rem)` | 400 | 1.05 | −0.028em | Services/offer pages |
| Final CTA headline | `clamp(2rem, 4.25vw, 3rem)` | 700 | 1.02 | −0.03em | "Cohort forming now" pattern |
| Final CTA — services | `clamp(2rem, 4.25vw, 3rem)` | 400 | 1.02 | −0.03em | Services/offer pages |
| Hero body / subhead | `clamp(1.0625rem, 1.4vw, 1.1875rem)` | 300 | 1.6 | default | max-width 560px |
| Prose | 1.125rem (18px) | 300 | 1.65 | default | max-width 60ch; `+ .prose` adds 1rem top margin |
| Body default | 1.0625rem (17px) | 300 | 1.6 | default | Body inherits this |
| Eyebrow primary (`.micro`) | 0.75rem (12px) | 700 | inherit | 0.08em | uppercase, accent orange |
| Eyebrow muted (`.micro-muted`) | 0.75rem (12px) | 700 | inherit | 0.08em | uppercase, secondary text gray |
| Small label / detail `dt` | 0.6875rem (11px) | 700 | inherit | 0.08em | uppercase, gray (details list) or orange (important dates) |
| Session number / marker | 0.6875rem (11px) | 700 | inherit | 0.08em | uppercase, accent orange |
| Nav CTA / inline CTA | 0.8125rem (13px) | 700 | default | 0.04em | uppercase, accent orange |
| Detail `dd` | 0.9375rem (15px) | 300 | default | default | body color; inside offer-card details |
| Important-date `dd` | 1.0625rem (17px) | 300 | 1.5 | default | body color; welcome page |

### Fallback stack

```css
font-family: 'Inter', system-ui, -apple-system, sans-serif;
```

---

## Color

### Primary palette

The brand uses a minimal, high-contrast palette. The identity lives in typography and weight contrast — color is a supporting layer.

| Role | CSS variable | Light mode | Dark mode | Usage |
|------|--------------|-----------|-----------|-------|
| Primary text | `--text` | #1A1A1A | #f0f0f0 | Wordmark, icon background, headings, primary copy |
| Secondary text | `--text-secondary` | #5C5C5C | #a0a0a0 | Tagline, secondary body, captions, muted `dt` labels |
| Page background | `--bg` | #FAF9F7 | #121212 | Page surfaces (cream, not pure white) |
| Card background | `--card-bg` | #FFFFFF | #1C1C1C | Cards, elevated surfaces, phase blocks |
| Card hover | `--card-hover` | #F5F4F2 | #242424 | Hover state on cards and interactive surfaces |
| Border | `--border` | #E0DFDC | #2F2E2B | Dividers, card outlines, subtle separators |
| Accent (orange) | `--accent` | #D4602A | #E47339 | CTAs, links, highlighted metadata, indicator states |
| Accent hover | `--accent-hover` | #B8521F | (TBD) | Hover state on orange CTAs and buttons |

All eight variables must be declared in every page's `:root`. Don't hardcode hex values in component CSS; reference the variables.

### Color rules

- The logo is monochromatic. It works in any single dark color on a light background, or light color on a dark background.
- No gradients, no shadows, no glow effects on the logo.
- The monogram icon inverts: dark background with light letters in light mode, light background with dark letters in dark mode.
- The accent orange is used sparingly — CTAs, links, highlighted inline metadata, and gate or indicator states only. Never for body copy, plain headings, or large surfaces. The typography carries the identity, not the color.
- **Emphasis exception.** Accent orange may be used for emphasis markup (`<em>`) within headlines and for complete standalone pull quotes. In these contexts orange marks the conceptual payload — the one word or phrase that carries the idea. The reader learns the grammar: orange = the point.

---

## Logo usage

### Minimum clear space

Maintain clear space around the full logo equal to the height of the monogram icon on all sides. No other elements should intrude into this zone.

### Minimum size

- Full logo (icon + wordmark + tagline): minimum width 280px / 2.5 inches
- Wordmark only (no icon, no tagline): minimum width 200px / 1.75 inches
- Monogram icon only: minimum 32px / 0.3 inches

### Acceptable configurations

1. **Wordmark only (primary):** `agencystate` outlined — the default use across site navigation, footer, documents, decks, headers, email signatures. Rendered from the outlined SVG, not font-dependent.
2. **Monogram only:** Square icon with a/s — favicon, social avatars, app icons, small-format contexts. Not combined into a lockup with the wordmark in production.
3. **Full logo (reserved):** Icon + wordmark + tagline — reserved for brand-introduction contexts where full positioning is useful (press kits, slide title pages). Not used in-product or in body documents.

### Do not

- Add space between "agency" and "state" in the wordmark
- Use the wordmark in all caps or title case
- Change the weight relationship (both words same weight)
- Add color, gradient, or effects to the logo
- Rotate, skew, or distort the logo
- Place the logo on busy backgrounds without sufficient contrast
- Rearrange the elements (tagline above wordmark, icon on right, etc.)
- Use a different typeface for the wordmark

---

## Logo SVG (reference)

```svg
<svg width="100%" viewBox="0 0 680 150" xmlns="http://www.w3.org/2000/svg">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
.logo-heavy { font-family: 'Inter', sans-serif; font-weight: 700; font-size: 52px; fill: #1a1a1a; }
.logo-light { font-family: 'Inter', sans-serif; font-weight: 400; font-size: 52px; fill: #1a1a1a; }
.logo-tag { font-family: 'Inter', sans-serif; font-weight: 400; font-size: 14px; fill: #6b6b6b; }
.mark-bg { fill: #1a1a1a; }
.mark-star { fill: #ffffff; }
</style>
<!-- Monogram: rounded square with star (representing *state*) exiting the right edge.
     Production asset stored separately; star path to be inserted from the finalized
     vector mark. The rect below is the institutional frame the star exits. -->
<rect class="mark-bg" x="40" y="38" width="44" height="44" rx="8"/>
<!-- <path class="mark-star" d="..." /> star path goes here once finalized -->
<text y="75" x="100">
<tspan class="logo-heavy">agency</tspan><tspan class="logo-light">state</tspan>
</text>
<text class="logo-tag" x="100" y="105">In-stack AI for marketers.</text>
</svg>
```

---

## Spacing scale

Use only these rem values for margins, paddings, and gaps. No in-between values. If a layout seems to need a value not on this scale, the layout is wrong, not the scale.

```
0.25  0.5  0.75  1  1.25  1.5  1.75  2  2.5  3  4  5  6.5  7.5  8.5
```

Canonical uses:

| Value | Used for |
|-------|----------|
| 0.25–0.5rem | Tight grouping (dl row gaps, element-level margins) |
| 0.75rem | Offer-card details row gap |
| 1rem | Default text-block rhythm, small gaps |
| 1.25rem | Mobile container horizontal padding |
| 1.5rem | Eyebrow → headline gap, card head padding |
| 1.75rem | Headline → body gap, card internal padding |
| 2rem | Desktop container horizontal padding, section header → content |
| 2.5rem | Heading block → first content block |
| 3rem | Section-internal stacks |
| 4rem | Standard section vertical padding |
| 5rem | Hero bottom padding (generous variant) |
| 6.5rem | Final CTA section bottom padding |
| 7.5rem | Hero top padding (cohort variant — tight) |
| 8.5rem | Hero top padding (umbrella variant — breathing room) |

---

## Layout

### Container

- `max-width: 1200px`
- Horizontal padding: `2rem` desktop, `1.25rem` mobile (≤ 600px)
- `margin: 0 auto` (centered)

All main content sits inside a `.container` wrapper. Full-bleed sections wrap their inner content in `.container`.

### Section rhythm

Each major section is a `<section>` with `padding: 4rem 0` and `border-top: 1px solid var(--border)`. Exceptions:

- **Hero:** no top border. Padding `7.5rem 0 4rem` (cohort/statement) or `8.5rem 0 5rem` (umbrella/tagline).
- **Final CTA (`.book` / `.cta-section`):** `padding: 5rem 0 6.5rem` with top border.
- **Services / offer pages:** `padding: 3rem 0` at all breakpoints. Tighter than the `4rem 0` default to match the services-page register — less air between sections to read as quieter and offer-focused. See *Page types: Services / offer page*.
- **Umbrella / personal-statement pages:** no `border-top` on any section, including the footer. Whitespace alone separates sections. Padding is sized to give breaks visual weight without visible rules — the bio block flows into the offer mention, then a wider gap (typically `5rem` of section padding) before the contact line. The footer drops its top border too. See *Page types: Umbrella / personal statement*.

### Fixed nav offset

The nav is fixed at the top (height 64px desktop, 56px mobile). Hero padding-top accounts for the nav — don't rely on margin-top workarounds.

---

## Components

Core reusable patterns. If you're building something that matches one of these, use the existing class structure — don't invent a parallel implementation.

### Bracket-corner card (`.offer-card`, `.offer-tile--active`)

White card with 1px gray border plus 16×16px orange L-shaped brackets at top-left and bottom-right (via `::before` and `::after`).

**Use when:** featuring a primary card on a cohort / sales page — offer tile, offer detail, anything that deserves visual weight in a conversion-focused register.

**Structure:**
```
.card
  ::before (top-left bracket)
  ::after (bottom-right bracket)
  .card-head (flex, space-between, border-bottom)
    eyebrow + meta value
  .card-body
    (dl or content)
  .card-cta
    (button)
```

**Do not** use cards without the bracket corners for "primary" items on cohort / sales pages — the brackets are a signature. A card without brackets reads as secondary in that context.

**Do not use on:** umbrella / personal-statement pages or services / offer pages. The bracket-corner card carries cohort/sales-page weight; on quieter page types it reads as marketing assertion. For those page types, mention the offer in prose with a bold inline title and an inline accent-orange CTA link instead (see *Inline offer-mention pattern* below).

### Inline offer-mention pattern

Pattern for surfacing a current offer on umbrella / personal-statement pages — page types where a bracket-corner card or even a separate CTA element would over-perform.

**Use when:** a personal-statement page needs to point at a current offer without adopting any conversion-page furniture (eyebrow, card, button, arrow CTA).

**Structure:**
```
section
  p.offer-prose
    "Right now the way to engage is the "
    a (offer name → offer page)
    " — short qualifying clause."
```

**Specs:**

- `.offer-prose` — body register (1.125rem, weight 300, line-height 1.65, max-width 60ch). One short sentence. No bold inline title, no eyebrow, no separate CTA element below.
- `.offer-prose a` — the inline-prose link pattern shared across the page register. Color-only signaling: `var(--accent)` default, no underline or border, `transition: color 0.2s ease`, hover shifts to `var(--accent-hover)`, visited matches default. Focus state uses the browser default outline ring — do not suppress with `outline: none`. The offer name *is* the link; clicking it goes to the offer detail page.
- The offer paragraph follows the bio or surrounding prose with no section divider, no eyebrow, and no special spacing treatment; the offer mention reads as continuous prose with the bio.

**What this pattern is not:**

- Not a button. Not a CTA-styled link with an arrow. Not bolded. The inline link does the navigation work without performing.
- Not a multi-sentence offer description. One sentence is the cap. Detail belongs on the offer page the link points to, not the homepage.

### Definition list (`dl` / `.offer-details`)

Two-column grid for label/value pairs.

**Spec:**
- `display: grid; grid-template-columns: auto 1fr`
- `column-gap: 1.5rem`, `row-gap: 0.75rem`
- `dt`: small uppercase label (see Type scale)
- `dd`: body-size value

**Color variants:**
- `dt` gray (`var(--text-secondary)`): offer details (Format, Price, etc.)
- `dt` orange (`var(--accent)`): important dates (Today, Jun 8) — use when the label is itself content, not just a frame for the value

### Hero offer-card layout

Two-column hero: narrative left, offer card right. Used on cohort/sales pages.

**Spec:**
- Grid: `grid-template-columns: minmax(0, 1.6fr) minmax(300px, 1fr)`, `gap: 5rem`, `align-items: end`
- Applies at ≥ 920px; collapses to single column below
- Left column height should roughly match card height for natural bottom alignment

### Eyebrow pattern

Small uppercase label above a headline or section heading.

**Pattern:** `<p class="micro hero-label">…</p>` then `<h1>…</h1>`
- `.micro` (orange) for primary eyebrows (cohort/section identity)
- `.micro-muted` (gray) for secondary (e.g., "Offers" heading)
- Bottom margin to next element: `1.5rem`

### Reveal-on-scroll (`.reveal`, `.d1`–`.d5`)

Content reveals with opacity + translateY as it scrolls into view.

**Pattern:** Add `.reveal` to any block. Add `.d1`/`.d2`/`.d3`/`.d4`/`.d5` to stagger reveal delays within a group.

**Hero exception:** hero `.reveal` elements are forced visible on `DOMContentLoaded` (no scroll needed).

**Script dependency:** pages require the IntersectionObserver script at the end of the body (see live pages).

### Em underline animation

Orange underline draws left-to-right under an emphasized word in a hero headline.

**Pattern:** `<h1 class="hero-headline"><em>word</em></h1>`

**Use when:** marking the conceptual payload of a cohort/welcome headline ("deserves **better.**", "You're **in.**").

**Do not use on:**

- Umbrella/personal-statement pages (e.g., the homepage). The animation reads as marketing — inappropriate for pages that aren't selling something specific.
- Services/offer pages. The services-page register is confident and quiet; the underline draw reads as performing. The orange `<em>` color emphasis is still used to mark the conceptual payload — just without the animated draw.

### Nav

Fixed top, backdrop-blur, border-bottom transitions to visible when scrolled past 16px.

**Spec:**
- `height: 64px` (desktop), `56px` (mobile ≤ 600px)
- `background: rgba(250, 249, 247, 0.9)` with `backdrop-filter: blur(16px)`
- Wordmark left (`width: 160px` desktop, `130px` mobile), optional CTA right

**Script dependency:** scroll listener toggles `.scrolled` class at scrollY > 16px.

### Footer

**Structure:** wordmark left (130px), copyright + "Built with Claude Code" right. Flex, space-between, wraps on mobile.

---

## Motion

All animations use Inter's default font metrics. Any motion is short, cubic-bezier-eased, and never loops.

### Reveal

- Initial: `opacity: 0; transform: translateY(14px)`
- Visible: `opacity: 1; transform: translateY(0)`
- Transition: `0.55s cubic-bezier(0.22, 1, 0.36, 1)`

Stagger delays (applied via `.d1`–`.d5`):

| Class | Delay |
|-------|-------|
| `.d1` | 0.05s |
| `.d2` | 0.15s |
| `.d3` | 0.25s |
| `.d4` | 0.38s |
| `.d5` | 0.5s |

**IntersectionObserver config:** `threshold: 0.12`, `rootMargin: '0px 0px -80px 0px'`.

### Underline draw

- Duration: `0.7s`
- Easing: `cubic-bezier(0.22, 1, 0.36, 1)`
- Delay: `0.55s` after `.visible` is applied
- Mechanism: `background-size` animates from `0% 0.08em` to `100% 0.08em` on the `em`

### Hover

- Color (inline-prose links): `0.2s ease`, color shifts from `var(--accent)` to `var(--accent-hover)`. No underline at any state. Focus uses the browser default outline ring (do not suppress).
- Background (buttons): `0.2s ease` (accent → accent-hover)
- Transform (arrows): `0.25s cubic-bezier(0.22, 1, 0.36, 1)` — typically `translateX(3–4px)` or `translateY(3px)`

### Nav scroll state

- Border transition: `border-color 0.3s ease`
- Threshold: `scrollY > 16px`

### Never use

- Loops, pulses, bounces, or continuous motion
- Shadows on elevation change
- Parallax
- Motion timings faster than 0.2s or slower than 0.7s

---

## Responsive system

### Breakpoints used

| Width | Triggers |
|-------|----------|
| ≤ 600px | Mobile / single column; container padding and hero padding reduce, nav shrinks |
| ≥ 700px | Curriculum sessions go 1 col → 2 col |
| ≥ 820px | Offer-grid (homepage) goes 1 col → 2 col; book-inner (CTA) goes 1 col → 2 col |
| ≥ 920px | Hero-grid goes 1 col → 2 col (narrative + offer-card) |
| ≥ 1300px | Curriculum sessions go 2 col → 4 col |

### Mobile adjustments (≤ 600px)

| | Desktop | Mobile |
|-|---------|--------|
| Container horizontal padding | 2rem | 1.25rem |
| Hero top padding | 7.5rem / 8.5rem | 6rem |
| Hero bottom padding | 4rem / 5rem | 3rem |
| Nav height | 64px | 56px |
| Nav wordmark width | 160px | 130px |
| Section vertical padding | 4rem; 3rem (services) | 3rem (homepage, services) / 4rem (cohort) |

---

## Page types

Three page types exist in the Agency State system. Each carries a voice and a set of allowed components.

### Umbrella / personal statement (e.g., `agencystate.ai/`)

**Tone:** personal, not marketing. The page is a statement of what the brand is, not a sales pitch. The page flows as continuous prose; section transitions are handled by whitespace, not by visible rules.

**Allowed:**
- H1 greeting — small light register (e.g., `clamp(1.75rem, 3vw, 2.25rem)`, weight 300) when a quiet "Hi." or similar greeting opens the page
- Hero — tagline variant (light 300, smaller scale, max-width 24ch) when a tagline is rendered above the bio
- Lead paragraph — prose register (1.125rem, weight 300, line-height 1.65) for the bio or opening statement
- Eyebrow (optional)
- Byline / signoff (`— Greg Appler`) — appropriate here because the page carries personal voice
- Inline offer-mention pattern (`.offer-prose` with one inline-prose link) — see *Components > Inline offer-mention pattern*
- About section with prose
- Whitespace-only section separation — sections sit beside one another with generous padding; no visible rules anywhere on the page

**Not allowed:**
- Em underline animation (too markety)
- Bold statement hero (reserved for cohort pages)
- Final CTA section
- Bracket-corner cards (reserved for cohort / sales pages — the bracketed card reads as marketing assertion in the personal-statement register)
- Hero-scale typography on offer mentions or section headings — keep the page quiet throughout
- `border-top` on `<section>` elements or the footer — visible horizontal rules belong on cohort / sales pages where each section is doing distinct conversion work; on personal-statement pages they fight the continuous-prose register
- Standalone CTA buttons or arrow CTAs for the offer mention — the inline link inside the prose sentence does the navigation work

### Cohort / sales page (e.g., `/associations/`)

**Tone:** bold, specific, conversion-focused.

**Allowed:**
- Hero — statement variant (bold 700, larger scale, optional em underline)
- Hero offer-card layout (narrative + offer-card two-column)
- Section blocks with eyebrows and prose
- Session cards (curriculum layout)
- Final CTA section with instructor bio + CTA + meta
- Register CTAs (offer-card + final section, typically two per page)

**Not allowed:**
- First-person signoff (`— Greg`) — use third-person instructor bio instead
- Nav CTAs (keep the nav wordmark-only; the page has its own CTAs)

**Meta:** full OG/Twitter meta, canonical URL.

### Welcome / utility page (e.g., `/welcome/`)

**Tone:** confirmatory, condensed, no marketing pressure.

**Allowed:**
- Hero — statement variant (consistency with cohort pages)
- Em underline on affirming words ("You're **in.**")
- Single-column layout
- Inline definition list for important dates (orange `dt` labels)
- Email link with Plausible tracking

**Not allowed:**
- Offer cards (this isn't a sale)
- Bracket-corner components
- CTAs (nothing to convert to; the transaction is complete)
- Signoff

**Meta:** `<meta name="robots" content="noindex,nofollow">`. No OG/Twitter meta needed — page shouldn't be shared or indexed.

### Services / offer page (e.g., `/workflow-automation-sprint/`)

**Tone:** confident and quiet. Offer-focused, type-driven. The page presents a service offer for the buyer to evaluate — reads as a senior practitioner explaining what they do, not a marketing page selling something. The lighter typographic register is the point: scale carries presence; weight does not perform.

Section vertical padding tightens to `3rem 0` (from the `4rem 0` default) at all breakpoints. Less air between sections matches the quieter typographic treatment.

**Allowed:**

- Hero — services variant (smaller scale than cohort statement; weight 300; line-height 1.1)
- Section heading — services variant (weight 400)
- Final CTA — services variant (weight 400)
- Em color emphasis in hero — orange `<em>` for the conceptual payload, **without** the underline animation
- Section blocks with H2s and prose
- Numbered outcome list (counter-based, no card wrapper)
- Inline-labeled detail paragraphs (bold inline label leading prose)
- Reveal-on-scroll for soft entry; hero `.reveal` elements forced visible on `DOMContentLoaded`
- Hero CTA + final CTA buttons (accent orange, same button treatment as cohort pages)

**Not allowed:**

- Em underline animation
- 700-weight headings (the lighter register is the point; bold remains for inline labels and CTA buttons only)
- Bracket-corner cards
- Hero offer-card two-column layout (hero is single-column statement, no card)
- First-person signoff (`— Greg`)
- Nav CTAs (the page has its own)

**Meta:** full OG/Twitter meta, canonical URL.

---

## Voice, tone, and copy

See `brand-platform.md`. It's the single source of truth for voice, positioning, brand-name spelling, and what-to-say / what-not-to-say. This doc covers visual identity only.

---

## Pending updates

These items need attention but aren't blocking current work. Resolve when the relevant work happens, not before.

- **Hero offer-card layout — `align-items` value.** Currently documented as `end`; production was changed to `start` on April 24 to fix a vertical alignment issue. Update the spec to `start` once the new cohort page is built and confirms the change is permanent.

- **Hero padding values.** Currently documented as `7.5rem 0 4rem` for the cohort variant. Production was tightened to `7.5rem 0 2.5rem` on April 24. Update once the new cohort page is built.

- **Cohort/sales page type — pattern documentation.** The current page type description references "two register CTAs (offer-card + final section, typically two per page)." The most recent cohort page iteration removed the second offer card in favor of a simpler close section (bio + register button only). When the new cohort page (Annual Planning, July 2026) is built, document whatever pattern it lands on and update this section.

- **Homepage tagline placement.** The current homepage opens directly with the bio paragraph; no tagline rendered above it. With *In-stack AI for marketers.* now the canonical tagline (v2.7), evaluate whether it deserves a slot above the bio or stays reserved for logo lockups, social bios, and slide decks per the existing usage rule. Working assumption: stays reserved.

- **Hero `display: flex`.** The `.hero` rule had `display: flex; align-items: center` which caused the indent issue on April 24. Both properties were removed. The visual guide doesn't explicitly document this, but if it's ever added back to a page in the future, verify it doesn't reintroduce the indent before committing.
