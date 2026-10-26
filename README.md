# BrainOS Starter Kit

A markdown-native personal workspace system that AI agents can navigate on their own. Your knowledge lives in plain markdown files; a root "router" file (`AGENTS.md`) tells any AI agent where to find each domain of your life; task folders carry diaries; a lessons ledger stores what you learn once so no agent repeats a mistake. No proprietary formats, no vendor lock-in — just folders and markdown.

## What's in here

- `start_here.md` — the onboarding walkthrough: go from zero to a working BrainOS in 30-60 minutes.
- `AGENTS.md` — the workspace router. It is both the router for this kit and the copy-paste template for your own.
- `docs/changelog.md` — a simple dated changelog for structural changes to your workspace.
- `docs/diaries/` — optional home for standalone/dated diaries (the modern pattern keeps diaries inside task folders).
- `tools/` — dependency-free helper scripts: `new_task` scaffold flavors (Python, PowerShell, Bash) that create task folders + diary skeletons deterministically, and `validate_brain.py`, a drift checker for the whole structure. See [`tools/README.md`](tools/README.md).

## Quick start

1. Read [`start_here.md`](start_here.md).
2. Copy the structure (root router + domain folders + `docs/`) into your own brain folder.
3. Point any AI agent at the folder and ask it to read `AGENTS.md` and report what it can see.

## Who this is for

Anyone who wants an AI-assisted second brain: knowledge workers, PMs, researchers, hobbyists — anyone with a life that spans multiple domains (work, home, health, learning) and an AI assistant that does the legwork.

## Tool-agnostic and OS-agnostic

Works with any AI coding assistant that reads AGENTS.md-style instruction files (Amp, Cursor, Codex, Droid, Claude Code, etc.), on any OS. Everything is plain markdown.

## License

MIT — see [LICENSE](LICENSE). Copy the kit, adapt it, ship your own brain.
