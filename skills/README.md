# Skills

A **skill** is a self-contained folder that teaches an agent a repeatable capability: when to use it, what its workflow is, and where its deeper reference docs live. A skill is just a folder with a `SKILL.md` (frontmatter `name` + `description`, plus the body) and an optional `references/` folder.

Skills are the difference between explaining a workflow to your agent every session and routing to it once: write the skill, add a route, and every future session starts already briefed.

## How agents reach skills

The root `AGENTS.md` routes to skills the same way it routes to domains: a priority-route row pointing at the skill's `SKILL.md`, for example:

| Topic / keywords | Primary route |
| --- | --- |
| diagram, mermaid, flowchart | `skills/mermaid/SKILL.md` |

## Shipped examples

| Skill | Purpose |
| --- | --- |
| [`mermaid/`](mermaid/SKILL.md) | Generate Mermaid diagrams (23 types) with dark-fill styling rules; full syntax references in `references/`. |
| [`pdf-to-markdown/`](pdf-to-markdown/SKILL.md) | Convert PDFs and office documents to Markdown, including encrypted and scanned PDFs; local-first OCR. |

## Create your own

1. Copy `skills/_template/SKILL.md` into a new folder: `skills/<skill-name>/SKILL.md`.
2. Fill in the frontmatter (`name`, `description`) and the "When to invoke" and "Scope" sections.
3. Add a `references/` folder if the skill needs deeper docs.
4. Add a route row in your root `AGENTS.md`.

## Conventions

- **One skill per folder.** The folder name matches the skill `name`.
- **Frontmatter always has `name` and `description`** — routers use them for discovery.
- **State scope explicitly.** A skill must say what a request does and does NOT authorize (asking about a purchase is not authorization to place one).
- **Keep them shareable.** Keep personal credentials, account names, and private paths OUT of skills you might share — parameterize with placeholders like `<document-password>`.
- Skills are **optional**. The brain works without any; add one only when a workflow repeats.
