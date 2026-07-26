#!/usr/bin/env python3
"""Regression tests for Book 6 export scope validation."""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPELINE = HERE / "finalize-package.py"
HISTORICAL_SOURCE_BASE = "d23d2e745ea0a5fda414321b6c82eda427459a87"


class Validation:
    def __init__(self, checks):
        self.checks = list(checks)

    def add(self, name: str, passed: bool, detail: str) -> None:
        self.checks.append((name, passed, detail))

    def require(self) -> None:
        failures = [f"{name}: {detail}" for name, passed, detail in self.checks if not passed]
        if failures:
            raise RuntimeError("\n".join(failures))


class Book4Stub:
    Validation = Validation


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{result.stdout}")
    return result.stdout.strip()


@contextmanager
def working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


@contextmanager
def scope_environment(value: str | None = "main"):
    previous_explicit = os.environ.get("BOOK6_SCOPE_BASE_REF")
    previous_github = os.environ.get("GITHUB_BASE_REF")
    try:
        if value is None:
            os.environ.pop("BOOK6_SCOPE_BASE_REF", None)
            os.environ.pop("GITHUB_BASE_REF", None)
        else:
            os.environ["BOOK6_SCOPE_BASE_REF"] = value
            os.environ.pop("GITHUB_BASE_REF", None)
        yield
    finally:
        if previous_explicit is None:
            os.environ.pop("BOOK6_SCOPE_BASE_REF", None)
        else:
            os.environ["BOOK6_SCOPE_BASE_REF"] = previous_explicit
        if previous_github is None:
            os.environ.pop("GITHUB_BASE_REF", None)
        else:
            os.environ["GITHUB_BASE_REF"] = previous_github


def load_pipeline():
    spec = importlib.util.spec_from_file_location("book6_scope_test_pipeline", PIPELINE)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {PIPELINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_repo(changed_path: str) -> tuple[Path, tempfile.TemporaryDirectory[str], str]:
    holder = tempfile.TemporaryDirectory()
    repo = Path(holder.name)
    git(repo, "init", "-b", "main")
    git(repo, "config", "user.name", "Scope Test")
    git(repo, "config", "user.email", "scope@example.invalid")

    baseline_files = {
        "books/book-05/README.md": "Book 5 baseline\n",
        "books/book-06/manuscript/ch-01.md": "Book 6 manuscript baseline\n",
        "books/book-06/export/finalize-package.py": "validator baseline\n",
        "books/book-07/manuscript/ch-01.md": "lawful existing Book 7 prose\n",
        "books/book-08/outline.md": "Book 8 protected baseline\n",
    }
    for relative, content in baseline_files.items():
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "baseline")
    baseline_sha = git(repo, "rev-parse", "HEAD")
    git(repo, "checkout", "-b", "repair")

    target = repo / changed_path
    target.parent.mkdir(parents=True, exist_ok=True)
    prior = target.read_text(encoding="utf-8") if target.exists() else ""
    target.write_text(prior + "repair change\n", encoding="utf-8")
    git(repo, "add", changed_path)
    git(repo, "commit", "-m", "repair")
    return repo, holder, baseline_sha


class ScopeValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.pipeline = load_pipeline()

    def test_historical_source_baseline_remains_fixed(self) -> None:
        self.assertEqual(self.pipeline.SOURCE_BASE_SHA, HISTORICAL_SOURCE_BASE)

    def test_existing_book7_prose_is_allowed_when_unchanged(self) -> None:
        repo, holder, baseline_sha = make_repo("books/book-06/export/finalize-package.py")
        self.addCleanup(holder.cleanup)
        with working_directory(repo), scope_environment("main"):
            validation, scope_base_sha, changed = self.pipeline.scope_validation(Book4Stub, repo)
        self.assertEqual(scope_base_sha, baseline_sha)
        self.assertNotEqual(scope_base_sha, self.pipeline.SOURCE_BASE_SHA)
        self.assertEqual(changed, ["books/book-06/export/finalize-package.py"])
        self.assertTrue(all(passed for _, passed, _ in validation.checks))

    def test_github_base_ref_selects_current_pull_request_base(self) -> None:
        repo, holder, baseline_sha = make_repo("books/book-06/export/finalize-package.py")
        self.addCleanup(holder.cleanup)
        with working_directory(repo), scope_environment(None):
            os.environ["GITHUB_BASE_REF"] = "main"
            validation, scope_base_sha, _ = self.pipeline.scope_validation(Book4Stub, repo)
        self.assertEqual(scope_base_sha, baseline_sha)
        self.assertTrue(all(passed for _, passed, _ in validation.checks))

    def test_scope_violations_fail_closed(self) -> None:
        prohibited_paths = [
            "books/book-05/README.md",
            "books/book-06/manuscript/ch-01.md",
            "books/book-07/manuscript/ch-01.md",
            "books/book-08/outline.md",
            "books/book-06/package/metadata.md",
            "books/book-03/package/approved/The-Challenger-cover.jpg",
        ]
        for changed_path in prohibited_paths:
            with self.subTest(changed_path=changed_path):
                repo, holder, _ = make_repo(changed_path)
                try:
                    with working_directory(repo), scope_environment("main"):
                        with self.assertRaises(RuntimeError):
                            self.pipeline.scope_validation(Book4Stub, repo)
                finally:
                    holder.cleanup()

    def test_missing_explicit_scope_base_fails_closed(self) -> None:
        repo, holder, _ = make_repo("books/book-06/export/finalize-package.py")
        self.addCleanup(holder.cleanup)
        with working_directory(repo), scope_environment("missing-base"):
            with self.assertRaises(RuntimeError):
                self.pipeline.scope_validation(Book4Stub, repo)


if __name__ == "__main__":
    unittest.main()
