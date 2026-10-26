<#
pdf2md.ps1 - convert a PDF (or any anydoc-supported document) to Markdown.

Pipeline: anydoc direct -> pikepdf decrypt + retry for encrypted PDFs ->
guidance for scanned PDFs (OCR stays local; hosted OCR is not used by
default).

Examples:
  .\pdf2md.ps1 -Pdf "doc.pdf"                        # writes doc.md next to the PDF
  .\pdf2md.ps1 -Pdf "doc.pdf" -Out "out.md"          # explicit output path
  .\pdf2md.ps1 -Pdf "doc.pdf" -Password "<document-password>"   # password-protected PDF
  .\pdf2md.ps1 -Pdf "doc.pdf" -DecryptOnly           # writes doc_unencrypted.pdf only
  .\pdf2md.ps1 -Pdf "doc.pdf" -KeepIntermediates     # keeps the _unencrypted.pdf copy
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Pdf,
    [string]$Out = "",
    [string]$Password = "",
    [switch]$DecryptOnly,
    [switch]$KeepIntermediates
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Pdf)) { throw "Input not found: $Pdf" }
$Pdf = (Resolve-Path -LiteralPath $Pdf).Path
if ([string]::IsNullOrWhiteSpace($Out)) { $Out = [IO.Path]::ChangeExtension($Pdf, '.md') }

$skillDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$decryptPy = Join-Path $skillDir 'decrypt_pdf.py'

function Invoke-Anydoc {
    param([string]$Target, [string]$Dest)
    $anydocArgs = @($Target, '-o', $Dest)
    $output = & anydoc @anydocArgs 2>&1
    [pscustomobject]@{ Code = $LASTEXITCODE; Message = ($output -join "`n") }
}

$outDir = Split-Path -Parent $Out
if ($outDir -and -not (Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

$target = $Pdf
$intermediate = $null

# Step 1: direct conversion (local, private).
$r = Invoke-Anydoc -Target $target -Dest $Out
if ($r.Code -eq 0) {
    Write-Output "converted (direct): $Out"
    return
}

# Step 2: encrypted PDF -> decrypt with pikepdf, then retry.
if ($r.Message -match 'encrypted') {
    $base = [IO.Path]::GetFileNameWithoutExtension($target)
    $dir = [IO.Path]::GetDirectoryName($target)
    $intermediate = Join-Path $dir ($base + '_unencrypted.pdf')
    if ($Password) { & python $decryptPy $target $intermediate $Password } else { & python $decryptPy $target $intermediate }
    if ($LASTEXITCODE -eq 2) { throw "PDF needs a real password to open: $target (pass -Password with the document's password)" }
    if ($LASTEXITCODE -ne 0) { throw "pikepdf decrypt failed for: $target" }
    if ($DecryptOnly) {
        Write-Output "decrypted only: $intermediate"
        return
    }
    $target = $intermediate
    $r = Invoke-Anydoc -Target $target -Dest $Out
    if ($r.Code -eq 0) {
        if (-not $KeepIntermediates) { Remove-Item -LiteralPath $intermediate -Force }
        Write-Output "converted (decrypt then anydoc): $Out"
        return
    }
}

# Step 3: scanned pages need OCR. Keep it local by default.
if ($r.Code -eq 3 -or $r.Message -match 'ocr') {
    $msg = "scanned pages need OCR: $target. "
    if ($intermediate) { $msg += "Decrypted copy: $intermediate. " }
    $msg += "Local options: Tesseract (e.g. C:\Program Files\Tesseract-OCR), or render pages with pdftoppm and transcribe with a vision model the user approves. Do not send document content to any external API without asking the user first; be extra careful with documents containing ID numbers, bank details, or other sensitive personal data."
    throw $msg
}

throw "anydoc failed: $($r.Message)"
