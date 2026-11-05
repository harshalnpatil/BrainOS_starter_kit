# Draft tracking (opt-in)

Use this workflow only after the workspace owner chooses to track drafts. The included [draft ledger](draft-ledger.md) starts empty. Tracking does not authorize account access, message changes, or sending.

1. Store the exact text authored by the user or agent as a snapshot. Keep each distinct authored version separate; never overwrite an earlier version.
2. Add a ledger row with the creation date, destination, stable location, status, and snapshot path. Record only the account or context needed to find the draft.
3. Exclude credentials and secrets. Track sensitive drafts only when the owner explicitly chooses to include them.
4. Before comparing versions, verify the draft identity and author. Keep another person's reply separate from the owner's edits.
5. Record only observed changes. Mark missing, inaccessible, or ambiguous items instead of inferring delivery or authorship from timestamps or similar text.

This is a manual record. It does not provide background monitoring or complete coverage across tools. A later comparison requires access to the recorded location and an explicit task to inspect it.
