#!/usr/bin/env python3
"""Run the Book 5 export with a scoped fix for a Book 4 validator defect."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPELINE = HERE / "finalize-package.py"


def load_pipeline():
    spec = importlib.util.spec_from_file_location("book5_export_pipeline", PIPELINE)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {PIPELINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    pipeline = load_pipeline()
    original_load_book4 = pipeline.load_book4

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

    pipeline.load_book4 = load_book4_with_corrected_docx_check
    pipeline.main()


if __name__ == "__main__":
    main()
