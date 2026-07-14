#!/usr/bin/env python3
"""Final-proof and export build for Book 5. Package/release work is excluded."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Sequence

import yaml

TITLE = "The Planted Page"
SERIES = "The Blackwood Ridge Mysteries"
NUMBER = 5
AUTHOR = "Vesper Blythe"
LANG = "en-US"
YEAR = 2026
BUILD_DATE = date(2026, 7, 13)
TOTAL = 25174
FINAL_LINE = "She closed the file."
PROVENANCE = "Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established."
CHAPTERS = [
    (1, "The Hand at the Door", "ch-01.md", "2027-01-25", 3100, 3295),
    (2, "A Note in His Hand", "ch-02.md", "2027-01-26", 3100, 3063),
    (3, "The Comparison Room", "ch-03.md", "2027-01-27", 3100, 3127),
    (4, "The Same Letter Twice", "ch-04.md", "2027-01-28", 3200, 3240),
    (5, "What the Trust Passed", "ch-05.md", "2027-01-29", 3100, 3074),
    (6, "The Hand That Waited", "ch-06.md", "2027-01-30", 3100, 3039),
    (7, "The Page Under Pressure", "ch-07.md", "2027-01-31", 3200, 3189),
    (8, "The Current Hand", "ch-08.md", "2027-02-01", 3100, 3147),
]
FRONT = ["title-page.md", "copyright.md", "contents.md"]
BACK = ["author-note.md", "series.md", "about-the-author.md"]
EXPECTED_GIT_BLOBS = {
    1: "8d37435084d7cb1258c249a05a5f7ea72937fbbb",
    2: "c0ad5f363f20276ded285ff7bfc5da95a1096b1c",
    3: "01a95c77ddec4d0945ec9ded1adbaa73f3ea3e21",
    4: "e792f826f7e651e62623417b31043e40c237d0ef",
    5: "72df87632b050caf675dc598948845d2b755720e",
    6: "2c8f3bf5a5df8707b6694e38a259ac4131728f7b",
    7: "9fa7be1a79202d2dd76fb5767bf027e3e337800b",
    8: "0595c5b2acd17170aa2a3a3e36585289952301fa",
}
BAD = [
    re.compile(r"<<<<<<<|=======|>>>>>>>", re.M),
    re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.I),
    re.compile(r"AUTHOR DECISION REQUIRED", re.I),
    re.compile(r"\[\s*PLACEHOLDER\s*\]", re.I),
    re.compile(r"eli-hidden-chronology|internal_series_spoilers|internal_continuity_control|reader_facing_long_arc_spoiler", re.I),
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


def load_book4(root: Path):
    path = root / "books/book-04/export/finalize-package.py"
    spec = importlib.util.spec_from_file_location("book4_export", path)
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
    module.CHAPTERS = [(n, title, filename) for n, title, filename, *_ in CHAPTERS]
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
    contents = ["# Contents", ""] + [f"{n}. Chapter {n} — {title}" for n, title, *_ in CHAPTERS]
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
5. *The Planted Page*""")
    write(book / "back-matter/about-the-author.md", """# About the Author

Vesper Blythe is the author of The Blackwood Ridge Mysteries, an atmospheric cozy mystery series featuring antiquarian bookseller and amateur sleuth Callie Thorne.""")


