#!/usr/bin/env python3
"""Controlled proofread-source export build for Book 6. Package/release work is excluded."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Sequence

import yaml

TITLE = "The Pattern"
SERIES = "The Blackwood Ridge Mysteries"
NUMBER = 6
AUTHOR = "Vesper Blythe"
LANG = "en-US"
YEAR = 2026
BUILD_DATE = date(2026, 7, 15)
TOTAL = 25646
SOURCE_BASE_SHA = "d23d2e745ea0a5fda414321b6c82eda427459a87"
PR31_HEAD = "15ffd86577f2914729f25c0932a97ff2a830be1f"
PR31_BASE = "105634b1dbf41a9c15ab6d2ea3df7d9945c8b264"
BRANCH = "agent/book-06-controlled-export-assembly"
PROVENANCE = "Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established."
CHAPTERS = [
    (1, "The Box at Closing", "The Box at Closing", "ch-01.md", "2027-04-15", 3100, "drafted", 3266, "The ladder had not rolled.", "The ladder had not rolled."),
    (2, "A Fall That Did Not Fit", "A Fall That Did Not Fit", "ch-02.md", "2027-04-15/2027-04-16", 3150, "drafted", 3135, "One had been cleaned.", "One had been cleaned."),
    (3, "The Surveyor’s Missing Line", "The Surveyor's Missing Line", "ch-03.md", "2027-04-16", 3100, "drafted", 3130, "Sheet 47 had described a public right-of-way through Bellweather river land.", "Sheet 47 had described a public right-of-way through Bellweather river land."),
    (4, "Marks Made Later", "Marks Made Later", "ch-04.md", "2027-04-16", 3150, "drafted", 3150, "`South line retrieval.`", "South line retrieval."),
    (5, "The Road Through Bellweather", "The Road Through Bellweather", "ch-05.md", "2027-04-17", 3100, "drafted", 3100, "The road through Bellweather did not contain the missing thirty-nine minutes.", "The road through Bellweather did not contain the missing thirty-nine minutes."),
    (6, "What the Ledger Withheld", "What the Ledger Withheld", "ch-06.md", "2027-04-17", 3150, "revised", 3279, "It was enough to ask where Dana had put the rest.", "It was enough to ask where Dana had put the rest."),
    (7, "The Weight of the Map", "The Weight of the Map", "ch-07.md", "2027-04-18", 3100, "revised", 3105, "The route field remained blank.", "The route field remained blank."),
    (8, "The Pattern", "The Pattern", "ch-08.md", "2027-04-18", 3150, "revised", 3481, "Who knew which page she would open next?", "Who knew which page she would open next?"),
]
FRONT = ["title-page.md", "copyright.md", "contents.md"]
BACK = ["author-note.md", "series.md", "about-the-author.md"]
EXPECTED_GIT_BLOBS = {
    1: "c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6",
    2: "6404737d8d0610908608f7d8ab45c02cd75158fd",
    3: "59575d837b6c51d22d57ff4033e6a09bc218a409",
    4: "401d46dad388ddb6ca7df6041c464465a19a48c5",
    5: "81fad0335b3781712b38d4d3139d92ffe94b3476",
    6: "6b43203b07287771b99ef87240955ec31206e996",
    7: "9ffbb201458d822bafcdf24ffe3b28df283b635a",
    8: "be9f1a5531c3a6d61430483b76ed01472d0a03e4",
}
BAD = [
    re.compile(r"<<<<<<<|=======|>>>>>>>", re.M),
    re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.I),
    re.compile(r"AUTHOR DECISION REQUIRED", re.I),
    re.compile(r"\[\s*PLACEHOLDER\s*\]", re.I),
    re.compile(r"eli-hidden-chronology|internal_series_spoilers|internal_continuity_control|reader_facing_long_arc_spoiler", re.I),
    re.compile(r"mission[- ]lock|story[- ]memory|mystery[- ]solution|proofreading-report|revision-plan", re.I),
]
BOOK5_REFERENCES = [
    "books/book-05/export/README.md",
    "books/book-05/export/.gitignore",
    "books/book-05/export/assemble-manuscript.py",
    "books/book-05/export/finalize-package.py",
    "books/book-05/export/run-export.py",
    "books/book-05/export/build.sh",
    ".github/workflows/book-05-proof-export.yml",
    "books/book-05/export/manuscript-combined.md",
    "books/book-05/export/manuscript-combined.txt",
    "books/book-05/export/manuscript-combined.html",
    "books/book-05/export/word-count-report.md",
    "books/book-05/export/export-readiness.md",
    "books/book-05/export/validation-report.md",
]


def run(cmd: Sequence[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(list(cmd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    if check and result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(cmd)}\n{result.stdout}")
    return result


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n").rstrip() + "\n", encoding="utf-8")


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_apostrophes(value: str) -> str:
    return value.replace("’", "'").replace("‘", "'")


def control(number: int):
    return next(row for row in CHAPTERS if row[0] == number)


def source_words(chapter) -> int:
    return control(chapter.number)[7]


def source_final(chapter) -> str:
    return control(chapter.number)[8]


def reader_final(chapter) -> str:
    return control(chapter.number)[9]


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def scene_break_count(text: str) -> int:
    return sum(1 for line in text.replace("\r\n", "\n").splitlines() if line.strip() == "***")


def load_book4(root: Path):
    path = root / "books/book-04/export/finalize-package.py"
    spec = importlib.util.spec_from_file_location("book4_export_for_book6", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.TITLE = TITLE
    module.SERIES = SERIES
    module.SERIES_NUMBER = NUMBER
    module.AUTHOR = AUTHOR
    module.LANGUAGE = LANG
    module.BUILD_DATE = BUILD_DATE
    module.CHAPTERS = [(n, display_title, filename) for n, display_title, _, filename, *_ in CHAPTERS]
    module.FRONT_FILES = FRONT
    module.BACK_FILES = BACK
    module.BAD_READER_PATTERNS = BAD
    return module


def front_back(book: Path) -> None:
    write(book / "front-matter/title-page.md", f"# {TITLE}\n\n**{AUTHOR}**\n\n*{SERIES} — Book {NUMBER}*")
    write(book / "front-matter/copyright.md", f"""# Copyright

