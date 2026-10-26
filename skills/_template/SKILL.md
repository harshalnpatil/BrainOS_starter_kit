---
name: <skill-name>
description: <one-line what it does, used by routers>
---

# <Skill Name>

<!-- One short paragraph: what capability this skill gives an agent. -->

## When to invoke

- <!-- Concrete trigger: "the user asks to X", "a task requires Y". -->

## When NOT to invoke

- <!-- Out-of-scope cases and adjacent-but-different tasks to route elsewhere. -->

## Workflow

1. <!-- Step. -->
2. <!-- Step. -->
3. <!-- Step. -->

## Scope and authorization

<!-- State what a request does and does NOT authorize. Example: asking about
     a purchase never authorizes placing one; read-only discussion never
     authorizes writes. -->

- Authorizes: <!-- what an invocation may do -->
- Does NOT authorize: <!-- what it may never do without explicit user confirmation -->

## References

<!-- Optional: point to deeper docs, e.g. [flowchart.md](../mermaid/references/flowchart.md)
     or a local references/ folder next to this file. Delete if unused. -->
