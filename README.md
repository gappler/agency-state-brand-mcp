---
title: Agency State brand MCP server
version: 0.1.0
last_updated: 2026-05-28
status: working draft
---

# agency-state-brand-mcp

MCP server that serves the canonical Agency State brand platform (and visual guidelines) to downstream clients — n8n workflows, Claude Code sessions, any MCP client — so they can pull on-brand context on demand.

Source of truth is the [`agency-state-brand`](https://github.com/gappler/agency-state-brand) repo. This server is an *actor*, kept separate from that canonical repo.

## Tools

Each platform tool returns one section of `brand-platform.md`, sized to be served whole without bloating the context window.

| Tool | Returns |
|---|---|
| `get_identity` | §1 Identity |
| `get_competencies` | §2 What Agency State delivers (the six AI Enablement competencies) |
| `get_positioning` | §3 Positioning |
| `get_audience` | §4 Audience + fit criteria |
| `get_brand_voice` | §5 Voice (voice rule, POV, principles with ✓/✗ pairs) |
| `get_vocabulary` | §6 Vocabulary (use/avoid + terms with fixed meaning) |
| `get_never_say` | §7 Never say (banned phrasings) |
| `get_proof` | §8 Proof (the founder/AIA paragraph) |
| `get_boundaries` | §9 What Agency State is not |
| `get_full_platform` | §§1–9 whole, excluding the human-only Decisions & rationale section |
| `get_visual_identity` | the full `brand-guidelines.md` |

## Content source: live-read + bundled fallback

The server live-reads the latest docs from the `agency-state-brand` repo's raw URL (`BRAND_RAW_BASE`), with a short in-memory cache (`CACHE_TTL`, default 60s). If a fetch fails, it falls back to the bundled snapshot in `content/`.

- **Editing the brand:** edit + push `brand-platform.md` / `brand-guidelines.md` in `agency-state-brand`. This server serves the new content within the cache window — **no redeploy needed.**
- **The bundled `content/` snapshot** is only a failure fallback. Refresh it occasionally (`cp ../agency-state-brand/*.md content/`) so the fallback isn't badly stale, but it isn't load-bearing day to day.
- The brand repo is currently **public**, so no token is needed. If it's ever made private, set a read-only `GITHUB_TOKEN` env var (fine-grained PAT, Contents: read, scoped to that repo) and live-read keeps working.

## Config (env vars)

| Var | Default | Purpose |
|---|---|---|
| `BRAND_RAW_BASE` | `https://raw.githubusercontent.com/gappler/agency-state-brand/main` | raw base URL for live-read |
| `GITHUB_TOKEN` | (unset) | only needed if the brand repo is private |
| `CACHE_TTL` | `60` | seconds to cache fetched docs |
| `HOST` / `PORT` | `0.0.0.0` / `8000` | bind address (Railway sets `PORT`) |

## Transport

Streamable HTTP, mount path `/mcp` (FastMCP default).

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

Confirm it responds:

```bash
curl -s -X POST http://localhost:8000/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl","version":"0"}}}'
```

## Deploy (Railway)

Connect this repo to a Railway project. NIXPACKS build, start command `python server.py` (see `railway.json` / `Procfile`). No env vars required while the brand repo is public. Railway provides the public `/mcp` URL to register with Claude Code (`~/.claude.json`) and the n8n MCP node.

## Later (not now)

When the website / page-building workflow starts, `brand-guidelines.md` may want slicing into structured design-token tools (`get_colors`, `get_type_scale`, `get_spacing`, `get_components`) the way the platform is sliced by section. Build that when the page workflow shows the need — not speculatively. For v1, `get_visual_identity` serves the whole guidelines file.