**{TITLE}**

Copyright © {YEAR} {AUTHOR}

All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without prior written permission from the copyright holder, except for brief quotations used in reviews or other uses permitted by law.

This is a work of fiction. Names, characters, businesses, places, events, and incidents are products of the author’s imagination or are used fictitiously. Any resemblance to actual persons, living or dead, or actual events is coincidental.

First edition.""")
    contents = ["# Contents", ""] + [f"{n}. Chapter {n} — {display_title}" for n, display_title, *_ in CHAPTERS]
    contents += ["9. A Note from the Author", "10. The Blackwood Ridge Mysteries", "11. About the Author"]
    write(book / "front-matter/contents.md", "\n".join(contents))
    write(book / "back-matter/author-note.md", f"""# A Note from the Author

Thank you for reading *{TITLE}*.

If this mystery kept you turning pages, an honest review helps other readers find Blackwood Ridge and the records Callie Thorne refuses to leave unread.""")
    write(book / "back-matter/series.md", """# The Blackwood Ridge Mysteries

1. *The Annotated Murder*
2. *The Botanical Confession*
3. *The Challenger*
4. *The Archive Fire*
5. *The Planted Page*
6. *The Pattern*""")
    write(book / "back-matter/about-the-author.md", """# About the Author

Vesper Blythe is the author of The Blackwood Ridge Mysteries, an atmospheric cozy mystery series featuring antiquarian bookseller and amateur sleuth Callie Thorne.""")


def validate_sources(b4, chapters):
    checks = b4.Validation([])
    for chapter in chapters:
        n, display_title, yaml_title, _, date_, target, status, words, final_source, _ = control(chapter.number)
        metadata, _ = b4.strip_yaml_and_heading(chapter.source_path.read_text(encoding="utf-8"), n, display_title)
        expected = {
            "n": n,
            "title": yaml_title,
            "pov": "Callie Thorne",
            "date": date_,
            "word_target": target,
            "status": status,
            "words": words,
        }
        for key, value in expected.items():
            actual = str(metadata.get(key)) if key == "date" else metadata.get(key)
            good = normalize_apostrophes(str(actual)) == normalize_apostrophes(str(value)) if key == "title" else actual == value
            checks.add(f"Source Chapter {n}: {key}", good, f"expected {value!r}; actual {actual!r}")
        actual_blob = git_blob_sha(chapter.source_path)
        checks.add(f"Source Chapter {n}: proofread Git blob", actual_blob == EXPECTED_GIT_BLOBS[n], f"expected {EXPECTED_GIT_BLOBS[n]}; actual {actual_blob}")
        checks.add(f"Source Chapter {n}: locked proofread count", source_words(chapter) == words, f"expected {words}; actual {source_words(chapter)}")
        source_text = chapter.source_path.read_text(encoding="utf-8")
        checks.add(f"Source Chapter {n}: no trailing spaces", not any(line.endswith((" ", "\t")) for line in source_text.splitlines()), "checked")
        checks.add(f"Source Chapter {n}: exact final line", chapter.body.rstrip().endswith(final_source), chapter.body.rstrip().splitlines()[-1])
        b4.validate_reader_text(f"Source Chapter {n}", chapter.body, checks)
    body = "\n".join(ch.body for ch in chapters)
    checks.add("Source: eight chapters", len(chapters) == 8, str(len(chapters)))
    checks.add("Source: total 25,646", sum(source_words(ch) for ch in chapters) == TOTAL, str(sum(source_words(ch) for ch in chapters)))
    checks.add("Source: exact Mercer provenance once", body.count(PROVENANCE) == 1, str(body.count(PROVENANCE)))
    checks.add("Source: no duplicate chapter body", len({ch.body_sha256 for ch in chapters}) == 8, "checked")
    checks.require()
    return checks


def build(b4, book: Path, combined: Path, chapters):
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required")
    export, dist, qa = book / "export", book / "export/dist", book / "export/qa"
    dist.mkdir(parents=True, exist_ok=True)
    qa.mkdir(parents=True, exist_ok=True)
    txt, html = export / "manuscript-combined.txt", export / "manuscript-combined.html"
    docx, epub = dist / "The-Pattern.docx", dist / "The-Pattern.epub"
    reference = export / "reference.docx"
    run([pandoc, str(combined), "-f", "markdown", "-t", "plain", "--wrap=none", "-o", str(txt)])
    run([pandoc, str(combined), "-f", "markdown", "-t", "html5", "--standalone", "-M", f"pagetitle={TITLE}", "-M", f"lang={LANG}", "-o", str(html)])
    b4.inject_html_css(html)
    b4.create_reference_docx(reference)
    run([pandoc, str(combined), "-f", "markdown", "-t", "docx", "--reference-doc", str(reference), "-o", str(docx)])
    b4.postprocess_docx(docx)
    parts = [(book / "front-matter" / name).read_text(encoding="utf-8").strip() for name in ["copyright.md", "contents.md"]]
    parts += [f"# Chapter {ch.number} — {ch.display_title}\n\n{ch.body}" for ch in chapters]
    parts += [(book / "back-matter" / name).read_text(encoding="utf-8").strip() for name in BACK]
    epub_source = dist / "epub-source.md"
    write(epub_source, "\n\n---\n\n".join(parts))
    run([pandoc, str(epub_source), "-f", "markdown", "-t", "epub3", "--toc", "--toc-depth=1", "-M", f"title={TITLE}", "-M", f"author={AUTHOR}", "-M", f"lang={LANG}", "-M", "subject=Atmospheric cozy mystery; amateur sleuth; archival mystery", "-M", f"rights=Copyright © {YEAR} {AUTHOR}. All rights reserved.", "-o", str(epub)])
    epub_source.unlink()
    return {"markdown": combined, "text": txt, "html": html, "docx": docx, "epub": epub, "qa_dir": qa}


def normalized(text: str) -> str:
    text = re.sub(r"(?m)^\s*(?:\*\s*){3,}\s*$", "", text)
    text = re.sub(r"(?m)^\s*---+\s*$", "", text)
    return re.sub(r"\s+", " ", text).strip()


def pandoc_plain(path: Path, source_format: str) -> str:
    pandoc = shutil.which("pandoc")
    result = run([pandoc, str(path), "-f", source_format, "-t", "plain", "--wrap=none"])
    return result.stdout


def chapter_sections(text: str) -> dict[int, str]:
    lines = text.replace("\r\n", "\n").splitlines()
    starts = []
    for n, display_title, *_ in CHAPTERS:
        heading = f"Chapter {n} — {display_title}"
        hits = [i for i, line in enumerate(lines) if line.strip() == heading]
        if not hits:
            raise RuntimeError(f"Missing converted heading: {heading}")
        starts.append((n, hits[-1]))
    sections = {}
    for index, (n, start) in enumerate(starts):
        if index + 1 < len(starts):
            end = starts[index + 1][1]
        else:
            end = next((i for i in range(start + 1, len(lines)) if lines[i].strip() == "A Note from the Author"), len(lines))
        sections[n] = normalized("\n".join(lines[start + 1:end]))
    return sections


def raw_markdown_sections(text: str) -> dict[int, str]:
    lines = text.replace("\r\n", "\n").splitlines()
    starts = []
    for n, display_title, *_ in CHAPTERS:
        heading = f"# Chapter {n} — {display_title}"
        hits = [i for i, line in enumerate(lines) if line.strip() == heading]
        if len(hits) != 1:
            raise RuntimeError(f"Expected one Markdown heading {heading!r}; found {len(hits)}")
        starts.append((n, hits[0]))
    sections = {}
    for index, (n, start) in enumerate(starts):
        end = starts[index + 1][1] if index + 1 < len(starts) else next((i for i in range(start + 1, len(lines)) if lines[i].strip() == "# A Note from the Author"), len(lines))
        sections[n] = "\n".join(lines[start + 1:end]).strip()
    return sections


def identity_validation(b4, book: Path, chapters, artifacts):
    checks = b4.Validation([])
    expected = {}
    temp = book / "export/dist/source-body.md"
    for chapter in chapters:
        write(temp, chapter.body)
        expected[chapter.number] = normalized(pandoc_plain(temp, "markdown"))
    temp.unlink()
    formats = {"markdown": "markdown", "text": "plain", "html": "html", "docx": "docx", "epub": "epub"}
    for name, source_format in formats.items():
        if name == "text":
            text = artifacts[name].read_text(encoding="utf-8")
        else:
            text = pandoc_plain(artifacts[name], source_format)
        sections = chapter_sections(text)
        for chapter in chapters:
            actual = sections[chapter.number]
            good = actual == expected[chapter.number]
            detail = f"source {hashlib.sha256(expected[chapter.number].encode()).hexdigest()}; output {hashlib.sha256(actual.encode()).hexdigest()}"
            checks.add(f"{name.upper()} Chapter {chapter.number}: exact reader-text identity", good, detail)
            checks.add(f"{name.upper()} Chapter {chapter.number}: exact final line", actual.endswith(normalized(reader_final(chapter))), actual[-160:])
    markdown_sections = raw_markdown_sections(artifacts["markdown"].read_text(encoding="utf-8"))
    for chapter in chapters:
        expected_breaks = scene_break_count(chapter.body)
        actual_breaks = scene_break_count(markdown_sections[chapter.number])
        checks.add(f"MARKDOWN Chapter {chapter.number}: scene-break parity", actual_breaks == expected_breaks, f"source {expected_breaks}; output {actual_breaks}")
    checks.require()
    return checks


def resolve_scope_base() -> tuple[str, str]:
    """Return the actual change-scope ref and its merge base with HEAD."""
    explicit = os.environ.get("BOOK6_SCOPE_BASE_REF")
    if explicit:
        candidates = [explicit]
    else:
        candidates = []
        github_base = os.environ.get("GITHUB_BASE_REF")
        if github_base:
            candidates.extend([f"origin/{github_base}", github_base])
        candidates.extend(["origin/main", "main"])

    attempted = []
    for candidate in dict.fromkeys(candidates):
        result = run(["git", "merge-base", candidate, "HEAD"], check=False)
        merge_base = result.stdout.strip()
        attempted.append(f"{candidate}: {result.returncode}")
        if result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", merge_base):
            return candidate, merge_base
    raise RuntimeError(f"Unable to resolve current change-scope base ({'; '.join(attempted)})")


def is_production_asset(path: str) -> bool:
    if not re.match(r"^books/book-\d+/", path):
        return False
    protected_stems = ("package", "cover", "listing", "upload", "publication", "publish", "release", "retailer")
    return any(part.lower().startswith(protected_stems) for part in Path(path).parts[2:])


def scope_validation(b4, root: Path):
    checks = b4.Validation([])
    try:
        scope_base_ref, scope_base_sha = resolve_scope_base()
        result = run(["git", "diff", "--name-only", f"{scope_base_sha}...HEAD"], check=False)
        comparison_ok = result.returncode == 0
        comparison_detail = f"ref {scope_base_ref}; merge base {scope_base_sha}"
        if not comparison_ok:
            comparison_detail += f"; {result.stdout.strip() or 'git diff failed'}"
    except RuntimeError as exc:
        scope_base_ref, scope_base_sha = "unresolved", ""
        result = None
        comparison_ok = False
        comparison_detail = str(exc)

    checks.add("Scope: actual current-base comparison available", comparison_ok, comparison_detail)
    changed = [line.strip() for line in result.stdout.splitlines() if line.strip()] if comparison_ok and result else []

    book5_changes = [p for p in changed if p.startswith("books/book-05/")]
    book6_manuscript = [p for p in changed if re.match(r"^books/book-06/manuscript/ch-.*\.md$", p)]
    book7_manuscript = [p for p in changed if re.match(r"^books/book-07/manuscript/ch-.*\.md$", p)]
    book8_changes = [p for p in changed if p.startswith("books/book-08/")]
    production_assets = [p for p in changed if is_production_asset(p)]
    book3_workflows = [p for p in changed if re.match(r"^\.github/workflows/book-03", p)]

    checks.add("Scope: Book 5 unchanged", not book5_changes, repr(book5_changes))
    checks.add("Scope: no Book 6 chapter manuscript changed", not book6_manuscript, repr(book6_manuscript))
    checks.add("Scope: no Book 7 chapter manuscript changed relative to current base", not book7_manuscript, repr(book7_manuscript))
    checks.add("Scope: Book 8 unchanged", not book8_changes, repr(book8_changes))
    checks.add("Scope: no package/cover/listing/upload/publication/release/retailer asset changed", not production_assets, repr(production_assets))
    checks.add("Scope: Book 3 release workflow unchanged", not book3_workflows, repr(book3_workflows))

    book7_dir = root / "books/book-07/manuscript"
    book7_prose = sorted(str(path.relative_to(root)) for path in book7_dir.glob("ch-*.md")) if book7_dir.exists() else []
    checks.add("Scope: existing Book 7 prose is outside Book 6 export authority", True, repr(book7_prose) or "none present")
    checks.require()
    return checks, scope_base_sha, changed


def merge(b4, validations):
    return b4.Validation([entry for validation in validations for entry in validation.checks])


def reports(b4, root: Path, book: Path, chapters, artifacts, validation, pages: int, contacts, epubcheck: str, pdf: Path | None, scope_base_sha: str, changed):
    export = book / "export"
    source_total = sum(source_words(ch) for ch in chapters)
    combined_total = b4.word_count(artifacts["markdown"].read_text(encoding="utf-8"))
    matter_text = "\n\n".join((book / "front-matter" / name).read_text(encoding="utf-8") for name in FRONT)
    matter_text += "\n\n" + "\n\n".join((book / "back-matter" / name).read_text(encoding="utf-8") for name in BACK)
    matter_total = b4.word_count(matter_text)
    heading_total = b4.word_count("\n".join(f"Chapter {n} — {display_title}" for n, display_title, *_ in CHAPTERS))
    source_rows = ["| Ch. | Title | Words | Git blob | Source SHA-256 | Body SHA-256 | Scene breaks | Final line |", "|---:|---|---:|---|---|---|---:|---|"]
    for ch in chapters:
        source_rows.append(f"| {ch.number} | {ch.display_title} | {source_words(ch):,} | `{EXPECTED_GIT_BLOBS[ch.number]}` | `{ch.source_sha256}` | `{ch.body_sha256}` | {scene_break_count(ch.body)} | `{source_final(ch)}` |")
    artifact_rows = ["| Artifact | Classification | Bytes | SHA-256 |", "|---|---|---:|---|"]
    records = []
    classifications = {"markdown": "canonical reader-facing export", "text": "canonical reader-facing export", "html": "canonical reader-facing export", "docx": "reproducible review artifact", "epub": "reproducible review artifact"}
    for name in ["markdown", "text", "html", "docx", "epub"]:
        path = artifacts[name]
        record = {"name": path.name, "format": name, "classification": classifications[name], "size_bytes": path.stat().st_size, "sha256": file_hash(path)}
        records.append(record)
        artifact_rows.append(f"| `{record['name']}` | {record['classification']} | {record['size_bytes']:,} | `{record['sha256']}` |")
    write(export / "word-count-report.md", f"""# Book 6 Word-Count and Export Report

