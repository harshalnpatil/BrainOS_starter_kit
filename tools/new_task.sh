#!/usr/bin/env bash
# Creates a date-named task folder with a diary.md skeleton inside a BrainOS root.
# Equivalent flavors: new_task.py (Python) and new_task.ps1 (PowerShell) — same behavior.
# Pure Bash, POSIX-safe constructs only; no external dependencies.

set -euo pipefail

usage() {
    echo "usage: ./new_task.sh <slug> [--domain <name>] [--date YYYY-MM-DD] [--root <path>]" >&2
    exit 1
}

SLUG=""
DOMAIN=""
DATE_ARG=""
ROOT="."

while [ $# -gt 0 ]; do
    case "$1" in
        --domain) DOMAIN="${2:?}"; shift 2 ;;
        --date)   DATE_ARG="${2:?}"; shift 2 ;;
        --root)   ROOT="${2:?}"; shift 2 ;;
        -h|--help) usage ;;
        *) SLUG="$1"; shift ;;
    esac
done

[ -n "$SLUG" ] || usage

# Normalize slug: lowercase, spaces/hyphens to underscores, strip trailing slashes.
clean="$(echo "$SLUG" | tr '[:upper:]' '[:lower:]' | tr ' -' '_' | sed 's#[/\\]*$##')"
if [ -z "$clean" ] || ! echo "$clean" | grep -Eq '^[a-z0-9_]+$'; then
    echo "error: slug '$SLUG' is invalid after normalization ('$clean'): must contain only lowercase letters, digits, and underscores" >&2
    exit 1
fi

if [ -n "$DATE_ARG" ]; then
    date_compact="$(date -d "$DATE_ARG" +%Y_%m_%d 2>/dev/null || date -j -f "%Y-%m-%d" "$DATE_ARG" +%Y_%m_%d 2>/dev/null)" || {
        echo "error: invalid date '$DATE_ARG', expected YYYY-MM-DD" >&2
        exit 1
    }
    date_iso="$(echo "$date_compact" | sed 's/_/-/g')"
else
    date_compact="$(date +%Y_%m_%d)"
    date_iso="$(date +%Y-%m-%d)"
fi

base="$ROOT"
[ -n "$DOMAIN" ] && base="$ROOT/$DOMAIN"
task_dir="$base/${date_compact}_${clean}"
diary="$task_dir/diary.md"

if [ -e "$task_dir" ]; then
    echo "error: task folder already exists: $task_dir" >&2
    echo "existing diary: $diary" >&2
    echo "not overwriting; reuse the existing task folder for follow-ups." >&2
    exit 1
fi

mkdir -p "$task_dir"

title="$(echo "$clean" | sed 's/_/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)}1')"

cat > "$diary" <<EOF
# $date_iso: $title

Status: In progress

## Context

<!-- Why this task exists; link related files by path. -->

## Log

<!-- What you tried, what failed, decisions made. Summarize; no raw transcripts. -->

## Resolution

<!-- Root cause / actual fix / verification / follow-ups. Then set Status: Resolved with a timestamp. -->
EOF

echo "created: $task_dir"
echo "created: $diary"
echo "If this is a structural/user-visible change, add a dated line to docs/changelog.md."
