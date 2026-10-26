---
title: Agency State Brand Guidelines
version: 5.1
status: Canonical
date: 2026-10-25
last_updated: 2026-10-25
source: Approved by Greg 2026-10-25. Derived from the redesigned homepage (agency-state/index.html) and the shared stylesheet every page links (agency-state/site.css), October 2026. Replaces v4.1 in full; earlier guidance on faces, sizes, color, and accent use no longer applies.
---

# Agency State Brand Guidelines

**URL:** agencystate.ai

The look is quiet, text-first, and personal: one reading column, a gray scale on white, three typefaces, and the orange mark as the only color. Hierarchy comes mainly from typeface and gray value; the size range is narrow (11 to 19px). The homepage is the reference for shared elements, and the article pages (for example brand-os.html) for article-only elements; site.css holds the exact values for both.

These are the brand-level rules. `site.css` in the agency-state repo holds the exact implementation values (spacing, widths, breakpoints, timings) and is the file to change when they change.

---

## Logo

### Wordmark

- `agencystate`, lowercase, one word with no space, from outlined SVG paths (`wordmark-black-on-white.svg`, and `wordmark-white-on-black.svg` for dark grounds).
- "agency" in bold and "state" in regular. The weight shift is the identity. It is locked in the outlined paths, so never retype the wordmark as live text.

### Mark

- A white star on a sharp square, the star rotated and leaving the square toward the right edge. No corner radius.
- **Orange mark** (`#D4602A` square, `agency-state-mark-orange.svg`): the site's mark. Used for the favicon, in the header next to the wordmark, on social preview cards, and on document covers.
- **Black mark** (`#111111` square, `agency-state-mark-black.svg`): for one-color contexts, such as print, embossing, or a place where orange would clash.

### Star watermark

The star alone (`agency-state-watermark.svg`, `#111111`, rotated) appears once per page as a fixed background element near the lower right, at very low opacity. It is texture, never a logo: no other use of the star without its square.

### Lockups

1. **Header:** orange mark immediately left of the wordmark, at the header's small scale.
2. **Social preview card:** orange mark and wordmark with the tagline, "On brand, at the speed of AI," plus the descriptor where a reader may not yet know Agency State (brand platform §1).
3. **Document cover:** orange mark and wordmark, with the same tagline and descriptor rule.

### Lines

The tagline and the descriptor are set in the brand platform (§1). On the homepage, the descriptor, "AI Enablement for brand marketing teams," sits under Greg's name. The tagline appears with the mark and wordmark on social cards and covers.

### Do not

- Add space between "agency" and "state," set the wordmark in capitals, or give both words the same weight.
- Recolor the mark beyond the orange and black versions, or add gradients or effects.
- Round the square, rotate or distort the mark, or put the mark to the right of the wordmark.

---

## Color

White ground, gray type, and no accent color in the page itself. Orange appears only in the mark.

| Token | Value | Use |
|---|---|---|
| white | `#ffffff` | Page background, card background |
| gray-50 | `#f9f9f9` | Spec panel background, card hover |
| gray-100 | `#f4f4f4` | Number badge on link cards |
| gray-200 | `#ededed` | Rules between rows, card and panel borders |
| gray-300 | `#dddddd` | Link underline, card border on hover |
| gray-400 | `#a0a0a0` | Meta line, nav, footer, small labels |
| gray-500 | `#707070` | Body text, descriptions |
| gray-600 | `#505050` | Spec panel text, numbers in badges |
| gray-700 | `#343434` | Link text on hover |
| gray-800 | `#2e2e2e` | Names, section labels, titles |
| orange | `#D4602A` | The mark only |

Links in body text keep the surrounding color with a thin gray-300 underline that turns gray-500 on hover (text to gray-700). Navigation, meta, card, stack, and article-footer links have no underline. No colored links, buttons, or highlighted words.

---

## Typography

Three faces, at regular weight unless noted.

| Face | Role | Main size |
|---|---|---|
| **Schibsted Grotesk** | Greg's name and article titles, section labels, in-text headings; nav and article-footer links; tool names | 19px for names, titles, and labels; 12 to 13px for links and tool names |
| **Libre Franklin** | Body text, the homepage descriptor, article subtitles, card and row titles and descriptions, the footer | 15px body; 14px in cards and rows (titles at medium weight) |
| **DM Mono** | The header meta line, article eyebrows, row numbers and card meta, spec panels, inline code | 11 to 13px |

- **Hierarchy comes mainly from face and gray.** Greg's name and section labels are the same size; nothing on a page is set large.
- **Sentence case** for names, labels, titles, and buttons. The one exception: short monospace labels (row numbers, card meta, the "More" label) may be set in all caps as a small-label style. The links in the header's meta line are set in lowercase ("copy email," "linkedin"). Never set Schibsted or Libre Franklin text in all caps.

## Layout

- One narrow reading column on a white page, with generous space between sections.
- Each section is a Schibsted label above its content.
- The header holds the lockup and a short nav, a thin rule, then a monospace meta line: Washington, DC time, "Washington, DC," "copy email," and LinkedIn.
- The footer is one or two small gray lines.

## Components

Each visual form has one job. Use the form that matches what the content is.

- **Link cards** (boxed, rounded, with a gray number badge; they lighten on hover): only for items that link to another page, such as articles in "More reading." A box signals that it opens something.
- **Rows** (lines separated by thin gray rules, no box, no hover unless the row is a link): for lists that explain rather than link, such as the five parts of Brand OS.
- **Spec panels** (a light gray rounded panel in DM Mono, line breaks kept as written): for structured summaries in a system's own format (labeled breakdowns, file trees, tool calls, check results) and for copy specimens being inspected. They follow the prose they summarize. Not for ordinary prose, quotes, or decoration.
- **Inline code:** tool and file names inside a sentence use DM Mono. Nothing on a page falls back to a system font.
- **Stack rows:** the tools Greg works with, as ruled rows with a small tool icon and the tool name. Tool icons are gray monochrome where the tool's brand allows it; where a brand forbids modifying its icon (VS Code), use the official icon unchanged.

## Motion

- Motion is small and functional: content may fade or slide in slightly as it scrolls into view, and links and cards change color on hover.
- No exaggerated bounce, loops, pulses, or parallax. A slight settle at the end of a slide-in is fine (the stack rows on the homepage).
- Respect reduced motion: with `prefers-reduced-motion`, content appears without animation and nothing stays hidden.

## Assets

- Marks: agency-state-mark-orange.svg, agency-state-mark-black.svg, agency-state-watermark.svg.
- Wordmarks: wordmark-black-on-white.svg and wordmark-white-on-black.svg (both on transparent grounds; the black wordmark is #000000).
- Social preview images: og-image.png follows the social card lockup. og-claude-code-for-marketing.png and og-codifying-your-brand-for-ai.png predate it and use orange type; replace them when those pages are next revised.

## Voice, tone, and copy

Governed by the brand platform §5 and §7, served through the brand MCP.