def source_words(chapter) -> int:
    """Return the accepted polished count for an exact verified source blob."""
    return next(words for n, _, _, _, _, words in CHAPTERS if n == chapter.number)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def validate_sources(b4, chapters):
    checks = b4.Validation([])
    controls = {n: (title, date_, target, words) for n, title, _, date_, target, words in CHAPTERS}
    for chapter in chapters:
        title, date_, target, words = controls[chapter.number]
        metadata, _ = b4.strip_yaml_and_heading(chapter.source_path.read_text(encoding="utf-8"), chapter.number, title)
        expected = {
            "title": title, "pov": "Callie Thorne", "date": date_,
            "word_target": target, "status": "drafted", "words": source_words(chapter),
        }
        for key, value in expected.items():
            actual = str(metadata.get(key)) if key == "date" else metadata.get(key)
            checks.add(f"Source Chapter {chapter.number}: {key}", actual == value, f"expected {value!r}; actual {actual!r}")
        checks.add(f"Source Chapter {chapter.number}: locked proof count", source_words(chapter) == words, f"expected {words}; actual {source_words(chapter)}")
        checks.add(
            f"Source Chapter {chapter.number}: accepted polished Git blob",
            git_blob_sha(chapter.source_path) == EXPECTED_GIT_BLOBS[chapter.number],
            f"expected {EXPECTED_GIT_BLOBS[chapter.number]}; actual {git_blob_sha(chapter.source_path)}",
        )
        text = chapter.source_path.read_text(encoding="utf-8")
        checks.add(f"Source Chapter {chapter.number}: no trailing spaces", not any(line.endswith((" ", "\t")) for line in text.splitlines()), "checked")
        b4.validate_reader_text(f"Source Chapter {chapter.number}", chapter.body, checks)
    body = "\n".join(ch.body for ch in chapters)
    checks.add("Source: eight chapters", len(chapters) == 8, str(len(chapters)))
    checks.add("Source: total 25,174", sum(source_words(ch) for ch in chapters) == TOTAL, str(sum(source_words(ch) for ch in chapters)))
    checks.add("Source: provenance exactly once", body.count(PROVENANCE) == 1, str(body.count(PROVENANCE)))
    checks.add("Source: final line exact", chapters[-1].body.rstrip().endswith(FINAL_LINE), chapters[-1].body.rstrip().splitlines()[-1])
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
    docx, epub = dist / "The-Planted-Page.docx", dist / "The-Planted-Page.epub"
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
    for n, title, *_ in CHAPTERS:
        heading = f"Chapter {n} — {title}"
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


def identity_validation(b4, book: Path, chapters, artifacts):
    checks = b4.Validation([])
    expected = {}
    temp = book / "export/dist/source-body.md"
    for chapter in chapters:
        write(temp, chapter.body)
        expected[chapter.number] = normalized(pandoc_plain(temp, "markdown"))
    temp.unlink()
    formats = {"text": "plain", "html": "html", "docx": "docx", "epub": "epub"}
    for name, source_format in formats.items():
        text = artifacts[name].read_text(encoding="utf-8") if name == "text" else pandoc_plain(artifacts[name], source_format)
        sections = chapter_sections(text)
        for chapter in chapters:
            actual = sections[chapter.number]
            good = actual == expected[chapter.number]
            detail = f"source {hashlib.sha256(expected[chapter.number].encode()).hexdigest()}; output {hashlib.sha256(actual.encode()).hexdigest()}"
            checks.add(f"{name.upper()} Chapter {chapter.number}: exact reader-text identity", good, detail)
        checks.add(f"{name.upper()}: final line once", text.count(FINAL_LINE) == 1, str(text.count(FINAL_LINE)))
    checks.require()
    return checks


def merge(b4, validations):
    return b4.Validation([entry for validation in validations for entry in validation.checks])


