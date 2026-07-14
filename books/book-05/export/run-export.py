#!/usr/bin/env python3
"""Run the Book 5 export with scoped validation and reproducibility fixes."""
from __future__ import annotations

import importlib.util
import re
import sys
import uuid
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
PIPELINE = HERE / "finalize-package.py"
FIXED_ZIP_TIME = (2026, 7, 13, 0, 0, 0)
FIXED_ISO_TIME = "2026-07-13T00:00:00Z"
FIXED_EPUB_UUID = str(
    uuid.uuid5(
        uuid.NAMESPACE_URL,
        "urn:blackwood-ridge:book-5:the-planted-page:vesper-blythe",
    )
)


def load_pipeline():
    spec = importlib.util.spec_from_file_location("book5_export_pipeline", PIPELINE)
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
        text = re.sub(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
            FIXED_ISO_TIME,
            text,
        )
        return text.encode("utf-8")

    rewrite_archive(path, {"docProps/core.xml": core_xml})


def normalize_epub(path: Path) -> None:
    def content_opf(data: bytes) -> bytes:
        text = data.decode("utf-8")
        text = re.sub(r"urn:uuid:[0-9a-fA-F-]+", f"urn:uuid:{FIXED_EPUB_UUID}", text)
        text = re.sub(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
            FIXED_ISO_TIME,
            text,
        )
        return text.encode("utf-8")

    rewrite_archive(path, {"EPUB/content.opf": content_opf}, epub=True)


def main() -> None:
    pipeline = load_pipeline()
    original_load_book4 = pipeline.load_book4
    original_build = pipeline.build

    def deterministic_build(book4, book: Path, combined: Path, chapters):
        artifacts = original_build(book4, book, combined, chapters)
        normalize_docx(artifacts["docx"])
        normalize_epub(artifacts["epub"])
        return artifacts

    def load_book4_with_corrected_docx_check(root: Path):
        book4 = original_load_book4(root)
        original_validate_docx = book4.validate_docx

        def validate_docx(docx_path: Path, qa_dir: Path):
            try:
                return original_validate_docx(docx_path, qa_dir)
            except RuntimeError as exc:
                message = str(exc)
                known = "DOCX render: no broken replacement characters"
                failures = [line for line in message.splitlines() if line.startswith("- ")]
                if len(failures) != 1 or known not in failures[0]:
                    raise

                # Book 4 currently tests `if "" in text`, which is always true.
                # Preserve every other Book 4 DOCX check and replace only that
                # sentinel with the intended Unicode replacement-character test.
                pdf_path = qa_dir / "docx-render" / f"{docx_path.stem}.pdf"
                reader = book4.PdfReader(str(pdf_path))
                page_texts = [(page.extract_text() or "") for page in reader.pages]
                replacement_pages = [
                    index + 1 for index, text in enumerate(page_texts) if "\ufffd" in text
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
                return validation, len(reader.pages), contacts, pdf_path

        book4.validate_docx = validate_docx
        return book4

    pipeline.build = deterministic_build
    pipeline.load_book4 = load_book4_with_corrected_docx_check
    pipeline.main()


if __name__ == "__main__":
    main()