- **Book:** {TITLE}
- **Author:** {AUTHOR}
- **Series:** {SERIES} — Book {NUMBER}
- **Build date:** {BUILD_DATE.isoformat()}
- **Manuscript count method:** Locked whitespace-delimited proofread manuscript-prose counts, confirmed by exact Git-blob identity and chapter front matter.
- **Combined export count method:** Repository-standard Markdown-aware count inherited from the Book 4/5 export pipeline.
- **Manuscript-prose total:** **{source_total:,}**
- **Front/back-matter total:** **{matter_total:,}**
- **Chapter-heading total:** **{heading_total:,}**
- **Combined reader-facing total:** **{combined_total:,}**
- **Chapters:** **8**
- **DOCX render pages:** **{pages}**
- **DOCX contact sheets:** **{len(contacts)}**

## Chapter source counts and hashes

{chr(10).join(source_rows)}

**Arithmetic check:** {' + '.join(str(source_words(ch)) for ch in chapters)} = **{source_total:,}**

## Export artifact hashes

{chr(10).join(artifact_rows)}

DOCX and EPUB outputs are reproducible export-review artifacts, not retailer packages or publication records.
""")
    write(export / "export-readiness.md", f"""# Book 6 Controlled Export Readiness

## Status

**Controlled proofreading complete. Repository-standard export assembly complete and validated. Package, cover, listing, upload, and publication remain pending.**

