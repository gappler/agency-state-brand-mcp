---
title: Agency State Brand Guidelines
version: 4.1
date: 2026-08-28
last_updated: 2026-10-11
status: Current. The surface-independent brand layer only; visual implementation lives in the design system (see the closing section).
version_note: >
  v4.0 re-derives the document against the current draft pages and shared stylesheet (AGE-30).
  The 2026-08-25 staleness audit found nine of v3.2's twelve sections were a specification of the
  retired legacy site, false against the live pages. Those sections are removed, not rewritten.
  What remains is the layer that does not change when the surface changes: the wordmark, the mark,
  the typeface identity (the three faces and their roles), the accent grammar (orange marks the
  payload word), the logo do-not list, and the motion principles. The typeface identity is kept on
  the same footing as the fixed accent orange, an identity fact, not an implementation value.
  Everything a machine can read out of the CSS (the type ramp and stacks, the palette hexes, the
  spacing scale, the weight assignments, component specs) now lives in design-system.md plus
  design-system.css, generated and enforced there, and is not restated here. Provenance of this
  pass: the three typefaces, both accent hexes, and the wordmark and header-lockup descriptions
  were verified against design-system.css and the live pages; the logo minimum sizes (280px full
  logo, 200px wordmark, 32px mark) are carried forward from v3.2 unverified, kept as legibility
  minimums for the mark, which the website does not change. Audit of record:
  agency-state-practice/projects/brand-os/readiness-assessment/guidelines-staleness-audit.md.
---

# Agency State Brand Guidelines

**URL:** agencystate.ai

This document holds the **surface-independent brand layer**: the parts of the visual identity that stay true no matter how a given page is built. That is the wordmark, the mark, the typeface identity, the accent grammar, and the rules for how the logo may and may not be used.

It deliberately does **not** specify the type ramp, the font stacks, the weight assignments, the color palette, the spacing scale, layout, components, motion timings, breakpoints, or page types. Those are implementation, they change as the site is built, and they live in the design system where they are generated from the stylesheet and checked against it. Restating them here is what made the previous version drift into describing a site that no longer exists. See "Where the visual implementation lives."

## What earns a place in this guide

The default answer to "should we add this to the guide?" is **no**. This document carries only what is stable across surfaces and cannot be read out of a file by a machine. Repetition alone is not evidence a pattern belongs here; a thing appearing on two pages is a candidate for the design system, not for this brand layer. When the temptation arises, surface the question, name the tradeoff, and add only on explicit agreement. Codifying a one-off, or hand-copying a value that a machine already enforces elsewhere, is worse than leaving it out.

---

## Logo

### Wordmark (primary mark)

- `agencystate`, rendered from outlined SVG paths, set as a single string with no space between the two words.
- "agency" in bold (700) and "state" in regular (400). The weight shift is the visual identity and must always be preserved. Because the production asset is outlined SVG, the weight relationship is locked in the paths and does not depend on any loaded font.
- Always lowercase.
- Rendered on the site as the inline SVG wordmark (`.wmlogo`), filled to the ink color via CSS. Never re-typeset the wordmark as live text.
- This is the default form of the brand mark: site navigation, footer, documents, decks, email signatures.

### Monogram (the mark)

- A **white star on a sharp (non-rounded) square**, the square in near-black (`#111111`). The star (representing *state*) sits toward the right edge and is slightly rotated, exiting the square. The statement: *state* acts on its own *agency* (the capacity to act). The buyer sees themselves in the mark, a marketing builder stepping out of the institutional frame to do their best work.
- **No corner radius. The square is sharp.**
- The **black mark is the default** and the site-wide favicon. A **white-star-on-orange** variant (the square in the accent orange) is reserved for lead-magnet page types and branded social preview cards, where it works as an accent beside the wordmark. Black everywhere else.
- Used as favicon, social avatar, and app icon.
- Replaces the *as* monogram (lowercase a/s on a rounded square), retired in v2.8 because the lowercase letterforms did not read at small sizes.

### Full logo (reserved)

The full lockup (mark + wordmark + tagline) exists for brand-introduction contexts (press kits, slide title pages). It is not the default. In everyday use the wordmark stands alone.

### Tagline placement

The tagline string is an identity line, not a visual-identity spec. It lives in the brand platform (§1, served through `get_identity`), not here. This document governs only how a tagline is set when a lockup uses one:

- Sentence case, regular weight (400), default letter spacing.
- Sits below the wordmark, left-aligned with the wordmark start.
- Used only in lockups and brand-introduction contexts (press kits, slide title pages, social bios), not on pages where the headline and body already do the positioning work.

For the current tagline string, see platform §1.

---

## Logo usage

### Minimum clear space

Maintain clear space around the full logo equal to the height of the mark on all sides. No other element intrudes into that zone.

### Minimum size

- Full logo (mark + wordmark + tagline): minimum width 280px / 2.5 inches.
- Wordmark only (no mark, no tagline): minimum width 200px / 1.75 inches.
- Mark only: minimum 32px / 0.3 inches.

These minimums govern standalone and print placement. Responsive site chrome is exempt: the site header sizes the wordmark and mark for the nav by design, at values set in the design system, not by this minimum.

### Acceptable configurations

