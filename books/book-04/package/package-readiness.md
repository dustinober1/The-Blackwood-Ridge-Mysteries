# Book 4 Package Readiness Validation — The Archive Fire

2026-07-04 validation-only pass

This file documents package-readiness validation performed during export prep. It does **not** create a final package, final EPUB, cover file, retailer upload bundle, or publication event.

## Current package state

- Manuscript draft: complete.
- Revision/proof path: complete.
- Publication-readiness polish: complete.
- Export assembly tooling: prepared.
- Combined manuscript artifact: not yet committed as generated output.
- Package guidance: existing draft package guidance remains in `books/book-04/package/packaging.md`.
- Draft listing guidance: existing draft listing guidance remains in `books/book-04/publish/listing.md`.
- Package stage: pending.
- Publish stage: pending.

## Metadata snapshot

| Field | Value |
|---|---|
| Title | The Archive Fire |
| Author | Vesper Blythe |
| Series | The Blackwood Ridge Mysteries |
| Series number | Book 4 |
| Lead | Callie Thorne |
| Genre | Atmospheric cozy mystery / amateur sleuth |
| Current chapter-metadata word count | 36,026 |
| Export assembly tool | `books/book-04/export/assemble-manuscript.py` |
| Build script | `books/book-04/export/build.sh` |
| Expected combined manuscript | `books/book-04/export/manuscript-combined.md` |
| Expected EPUB output | `books/book-04/export/the-archive-fire.epub` |
| Package status | Pending |
| Publish status | Pending |

## Package-readiness audit

- Ruth's call still sets up the shelf that lied twice.
- Fake Ruth note remains staged and wrong because it lacks Ruth's record system.
- Brass cat charm setup, recovery, and payoff remain intact.
- Clara's K-two lie remains separate from Ruth's key-ring/charm path.
- Simon, Clara, Nell, and Tavis remain false-suspect / record-failure paths.
- Tavis remains morally responsible for the old 1991 failure, not Ruth's murderer.
- Lila Crowe remains a public hit-and-run death with a smoothed record, not a disappearance.
- Ben Calder remains exposed through accumulation, not confession.
- Cross's arrest basis remains accumulated present-day evidence.
- Callie remains a consulting records specialist, not a deputy.
- Eli remains useful but bounded.
- Mae's thaw remains work-based, not apology-based.
- Bell's photographs and Cross's log still make Callie's reading portable.
- Supplemental Crowe record remains restrained.
- Consultant arrangement remains case-by-case and bounded.
- Floorboard ending remains unchanged in meaning.
- Eleanor's brass magnifying glass remains beside damaged paper as a tool, not a relic.

## Package blockers before package can be complete

- Generate and commit or verify `books/book-04/export/manuscript-combined.md` from the assembly script.
- Build or otherwise verify the EPUB output from `books/book-04/export/build.sh` when the final retail file is needed.
- Finalize reader-facing package assets, including final cover/image guidance output and final listing copy.
- Confirm no package file implies upload or live publication.
- Keep `publish: pending` until an actual publication/upload pass is intentionally performed.

## Result

Book 4 is ready for the final export artifact generation step and then package finalization. Package is **not** complete. Publish is **pending**.
