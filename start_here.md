# Start here: build your BrainOS in 30-60 minutes

This guide takes you from an empty folder to a working, agent-navigable personal workspace. No prior setup needed beyond a folder and an AI assistant that reads markdown.

## 1. What is a BrainOS?

The mental model:

- **Your knowledge lives in plain markdown.** No app, no database, no lock-in. Any editor, any OS, any AI agent can read it.
- **AI agents read router files to find context.** The root `AGENTS.md` is a *router*: it does not answer domain questions itself — it points the agent at the right domain folder, which has its own `AGENTS.md`.
- **You talk to agents; they navigate.** You say "prep my review notes" — the agent reads the router, sees the domain routes, opens the right folder's `AGENTS.md`, and works from there.

### The five pillars

1. **The router** — a root `AGENTS.md` with persona inference, a workspace layout, explicit priority routes, and fallback discovery.
2. **Domain folders** — one self-contained folder per life area (`career/`, `home/`, `health/`, ...), each with its own `AGENTS.md`.
3. **Task folders + diaries** — date-named working folders (`yyyy_mm_dd_slug/`) each containing a `diary.md` narrating non-trivial work.
4. **The lessons ledger** — `agent-memory/workspace-lessons.md` inside a domain folder, holding only distilled, reusable rules.
5. **The changelog** — `docs/changelog.md`: dated one-liners for every meaningful structural change.

## 2. The 30-minute setup

### Step 1: Create the folder and the router

Make a folder for your brain (anywhere: `Documents/brain`, a synced drive, whatever) and copy this kit's `AGENTS.md` into it as your root router. You will fill in the workspace layout and routes as your structure grows — the template comments tell you where.

### Step 2: Create 2-3 starter domain folders

Pick your real life areas. Generic examples: `career/`, `home/`, `hobbies/`. Each domain folder gets a minimal `AGENTS.md` like this (copy-paste and edit):

```markdown
---
name: <domain-name>
description: <one-line description of what this domain covers>
---

# <Domain Name>

## What lives here

- Notes, plans, and task folders for <domain-name>.
- Key sub-folders:
  - <subfolder-or-topic>/
- Standing conventions:
  - <anything an agent must know before acting here>
```

Rules of thumb:

- Domains should be **broad but self-contained** — an agent routed into `career/` should need nothing from `home/` to do career work.
- 2-3 domains to start. Add more only when a real area of your life demands its own folder.
- Keep each domain `AGENTS.md` short. It is a briefing, not a novel.

### Step 3: Create the docs

In the brain root:

```
docs/
├── changelog.md
└── diaries/
    └── README.md
```

Copy `docs/changelog.md` from this kit and seed it with an initial entry. The `diaries/` folder can start empty (with a README explaining its purpose) — see this kit's `docs/diaries/README.md`.

### Step 3b (optional but recommended): copy the tools

Copy this kit's `tools/` folder into your brain root too. It gives you the `new_task` scaffold scripts and the `validate_brain.py` drift checker — both dependency-free. See [`tools/README.md`](tools/README.md). Everything works without them, but they make the conventions automatic instead of remembered.

### Step 3c (optional): copy the skills

Copy this kit's `skills/` folder into your brain root too: the skill pattern, a copy-paste `_template`, and two example skills (`mermaid`, `pdf-to-markdown`) — see [`skills/README.md`](skills/README.md). Everything works without any of them.

### Step 4: Smoke test

Open the folder with your AI agent and ask:

> Read AGENTS.md and tell me what domains you can see.

A working BrainOS passes when the agent correctly names your domains, cites the routes, and does not hallucinate structure that isn't there. If it ignores the router, see Troubleshooting below.

## 3. How to work in it daily

The task loop:

1. **When non-trivial work starts**, create a date-named task folder at the brain root (or inside the relevant domain): `2026_05_24_laptop_upgrade_check/`. Prefer the scaffold script (`tools/new_task`) to do this — it creates the folder and the `diary.md` skeleton in one deterministic step (see [`tools/README.md`](tools/README.md)). Agents can still create folders manually when the script isn't available, but the script guarantees the naming and diary conventions.
2. **Update the diary as you go** — what you tried, what failed, decisions made, verification steps. Summarize; never paste raw transcripts.
3. **Log durable lessons** to the domain's `agent-memory/workspace-lessons.md` — only things that pass the promotion test (see Conventions).
4. **Add a changelog line** in `docs/changelog.md` when something meaningful changes: a new domain, a structural change, a convention change. Not every diary update.
5. **Reuse task folders** for follow-ups on the same work. Create a new top-level folder only for genuinely separate work.

Small one-shot edits ("fix this typo") skip the loop entirely. No diary, no folder.

## 4. Conventions

- **Task folder naming**: `yyyy_mm_dd_NAME` — lowercase, underscores, e.g. `2026_06_01_garden_planning/`.
- **One diary per task folder**: `diary.md` inside the folder. Don't split a task's narrative across files.
- **Promotion test for lessons**: promote a lesson from a diary to the ledger only if it (a) would prevent a future mistake, (b) is about shared tooling, shell, agent behavior, or workspace conventions, (c) reflects a recurring user preference, or (d) has happened more than once / would be costly to repeat. Otherwise it stays in the diary.
- **Diary format**:
  - Top line: `# YYYY-MM-DD: <One-line Title>`
  - Link related files by path.
  - After resolution: record root cause, actual fix, verification steps, follow-ups, then mark `Status: Resolved` with a timestamp.
- **Startup reading order for agents**: root router → domain `AGENTS.md` → lessons ledger → task folder diary.

## 5. Growing it

All of these are optional. Start minimal; add only when needed:

- **More domain folders** — when a new life area accumulates enough material to deserve its own router.
- **Domain packs** — prebuilt domains for specific areas, installed by adding a route to the pack's `AGENTS.md` instead of building a domain from scratch. Example: [brainos-job-search](https://github.com/harshalnpatil/brainos-job-search) for job-search prep.
- **`skills/`** — reusable AI skills, each in its own folder with a `SKILL.md`. The kit ships the pattern, a `_template`, and two example skills (`mermaid`, `pdf-to-markdown`) — see [`skills/README.md`](skills/README.md). Add your own by copying the template into `skills/<skill-name>/` and adding a route row in your root `AGENTS.md`.
- **`tools/`** — CLIs and helper scripts your agents can invoke. The kit ships the essentials: `new_task` scaffold flavors and `validate_brain.py`, the drift guard that catches convention drift (malformed task folders, missing diaries, broken links) before it spreads. See [`tools/README.md`](tools/README.md).
- **`MCP_AGENTS.md`** — usage notes and gotchas for connected tools (Gmail, calendar, task boards, etc.), placed in the domain that uses them.
- **A domain-local ledger** — a domain's own `agent-memory/workspace-lessons.md` for lessons that only apply there.

Never grow for growth's sake: each addition should earn its place by preventing confusion.

## 6. Troubleshooting / gotchas

- **Agents ignoring the router.** Restate it: tell the agent "read AGENTS.md first" at the start of a session, and keep the router's routes explicit and up to date. Vague folders with no `AGENTS.md` give the router nothing to route to.
- **Diaries bloating with raw transcripts.** Summarize the outcome and link paths to files/logs instead of pasting dumps. If a lesson is buried in a wall of text, distill it into the ledger.
- **Empty folders vanishing in git.** Git doesn't track empty directories — that's why this kit puts a README in `docs/diaries/`. Do the same for any empty folder you want to survive a clone.
- **Multi-drive / sync-folder layouts.** If your brain spans a second drive or a sync folder (oneDrive, Dropbox, etc.), list every root explicitly in the router's "Workspace layout" section. A file missing under one root means the agent should check the others.