1. **Wordmark only (primary):** `agencystate` outlined. The default across site navigation, footer, documents, decks, headers, and email signatures. Rendered from the outlined SVG, not font-dependent.
2. **Mark only:** the square mark (white star on the black square). Favicon, social avatars, app icons, and small-format contexts where a wordmark would not read.
3. **Header lockup:** in site chrome, the mark sits immediately left of the wordmark. This is the one in-product context where mark and wordmark appear together. They are set side by side at the header's own scale; this is not the reserved full logo and carries no tagline.
4. **Full logo (reserved):** mark + wordmark + tagline. Brand-introduction contexts only (press kits, slide title pages). Not used in-product or in body documents.
5. **Cover lockup (lead-magnet / document covers):** wordmark plus the orange mark on a document cover. The mark reads as an accent; spacing is set by the cover layout.
6. **Social preview card:** wordmark plus the orange mark and the social preview line, "On brand, at the speed of AI." Used for OG/social cards only. The mark reads as an accent, not a general-purpose logo lockup.

### Do not

- Add space between "agency" and "state" in the wordmark.
- Set the wordmark in all caps or title case.
- Change the weight relationship (both words the same weight).
- Add color, gradient, or effects to the logo.
- Rotate, skew, or distort the logo.
- Place the logo on busy backgrounds without sufficient contrast.
- Rearrange the elements (tagline above the wordmark, mark on the right of the wordmark, and so on).
- Round the square mark's corners.
- Use a different typeface, or live text, in place of the outlined wordmark.

---

## Typography: the faces

The full type implementation (the ramp, the exact font stacks with fallbacks, and the weight assigned to each face) lives in the design system and is generated from the stylesheet, so it is not restated here. This section carries only the part that is brand identity rather than implementation: **which faces the brand is set in, and what each one is for.** These are an identity fact on the same footing as the accent orange, and they hold whether the surface is a page, a deck, a PDF, or an email.

- **Three faces, three jobs.**
  - **Display: Schibsted Grotesk.** Headings, layer and domain names, the hero thesis.
  - **Body: Source Sans 3.** Running copy, leads, descriptions, captions.
  - **Mono: IBM Plex Mono.** Labels, nav, kickers, chips, and every specimen block.
  - All three are Google Fonts, Open Font License.
- **Hierarchy comes from face, weight, color, and space, not from size inflation.** Only the hero is allowed to be big. Separating the three jobs is what makes that restraint possible. Never use weight alone to make a hierarchy step that face, color, or space should be making.
- **Mono is not decoration.** It marks machine artifacts, and it is what makes a specimen read as evidence rather than as a quotation. Do not set narrative prose in mono, and do not set a specimen in the body face.
- The three faces retire Inter, the legacy primary named in v3.2. The wordmark is unaffected: it is outlined SVG, so its weight relationship is locked in the paths and does not depend on any loaded font.

The type ramp, the font stacks, and the weight-per-face assignments are implementation. They live in `design-system.css` and its generated Reference in `design-system.md`. Use the tokens there; do not restate or re-pick those values.

---

## Color: accent grammar

The full palette (every token and its hex) lives in the design system and is not restated here. This section carries only the part that is brand grammar rather than implementation: **how the accent is allowed to behave.**

- **Accent orange** is `--accent` `#D4602A`, hover `--accent-hover` `#B8521F`. (These two are the brand's fixed accent; the rest of the palette is in the design system.)
- The identity lives in **typography and weight contrast, not color.** The accent is a supporting layer, used sparingly: action (CTAs, inline links) and state (a live or active indicator) only. Never for body copy, plain headings, or large surfaces.
- **The payload rule.** Accent orange may mark the single conceptual payload: the one word or phrase in a headline that carries the idea (set as `<em>` inside the headline), or a complete standalone pull quote. The reader learns the grammar: orange means "this is the point." One payload word, not scattered emphasis.
- The logo is monochromatic. It works in any single dark color on a light ground, or light on dark. No gradients, no shadows, no glow on the logo.

---

## Motion principles

The motion **spec** (easing, durations, the load reveal) lives in the design system and is generated from the stylesheet. What belongs here is the principle, which does not change with the implementation:

- Any motion is short and eased, and it never loops.
- **Never use:** loops, pulses, bounces, or any continuous motion; shadows that appear on an elevation change; parallax; or timings so fast or so slow that the motion calls attention to itself rather than easing the eye.
- `prefers-reduced-motion` is always respected.

---

## Voice, tone, and copy

See `brand-platform.md` (served live through the brand MCP, `get_brand_voice` / `get_full_platform`). It is the single source of truth for voice, positioning, brand-name spelling, and what to say and not say. This document covers the visual brand layer only.

---

## Where the visual implementation lives

Everything this document used to specify about the built surface (the type ramp and font stacks, the weight-per-face assignments, the full color palette, the spacing scale, container and layout, the nav and footer, components, the motion spec, breakpoints, and page types) now lives in the **design system**, where it is generated from the stylesheet and enforced against it:

- **`design-system.css`** is the single shared stylesheet every page links. It is the source of the token values.
- **`design-system.md`** carries the color roles, the patterns, the systemic-versus-page-specific calls, and the open decisions, plus a generated Reference block emitted from the CSS by `audit.py --emit-reference` and checked by `audit.py --check-reference` (both fail if the doc and the CSS disagree).

The design system is the canonical source for every value above. An agent asking for the type ramp, a palette hex, or a spacing value reads it there, never a hand-kept paraphrase and never this document.
