#!/usr/bin/env python3
"""Authorize Book 7 drafting diffs for the Book 6 controlled-export workflow.

The Book 6 exporter retains its own historical-source and protected-scope checks.
This preflight grants a narrow current-diff override only when the pull request is
unambiguously Book 7 manuscript drafting and contains no Book 6-authority change.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Sequence

BOOK7_MANUSCRIPT_RE = re.compile(r"^books/book-07/manuscript/ch-\d+\.md$")
BOOK7_MISSION_LOCK_RE = re.compile(r"^books/book-07/control/chapter-\d+-mission-lock\.md$")
BOOK3_WORKFLOW_RE = re.compile(r"^\.github/workflows/book-03")
ALLOWED_BOOK7_CONTROL_PATHS = {
    "books/book-07/README.md",
    "books/book-07/progress.yaml",
    "books/book-07/manuscript/README.md",
    "books/book-07/bible/story-memory.md",
    "progress.yaml",
    "series-outline.md",
}
PROTECTED_STEMS = (
    "package",
    "cover",
    "listing",
    "upload",
    "publication",
    "publish",
    "release",
    "retailer",
    "advertising",
    "distribution",
)


def run(cmd: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(cmd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def resolve_scope_base() -> tuple[str, str]:
    explicit = os.environ.get("BOOK6_SCOPE_BASE_REF")
    if explicit:
        candidates = [explicit]
    else:
        candidates: list[str] = []
        github_base = os.environ.get("GITHUB_BASE_REF")
        if github_base:
            candidates.extend([f"origin/{github_base}", github_base])
        candidates.extend(["origin/main", "main"])

    attempted: list[str] = []
    for candidate in dict.fromkeys(candidates):
        result = run(["git", "merge-base", candidate, "HEAD"])
        merge_base = result.stdout.strip()
        attempted.append(f"{candidate}: {result.returncode}")
        if result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", merge_base):
            return candidate, merge_base
    raise RuntimeError(
        f"Unable to resolve current change-scope base ({'; '.join(attempted)})"
    )


def changed_paths(merge_base: str) -> list[str]:
    result = run(["git", "diff", "--name-only", f"{merge_base}...HEAD"])
    if result.returncode:
        raise RuntimeError(result.stdout.strip() or "git diff failed")
    return sorted({line.strip() for line in result.stdout.splitlines() if line.strip()})


def is_production_asset(path: str) -> bool:
    if not re.match(r"^books/book-\d+/", path):
        return False
    return any(
        part.lower().startswith(PROTECTED_STEMS)
        for part in Path(path).parts[2:]
    )


def is_allowed_book7_authoring_path(path: str) -> bool:
    return (
        bool(BOOK7_MANUSCRIPT_RE.fullmatch(path))
        or bool(BOOK7_MISSION_LOCK_RE.fullmatch(path))
        or path in ALLOWED_BOOK7_CONTROL_PATHS
    )


def classify_scope(changed: list[str]) -> str:
    book7_manuscript = [path for path in changed if BOOK7_MANUSCRIPT_RE.fullmatch(path)]
    if not book7_manuscript:
        return "book6_validation"

    violations: list[str] = []
    violations.extend(path for path in changed if path.startswith("books/book-05/"))
    violations.extend(path for path in changed if path.startswith("books/book-06/"))
    violations.extend(path for path in changed if path.startswith("books/book-08/"))
    violations.extend(path for path in changed if BOOK3_WORKFLOW_RE.match(path))
    violations.extend(path for path in changed if is_production_asset(path))
    violations.extend(path for path in changed if not is_allowed_book7_authoring_path(path))

    if violations:
        unique = sorted(set(violations))
        raise RuntimeError(
            "Book 7 manuscript changes cannot be authorized with mixed or protected "
            f"scope: {unique}"
        )
    return "authorized_book7_drafting"


def write_github_env(name: str, value: str) -> None:
    env_path = os.environ.get("GITHUB_ENV")
    if not env_path:
        return
    with open(env_path, "a", encoding="utf-8") as handle:
        handle.write(f"{name}={value}\n")


def main() -> int:
    try:
        scope_ref, merge_base = resolve_scope_base()
        changed = changed_paths(merge_base)
        mode = classify_scope(changed)
    except RuntimeError as exc:
        print(f"Book 6 scope authorization failed closed: {exc}", file=sys.stderr)
        return 1

    print(f"Book 6 scope base: {scope_ref} -> {merge_base}")
    print(f"Book 6 workflow authority mode: {mode}")
    print(f"Changed paths: {changed or ['none']}")

    write_github_env("BOOK6_AUTHORITY_MODE", mode)
    if mode == "authorized_book7_drafting":
        # The preflight has validated the real current-base diff. Point the legacy
        # exporter scope comparison at HEAD so it validates Book 6 source/export
        # identity without falsely claiming authority over the authorized Book 7 file.
        write_github_env("BOOK6_SCOPE_BASE_REF", "HEAD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