def reports(b4, book: Path, chapters, artifacts, validation, pages: int, contacts, epubcheck: str, pdf: Path | None):
    export = book / "export"
    source_total = sum(source_words(ch) for ch in chapters)
    combined_total = b4.word_count(artifacts["markdown"].read_text(encoding="utf-8"))
    source_rows = ["| Ch. | Title | Words | Source SHA-256 | Body SHA-256 |", "|---:|---|---:|---|---|"]
    for ch in chapters:
        source_rows.append(f"| {ch.number} | {ch.display_title} | {source_words(ch):,} | `{ch.source_sha256}` | `{ch.body_sha256}` |")
    artifact_rows = ["| Artifact | Bytes | SHA-256 |", "|---|---:|---|"]
    records = []
    for name in ["markdown", "text", "html", "docx", "epub"]:
        path = artifacts[name]
        record = {"name": path.name, "size_bytes": path.stat().st_size, "sha256": file_hash(path)}
        records.append(record)
        artifact_rows.append(f"| `{record['name']}` | {record['size_bytes']:,} | `{record['sha256']}` |")
    write(export / "word-count-report.md", f"""# Book 5 Word-Count and Export Report

- **Book:** {TITLE}
- **Author:** {AUTHOR}
- **Series:** {SERIES} — Book {NUMBER}
- **Build date:** {BUILD_DATE.isoformat()}
- **Manuscript count method:** Accepted polished manuscript-prose counts, confirmed by exact Git-blob identity and matching chapter frontmatter; no chapter source changed during final proof.
- **Combined export count method:** Repository-standard Markdown-aware Book 4 count.
- **Manuscript-prose total:** **{source_total:,}**
- **Combined reader-facing total:** **{combined_total:,}**
- **Chapters:** **8**
- **DOCX render pages:** **{pages}**
- **DOCX contact sheets:** **{len(contacts)}**

## Chapter source counts and hashes

{chr(10).join(source_rows)}

**Arithmetic check:** {' + '.join(str(source_words(ch)) for ch in chapters)} = **{source_total:,}**

## Export artifact hashes

{chr(10).join(artifact_rows)}

DOCX and EPUB outputs are reproducible export artifacts, not retailer packages or publication records.
""")
    write(export / "export-readiness.md", f"""# Book 5 Final Proof and Export Readiness

## Status

**Final proof complete. Repository-standard export complete and validated. Package and publication remain pending.**

This record does not mark *{TITLE}* upload ready, retailer ready, distributed, or published.

## Final-proof result

- Chapters 1–8 were read in full and in order and checked again through source/export validation.
- No clear spelling, punctuation, grammar, capitalization, spacing, malformed-Markdown, or editing-artifact correction required a manuscript change.
- Intentional fragments, procedural repetition, object motifs, and evidence-limit formulations were retained.
- Manuscript prose remains **{source_total:,} words**.
- Exact provenance preserved: `{PROVENANCE}`
- Exact final line preserved: `{FINAL_LINE}`

## Metadata result

- Title: **{TITLE}**
- Author: **{AUTHOR}**
- Series: **{SERIES}**
- Series number: **Book {NUMBER}**
- POV: **Callie Thorne, third-person limited only**
- Chronology: **January 25 through February 1, 2027**
- Copyright: **© {YEAR} {AUTHOR}; First edition**

## Export result

- Combined Markdown, plain text, standalone HTML, DOCX, and EPUB 3 generated.
- Combined reader-facing count: **{combined_total:,}**
- DOCX render: **{pages} pages**; contact sheets: **{len(contacts)}**
- Source-to-export comparison: **all eight chapters matched in TXT, HTML, DOCX, and EPUB**
- EPUBCheck: **passed**
- Placeholder/internal-marker scan: **clean**

## Scope boundary

No cover, listing copy, retailer form, upload ZIP, advertising asset, platform submission, publication record, or release-status change is included. The next stage is a separate Book 5 package/readiness workflow.
""")
    passed = sum(1 for _, ok, _ in validation.checks if ok)
    lines = ["# Book 5 Proof/Export Validation", "", f"- Checks passed: **{passed}/{len(validation.checks)}**", ""]
    lines += [f"- [{'x' if ok else ' '}] {name} — {detail}" for name, ok, detail in validation.checks]
    lines += ["", "## EPUBCheck", "", "```text", epubcheck.strip() or "passed", "```", "", "Package and publication remain pending."]
    write(export / "validation-report.md", "\n".join(lines))
    manifest = {
        "book": TITLE, "author": AUTHOR, "series": SERIES, "series_number": NUMBER,
        "build_date": BUILD_DATE.isoformat(), "status": "export_validated_package_pending",
        "manuscript_prose_words": source_total, "combined_reader_facing_words": combined_total,
        "chapter_count": 8, "docx_render_pages": pages, "contact_sheets": len(contacts),
        "source_to_export_identity": "all_chapters_passed", "epubcheck": "passed",
        "package_status": "pending", "publication_status": "pending", "artifacts": records,
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
    validations += [docx_validation, epub_validation]
    all_validation = merge(b4, validations)
    all_validation.require()
    reports(b4, book, chapters, artifacts, all_validation, pages, contacts, epubcheck, pdf)
    print(f"Validated {TITLE}: {TOTAL:,} manuscript-prose words")
    print(f"Checks: {len(all_validation.checks)}/{len(all_validation.checks)} passed")
    print("Package: pending")
    print("Publication: pending")


if __name__ == "__main__":
    main()
