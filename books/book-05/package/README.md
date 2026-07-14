# Book 5 Package Layer

This directory contains the non-publishing package controls for *The Planted Page*.

- `packaging.md` defines the exact cover requirements and spoiler-safe branding guardrails.
- `cover-approval.json` records explicit author approval and the SHA-256 of the exact approved cover; it remains pending until a final cover is supplied.
- `package-readiness.md` records completed work and the current blocker.
- `author-decision-checklist.md` isolates author-controlled retailer and print choices.
- `validate-readiness.py` validates metadata, accepted export controls, the canonical cover, and the matching approval record.
- `test_validate_readiness.py` protects the fail-closed cover and metadata gates.
- `package-validation.md` is the stable current-state report.

The validator may report `ready_for_release_build` only after a technically valid cover and matching explicit approval record are present. It does not change repository status or publish the book. The release builder under `../export/` performs the final EPUB/ZIP validation. A permanent `../release/` directory must not be created until that final build passes.
