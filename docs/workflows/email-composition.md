# Email composition checks

Follow the workspace owner's recipient and sending policy, plus the connected service's instructions.

## Before composing

- Confirm the sending account, To, Cc, and Bcc recipients, subject, and intended thread. Keep Bcc private.
- For a reply, inspect the message headers and recent thread. Include participants needed for the requested reply and keep Bcc private.
- Do not infer permission to send from a request to draft or compose. Apply the owner's sending policy before sending.

## Format and review

- Use structured paragraphs and lists in HTML when supported. Use actual paragraph and list elements, not Markdown markers or newline characters inside HTML.
- For plain text, preserve line breaks and blank lines. When constructing raw MIME, use UTF-8 and normalized CRLF line endings.
- Read back the saved recipients, sender, subject, body, attachments, and thread association where available. Check that paragraphs and lists render as intended.
- For layout-sensitive messages, inspect the saved draft in the target interface when practical. A sender-side preview does not prove how another mail client will render it.
- Do not send a test message solely to check formatting. After an authorized send, read back the sent item and check recipients, body, and attachments.