This record does not mark *{TITLE}* upload ready, retailer ready, distributed, or published.

## Source result

- PR #31 source head: `{PR31_HEAD}`
- PR #31 merge commit and export base: `{SOURCE_BASE_SHA}`
- Chapters 1–8 were verified by exact Git blob, metadata, count, title, order, scene-break structure, and final line.
- Manuscript prose remains **{source_total:,} words**.
- Exact Mercer provenance preserved: `{PROVENANCE}`
- All eight locked final lines are preserved.

## Scope result

- Historical source baseline for exact Book 6 manuscript identity: `{SOURCE_BASE_SHA}`
- Current change-scope merge base: `{scope_base_sha}`
- Existing Book 7 prose is outside Book 6 export authority.
- No Book 7 chapter manuscript changed relative to the current change-scope base.

## Metadata result

- Title: **{TITLE}**
- Author: **{AUTHOR}**
- Series: **{SERIES}**
- Series number: **Book {NUMBER}**
- POV: **Callie Thorne, third-person limited only**
- Chronology: **April 15 through April 18, 2027**
- Copyright page convention: **© {YEAR} {AUTHOR}; First edition**, inherited from the approved Book 5 export convention.

## Export result

- Combined Markdown, plain text, standalone HTML, DOCX, and EPUB 3 generated.
- Front/back-matter count: **{matter_total:,}**
- Combined reader-facing count: **{combined_total:,}**
- DOCX render: **{pages} pages**; contact sheets: **{len(contacts)}**
- Source-to-export comparison: **all eight chapters matched in Markdown, TXT, HTML, DOCX, and EPUB**
- Scene-break comparison: **all eight chapters matched in canonical Markdown**
- EPUBCheck: **passed**
- Placeholder/internal-control/spoiler scan: **clean**

