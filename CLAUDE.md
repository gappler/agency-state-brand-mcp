---
title: Claude Code guidance for agency-state-brand-mcp
description: Working instructions for the Agency State brand MCP server repo
last_updated: 2026-10-26
---

This repo is the **brand MCP server** — it serves the canonical Agency State brand (platform + guidelines) to clients (Claude Code, Codex, any MCP client). It is an *actor*: the **source of truth is `agency-state-brand`**, not this repo.

## Don't edit the brand here

To change brand content, edit and push `brand-platform.md` / `brand-guidelines.md` in **`agency-state-brand`**. The server **live-reads** the latest from that repo's raw URL (`BRAND_RAW_BASE`, ~60s cache) and serves it — no redeploy.

- `content/` is a **failure-fallback snapshot only**, not the source. Don't hand-edit it. Refresh occasionally so it isn't badly stale: `cp ../../10-active/agency-state-brand/*.md content/`.
- Editing brand content here instead of in `agency-state-brand` changes nothing clients see and creates a fork — almost always a mistake.

## What lives here

- `server.py` — the MCP server. Edit this for server *behavior* (tools, caching, fallback).
- `content/` — the bundled fallback snapshot (see above).
- `README.md` — architecture, env vars, deploy. Read before changing server behavior.
- Deploy: Railway (NIXPACKS, `python server.py`); see `railway.json` / `Procfile`.

## Conventions

- Lowercase-hyphen filenames. Preserve existing version metadata when a file has
  it; use focused commits so git remains the audit trail.
- Don't break the serving path — if you change `server.py`, verify the MCP still returns brand content before committing.
