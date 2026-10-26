---
name: workspace-router
description: Root router for a BrainOS workspace — routes requests to domain folders, never answers domain questions itself.
---

# Workspace Router (root level)

This root `AGENTS.md` is a ROUTER, not a domain specialist. Your job here is to determine which domain a request belongs to and route to that domain's `AGENTS.md`. Do not attempt domain work from the root: route first, then work inside the domain.

## Persona inference

Infer the likely primary user from, in order of reliability:

1. **Explicit prompt statements** ("I am <your-name>", "for my <domain> work").
2. **Explicit file/folder paths** the user references.
3. **Machine name / hostname**.
4. **OS username**.

Explicit signals win over environment heuristics. Stay neutral and route by domain when no strong signal exists. Never let persona inference override explicit domain routes.

## Workspace layout

<!-- TEMPLATE: List every root that holds part of this brain. Include second drives and sync folders. -->

Roots that may contain workspace files:

- `.` (this folder — the primary brain root)
- <!-- e.g. `D:/synced-brain/` — a second drive or sync folder -->

A file may live on any listed root. If an expected file is missing under one root, check the others before concluding it doesn't exist.

## Priority routes (explicit, high confidence)

When a request matches a topic below, go directly to the primary route:

| Topic / keywords | Primary route |
| --- | --- |
| career, job search, resume, interviews | `career/AGENTS.md` |
| home, household, maintenance, garden | `home/AGENTS.md` |
| health, fitness, sleep, training | `health/AGENTS.md` |
| learning, courses, reading, notes | `learning/AGENTS.md` |

<!-- TEMPLATE: These are EXAMPLES. Replace them with your real domains and routes. Explicit routes always beat discovery. -->

## One-level discovery (fallback)

If no priority route matches:

1. Scan exactly one level below this root for `*/AGENTS.md`.
2. Build candidate domains from: the folder name, the `name`/`description` frontmatter, and the top headings of each file.
3. Pick the best match. Explicit routes always beat discovery.

## Task tracking

- Non-trivial work gets a date-named task folder: `yyyy_mm_dd_NAME` (lowercase, underscores), e.g. `2026_05_24_laptop_upgrade_check/` or `2026_06_01_garden_planning/`.
- Each task folder contains a `diary.md`.
- Reuse an existing task folder for follow-ups on the same work; create a new top-level task folder only for genuinely separate work.
- Prefer the scaffold script `tools/new_task.py` (or `.ps1`/`.sh` variants) when present; it enforces naming and diary conventions deterministically.

## Validation

- After agent edits that change structure, run `python tools/validate_brain.py .` when available; fix FAILs before finishing.

## Hybrid agent memory

Two layers:

1. **Task diaries** — `diary.md` inside each task folder: task narrative, debugging trail, decisions, verification, handoff notes.
2. **Lessons ledger** — `agent-memory/workspace-lessons.md` inside the relevant domain folder (never at the brain root): only distilled, reusable rules.

**Promotion test** — promote a lesson from a diary to the ledger only if:

- it would prevent a future mistake, AND
- it is about shared tooling, shell/agent behavior, or workspace conventions, OR reflects a recurring user preference, OR has happened more than once / would be costly to repeat.

Never paste raw transcripts or large command dumps into the ledger. Summarize and link paths instead.

## Diary operating rules

- Create a diary only for **non-trivial** tasks: multi-file changes, >~15 minutes of work, architectural choices, debugging, or handoff risk. Skip tiny one-shot edits.
- One diary per task folder.
- No raw transcripts or command dumps — summarize and link paths.
- Format: top line `# YYYY-MM-DD: <One-line Title>`; link related files by path; after resolution record root cause, actual fix, verification, and follow-ups, then mark `Status: Resolved` with a timestamp.
- **Startup reading order**: root router → domain `AGENTS.md` → lessons ledger → task folder diary.

## Changelog discipline

When a change is user-visible or structural (new domain, convention change, new skill, structural reorg), add a dated entry to [`docs/changelog.md`](docs/changelog.md). Do not log routine diary updates.

## Fallback behavior

If no route matches, proceed with general best-effort behavior. When choosing among plausible matches, state your assumptions briefly before acting.

## Windows PowerShell note

On Windows PowerShell, use normal Windows drive paths (e.g. `C:\Users\...`), not WSL-style `/c/...` paths.