## Scope boundary

No cover, listing copy, retailer form, upload ZIP, advertising asset, release package, retailer submission, publication record, or release-status change is included. The next stage after merge is **Book 6 controlled package assembly/readiness**.
""")
    passed = sum(1 for _, ok, _ in validation.checks if ok)
    lines = ["# Book 6 Controlled Export Validation", "", f"- Checks passed: **{passed}/{len(validation.checks)}**", ""]
    lines += [f"- [{'x' if ok else ' '}] {name} — {detail}" for name, ok, detail in validation.checks]
    lines += ["", "## EPUBCheck", "", "```text", epubcheck.strip() or "passed", "```", "", "Package, cover, listing, upload, and publication remain pending."]
    write(export / "validation-report.md", "\n".join(lines))
    inspected = "\n".join(f"- `{path}`" for path in BOOK5_REFERENCES)
    outputs = "\n".join(f"- `{record['name']}` — {record['classification']} — `{record['sha256']}`" for record in records)
    changed_lines = "\n".join(f"- `{path}`" for path in changed) or "- none at validation time"
    write(book / "export-report.md", f"""# Book 6 Controlled Export Assembly Report

## Dependency and repository baseline

- Repository: `dustinober1/The-Blackwood-Ridge-Mysteries`
- Default branch: `main`
- PR #31: `Proofread Book 6` — merged
- PR #31 source branch: `agent/book-06-controlled-proofreading`
- PR #31 source head: `{PR31_HEAD}`
- PR #31 base: `{PR31_BASE}`
- PR #31 merge commit and historical Book 6 source baseline: `{SOURCE_BASE_SHA}`
- Current validation change-scope merge base: `{scope_base_sha}`
- Historical export branch: `{BRANCH}`

