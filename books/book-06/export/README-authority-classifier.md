# Book 6 Workflow Authority Classifier

`authorize-scope.py` distinguishes authorized Book 7 manuscript drafting from Book 6 export-authority work before the legacy Book 6 exporter runs.

Authorized Book 7 drafting must contain at least one numbered Book 7 chapter manuscript and may contain only the matching mission lock, Book 7 lifecycle records, root progress tracking, and `series-outline.md`. Any Book 5, Book 6, Book 8, Book 3 release-workflow, protected production/release, or unrecognized path fails closed.

When that narrow classification passes, the workflow records `BOOK6_AUTHORITY_MODE=authorized_book7_drafting` and points only the legacy current-diff comparison at `HEAD`. The exporter still performs all fixed Book 6 source, chapter-identity, export-identity, EPUBCheck, and reader-text validations. Book 6 changes never receive this override.
