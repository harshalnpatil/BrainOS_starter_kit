"""Decrypt a PDF by re-saving it without encryption.

Handles two cases:
- Owner-password restriction with an empty user password: opens with no
  password needed.
- User-password protected PDFs: pass the password as the third argument.
  Use the password that came with the document.

Exits with code 2 if the PDF requires a password and none (or a wrong one)
was provided.

Usage: python decrypt_pdf.py <input.pdf> <output.pdf> [password]
"""
import sys

import pikepdf


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print("usage: decrypt_pdf.py <input.pdf> <output.pdf> [password]", file=sys.stderr)
        return 1
    src, dst = sys.argv[1], sys.argv[2]
    password = sys.argv[3] if len(sys.argv) == 4 else ""
    try:
        with pikepdf.open(src, password=password) as pdf:
            pdf.save(dst)
    except pikepdf.PasswordError:
        print(f"needs a password to open: {src}", file=sys.stderr)
        return 2
    except Exception as exc:  # pikepdf.PdfError, OSError, and friends
        print(f"failed to decrypt {src}: {exc}", file=sys.stderr)
        return 3
    print(f"decrypted: {src} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