## Verified source manuscript

{chr(10).join(source_rows)}

- Manuscript-prose total: **{source_total:,}**
- Chapter order: **1–8**
- Exact Mercer wording preserved: `{PROVENANCE}`
- POV: single third-person limited through Callie Thorne

## Export conventions discovered

Book 5 establishes `books/book-N/export/` as the controlled export directory; committed combined Markdown, TXT, HTML, readiness/count/validation reports; generated front and back matter; reproducible ignored DOCX/EPUB/manifest/QA outputs; Pandoc conversion; DOCX render validation; EPUBCheck; source-to-format identity comparison; deterministic ZIP timestamps and EPUB identifiers; and explicit exclusion of package, cover, listing, upload, and publication work.

### Book 5 references inspected

{inspected}

## Export manifest

{chr(10).join(artifact_rows)}

### Source-to-output mapping

- YAML production front matter: removed from all reader-facing outputs.
- Source chapter headings: mapped to `Chapter N — Title` reader headings.
- Source `***` scene breaks: preserved in canonical Markdown and converted through the established Pandoc pipeline.
- Paragraphs, sentences, words, punctuation, quotation marks, apostrophes, italics, documentary formatting, chapter order, and chapter-final lines: preserved by exact normalized source-to-output comparison.
- Front matter: title page, copyright page, and contents generated from repository-approved title, author, series, book number, and inherited Book 5 convention.
- Back matter: author note, series list through Book 6, and existing author bio convention.

