#!/usr/bin/env python3
"""Run the fail-closed Book 6 retailer package build."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPELINE = HERE / "release-package.py"


def main() -> None:
    spec = importlib.util.spec_from_file_location("book6_release_pipeline", PIPELINE)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {PIPELINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.main()


if __name__ == "__main__":
    main()
