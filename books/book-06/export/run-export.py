#!/usr/bin/env python3
"""Run the Book 6 export with inherited validation and reproducibility fixes."""
from __future__ import annotations

import importlib.util
import re
import sys
import uuid
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
PIPELINE = HERE / "finalize-package.py"
FIXED_ZIP_TIME = (2026, 7, 15, 0, 0, 0)
FIXED_ISO_TIME = "2026-07-15T00:00:00Z"
FIXED_EPUB_UUID = str(
    uuid.uuid5(
        uuid.NAMESPACE_URL,
        "urn:blackwood-ridge:book-6:the-pattern:vesper-blythe",
    )
)
DOCX_STATUS = (
    "Controlled export review manuscript; package, cover, listing, upload, "
    "and publication pending."
)


def load_pipeline():
    spec = importlib.util.spec_from_file_location("book6_export_pipeline", PIPELINE)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {PIPELINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rewrite_archive(path: Path, transforms, epub: bool = False) -> None:
    """Rewrite a ZIP container with fixed metadata and deterministic ordering."""
    temporary = path.with_suffix(path.suffix + ".deterministic")
    with ZipFile(path, "r") as source:
        entries = source.infolist()
        if epub:
            entries = sorted(entries, key=lambda item: (item.filename != "mimetype", item.filename))
        else:
            entries = sorted(entries, key=lambda item: item.filename)

        with ZipFile(temporary, "w") as target:
            for original in entries:
                data = source.read(original.filename)
                transform = transforms.get(original.filename)
                if transform:
                    data = transform(data)

                info = ZipInfo(original.filename, FIXED_ZIP_TIME)
                info.create_system = original.create_system
                info.external_attr = original.external_attr
                info.internal_attr = original.internal_attr
                info.comment = original.comment
                info.extra = b""
                compression = ZIP_STORED if epub and original.filename == "mimetype" else ZIP_DEFLATED
                info.compress_type = compression
                target.writestr(info, data, compress_type=compression, compresslevel=9)
    temporary.replace(path)


def normalize_docx(path: Path) -> None:
    def core_xml(data: bytes) -> bytes:
        text = data.decode("utf-8")
        text = re.sub(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", FIXED_ISO_TIME, text)
        status = re.escape(DOCX_STATUS)
        if re.search(r"<dc:description>.*?</dc:description>", text):
            text = re.sub(
                r"<dc:description>.*?</dc:description>",
                f"<dc:description>{DOCX_STATUS}</dc:description>",
                text,
            )
        elif "</cp:coreProperties>" in text:
            text = text.replace(
                "</cp:coreProperties>",
                f"<dc:description>{DOCX_STATUS}</dc:description></cp:coreProperties>",
            )
        if not re.search(status, text):
            raise RuntimeError("DOCX controlled-status metadata was not written")
        return text.encode("utf-8")

    rewrite_archive(path, {"docProps/core.xml": core_xml})


def normalize_epub(path: Path) -> None:
    def identifier_xml(data: bytes) -> bytes:
        text = data.decode("utf-8")
        text = re.sub(r"urn:uuid:[0-9a-fA-F-]+", f"urn:uuid:{FIXED_EPUB_UUID}", text)
        text = re.sub(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", FIXED_ISO_TIME, text)
        return text.encode("utf-8")

    rewrite_archive(
        path,
        {
            "EPUB/content.opf": identifier_xml,
            "EPUB/toc.ncx": identifier_xml,
        },
        epub=True,
    )


def ensure_html_author_metadata(path: Path) -> None:
    """Preserve the approved author metadata in the standalone HTML export."""
    text = path.read_text(encoding="utf-8")
    author_meta = '  <meta name="author" content="Vesper Blythe" />\n'
    if author_meta in text:
        return
    viewport_meta = (
        '  <meta name="viewport" content="width=device-width, '
        'initial-scale=1.0, user-scalable=yes" />\n'
    )
    if viewport_meta not in text:
        raise RuntimeError("HTML viewport metadata anchor was not found")
    path.write_text(text.replace(viewport_meta, viewport_meta + author_meta, 1), encoding="utf-8")


def main() -> None:
    pipeline = load_pipeline()
    original_load_book4 = pipeline.load_book4
    original_build = pipeline.build

    def deterministic_build(book4, book: Path, combined: Path, chapters):
        artifacts = original_build(book4, book, combined, chapters)
        ensure_html_author_metadata(artifacts["html"])
        normalize_docx(artifacts["docx"])
        normalize_epub(artifacts["epub"])
        return artifacts

    def load_book4_with_corrected_docx_check(root: Path):
        book4 = original_load_book4(root)
        original_strip_yaml = book4.strip_yaml_and_heading
        original_validate_docx = book4.validate_docx

        def strip_yaml_and_heading(source: str, expected_number: int, expected_title: str):
            """Adapt the Book 4 title-only loader to Book 6's full source headings."""
            full_heading = expected_title
            if not full_heading.startswith(f"Chapter {expected_number} — "):
                full_heading = f"Chapter {expected_number} — {expected_title}"
            return original_strip_yaml(source, expected_number, full_heading)

        def validate_docx(docx_path: Path, qa_dir: Path):
            try:
                result = original_validate_docx(docx_path, qa_dir)
            except RuntimeError as exc:
                message = str(exc)
                known = "DOCX render: no broken replacement characters"
                failures = [line for line in message.splitlines() if line.startswith("- ")]
                if len(failures) != 1 or known not in failures[0]:
                    raise

                # The inherited Book 4 check uses an empty-string sentinel.
                # Preserve all other checks and replace only that sentinel with
                # the intended Unicode replacement-character test.
                pdf_path = qa_dir / "docx-render" / f"{docx_path.stem}.pdf"
                reader = book4.PdfReader(str(pdf_path))
                page_texts = [(page.extract_text() or "") for page in reader.pages]
                replacement_pages = [
                    index + 1 for index, text in enumerate(page_texts) if "�" in text
                ]
                page_pngs = sorted((qa_dir / "docx-pages").glob("page-*.png"))
                contacts = sorted((qa_dir / "contact-sheets").glob("*.png"))

                validation = book4.Validation([])
                validation.add(
                    "DOCX: inherited Book 4 structural and render checks",
                    True,
                    "all checks passed except the known empty-string sentinel defect",
                )
                validation.add(
                    "DOCX render: no broken replacement characters",
                    not replacement_pages,
                    repr(replacement_pages),
                )
                validation.add(
                    "DOCX render: every page rendered",
                    len(page_pngs) == len(reader.pages),
                    f"{len(page_pngs)} PNGs for {len(reader.pages)} pages",
                )
                validation.add(
                    "DOCX render: contact sheets created",
                    bool(contacts),
                    f"{len(contacts)} sheets",
                )
                validation.require()
                result = validation, len(reader.pages), contacts, pdf_path

            with ZipFile(docx_path, "r") as archive:
                core = archive.read("docProps/core.xml").decode("utf-8")
            if DOCX_STATUS not in core:
                raise RuntimeError("DOCX controlled-status metadata is missing")
            return result

        book4.strip_yaml_and_heading = strip_yaml_and_heading
        book4.validate_docx = validate_docx
        return book4

    pipeline.build = deterministic_build
    pipeline.load_book4 = load_book4_with_corrected_docx_check
    pipeline.main()


if __name__ == "__main__":
    main()