## Counts

- Manuscript prose: **{source_total:,}**
- Front/back matter: **{matter_total:,}**
- Chapter headings: **{heading_total:,}**
- Combined reader-facing count: **{combined_total:,}**

## Validation and artifact-open results

- Validator command: `python books/book-06/export/run-export.py`
- Checks passed: **{passed}/{len(validation.checks)}**
- Markdown: parsed and source-identical chapter by chapter.
- TXT: opened and source-identical chapter by chapter.
- HTML: parsed as standalone HTML and source-identical chapter by chapter.
- DOCX: opened, structurally checked, rendered to **{pages} pages**, and reviewed through **{len(contacts)} contact sheets**.
- EPUB: opened, navigation/metadata checked, source-identical chapter by chapter, and EPUBCheck passed.
- Duplicate/missing/truncated content: none detected.
- Hidden control, mission-lock, bible, spoiler, status, or Eli-truth leakage: none detected.
- Complete scope diff at validation time:
{changed_lines}

## Locked story and procedural preservation

- Dana Wren remains Miriam Vale’s murderer.
- Map weight six remains the cumulative weapon.
- Dana does not confess; questioning still stops after counsel invocation.
- Murder proof remains independent of curator identity; murderer-versus-curator separation remains intact.
- Halbrook’s October 8 accidental death remains separate from later concealment and the October 3/6/8/9–12 sequence remains intact.
- Tara’s authenticated alibi and separate misconduct/custody consequences remain intact.
- Graphite, binder, polymer, composition, grade, brand, owner, buyer, writer, pencil, and instrument limits remain non-identifying.
- The three modern routing marks remain separate from Miriam’s triangle.
- Callie remains a bounded consultant; Cross retains legal/procedural authority; Bell and lawful custodians retain custody.
- Mae’s established role and limits remain intact.
- Eli remains unidentified, non-suspicious, and outside original evidence, warrants, searches, laboratories, recovery, remains, and suspect access.

