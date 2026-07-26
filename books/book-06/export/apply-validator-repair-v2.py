#!/usr/bin/env python3
"""Run the reviewed validator patch without altering its bootstrap files."""
from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PIPELINE = (ROOT / "books/book-06/export/finalize-package.py").resolve()
LEGACY = (ROOT / "books/book-06/export/apply-validator-repair.py").resolve()
WORKFLOW = (ROOT / ".github/workflows/book-06-proof-export.yml").resolve()

current = PIPELINE.read_text(encoding="utf-8")
if "SOURCE_BASE_SHA" in current and "def resolve_scope_base()" in current:
    print("Book 6 validator repair is already applied")
    raise SystemExit(0)

original_write_text = Path.write_text
original_unlink = Path.unlink


def guarded_write_text(path: Path, data: str, *args, **kwargs):
    if path.resolve() == WORKFLOW:
        print("Suppressed one-time workflow self-edit")
        return len(data)
    return original_write_text(path, data, *args, **kwargs)


def guarded_unlink(path: Path, *args, **kwargs):
    if path.resolve() == LEGACY:
        print("Suppressed one-time bootstrap self-delete")
        return None
    return original_unlink(path, *args, **kwargs)


Path.write_text = guarded_write_text
Path.unlink = guarded_unlink
try:
    runpy.run_path(str(LEGACY), run_name="__main__")
finally:
    Path.write_text = original_write_text
    Path.unlink = original_unlink

updated = PIPELINE.read_text(encoding="utf-8")
if "SOURCE_BASE_SHA" not in updated or "def resolve_scope_base()" not in updated:
    raise RuntimeError("Reviewed Book 6 validator repair did not apply")
print("Applied reviewed Book 6 validator repair")
