# Diaries

This folder is the **optional** home for standalone, dated diaries — either flat files or the legacy `YYYY/MM/YYYY-MM-DD--slug.md` layout.

The **preferred modern pattern** is a `diary.md` inside each task folder (`yyyy_mm_dd_slug/diary.md`): the diary travels with the task's files and links naturally by relative path. Keep task-local diaries when possible; use this folder only for diary entries that don't belong to any single task folder.

See the workspace router ([`../../AGENTS.md`](../../AGENTS.md)) for the full diary operating rules.

## Diary format template

Copy-paste and edit:

```markdown
# YYYY-MM-DD: <One-line Title>

Status: In progress

## Context

Why this task exists; links to related files by path.

## Log

- Tried X — failed because Y.
- Tried Z — worked.

## Resolution

- Root cause: ...
- Actual fix: ...
- Verification: ...
- Follow-ups: ...

Status: Resolved (YYYY-MM-DD HH:MM)
```

Rules: link related files by path; summarize rather than paste raw transcripts; mark `Status: Resolved` with a timestamp when done.