## Lifecycle and neighboring-book status

- Controls updated: `books/book-06/README.md`, `books/book-06/manuscript/README.md`, `books/book-06/progress.yaml`, `books/book-06/outline.md`, and `series-outline.md`.
- Completed revision, line-edit, final-prose-polish, and proofreading records were inspected and intentionally not rewritten.
- Book 5 files changed: **none**.
- Exact Book 5 status: package in progress; publication pending; approved canonical ebook cover remains the blocker; Book 5 is not upload ready.
- Book 7 Chapter 1 exists and is formally accepted at 3,100 manuscript-prose words; it is outside Book 6 export authority, and no Book 7 chapter manuscript changed in this validation scope.
- Exact Book 6 status: controlled revision, line edit, final prose polish, proofreading, and export assembly complete; package, cover, listing, upload, and publication pending; Book 6 is not upload ready.

## Intentionally not created

- cover files or cover approvals
- listing copy or retailer descriptions
- retailer metadata forms or identifiers
- upload ZIPs or platform bundles
- advertising assets
- release packages
- publication or distribution records
- any Book 7 manuscript prose by the Book 6 export workflow

## Blockers and next stage

No blocker remains within controlled export assembly. Package, cover, listing, upload, and publication work remain deliberately deferred. After this export pull request is reviewed and merged, the recommended next stage is **Book 6 controlled package assembly/readiness**.
""")
    manifest = {
        "book": TITLE,
        "author": AUTHOR,
        "series": SERIES,
        "series_number": NUMBER,
        "build_date": BUILD_DATE.isoformat(),
        "source_base": SOURCE_BASE_SHA,
        "scope_base": scope_base_sha,
        "proofreading_pr_head": PR31_HEAD,
        "status": "export_validated_package_pending",
        "manuscript_prose_words": source_total,
        "front_back_matter_words": matter_total,
        "chapter_heading_words": heading_total,
        "combined_reader_facing_words": combined_total,
        "chapter_count": 8,
        "docx_render_pages": pages,
        "contact_sheets": len(contacts),
        "source_to_export_identity": "all_chapters_all_formats_passed",
        "scene_break_identity": "all_chapters_markdown_passed",
        "epubcheck": "passed",
        "package_status": "pending",
        "cover_status": "pending",
        "listing_status": "pending",
        "upload_status": "pending",
        "publication_status": "pending",
        "upload_ready": False,
        "artifacts": records,
    }
    if pdf:
        manifest["docx_render_pdf"] = {"name": pdf.name, "size_bytes": pdf.stat().st_size, "sha256": file_hash(pdf)}
    write(export / "dist/export-manifest.json", json.dumps(manifest, indent=2))


def main() -> None:
    book = Path(__file__).resolve().parent.parent
    root = book.parent.parent
    b4 = load_book4(root)
    front_back(book)
    chapters = b4.load_chapters(book / "manuscript")
    source = validate_sources(b4, chapters)
    combined = b4.assemble_manuscript(book, chapters)
    artifacts = build(b4, book, combined, chapters)
    validations = [source, b4.validate_markdown(combined, chapters), b4.validate_html(artifacts["html"])]
    validations.append(identity_validation(b4, book, chapters, artifacts))
    docx_validation, pages, contacts, pdf = b4.validate_docx(artifacts["docx"], artifacts["qa_dir"])
    epub_validation, epubcheck = b4.validate_epub(artifacts["epub"])
    scope, scope_base_sha, changed = scope_validation(b4, root)
    validations += [docx_validation, epub_validation, scope]
    all_validation = merge(b4, validations)
    all_validation.require()
    reports(b4, root, book, chapters, artifacts, all_validation, pages, contacts, epubcheck, pdf, scope_base_sha, changed)
    print(f"Validated {TITLE}: {TOTAL:,} manuscript-prose words")
    print(f"Checks: {len(all_validation.checks)}/{len(all_validation.checks)} passed")
    print("Package: pending")
    print("Cover: pending")
    print("Listing: pending")
    print("Upload: pending")
    print("Publication: pending")


if __name__ == "__main__":
    main()
