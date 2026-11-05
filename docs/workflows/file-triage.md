# File triage

Keep the destination map and any access or deletion rules specific to the workspace owner.

## Plan

1. Inventory candidate files with their current paths, sizes, and dates. Read file contents only when needed and authorized.
2. Map each source to a destination before changing files. Proceed with clear moves already covered by the user's request. Ask only about unresolved destinations, naming rules, or choices that change the requested scope.
3. Check each destination for collisions. A matching name or size alone does not prove that 2 files are duplicates. Compare a cryptographic hash such as SHA-256 when identity matters.
4. Treat deletion as a separate action requiring explicit authorization. A duplicate check does not authorize deletion.

## Move and verify

1. Execute the mapping within the user's existing authorization. Use literal paths and avoid broad patterns that can select unintended files.
2. Record each completed move in a ledger with date, original path, destination, decision source, and verification result. Add before-and-after hashes when identity matters.
3. Verify the destination content and check the source path to confirm the move result.
4. If a sync service or another process can restore files, verify the final state again after an appropriate delay.

The ledger records changes; it does not authorize a move. Keep personal paths, destination rules, and service-specific behavior out of shared templates.
