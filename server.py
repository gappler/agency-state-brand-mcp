"""Agency State brand MCP server.

Serves the canonical Agency State brand platform (and visual guidelines) to
downstream agents — n8n workflows, Claude Code sessions, any MCP client — so
they can pull on-brand context on demand.

Source of truth is the `agency-state-brand` repo. The server live-reads the
latest docs from the repo's raw URL (short in-memory cache) and falls back to
the bundled snapshot in ./content if the fetch fails. Editing + pushing the
brand docs updates what this server serves within the cache window — no
redeploy needed.
"""

from __future__ import annotations

import os
import time
import urllib.request
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# --- configuration -----------------------------------------------------------

RAW_BASE = os.environ.get(
    "BRAND_RAW_BASE",
    "https://raw.githubusercontent.com/gappler/agency-state-brand/main",
)
# Optional: only needed if the brand repo is made private again.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
CACHE_TTL = int(os.environ.get("CACHE_TTL", "60"))  # seconds

BUNDLE_DIR = Path(__file__).parent / "content"
PLATFORM_FILE = "brand-platform.md"
GUIDELINES_FILE = "brand-guidelines.md"

PORT = int(os.environ.get("PORT", "8000"))
HOST = os.environ.get("HOST", "0.0.0.0")

mcp = FastMCP("agency-state-brand", host=HOST, port=PORT)

# --- content loading (live-read with bundled fallback) -----------------------

_cache: dict[str, tuple[float, str]] = {}


def _fetch(name: str) -> str:
    url = f"{RAW_BASE}/{name}"
    req = urllib.request.Request(url)
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode("utf-8")


def _content(name: str) -> str:
    """Return doc text: live from the brand repo, cached briefly, bundled on failure."""
    now = time.time()
    cached = _cache.get(name)
    if cached and now - cached[0] < CACHE_TTL:
        return cached[1]
    try:
        text = _fetch(name)
    except Exception:
        text = (BUNDLE_DIR / name).read_text(encoding="utf-8")
    _cache[name] = (now, text)
    return text


# --- markdown section slicing ------------------------------------------------

def _strip_frontmatter(md: str) -> str:
    if md.startswith("---"):
        end = md.find("\n---", 3)
        if end != -1:
            return md[end + 4 :].lstrip("\n")
    return md


def _sections(md: str) -> dict[str, str]:
    """Map each H2 section title -> the section text (heading included)."""
    md = _strip_frontmatter(md)
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in md.splitlines():
        if line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = [line]
        elif current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def _platform_section(title: str) -> str:
    section = _sections(_content(PLATFORM_FILE)).get(title)
    if section is None:
        return f"(Section '{title}' not found in {PLATFORM_FILE}.)"
    return section


def _full_platform() -> str:
    """Whole platform minus the human-only Decisions & rationale section."""
    md = _strip_frontmatter(_content(PLATFORM_FILE))
    idx = md.find("\n## Decisions & rationale")
    if idx != -1:
        md = md[:idx]
    return md.strip()


# --- tools -------------------------------------------------------------------

@mcp.tool()
def get_identity() -> str:
    """What Agency State is, in one statement, and who runs it.

    Use to ground any output in what the practice fundamentally is before
    writing copy or describing the brand.
    """
    return _platform_section("1. Identity")


@mcp.tool()
def get_competencies() -> str:
    """The substance of what Agency State delivers: the six AI Enablement competencies.

    Use when describing what the practice does or what an engagement produces.
    """
    return _platform_section("2. What Agency State delivers")


@mcp.tool()
def get_positioning() -> str:
    """What makes Agency State distinct — the positioning claims.

    Use when differentiating the practice or writing positioning-level copy.
    """
    return _platform_section("3. Positioning")


@mcp.tool()
def get_audience() -> str:
    """Who Agency State is for: the buyer, defined by ownership/authority, plus fit criteria.

    Use to check audience fit or target copy to the right reader.
    """
    return _platform_section("4. Audience")


@mcp.tool()
def get_brand_voice() -> str:
    """The Agency State voice: the voice rule, point of view, and principles with sounds-like / not-like pairs.

    Read this before drafting any Agency State copy — it defines how the brand sounds.
    """
    return _platform_section("5. Voice")


@mcp.tool()
def get_vocabulary() -> str:
    """Words with fixed meaning, and use/avoid pairs.

    Use to keep terminology exact and avoid off-brand word choices while writing.
    """
    return _platform_section("6. Vocabulary")


@mcp.tool()
def get_never_say() -> str:
    """Banned phrasings — fear framing, overclaim, SaaS clichés, consultant-speak, and more.

    Check copy against this list before finalizing; these are hard exclusions.
    """
    return _platform_section("7. Never say")


@mcp.tool()
def get_proof() -> str:
    """Proof and credentials — the founder/AIA paragraph, ready to use as a whole asset.

    Use when copy needs to establish authority or credentials.
    """
    return _platform_section("8. Proof")


@mcp.tool()
def get_boundaries() -> str:
    """What Agency State is not — the sharp exclusion list.

    Use to avoid mis-describing the practice (e.g., as enterprise consulting or a course).
    """
    return _platform_section("9. What Agency State is not")


@mcp.tool()
def get_full_platform() -> str:
    """The entire brand platform (sections 1-9) in one response, excluding the human-only Decisions section.

    Use when a task needs broad brand context rather than one focused slice.
    """
    return _full_platform()


@mcp.tool()
def get_visual_identity() -> str:
    """The full Agency State brand guidelines: logo, typography, color, spacing, components, page types.

    Use when building or styling a page, component, or visual artifact that must match the brand.
    """
    return _content(GUIDELINES_FILE)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
