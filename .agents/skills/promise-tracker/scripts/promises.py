#!/usr/bin/env python3
"""Unified promise tracker: every setup the text makes, and whether it paid.

Tracks promises for both fiction and non-fiction. A "promise" is anything
the text tells the reader to remember (Chekhov's guns, unanswered questions,
thesis threads, promised counterarguments/definitions, "we'll return to this",
unresolved tensions, etc.).

    python3 scripts/promises.py                     whole ledger
    python3 scripts/promises.py --chapter ch12      due/overdue/paid here
    python3 scripts/promises.py --book Book-2       pick ledger explicitly
    python3 scripts/promises.py --final             gate finished book

Ledger lives at Wiki/Story/Book-N/promises.yaml; walks up from CWD to find Wiki/.
Exit status 1 under --final if anything unpaid and not deferred.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

WEIGHTS = {"whisper": 0, "plain": 1, "loud": 2}
LEDGER_REL = Path("Wiki") / "Story"


def chapter_number(value) -> int | None:
    """'ch12' / 12 / 'Chapter 12' / 'sec2.1' -> extract leading number if simple."""
    if value is None:
        return None
    text = str(value).strip().lower()
    # try to extract first integer
    digits = ""
    for c in text:
        if c.isdigit():
            digits += c
        elif digits:
            break
    return int(digits) if digits else None


def find_wiki_root() -> Path | None:
    for candidate in (Path.cwd(), *Path.cwd().parents):
        if (candidate / "Wiki").is_dir():
            return candidate
    return None


def find_ledger(root: Path, book: str | None) -> tuple[Path | None, str | None]:
    story = root / LEDGER_REL
    if book:
        path = story / book / "promises.yaml"
        return (path, None) if path.exists() else (None, f"no ledger at {path}")
    candidates = sorted(story.glob("Book-*/promises.yaml"))
    if not candidates:
        return None, ("no ledger found under Wiki/Story/Book-N/ — copy the skill's "
                      "assets/promises.yaml there to start tracking")
    if len(candidates) > 1:
        names = ", ".join(c.parent.name for c in candidates)
        return None, f"several ledgers found ({names}) — pass --book to pick one"
    return candidates[0], None


def load(ledger_path: Path) -> tuple[list[dict], str | None]:
    if yaml is None:
        return [], "PyYAML not importable; cannot read ledger"
    try:
        data = yaml.safe_load(ledger_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        return [], f"{ledger_path} could not be parsed: {exc}"
    promises = [p for p in (data.get("promises") or []) if isinstance(p, dict)]
    return [p for p in promises if str(p.get("promise") or "").strip()], None


def is_paid(promise: dict) -> bool:
    return bool(str(promise.get("paid_in_ch") or "").strip())


def is_deferred(promise: dict) -> bool:
    return bool(promise.get("deferred_to_series"))


def status(promise: dict, current: int | None) -> str:
    if is_paid(promise):
        return "paid"
    if is_deferred(promise):
        return "deferred"
    due = chapter_number(promise.get("payoff_by_ch"))
    if due is None:
        return "undated"
    if current is None:
        return "open"
    if due < current:
        return "overdue"
    if due == current:
        return "due"
    if due - current <= 1:
        return "due soon"
    return "open"


def describe(promise: dict) -> str:
    ident = str(promise.get("id") or "?")
    text = str(promise.get("promise") or "").strip()
    kind = str(promise.get("kind") or "").strip()
    ptype = str(promise.get("project_type") or "").strip()

    def chref(value: object, fallback: str) -> str:
        t = str(value or "").strip()
        return t if t else fallback

    where = chref(promise.get("introduced_ch"), "unknown")
    due = chref(promise.get("payoff_by_ch"), "no deadline")
    weight = str(promise.get("weight") or "plain")
    tag = f"/{ptype}" if ptype else ""
    return (f"{ident} [{kind or 'promise'}{tag}/{weight}] {text[:80]}\n"
            f"       made {where} · owed by {due}")


def report(promises: list[dict], current: int | None) -> str:
    if not promises:
        return ("Promise tracker — empty.\n"
                "  Nothing tracked. Every setup creating reader expectation is currently\n"
                "  unbooked; harvest from the text to populate the ledger.")
    buckets: dict[str, list[dict]] = {}
    for promise in promises:
        buckets.setdefault(status(promise, current), []).append(promise)
    paid = len(buckets.get("paid", []))
    out = [f"Promise tracker — {len(promises)} promise(s), {paid} paid"]
    for key, label in (
        ("overdue", "OVERDUE — reader already owed this"),
        ("due", "DUE THIS UNIT"),
        ("due soon", "DUE SOON (next unit)"),
        ("undated", "NO DEADLINE — will be forgotten"),
        ("open", "OPEN"),
        ("deferred", "DEFERRED TO LATER VOLUME"),
    ):
        items = buckets.get(key) or []
        if not items:
            continue
        items.sort(key=lambda p: -WEIGHTS.get(str(p.get("weight")), 1))
        out.append(f"\n  {label} ({len(items)}):")
        out += [f"    {describe(p)}" for p in items]
    if buckets.get("deferred"):
        out.append("\n  Deferred promises must appear in the series/inter-book promise map\n"
                   "  (e.g. Wiki/Story/series-arc.md) if tracked there.")
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--chapter", help="evaluate as of this unit (e.g. ch12, sec3.2)")
    parser.add_argument("--book", help="book folder name (default: only ledger found)")
    parser.add_argument("--ledger", type=Path, help="explicit path to promises.yaml")
    parser.add_argument("--final", action="store_true",
                        help="exit 1 if any promise unpaid and not deferred")
    args = parser.parse_args()

    root = find_wiki_root()
    if args.ledger:
        ledger_path = args.ledger
        problem = None if ledger_path.exists() else f"no ledger at {ledger_path}"
    elif root is None:
        ledger_path, problem = None, "no Wiki/ found above working directory"
    else:
        ledger_path, problem = find_ledger(root, args.book)

    if problem:
        print(f"Promise tracker — {problem}.")
        raise SystemExit(0 if not args.final else 1)

    promises, problem = load(ledger_path)
    current = chapter_number(args.chapter) if args.chapter else None

    if args.final:
        if problem:
            print(f"Promise tracker unavailable ({problem}) — cannot certify final.")
            raise SystemExit(1)
        outstanding = [p for p in promises if not is_paid(p) and not is_deferred(p)]
        if outstanding:
            print(f"{len(outstanding)} promise(s) unpaid — not finished:")
            for p in outstanding:
                print(f"  {describe(p)}")
            print("\nPay them, mark deferred_to_series true (with series map), or record ruling in notes.")
            raise SystemExit(1)
        print(f"All {len(promises)} promise(s) paid or deliberately deferred.")
        return

    if problem:
        print(f"Promise tracker — {problem}.")
        return
    print(report(promises, current))


if __name__ == "__main__":
    main()
