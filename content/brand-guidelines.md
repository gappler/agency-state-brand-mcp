---
title: Agency State — Brand Guidelines
date: 2026-06-25
version: 3.2
status: active
---

# Agency State — Brand Guidelines

**URL:** agencystate.ai
**Tagline:** Enabling human/AI marketing teams.

This is the system of truth for Agency State's visual language. When you build a new page or component, build from this document.

Novel variations live in a page's own CSS. Don't elevate a pattern to this guide just because it appeared twice — repetition alone isn't evidence it belongs in the system. The default answer to "should we add this to the guide?" is **no**. When the temptation arises, push back: surface the question, name the tradeoff, and only update if explicit agreement is reached. Codifying a mistake or a one-off is worse than leaving it out.

This guide was reduced to the brand foundation in v3.0 — logo, type, color, spacing, motion — plus the one page type documented here (the personal-statement homepage). The page-type catalog and conversion components from earlier versions were removed when the cohort/sales offers were retired. New page patterns get documented here *after* they're built, per the rule above — not prescribed in advance. Buildable page recipes (e.g., the lead-magnet page) live in their own skill and reference this foundation rather than duplicating it.

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

- A **white star on a sharp (non-rounded) black square** — the star (representing *state*) positioned toward the right edge and slightly rotated, exiting the square. The visual statement: *state* (the second word) acts on its own *agency* (the first word's secondary meaning, the capacity to act). The buyer sees themselves in the mark — a marketing builder exiting the institutional frame to do their best work.
- **No corner radius — the square is sharp.** Used as the favicon.
- The black mark is the default and the site-wide favicon. A **white-star-on-orange** variant (square in `--accent` `#D4602A`) is in production on the lead-magnet page type — as that page's favicon and as its cover mark. Black remains the default everywhere else.
- Production assets in the brand repo `assets/`: `agency-state-mark-black.svg` / `.png` (default), `agency-state-mark-orange.svg` / `.png` (lead-magnet page).
- Use as favicon, social avatar, and app icon. Not combined with the wordmark into a lockup in production — with one carve-out: **lead-magnet / document covers** may pair the wordmark with the orange mark (see Logo usage › Acceptable configurations).
- Replaces the *as* monogram (lowercase a/s on a rounded square), retired in v2.8 — the lowercase letterforms didn't read at small sizes.

### Full logo (reserved)

The full lockup — monogram icon + wordmark + tagline — exists for brand-introduction contexts (press kits, slide title pages). It is not the default form. In everyday use, the wordmark stands alone.

### Tagline

- "Enabling human/AI marketing teams." in sentence case, regular weight (400), default letter spacing
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
| Bold | 700 | Monogram "a", headings, inline emphasis |

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

The roles currently in production (the homepage). Use these — don't pick new values.

| Role | font-size | weight | line-height | letter-spacing | notes |
|------|-----------|--------|-------------|----------------|-------|
| Hero — tagline | `clamp(1.875rem, 4vw, 3rem)` | 300 | 1.1 | −0.025em | Homepage hero H1; max-width 24ch |
| Prose | 1.125rem (18px) | 300 | 1.65 | default | Bio / lead / body copy; max-width 60ch |
| Body default | 1.0625rem (17px) | 300 | 1.6 | default | Body inherits this |

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
| Secondary text | `--text-secondary` | #5C5C5C | #a0a0a0 | Tagline, secondary body, captions |
| Page background | `--bg` | #FAF9F7 | #121212 | Page surfaces (cream, not pure white) |
| Card background | `--card-bg` | #FFFFFF | #1C1C1C | Cards, elevated surfaces |
| Card hover | `--card-hover` | #F5F4F2 | #242424 | Hover state on cards and interactive surfaces |
| Border | `--border` | #E0DFDC | #2F2E2B | Dividers, subtle separators |
| Accent (orange) | `--accent` | #D4602A | #E47339 | CTAs, links, highlighted metadata, indicator states |
| Accent hover | `--accent-hover` | #B8521F | (TBD) | Hover state on orange CTAs and links |

All eight variables must be declared in every page's `:root`. Don't hardcode hex values in component CSS; reference the variables.

### Color rules

- The logo is monochromatic. It works in any single dark color on a light background, or light color on a dark background.
- No gradients, no shadows, no glow effects on the logo.
- The monogram is a **white star on a sharp square** — black by default (site-wide favicon), orange (`--accent`) on the lead-magnet page type (favicon + cover mark).
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

These minimums govern standalone and print placement. Responsive site chrome is exempt — the fixed nav renders the wordmark at 180px (146px mobile) by design.

### Acceptable configurations

1. **Wordmark only (primary):** `agencystate` outlined — the default use across site navigation, footer, documents, decks, headers, email signatures. Rendered from the outlined SVG, not font-dependent.
2. **Monogram only:** Square mark (white star on black) — favicon, social avatars, app icons, small-format contexts. Not combined into a lockup with the wordmark in production, except on lead-magnet / document covers (config 4).
3. **Full logo (reserved):** Icon + wordmark + tagline — reserved for brand-introduction contexts where full positioning is useful (press kits, slide title pages). Not used in-product or in body documents.
4. **Cover lockup (lead-magnet / document covers):** wordmark + orange monogram stacked on a document cover — the one production context where the wordmark and mark appear together outside the reserved full logo. The mark reads as an accent, not a fixed lockup; spacing is set by the cover layout.

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

## Spacing scale

Use only these rem values for margins, paddings, and gaps. No in-between values. If a layout seems to need a value not on this scale, the layout is wrong, not the scale.

```
0.25  0.5  0.75  1  1.25  1.5  1.75  2  2.5  3  4  5  6.5  7.5  8.5
```

Canonical uses (current pages):

| Value | Used for |
|-------|----------|
| 0.25–0.5rem | Tight grouping (element-level margins, small gaps) |
| 1rem | Default text-block rhythm, small gaps |
| 1.25rem | Mobile container horizontal padding; stacked-item gaps |
| 1.5rem | General gaps (footer rows, content blocks) |
| 1.75rem | Headline → body gap, block rhythm |
| 2rem | Desktop container horizontal padding |
| 2.5rem | Footer block padding |
| 8.5rem | Hero top padding (homepage) |

---

## Layout

### Container

- `max-width: 1200px`
- Horizontal padding: `2rem` desktop, `1.25rem` mobile (≤ 600px)
- `margin: 0 auto` (centered)

All main content sits inside a `.container` wrapper.

### Section rhythm

The homepage uses **whitespace-only separation** — sections sit beside one another with generous padding and no visible rules. No `border-top` on sections or the footer; whitespace alone separates them. The hero uses generous top padding (`8.5rem 0 0`).

### Fixed nav offset

The nav is fixed at the top (height 64px desktop, 56px mobile). Hero padding-top accounts for the nav — don't rely on margin-top workarounds.

---

## Components

Core reusable patterns. If you're building something that matches one of these, use the existing class structure — don't invent a parallel implementation.

### Inline prose link (`.offer-prose a`)

An accent-colored link set inside body prose — used for inline calls to action in running text (e.g., the homepage's "schedule a call" / "LinkedIn" links).

**Specs:**

- `.offer-prose` — body register (1.125rem, weight 300, line-height 1.65, max-width 60ch).
- `.offer-prose a` — color-only signaling: `var(--accent)` default, no underline or border, `transition: color 0.2s ease`, hover shifts to `var(--accent-hover)`, visited matches default. Focus state uses the browser default outline ring — do not suppress with `outline: none`.
- The link reads as continuous prose. No button, arrow, or eyebrow furniture.

### Reveal-on-scroll (`.reveal`, `.d1`–`.d4`)

Content reveals with opacity + translateY as it scrolls into view.

**Pattern:** Add `.reveal` to any block. Add `.d1`/`.d2`/`.d3`/`.d4` to stagger reveal delays within a group.

**Hero exception:** hero `.reveal` elements are forced visible on `DOMContentLoaded` (no scroll needed).

**Script dependency:** pages require the IntersectionObserver script at the end of the body (see live pages).

### Nav

Fixed top, backdrop-blur, border-bottom transitions to visible when scrolled past 16px.

**Spec:**
- `height: 64px` (desktop), `56px` (mobile ≤ 600px)
- `background: rgba(250, 249, 247, 0.9)` with `backdrop-filter: blur(16px)`
- Wordmark left (`width: 180px` desktop, `146px` mobile), no CTA

**Script dependency:** scroll listener toggles `.scrolled` class at scrollY > 16px.

### Footer

**Structure:** brand-definition prose line, then wordmark left (130px) + copyright right. No top border. Flex, space-between, wraps on mobile.

---

## Motion

All animations use Inter's default font metrics. Any motion is short, cubic-bezier-eased, and never loops.

### Reveal

- Initial: `opacity: 0; transform: translateY(14px)`
- Visible: `opacity: 1; transform: translateY(0)`
- Transition: `0.55s cubic-bezier(0.22, 1, 0.36, 1)`

Stagger delays (applied via `.d1`–`.d4`):

| Class | Delay |
|-------|-------|
| `.d1` | 0.05s |
| `.d2` | 0.15s |
| `.d3` | 0.25s |
| `.d4` | 0.35s |

**IntersectionObserver config:** `threshold: 0.12`, `rootMargin: '0px 0px -80px 0px'`.

### Hover

- Color (inline-prose links): `0.2s ease`, color shifts from `var(--accent)` to `var(--accent-hover)`. No underline at any state. Focus uses the browser default outline ring (do not suppress).

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
| ≤ 600px | Mobile / single column; container and hero padding reduce, nav shrinks |

### Mobile adjustments (≤ 600px)

| | Desktop | Mobile |
|-|---------|--------|
| Container horizontal padding | 2rem | 1.25rem |
| Hero top padding | 8.5rem | 6rem |
| Nav height | 64px | 56px |
| Nav wordmark width | 180px | 146px |

---

## Page type

Two page types are in use. The umbrella / personal-statement homepage is documented below. The **lead-magnet / conversion page** (two-column sticky-panel capture page, e.g. `agencystate.ai/claude-code-for-marketing/`) is a buildable recipe — its layout, CTA button, and capture/delivery wiring live in the **leadgen-page skill**, not here, since those are build-time concerns rather than brand foundation. Both page types share the foundation above (logo, type, color, spacing, motion). New page types get documented (or skill-ified) after they're built, not before.

### Umbrella / personal statement (e.g., `agencystate.ai/`)

**Tone:** personal, not marketing. The page is a statement of what the brand is, not a sales pitch. It flows as continuous prose; section transitions are handled by whitespace, not visible rules.

**Allowed:**
- Hero — tagline variant (light 300, smaller scale, max-width 24ch)
- Lead / prose paragraphs (1.125rem, weight 300, line-height 1.65)
- Inline accent link in prose (`.offer-prose a`)
- Reveal-on-scroll for soft entry; hero `.reveal` elements forced visible on `DOMContentLoaded`
- Whitespace-only section separation — sections sit beside one another with generous padding; no visible rules anywhere on the page

**Not allowed:**
- Marketing-style animation or bold "statement" heroes — keep the page quiet throughout
- Visible `border-top` on `<section>` elements or the footer — whitespace alone separates sections
- Standalone CTA buttons or arrow CTAs — the inline prose link does the navigation work

**Meta:** full OG/Twitter meta, canonical URL.

---

## Voice, tone, and copy

See `brand-platform.md`. It's the single source of truth for voice, positioning, brand-name spelling, and what-to-say / what-not-to-say. This doc covers visual identity only.

---

## Pending updates

These items need attention but aren't blocking current work. Resolve when the relevant work happens, not before.

- **Hero `display: flex`.** A prior `.hero` rule had `display: flex; align-items: center` which caused an indent issue; both properties were removed. If it's ever added back to a page, verify it doesn't reintroduce the indent before committing.

- **New page patterns.** The lead-magnet page type shipped (2026-06-25); per the philosophy above, its build recipe lives in the leadgen-page skill rather than this guide. Promote a pattern up to this foundation only if a second, non-lead-gen page adopts it — repetition inside one page type isn't evidence it belongs here.
