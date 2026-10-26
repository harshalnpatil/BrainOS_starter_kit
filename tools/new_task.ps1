# Creates a date-named task folder with a diary.md skeleton inside a BrainOS root.
# Equivalent flavors: new_task.py (Python) and new_task.sh (Bash) — same behavior.
# Pure PowerShell; no external dependencies. Requires PowerShell 7 (pwsh).

param(
    [Parameter(Mandatory = $true, Position = 0)][string]$Slug,
    [string]$Domain,
    [string]$Date,
    [string]$Root = "."
)

$ErrorActionPreference = "Stop"

# Normalize slug: lowercase, spaces/hyphens to underscores, strip trailing slashes.
$clean = $Slug.Trim().TrimEnd("/", "\").ToLower() -replace "[ -]", "_"
if ($clean -notmatch "^[a-z0-9_]+$") {
    Write-Error "error: slug '$Slug' is invalid after normalization ('$clean'): must contain only lowercase letters, digits, and underscores"
    exit 1
}

if ($Date) {
    try {
        $taskDate = [datetime]::ParseExact($Date, "yyyy-MM-dd", $null)
    } catch {
        Write-Error "error: invalid date '$Date', expected YYYY-MM-DD"
        exit 1
    }
} else {
    $taskDate = Get-Date
}

$dateCompact = $taskDate.ToString("yyyy_MM_dd")
$dateIso = $taskDate.ToString("yyyy-MM-dd")

$base = if ($Domain) { Join-Path $Root $Domain } else { $Root }
$taskDir = Join-Path $base "${dateCompact}_${clean}"
$diary = Join-Path $taskDir "diary.md"

if (Test-Path $taskDir) {
    Write-Error "error: task folder already exists: $taskDir; existing diary: $diary; not overwriting; reuse the existing task folder for follow-ups."
    exit 1
}

New-Item -ItemType Directory -Path $taskDir -Force | Out-Null

$title = ($clean -split "_") | ForEach-Object {
    if ($_.Length -gt 0) { $_.Substring(0, 1).ToUpper() + $_.Substring(1) } else { $_ }
}
$title = $title -join " "

$diaryContent = @"
# $dateIso`: $title

Status: In progress

## Context

<!-- Why this task exists; link related files by path. -->

## Log

<!-- What you tried, what failed, decisions made. Summarize; no raw transcripts. -->

## Resolution

<!-- Root cause / actual fix / verification / follow-ups. Then set Status: Resolved with a timestamp. -->
"@

Set-Content -Path $diary -Value $diaryContent -Encoding utf8 -NoNewline

Write-Host "created: $taskDir"
Write-Host "created: $diary"
Write-Host "If this is a structural/user-visible change, add a dated line to docs/changelog.md."
exit 0
