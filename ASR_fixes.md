# Speech-recognition corrections

Use this dictionary when interpreting dictated or transcribed requests. Match each correction to its context. Explicit wording and verified source evidence take precedence.

## Terms

| Heard or transcribed | Intended term | Apply when |
| --- | --- | --- |
| `<variant>` | `<confirmed term>` | `<context that distinguishes it from other meanings>` |

## Paths

| Dictated path | Verified path or alias | Apply when |
| --- | --- | --- |
| `<dictated path>` | `<verified path>` | `<specific project or context>` |

## Application rules

- Apply context-supported corrections silently unless the distinction affects the task.
- Verify a mapped path before using it. If it is missing, search the configured workspace roots.
- Ask when multiple meanings remain plausible, especially for identities, amounts, accounts, or actions with external consequences.
- Add only user-confirmed corrections. Keep uncertain guesses out of the dictionary.
- Corrections do not rename files, alter quoted text, or authorize actions.

## Evidence

Record when and how the owner confirmed each correction, plus any source that verifies a path. Avoid private examples that are not needed to disambiguate future requests.
