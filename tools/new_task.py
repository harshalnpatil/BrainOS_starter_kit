#!/usr/bin/env python3
# Creates a date-named task folder with a diary.md skeleton inside a BrainOS root.
# Equivalent flavors: new_task.ps1 (PowerShell) and new_task.sh (Bash) — same behavior.
# Python 3 standard library only; no external dependencies.

import argparse
import datetime
import re
import sys
from pathlib import Path

DIARY_TEMPLATE = """\
# {date_iso}: {title}

Status: In progress

## Context

<!-- Why this task exists; link related files by path. -->

## Log

<!-- What you tried, what failed, decisions made. Summarize; no raw transcripts. -->

## Resolution

<!-- Root cause / actual fix / verification / follow-ups. Then set Status: Resolved with a timestamp. -->
"""


def normalize_slug(raw: str) -> str:
    slug = raw.strip().rstrip("/\\")
    slug = slug.lower().replace(" ", "_").replace("-", "_")
    if not slug:
        raise ValueError("slug is empty after normalization")
    if not re.fullmatch(r"[a-z0-9_]+", slug):
        raise ValueError(
            f"slug {raw!r} is invalid after normalization ({slug!r}): "
            "must contain only lowercase letters, digits, and underscores"
        )
    return slug


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a BrainOS task folder (yyyy_mm_dd_slug) with a diary.md skeleton."
    )
    parser.add_argument("slug", help="task slug, e.g. laptop_upgrade_check")
    parser.add_argument("--domain", default=None, help="domain folder to create the task under")
    parser.add_argument("--date", default=None, help="date as YYYY-MM-DD (default: today)")
    parser.add_argument("--root", default=".", help="brain root (default: current directory)")
    args = parser.parse_args()

    try:
        slug = normalize_slug(args.slug)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.date is None:
        task_date = datetime.date.today()
    else:
        try:
            task_date = datetime.date.fromisoformat(args.date)
        except ValueError:
            print(f"error: invalid date {args.date!r}, expected YYYY-MM-DD", file=sys.stderr)
            return 1

    date_compact = task_date.strftime("%Y_%m_%d")
    date_iso = task_date.isoformat()

    root = Path(args.root)
    base = root / args.domain if args.domain else root
    task_dir = base / f"{date_compact}_{slug}"
    diary = task_dir / "diary.md"

    if task_dir.exists():
        print(f"error: task folder already exists: {task_dir}", file=sys.stderr)
        print(f"existing diary: {diary}", file=sys.stderr)
        print("not overwriting; reuse the existing task folder for follow-ups.", file=sys.stderr)
        return 1

    task_dir.mkdir(parents=True, exist_ok=False)
    title = slug.replace("_", " ").title()
    diary.write_text(DIARY_TEMPLATE.format(date_iso=date_iso, title=title), encoding="utf-8")

    print(f"created: {task_dir}")
    print(f"created: {diary}")
    print("If this is a structural/user-visible change, add a dated line to docs/changelog.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
