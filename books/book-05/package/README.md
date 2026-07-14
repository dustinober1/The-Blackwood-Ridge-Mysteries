# Book 5 Package Layer

This directory contains the non-publishing package controls for *The Planted Page*.

- `packaging.md` defines the exact cover requirements and spoiler-safe branding guardrails.
- `package-readiness.md` records completed work and the current blocker.
- `author-decision-checklist.md` isolates author-controlled retailer and print choices.
- `validate-readiness.py` validates metadata, accepted export controls, and the canonical cover gate.
- `package-validation.md` is the generated current-state report.

The validator may report `ready_for_release_build` after a valid approved cover is present, but it does not change repository status or publish the book. The release builder under `../export/` performs the final EPUB/ZIP validation. A permanent `../release/` directory must not be created until that final build passes.
