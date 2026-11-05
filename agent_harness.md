# Agent harness policy

Use this file for technical investigation, debugging, implementation, and computer use such as browser or desktop control. Keep product-runtime settings separate from agent harness policy.

## Confirm the active harness

- Use an explicit user statement or session information that names the active harness. Do not guess from model names or task wording.
- Check which tools and capabilities are available before assigning work.
- If a required capability is unavailable, state the limitation. Do not silently substitute a different tool or role.

## Choose direct work or delegation

Decide before planning whether to work directly or delegate.

- Work directly when the task is understood and localized, such as a small edit, known read-only inspection, or mechanical change with clear validation.
- Delegate when a separate worker adds independent review, isolated investigation, or end-to-end implementation with clear ownership.
- Keep parallel work for explicitly authorized parallel tasks or genuinely independent workstreams.
- For computer use, assign one designated worker to control the shared browser or desktop. Do not let multiple agents or tools operate the same interface at once.

## Bound delegated work

Give each worker a concrete objective, only needed context, owned files or systems, explicit limits, and completion checks. Keep concurrent workers on disjoint files or isolated checkouts.

Delegation does not expand user authorization. Preserve existing approval gates. The coordinator reviews the result and remains responsible for the task.

This file governs agents in the active coding harness. Follow each application's or automation's own runtime policy separately.

## Shared workspace discipline

- Inspect the current state before editing. Preserve unrelated user changes and keep concurrent ownership disjoint.
- When reporting workspace findings, name the files actually inspected and distinguish evidence from assumptions.
- Write text files as UTF-8 and preserve their existing line-ending and formatting conventions where practical.
