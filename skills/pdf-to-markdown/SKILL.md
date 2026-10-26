---
name: pdf-to-markdown
description: Convert PDFs and office documents to Markdown, including encrypted and scanned PDFs. Wraps the anydoc CLI with a pikepdf decrypt step. OCR stays local (Tesseract or a user-approved vision model). Local-first and usable by any coding agent from any shell.
---

# PDF to Markdown Converter

Convert documents to Markdown with one script. Handles the 3 common cases: clean text-based PDFs, password-protected PDFs (for example, a bank statement pack), and scanned PDFs (for example, an encrypted benefits PDF).

## Toolchain

| Tool | Version | Purpose |
| --- | --- | --- |
| anydoc (`npm install -g @firecrawl/anydoc`) | any recent version | Local conversion of text-based PDFs and 14 office formats |
| python + pikepdf | any recent version | Decrypting protected PDFs |
| Tesseract | any recent version | Local OCR (on Windows, typically `C:\Program Files\Tesseract-OCR`) |
| poppler (`pdftotext`, `pdftoppm`) | any recent version | Raw text extraction and page rendering for vision-model OCR |

Verify the toolchain:

```powershell
anydoc --version
python -c "import pikepdf; print(pikepdf.__version__)"
```

## The script

`pdf2md.ps1` in this folder:

```powershell
.\pdf2md.ps1 -Pdf "path\to\document.pdf"                       # writes document.md next to the PDF
.\pdf2md.ps1 -Pdf "document.pdf" -Out "C:\temp\document.md"   # explicit output path
.\pdf2md.ps1 -Pdf "document.pdf" -Password "<document-password>"  # password-protected PDF
.\pdf2md.ps1 -Pdf "document.pdf" -DecryptOnly                  # just produces document_unencrypted.pdf
.\pdf2md.ps1 -Pdf "document.pdf" -KeepIntermediates            # keeps the _unencrypted.pdf copy
```

Pipeline, in order:

1. Try anydoc directly. Local, private, fast.
2. If anydoc reports the document is encrypted, decrypt with pikepdf (`decrypt_pdf.py`) to `<name>_unencrypted.pdf` and retry anydoc on the unencrypted copy. Use `-Password` with the document's password for user-password PDFs.
3. If anydoc reports pages needing OCR, stop with guidance. The decrypted copy is kept so a local OCR pass can use it.

The script throws on missing input, a password-protected PDF without `-Password` (or a wrong one), or failed conversion.

## OCR policy (local-first)

- Prefer local OCR (Tesseract) or a vision model the user approves.
- Always ask the user before sending any document content to an external API.
- Be careful with documents containing ID numbers, bank details, or other sensitive personal data.
- Password handling: the password is passed as a plain argument. Use it only on this machine for the user's own documents.

## What each document type needs

| Document type | Handling |
| --- | --- |
| Text-based PDF | anydoc direct |
| Password-protected PDF | pikepdf decrypt with `-Password`, then anydoc |
| Scanned PDF | local Tesseract, or `pdftoppm` + vision model; never hosted OCR without asking first |
| Office documents (.doc, .docx, .pptx, .xlsx, .rtf, .csv, .odt, .epub) | anydoc direct |

## Output conventions

- Default output: same basename as the input, .md extension, same folder.
- Decrypted intermediates are named `<name>_unencrypted.pdf` and deleted automatically after a successful conversion (pass `-KeepIntermediates` to keep them).

## For agents with their own PDF reading

Some agents read PDFs directly (up to a few MB), which is fine for question answering on small documents. Use `pdf2md.ps1` when the task is to produce a reusable .md file, when the PDF is encrypted, when the document exceeds the agent's reader limit, or when the agent has no PDF-capable reader.

## Maintenance

- Update anydoc: `npm update -g @firecrawl/anydoc`
- Update pikepdf: `python -m pip install -U pikepdf`
- Upstream: https://github.com/firecrawl/anydoc
