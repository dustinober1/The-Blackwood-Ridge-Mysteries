#!/usr/bin/env python3
"""Remove stale downstream-lifecycle claims from Book 6 export artifacts.

The controlled-export workflow proves source and reader-output identity. Package,
cover, listing, upload, release, retailer, and publication state are governed by
separate repository controls and must not be inferred from this historical
export-stage generator.
"""
from __future__ import annotations

import json
from pathlib import Path

REPLACEMENTS = {
    "books/book-06/export/export-readiness.md": (
        (
            "**Controlled proofreading complete. Repository-standard export assembly complete and validated. Package, cover, listing, upload, and publication remain pending.**",
            "**Controlled proofreading and repository-standard export identity are complete and validated. Current package, cover, listing, upload, release, retailer, and publication state is outside this controlled-export record's authority.**",
        ),
        (
            "No cover, listing copy, retailer form, upload ZIP, advertising asset, release package, retailer submission, publication record, or release-status change is included. The next stage after merge is **Book 6 controlled package assembly/readiness**.",
            "No cover, listing copy, retailer form, upload ZIP, advertising asset, release package, retailer submission, publication record, or release-status change is created or modified by this controlled-export run. Current downstream lifecycle state and next-task authority are governed elsewhere in the repository.",
        ),
    ),
    "books/book-06/export/validation-report.md": (
        (
            "Package, cover, listing, upload, and publication remain pending.",
            "Current package, cover, listing, upload, release, retailer, and publication state is outside this controlled-export record's authority.",
        ),
    ),
    "books/book-06/export-report.md": (
        (
            "- Exact Book 5 status: package in progress; publication pending; approved canonical ebook cover remains the blocker; Book 5 is not upload ready.",
            "- Book 5 files changed: **none**; current Book 5 lifecycle state is outside this controlled-export record's authority.",
        ),
        (
            "- Book 7 Chapter 1 exists and is formally accepted at 3,100 manuscript-prose words; it is outside Book 6 export authority, and no Book 7 chapter manuscript changed in this validation scope.",
            "- Existing Book 7 chapter manuscripts are outside Book 6 export authority, and no Book 7 chapter manuscript changed in this validation scope.",
        ),
        (
            "- Exact Book 6 status: controlled revision, line edit, final prose polish, proofreading, and export assembly complete; package, cover, listing, upload, and publication pending; Book 6 is not upload ready.",
            "- This report validates Book 6 source and export identity only; current package, cover, listing, upload, release, retailer, and publication state is outside this controlled-export record's authority.",
        ),
        (
            "## Intentionally not created",
            "## Controlled-export exclusions",
        ),
        (
            "No blocker remains within controlled export assembly. Package, cover, listing, upload, and publication work remain deliberately deferred. After this export pull request is reviewed and merged, the recommended next stage is **Book 6 controlled package assembly/readiness**.",
            "No blocker remains within controlled export validation. This record does not prescribe or authorize a downstream package, release, retailer, or publication task.",
        ),
    ),
    "books/book-06/export/build.log": (
        (
            "Package: pending\nCover: pending\nListing: pending\nUpload: pending\nPublication: pending",
            "Downstream lifecycle status: not evaluated by controlled export",
        ),
    ),
}

NORMALIZED_MANIFEST = {
    "status": "export_identity_validated",
    "package_status": "not_evaluated",
    "cover_status": "not_evaluated",
    "listing_status": "not_evaluated",
    "upload_status": "not_evaluated",
    "publication_status": "not_evaluated",
    "upload_ready": None,
    "lifecycle_status_authority": "governing repository lifecycle records",
}


def replace_once_or_already(text: str, old: str, new: str, label: str) -> str:
    old_count = text.count(old)
    new_count = text.count(new)
    if old_count == 1 and new_count == 0:
        return text.replace(old, new)
    if old_count == 0 and new_count == 1:
        return text
    raise RuntimeError(
        f"Ambiguous or missing controlled-export record text in {label}: "
        f"old={old_count}, normalized={new_count}"
    )


def normalize_text(path: Path, replacements: tuple[tuple[str, str], ...]) -> None:
    if not path.is_file():
        raise RuntimeError(f"Missing controlled-export record: {path}")
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        text = replace_once_or_already(text, old, new, str(path))
    path.write_text(text.replace("\r\n", "\n").rstrip() + "\n", encoding="utf-8")


def normalize_manifest(path: Path) -> None:
    if not path.is_file():
        raise RuntimeError(f"Missing controlled-export manifest: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    expected_old = {
        "status": "export_validated_package_pending",
        "package_status": "pending",
        "cover_status": "pending",
        "listing_status": "pending",
        "upload_status": "pending",
        "publication_status": "pending",
        "upload_ready": False,
    }
    already = all(data.get(key) == value for key, value in NORMALIZED_MANIFEST.items())
    if not already:
        mismatches = {
            key: data.get(key)
            for key, value in expected_old.items()
            if data.get(key) != value
        }
        if mismatches:
            raise RuntimeError(f"Unexpected controlled-export manifest lifecycle fields: {mismatches}")
        data.update(NORMALIZED_MANIFEST)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sanitize(root: Path) -> None:
    for relative, replacements in REPLACEMENTS.items():
        normalize_text(root / relative, replacements)
    normalize_manifest(root / "books/book-06/export/dist/export-manifest.json")


def main() -> int:
    root = Path(__file__).resolve().parents[3]
    sanitize(root)
    print("Normalized Book 6 export records to export-only lifecycle authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
