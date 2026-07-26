#!/usr/bin/env python3
"""Validate Book 6 package readiness without manufacturing a release state.

The validator treats the accepted proof/export reports as immutable controls. It
reports a missing, invalid, or unapproved cover as a blocker and never marks the
book upload ready by itself.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from PIL import Image

BOOK_PATH = Path("books/book-06")
COVER_PATH = BOOK_PATH / "cover.jpeg"
APPROVAL_PATH = BOOK_PATH / "package/cover-approval.json"
ALLOWED_TAGS = {"p", "b", "em", "i", "u", "br", "h4", "h5", "h6", "ol", "ul", "li"}
EXPECTED_COVER_SIZE = (1600, 2560)
EXPECTED_CHAPTERS = [
    "Chapter 1 — The Box at Closing",
    "Chapter 2 — A Fall That Did Not Fit",
    "Chapter 3 — The Surveyor’s Missing Line",
    "Chapter 4 — Marks Made Later",
    "Chapter 5 — The Road Through Bellweather",
    "Chapter 6 — What the Ledger Withheld",
    "Chapter 7 — The Weight of the Map",
    "Chapter 8 — The Pattern",
]
EXPECTED_FINAL_LINE = "Who knew which page she would open next?"
EXPECTED_PROVENANCE = (
    "Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established."
)


class TagCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag.lower())

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag.lower())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(repo_root: Path) -> dict[str, Any]:
    root = Path(repo_root)
    book = root / BOOK_PATH
    checks: list[dict[str, Any]] = []
    blockers: list[str] = []

    def check(name: str, passed: bool, detail: str, blocker: str | None = None) -> None:
        checks.append({"name": name, "passed": passed, "detail": detail})
        if not passed and blocker:
            blockers.append(blocker)

    description_path = book / "listing/retailer-description.html"
    description = description_path.read_text(encoding="utf-8") if description_path.exists() else ""
    check(
        "Retailer description exists",
        bool(description),
        str(description_path.relative_to(root)) if description_path.exists() else "missing",
        "Missing retailer-description.html",
    )
    check(
        "Retailer description is within 4,000 characters",
        0 < len(description) <= 4000,
        f"{len(description)} characters including HTML",
        f"Retailer description is {len(description)} characters; KDP limit is 4,000",
    )
    collector = TagCollector()
    collector.feed(description)
    unsupported = sorted(set(collector.tags) - ALLOWED_TAGS)
    check(
        "Retailer description uses supported basic HTML",
        not unsupported,
        f"tags={sorted(set(collector.tags))}",
        f"Retailer description contains unsupported HTML tag(s): {', '.join(unsupported)}" if unsupported else None,
    )

    listing_path = book / "listing/listing-copy.md"
    listing = listing_path.read_text(encoding="utf-8") if listing_path.exists() else ""
    keywords = re.findall(r"(?m)^\s*[1-7]\.\s+`([^`]+)`\s*$", listing)
    check(
        "Exactly seven keyword phrases",
        len(keywords) == 7 and len(set(keywords)) == 7,
        f"found={len(keywords)} unique={len(set(keywords))}",
        f"Listing copy must contain exactly seven keyword phrases; found {len(keywords)}",
    )

    word_report_path = book / "export/word-count-report.md"
    word_report = word_report_path.read_text(encoding="utf-8") if word_report_path.exists() else ""
    counts_ok = "25,646" in word_report and "25,918" in word_report
    check(
        "Accepted word counts retained",
        counts_ok,
        "25,646 manuscript / 25,918 reader-facing" if counts_ok else "expected counts not found",
        "Accepted Book 6 word counts are missing or changed",
    )

    validation_path = book / "export/validation-report.md"
    validation = validation_path.read_text(encoding="utf-8") if validation_path.exists() else ""
    proof_ok = "293/293" in validation
    check(
        "Accepted proof/export validation retained",
        proof_ok,
        "293/293" if proof_ok else "expected proof total not found",
        "Accepted 293/293 proof/export validation record is missing",
    )

    combined_path = book / "export/manuscript-combined.md"
    combined = combined_path.read_text(encoding="utf-8") if combined_path.exists() else ""
    check(
        "Combined reader-facing manuscript exists",
        bool(combined),
        str(combined_path.relative_to(root)) if combined_path.exists() else "missing",
        "Combined reader-facing manuscript is missing",
    )
    chapter_headings = re.findall(r"(?m)^# (Chapter [1-8] — .+)$", combined)
    check(
        "Eight locked chapter headings remain in order",
        chapter_headings == EXPECTED_CHAPTERS,
        repr(chapter_headings),
        "Combined manuscript must contain the eight locked chapter headings in order",
    )
    final_count = combined.count(EXPECTED_FINAL_LINE)
    check(
        "Locked final line appears exactly once",
        final_count == 1,
        f"count={final_count}",
        f"Combined manuscript must retain the locked final line exactly once; found {final_count}",
    )
    provenance_count = combined.count(EXPECTED_PROVENANCE)
    check(
        "Exact provenance appears once",
        provenance_count == 1,
        f"count={provenance_count}",
        f"Combined manuscript must retain the exact provenance once; found {provenance_count}",
    )
    forbidden_patterns = [
        re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE),
        re.compile(r"<<<<<<|======|>>>>>>"),
        re.compile(r"eli-hidden-chronology|internal_series_spoilers|internal_continuity_control", re.IGNORECASE),
    ]
    source_marker = next((match for pattern in forbidden_patterns if (match := pattern.search(combined))), None)
    check(
        "Combined manuscript contains no internal markers",
        source_marker is None,
        "clean" if source_marker is None else repr(source_marker.group(0)),
        f"Combined manuscript contains internal marker: {source_marker.group(0)!r}" if source_marker else None,
    )

    epubcheck_ok = "0 fatals / 0 errors / 0 warnings / 0 infos" in validation
    check(
        "Accepted export EPUBCheck remains clean",
        epubcheck_ok,
        "0 fatals / 0 errors / 0 warnings / 0 infos" if epubcheck_ok else "clean result not found",
        "Accepted export EPUBCheck result is missing or not clean",
    )

    cover_path = root / COVER_PATH
    approval_path = root / APPROVAL_PATH
    cover_info: dict[str, Any] | None = None
    approval: dict[str, Any] | None = None
    technical_ok = False
    approval_ok = False
    cover_detail_parts: list[str] = []

    if cover_path.exists():
        try:
            with Image.open(cover_path) as image:
                image.load()
                cover_info = {
                    "path": COVER_PATH.as_posix(),
                    "format": image.format,
                    "mode": image.mode,
                    "width": image.width,
                    "height": image.height,
                    "size_bytes": cover_path.stat().st_size,
                    "sha256": sha256(cover_path),
                }
            technical_ok = (
                cover_info["format"] == "JPEG"
                and cover_info["mode"] == "RGB"
                and (cover_info["width"], cover_info["height"]) == EXPECTED_COVER_SIZE
                and cover_info["size_bytes"] < 50 * 1024 * 1024
            )
            cover_detail_parts.append(json.dumps(cover_info, sort_keys=True))
        except Exception as exc:
            cover_detail_parts.append(f"cover unreadable: {exc}")
    else:
        cover_detail_parts.append("cover missing")

    if approval_path.exists():
        try:
            approval = json.loads(approval_path.read_text(encoding="utf-8"))
            approval_ok = bool(
                technical_ok
                and approval.get("cover_path") == COVER_PATH.as_posix()
                and approval.get("status") == "approved"
                and approval.get("approved_by")
                and re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(approval.get("approved_on") or ""))
                and approval.get("sha256") == (cover_info or {}).get("sha256")
            )
            cover_detail_parts.append(f"approval={json.dumps(approval, sort_keys=True)}")
        except Exception as exc:
            cover_detail_parts.append(f"approval record unreadable: {exc}")
    else:
        cover_detail_parts.append("approval record missing")

    cover_ok = technical_ok and approval_ok
    check(
        "Approved ebook cover passes technical and approval gates",
        cover_ok,
        "; ".join(cover_detail_parts),
        (
            "Missing or unapproved ebook cover: supply books/book-06/cover.jpeg as JPEG/RGB/1600×2560/under 50 MB, "
            "then record explicit author approval and the matching SHA-256 in books/book-06/package/cover-approval.json"
        ),
    )

    passed = sum(1 for item in checks if item["passed"])
    return {
        "book": "The Pattern",
        "series": "The Blackwood Ridge Mysteries",
        "series_number": 6,
        "status": "ready_for_release_build" if not blockers else "blocked",
        "checks_passed": passed,
        "checks_total": len(checks),
        "blockers": blockers,
        "cover": cover_info,
        "cover_approval": approval,
        "checks": checks,
    }


def render_report(result: dict[str, Any]) -> str:
    lines = [
        "# Book 6 Package-Readiness Validation",
        "",
        f"- Status: **{result['status']}**",
        f"- Checks passed: **{result['checks_passed']}/{result['checks_total']}**",
        "- Publication status: **pending; not published**",
        "",
        "## Checks",
        "",
    ]
    for item in result["checks"]:
        mark = "x" if item["passed"] else " "
        lines.append(f"- [{mark}] {item['name']} — {item['detail']}")
    lines.extend(["", "## Blockers", ""])
    if result["blockers"]:
        lines.extend(f"- {blocker}" for blocker in result["blockers"])
    else:
        lines.append("- None. The release build may proceed, but publication remains pending.")
    lines.extend([
        "",
        "This report does not mark the book upload ready, uploaded, accepted, distributed, or published.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--json", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = validate(args.repo_root)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report = render_report(result)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    print(report)
    return 0 if result["status"] == "ready_for_release_build" else 2


if __name__ == "__main__":
    raise SystemExit(main())
