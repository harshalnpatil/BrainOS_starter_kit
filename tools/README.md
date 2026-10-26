# Tools

Small, dependency-free helpers that make the BrainOS conventions deterministic. Scaffolding scripts create task folders and diary skeletons in one step; the validator checks that the structure still matches the conventions after agents have edited it — so structure never depends on agent memory.

## The tools

| Tool | What it does | When to run |
| --- | --- | --- |
| `new_task.py` / `new_task.ps1` / `new_task.sh` | Creates a `yyyy_mm_dd_slug/` task folder with a `diary.md` skeleton. Three flavors, identical behavior. | When a non-trivial task starts (step 1 of the daily task loop). |
| `validate_brain.py` | Drift guard: checks the root router, task-folder naming, diaries, and relative links; prints a PASS/WARN/FAIL report. | After agent edits that change structure; optionally as a hook or in CI. |

All tools are zero-dependency: `new_task.py` and `validate_brain.py` use only the Python 3 standard library; the PowerShell and Bash flavors use only their shell.

## Usage

Three scaffold flavors — pick whichever your platform prefers. Windows (PowerShell 7):

```powershell
py tools\new_task.py laptop_upgrade_check --domain career
.\tools\new_task.ps1 laptop_upgrade_check -Domain career
```

macOS/Linux:

```bash
python tools/new_task.py laptop_upgrade_check --domain career
./tools/new_task.sh laptop_upgrade_check --domain career
```

Common options for all flavors: `--date YYYY-MM-DD` (default: today) and `--root <path>` (default: current directory). Slugs are normalized (lowercase, spaces/hyphens become underscores); invalid slugs are rejected with a clear error. Existing task folders are never overwritten.

The validator:

```bash
python tools/validate_brain.py .   # run from your brain root
```

## Wiring the validator

Three escalating options — (a) alone is already useful; (b) and (c) are optional.

**a) Run manually after agent edits.** The cheapest habit: after an agent finishes structural work, run `python tools/validate_brain.py .` and fix any FAILs before closing the task.

**b) Claude Code PostToolUse hook** (Claude-specific; other agents simply ignore it). In your brain folder's `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "python tools/validate_brain.py . || true" }
        ]
      }
    ]
  }
}
```

**c) CI check on push** (if your brain lives in git). `.github/workflows/validate.yml`:

```yaml
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python tools/validate_brain.py .
```

## Growing it

All optional; the brain works without any of them:

- **CLI wrapper for task-board integration** — when you keep a task board (e.g. a hosted card board or GitHub Projects) and want `new_task` to also create a card.
- **MCP tool health checks** — when you connect MCP servers and want the validator to also confirm their config files exist and parse.
- **Per-domain validators** — when a domain accumulates its own conventions (e.g. a specific notes layout) worth checking beyond the root-level rules.

Add each only when the need is real. Never grow for growth's sake.
