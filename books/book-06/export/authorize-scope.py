#!/usr/bin/env python3
"""Authorize one evidence-backed Book 7 chapter addition in Book 6 CI.

The Book 6 exporter retains the fixed historical source baseline and its complete
protected-scope validation. This preflight may suppress only the legacy false
positive for one positively proven, sequential Book 7 drafting change.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

BOOK7_MANUSCRIPT_RE = re.compile(r"^books/book-07/manuscript/ch-(\d{2})\.md$")
BOOK7_MISSION_LOCK_RE = re.compile(
    r"^books/book-07/control/chapter-(\d{2})-mission-lock\.md$"
)
LOCKED_MISSION_MARKER = "LOCKED FOR FIRST-DRAFT PRODUCTION"
ALLOWED_BOOK7_LIFECYCLE_PATHS = {
    "books/book-07/README.md",
    "books/book-07/bible/story-memory.md",
    "books/book-07/manuscript/README.md",
    "books/book-07/progress.yaml",
    "progress.yaml",
    "series-outline.md",
}


@dataclass(frozen=True)
class Change:
    """One unambiguous record from ``git diff --name-status -z``."""

    status: str
    path: str
    old_path: str | None = None

    @property
    def kind(self) -> str:
        return self.status[:1]

    def all_paths(self) -> tuple[str, ...]:
        return (self.old_path, self.path) if self.old_path else (self.path,)


def run_text(cmd: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(cmd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def run_bytes(cmd: Sequence[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        list(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def decode_git_path(raw: bytes) -> str:
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError("Git returned a non-UTF-8 repository path") from exc


def resolve_scope_base() -> tuple[str, str]:
    """Resolve a real commit and merge base; incomplete history fails closed."""
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
        resolved = run_text(["git", "rev-parse", "--verify", f"{candidate}^{{commit}}"])
        candidate_sha = resolved.stdout.strip()
        if resolved.returncode or not re.fullmatch(r"[0-9a-f]{40}", candidate_sha):
            attempted.append(f"{candidate}: unresolved")
            continue

        result = run_text(["git", "merge-base", candidate_sha, "HEAD"])
        merge_base = result.stdout.strip()
        attempted.append(f"{candidate}: merge-base {result.returncode}")
        if result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", merge_base):
            return candidate, merge_base

    raise RuntimeError(
        "Unable to resolve a complete current change-scope base "
        f"({'; '.join(attempted) or 'no candidates'})"
    )


def parse_name_status_z(raw: bytes) -> list[Change]:
    """Parse NUL-delimited Git status records without whitespace ambiguity."""
    fields = raw.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()

    changes: list[Change] = []
    index = 0
    while index < len(fields):
        try:
            status = fields[index].decode("ascii")
        except UnicodeDecodeError as exc:
            raise RuntimeError("Git returned a non-ASCII change status") from exc
        index += 1
        if not re.fullmatch(r"[ACDMRTUXB][0-9]*", status):
            raise RuntimeError(f"Unrecognized Git change status: {status!r}")

        if status[0] in {"R", "C"}:
            if index + 1 >= len(fields):
                raise RuntimeError(f"Incomplete Git {status[0]} record")
            old_path = decode_git_path(fields[index])
            path = decode_git_path(fields[index + 1])
            index += 2
            changes.append(Change(status=status, old_path=old_path, path=path))
        else:
            if index >= len(fields):
                raise RuntimeError(f"Incomplete Git {status[0]} record")
            path = decode_git_path(fields[index])
            index += 1
            changes.append(Change(status=status, path=path))

    return changes


def changed_records(merge_base: str) -> list[Change]:
    result = run_bytes(
        [
            "git",
            "diff",
            "--name-status",
            "-z",
            "--find-renames=50%",
            "--find-copies=50%",
            "--find-copies-harder",
            f"{merge_base}...HEAD",
        ]
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).decode("utf-8", "replace").strip()
        raise RuntimeError(detail or "git diff --name-status failed")
    return parse_name_status_z(result.stdout)


def path_exists_at(commit: str, path: str) -> bool:
    return run_bytes(["git", "cat-file", "-e", f"{commit}:{path}"]).returncode == 0


def read_path_at(commit: str, path: str) -> str:
    result = run_bytes(["git", "show", f"{commit}:{path}"])
    if result.returncode:
        detail = (result.stderr or result.stdout).decode("utf-8", "replace").strip()
        raise RuntimeError(f"Unable to read {path} at {commit}: {detail}")
    try:
        return result.stdout.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"Authorized text path is not UTF-8: {path}") from exc


def blob_oid(commit: str, path: str) -> str:
    result = run_text(["git", "rev-parse", "--verify", f"{commit}:{path}"])
    value = result.stdout.strip()
    if result.returncode or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise RuntimeError(f"Unable to resolve blob identity for {path} at {commit}")
    return value


def base_book7_chapters(merge_base: str) -> list[tuple[int, str]]:
    result = run_bytes(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            "-z",
            merge_base,
            "--",
            "books/book-07/manuscript",
        ]
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).decode("utf-8", "replace").strip()
        raise RuntimeError(detail or "Unable to inspect base Book 7 manuscript inventory")

    chapters: list[tuple[int, str]] = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        path = decode_git_path(raw)
        match = BOOK7_MANUSCRIPT_RE.fullmatch(path)
        if match:
            chapters.append((int(match.group(1)), path))
    chapters.sort()
    return chapters


def touches(pattern: re.Pattern[str], change: Change) -> bool:
    return any(path is not None and pattern.fullmatch(path) for path in change.all_paths())


def describe(change: Change) -> str:
    if change.old_path:
        return f"{change.status} {change.old_path!r} -> {change.path!r}"
    return f"{change.status} {change.path!r}"


def classify_scope(root: Path, merge_base: str, changes: list[Change]) -> str:
    """Return normal validation or prove one narrowly authorized draft addition."""
    manuscript_changes = [
        change for change in changes if touches(BOOK7_MANUSCRIPT_RE, change)
    ]
    if not manuscript_changes:
        return "book6_validation"

    if len(manuscript_changes) != 1:
        raise RuntimeError(
            "Authorized drafting requires exactly one Book 7 manuscript change; got "
            + repr([describe(change) for change in manuscript_changes])
        )

    manuscript = manuscript_changes[0]
    match = BOOK7_MANUSCRIPT_RE.fullmatch(manuscript.path)
    if manuscript.status != "A" or manuscript.old_path is not None or not match:
        raise RuntimeError(
            "The Book 7 manuscript must be one genuinely added chapter (status A): "
            + describe(manuscript)
        )
    chapter = int(match.group(1))

    if path_exists_at(merge_base, manuscript.path):
        raise RuntimeError(f"New chapter path already exists at the current base: {manuscript.path}")
    if not path_exists_at("HEAD", manuscript.path):
        raise RuntimeError(f"New chapter path is absent at HEAD: {manuscript.path}")

    base_chapters = base_book7_chapters(merge_base)
    numbers = [number for number, _ in base_chapters]
    expected_inventory = list(range(1, max(numbers, default=0) + 1))
    if numbers != expected_inventory:
        raise RuntimeError(
            f"Base Book 7 chapter inventory is incomplete or ambiguous: {numbers}"
        )
    expected_chapter = max(numbers, default=0) + 1
    if chapter != expected_chapter:
        raise RuntimeError(
            f"Authorized drafting must add sequential Chapter {expected_chapter:02d}; "
            f"got Chapter {chapter:02d}"
        )

    new_blob = blob_oid("HEAD", manuscript.path)
    copied_from = [
        path for _, path in base_chapters if blob_oid(merge_base, path) == new_blob
    ]
    if copied_from:
        raise RuntimeError(
            f"New chapter duplicates an existing Book 7 manuscript blob: {copied_from}"
        )

    mission_changes = [
        change for change in changes if touches(BOOK7_MISSION_LOCK_RE, change)
    ]
    expected_mission = (
        f"books/book-07/control/chapter-{chapter:02d}-mission-lock.md"
    )
    if len(mission_changes) != 1:
        raise RuntimeError(
            "Authorized drafting requires exactly one matching mission-lock change; got "
            + repr([describe(change) for change in mission_changes])
        )
    mission = mission_changes[0]
    mission_is_new = mission.status == "A" and mission.old_path is None
    mission_is_template_copy = (
        mission.kind == "C"
        and mission.old_path is not None
        and BOOK7_MISSION_LOCK_RE.fullmatch(mission.old_path) is not None
    )
    if mission.path != expected_mission or not (mission_is_new or mission_is_template_copy):
        raise RuntimeError(
            f"Chapter {chapter:02d} requires a newly created matching mission lock "
            f"at {expected_mission}; got " + describe(mission)
        )
    if path_exists_at(merge_base, mission.path):
        raise RuntimeError(f"Mission lock already exists at the current base: {mission.path}")
    mission_text = read_path_at("HEAD", mission.path)
    if LOCKED_MISSION_MARKER not in mission_text:
        raise RuntimeError(
            f"Mission lock lacks required authorized state {LOCKED_MISSION_MARKER!r}: "
            f"{mission.path}"
        )

    violations: list[str] = []
    for change in changes:
        if change == manuscript or change == mission:
            continue
        if (
            change.status == "M"
            and change.old_path is None
            and change.path in ALLOWED_BOOK7_LIFECYCLE_PATHS
            and path_exists_at(merge_base, change.path)
            and path_exists_at("HEAD", change.path)
        ):
            continue
        violations.append(describe(change))

    if violations:
        raise RuntimeError(
            "Book 7 drafting contains mixed, protected, non-precedent, or invalid-status "
            f"scope: {violations}"
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
        changes = changed_records(merge_base)
        mode = classify_scope(Path.cwd(), merge_base, changes)
    except RuntimeError as exc:
        print(f"Book 6 scope authorization failed closed: {exc}", file=sys.stderr)
        return 1

    print(f"Book 6 scope base: {scope_ref} -> {merge_base}")
    print(f"Book 6 workflow authority mode: {mode}")
    print("Changed records:")
    if changes:
        for change in changes:
            print(f"- {describe(change)}")
    else:
        print("- none")

    # Environment authority is written only after the real Git comparison and all
    # positive drafting evidence have passed.
    write_github_env("BOOK6_AUTHORITY_MODE", mode)
    if mode == "authorized_book7_drafting":
        write_github_env("BOOK6_SCOPE_BASE_REF", "HEAD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
