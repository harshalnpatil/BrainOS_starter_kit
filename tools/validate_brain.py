#!/usr/bin/env python3
# Drift guard for a BrainOS root: checks router presence, task-folder naming, diaries,
# and relative markdown links, then prints a PASS/WARN/FAIL report.
# Equivalent flavors: none (canonical validator). Python 3 standard library only.

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "node_modules"}
DIARY_HEADING = re.compile(r"^# \d{4}-\d{2}-\d{2}: .+")
TASK_NAME = re.compile(r"^\d{4}_\d{2}_\d{2}_[a-z0-9_]+$")
DATE_PREFIX = re.compile(r"^\d{4}_\d{2}_\d{2}_")
MD_LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")

pass_count = 0
warn_count = 0
fail_count = 0


def report(status: str, msg: str) -> None:
    global pass_count, warn_count, fail_count
    print(f"[{status}] {msg}")
    if status == "PASS":
        pass_count += 1
    elif status == "WARN":
        warn_count += 1
    else:
        fail_count += 1


def skip_dir(path: Path) -> bool:
    return path.name in SKIP_DIRS or path.name.startswith(".")


def walk(root: Path):
    for p in sorted(root.rglob("*")):
        rel_parents = p.relative_to(root).parts[:-1]
        if any(part in SKIP_DIRS or part.startswith(".") for part in rel_parents):
            continue
        yield p


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_brain.py <brain-root>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"error: brain root not found: {root}", file=sys.stderr)
        return 2

    # 1. Root AGENTS.md
    if (root / "AGENTS.md").is_file():
        report("PASS", f"root AGENTS.md exists ({root / 'AGENTS.md'})")
    else:
        report("FAIL", f"root AGENTS.md missing (expected {root / 'AGENTS.md'})")

    # 2. Domain folders with AGENTS.md need name: frontmatter
    for child in sorted(root.iterdir()):
        if not child.is_dir() or skip_dir(child):
            continue
        agents = child / "AGENTS.md"
        if agents.is_file():
            text = agents.read_text(encoding="utf-8", errors="replace")
            if re.search(r"^name:", text, re.MULTILINE):
                report("PASS", f"{child.name}/AGENTS.md has 'name:' frontmatter")
            else:
                report("WARN", f"{child.name}/AGENTS.md missing 'name:' frontmatter")

    # 3. Date-like task folders (root or one domain level deep)
    task_dirs = sorted(root.iterdir()) + [
        d / sub for d in sorted(root.iterdir())
        if d.is_dir() and not skip_dir(d)
        for sub in sorted(d.iterdir()) if sub.is_dir()
    ]
    for task_dir in task_dirs:
        if not task_dir.is_dir() or task_dir == root:
            continue
        rel = task_dir.relative_to(root).parts
        if len(rel) > 2 or not DATE_PREFIX.match(task_dir.name):
            continue
        if TASK_NAME.match(task_dir.name):
            report("PASS", f"task folder name ok: {task_dir.name}")
        else:
            report("FAIL", f"malformed task folder name: {task_dir.relative_to(root)} (expected yyyy_mm_dd_slug, lowercase, underscores)")
            continue
        if (task_dir / "diary.md").is_file():
            report("PASS", f"diary.md present: {task_dir.name}")
        else:
            report("FAIL", f"missing diary.md in {task_dir.relative_to(root)}")

    # 4. Every diary.md starts with a date heading
    for diary in sorted(root.rglob("diary.md")):
        parts = diary.relative_to(root).parts
        if any(part in SKIP_DIRS or part.startswith(".") for part in parts):
            continue
        if "docs" in parts and "diaries" in parts:
            continue
        first = diary.read_text(encoding="utf-8", errors="replace").lstrip().splitlines()
        heading = first[0].strip() if first else ""
        if DIARY_HEADING.match(heading):
            report("PASS", f"diary heading ok: {diary.relative_to(root)}")
        else:
            report("WARN", f"{diary.relative_to(root)}: first line is not '# YYYY-MM-DD: <title>' (got {heading!r})")

    # 5. Relative markdown links resolve
    broken = []
    for md in walk(root):
        if md.suffix.lower() != ".md":
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            report("WARN", f"could not read {md.relative_to(root)}: {exc}")
            continue
        for match in MD_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue  # pure anchor link
            if not (md.parent / path_part).exists():
                broken.append((md.relative_to(root), target))
    if broken:
        details = ", ".join(f"{f} -> {t}" for f, t in broken)
        report("FAIL", f"{len(broken)} broken relative markdown link(s): {details}")
    else:
        report("PASS", "all relative markdown links resolve")

    # 6. Duplicate task slugs across dates (root or one domain level deep)
    by_slug = {}
    for task_dir in task_dirs:
        if TASK_NAME.match(task_dir.name):
            slug = task_dir.name[11:]
            by_slug.setdefault(slug, []).append(str(task_dir.relative_to(root)))
    dups = {slug: folders for slug, folders in by_slug.items() if len(folders) > 1}
    if dups:
        details = "; ".join(f"{slug}: {', '.join(sorted(folders))}" for slug, folders in sorted(dups.items()))
        report("WARN", f"duplicate task slug(s) on different dates (possible duplicate or follow-up — consider reusing the earlier folder): {details}")
    else:
        report("PASS", "no duplicate task slugs")

    print(f"\nSummary: {pass_count} pass, {warn_count} warn, {fail_count} fail")
    return 1 if fail_count else 0


if __name__ == "__main__":
    sys.exit(main())
