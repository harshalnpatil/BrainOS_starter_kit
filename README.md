# BrainOS Starter Kit

[![License: MIT](https://img.shields.io/badge/License-MIT-3fb950)](LICENSE)
[![Domain pack: brainos-job-search](https://img.shields.io/badge/domain_pack-brainos--job--search-a371f7)](https://github.com/harshalnpatil/brainos-job-search)

A markdown-native personal workspace system that AI agents can navigate on their own. Your knowledge lives in plain markdown files; a root "router" file (`AGENTS.md`) tells any AI agent where to find each domain of your life; task folders carry diaries; a lessons ledger stores what you learn once so no agent repeats a mistake. No proprietary formats, no vendor lock-in — just folders and markdown.

## What's in here

- `start_here.md` — the onboarding walkthrough: go from zero to a working BrainOS in 30-60 minutes.
- `AGENTS.md` — the workspace router. It is both the router for this kit and the copy-paste template for your own.
- `agent_harness.md` and `ASR_fixes.md` — portable agent-work and speech-recognition guidance. Copy them with the root router because it routes to both files.
- `docs/changelog.md` — a simple dated changelog for structural changes to your workspace.
- `docs/diaries/` — optional home for standalone/dated diaries (the modern pattern keeps diaries inside task folders).
- `docs/workflows/` — optional patterns for draft tracking, email composition, and file triage. These are opt-in and include empty templates only.
- `tools/` — dependency-free helper scripts: `new_task` scaffold flavors (Python, PowerShell, Bash) that create task folders + diary skeletons deterministically, and `validate_brain.py`, a drift checker for the whole structure. See [`tools/README.md`](tools/README.md).
- `skills/` — reusable AI skills (each a folder with a `SKILL.md`): the pattern, a copy-paste `_template`, and two shipped examples (`mermaid`, `pdf-to-markdown`). See [`skills/README.md`](skills/README.md).

## Quick start

1. Read [`start_here.md`](start_here.md).
2. Copy the root router, its 2 policy files, domain folders, and core `docs/` files into your own brain folder. Add only the optional workflow files you want; see [`docs/workflows/README.md`](docs/workflows/README.md).
3. Point any AI agent at the folder and ask it to read `AGENTS.md` and report what it can see.

## Who this is for

Anyone who wants an AI-assisted second brain: knowledge workers, PMs, researchers, hobbyists — anyone with a life that spans multiple domains (work, home, health, learning) and an AI assistant that does the legwork.

## Domain packs

The kit covers the OS itself. Domain packs are prebuilt domains for specific areas — install one by pointing a route at the pack's `AGENTS.md` instead of building a domain from scratch. First pack: [brainos-job-search](https://github.com/harshalnpatil/brainos-job-search) — a PM job-search career domain (dated company folders, interview prep, referral drafts, application diaries).

## Tool-agnostic and OS-agnostic

Works with any AI coding assistant that reads AGENTS.md-style instruction files (Amp, Cursor, Codex, Droid, Claude Code, etc.), on any OS. Everything is plain markdown.

## License

MIT — see [LICENSE](LICENSE). Copy the kit, adapt it, ship your own brain.
