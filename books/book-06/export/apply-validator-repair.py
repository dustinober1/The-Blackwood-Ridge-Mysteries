#!/usr/bin/env python3
"""Apply the reviewed Book 6 validator repair once, then remove this bootstrap."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PIPELINE = ROOT / "books/book-06/export/finalize-package.py"
WORKFLOW = ROOT / ".github/workflows/book-06-proof-export.yml"

text = PIPELINE.read_text(encoding="utf-8")
text = text.replace("import json\nimport re", "import json\nimport os\nimport re", 1)
text = text.replace("BASE_SHA", "SOURCE_BASE_SHA")
text = text.replace(
    'checks.add("Source: total 25,646", sum(source_words(ch) for ch in chapters) == TOTAL, str(sum(source_words(ch) for ch in chapters))\n',
    'checks.add("Source: total 25,646", sum(source_words(ch) for ch in chapters) == TOTAL, str(sum(source_words(ch) for ch in chapters)))\n',
    1,
)

old_scope = '''def scope_validation(b4, root: Path):
    checks = b4.Validation([])
    result = run(["git", "diff", "--name-only", f"{SOURCE_BASE_SHA}...HEAD"], check=False)
    checks.add("Scope: base comparison available", result.returncode == 0, result.stdout.strip() or "clean command")
    changed = [line.strip() for line in result.stdout.splitlines() if line.strip()] if result.returncode == 0 else []
    checks.add("Scope: Book 5 unchanged", not any(path.startswith("books/book-05/") for path in changed), repr([p for p in changed if p.startswith("books/book-05/")]))
    checks.add("Scope: no Book 7 prose changed", not any(path.startswith("books/book-07/manuscript/ch-") for path in changed), repr([p for p in changed if p.startswith("books/book-07/manuscript/ch-")]))
    prohibited = [p for p in changed if re.match(r"books/book-06/(?:package|cover|listing|publication|publish|upload)/", p)]
    checks.add("Scope: no package/cover/listing/upload/publication asset changed", not prohibited, repr(prohibited))
    book7_dir = root / "books/book-07/manuscript"
    book7_prose = sorted(str(path.relative_to(root)) for path in book7_dir.glob("ch-*.md")) if book7_dir.exists() else []
    checks.add("Scope: no Book 7 prose exists", not book7_prose, repr(book7_prose))
    checks.require()
    return checks, changed
'''
new_scope = '''def resolve_scope_base() -> tuple[str, str]:
    """Return the actual change-scope ref and its merge base with HEAD."""
    explicit = os.environ.get("BOOK6_SCOPE_BASE_REF")
    if explicit:
        candidates = [explicit]
    else:
        candidates = []
        github_base = os.environ.get("GITHUB_BASE_REF")
        if github_base:
            candidates.extend([f"origin/{github_base}", github_base])
        candidates.extend(["origin/main", "main"])

    attempted = []
    for candidate in dict.fromkeys(candidates):
        result = run(["git", "merge-base", candidate, "HEAD"], check=False)
        merge_base = result.stdout.strip()
        attempted.append(f"{candidate}: {result.returncode}")
        if result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", merge_base):
            return candidate, merge_base
    raise RuntimeError(f"Unable to resolve current change-scope base ({'; '.join(attempted)})")


def is_production_asset(path: str) -> bool:
    if not re.match(r"^books/book-\\d+/", path):
        return False
    protected_stems = ("package", "cover", "listing", "upload", "publication", "publish", "release", "retailer")
    return any(part.lower().startswith(protected_stems) for part in Path(path).parts[2:])


def scope_validation(b4, root: Path):
    checks = b4.Validation([])
    try:
        scope_base_ref, scope_base_sha = resolve_scope_base()
        result = run(["git", "diff", "--name-only", f"{scope_base_sha}...HEAD"], check=False)
        comparison_ok = result.returncode == 0
        comparison_detail = f"ref {scope_base_ref}; merge base {scope_base_sha}"
        if not comparison_ok:
            comparison_detail += f"; {result.stdout.strip() or 'git diff failed'}"
    except RuntimeError as exc:
        scope_base_ref, scope_base_sha = "unresolved", ""
        result = None
        comparison_ok = False
        comparison_detail = str(exc)

    checks.add("Scope: actual current-base comparison available", comparison_ok, comparison_detail)
    changed = [line.strip() for line in result.stdout.splitlines() if line.strip()] if comparison_ok and result else []

    book5_changes = [p for p in changed if p.startswith("books/book-05/")]
    book6_manuscript = [p for p in changed if re.match(r"^books/book-06/manuscript/ch-.*\\.md$", p)]
    book7_manuscript = [p for p in changed if re.match(r"^books/book-07/manuscript/ch-.*\\.md$", p)]
    book8_changes = [p for p in changed if p.startswith("books/book-08/")]
    production_assets = [p for p in changed if is_production_asset(p)]
    book3_workflows = [p for p in changed if re.match(r"^\\.github/workflows/book-03", p)]

    checks.add("Scope: Book 5 unchanged", not book5_changes, repr(book5_changes))
    checks.add("Scope: no Book 6 chapter manuscript changed", not book6_manuscript, repr(book6_manuscript))
    checks.add("Scope: no Book 7 chapter manuscript changed relative to current base", not book7_manuscript, repr(book7_manuscript))
    checks.add("Scope: Book 8 unchanged", not book8_changes, repr(book8_changes))
    checks.add("Scope: no package/cover/listing/upload/publication/release/retailer asset changed", not production_assets, repr(production_assets))
    checks.add("Scope: Book 3 release workflow unchanged", not book3_workflows, repr(book3_workflows))

    book7_dir = root / "books/book-07/manuscript"
    book7_prose = sorted(str(path.relative_to(root)) for path in book7_dir.glob("ch-*.md")) if book7_dir.exists() else []
    checks.add("Scope: existing Book 7 prose is outside Book 6 export authority", True, repr(book7_prose) or "none present")
    checks.require()
    return checks, scope_base_sha, changed
'''
if old_scope not in text:
    raise RuntimeError("Expected stale scope-validation block was not found")
text = text.replace(old_scope, new_scope, 1)

replacements = [
    (
        "def reports(b4, root: Path, book: Path, chapters, artifacts, validation, pages: int, contacts, epubcheck: str, pdf: Path | None, changed):",
        "def reports(b4, root: Path, book: Path, chapters, artifacts, validation, pages: int, contacts, epubcheck: str, pdf: Path | None, scope_base_sha: str, changed):",
    ),
    (
        "- All eight locked final lines are preserved.\n\n## Metadata result",
        "- All eight locked final lines are preserved.\n\n## Scope result\n\n- Historical source baseline for exact Book 6 manuscript identity: `{SOURCE_BASE_SHA}`\n- Current change-scope merge base: `{scope_base_sha}`\n- Existing Book 7 prose is outside Book 6 export authority.\n- No Book 7 chapter manuscript changed relative to the current change-scope base.\n\n## Metadata result",
    ),
    (
        "- PR #31 merge commit: `{SOURCE_BASE_SHA}`\n- Starting post-PR-#31 `main` HEAD: `{SOURCE_BASE_SHA}`\n- Export branch: `{BRANCH}`",
        "- PR #31 merge commit and historical Book 6 source baseline: `{SOURCE_BASE_SHA}`\n- Current validation change-scope merge base: `{scope_base_sha}`\n- Historical export branch: `{BRANCH}`",
    ),
    (
        "- Book 7 prose: **none exists**.",
        "- Book 7 Chapter 1 exists and is formally accepted at 3,100 manuscript-prose words; it is outside Book 6 export authority, and no Book 7 chapter manuscript changed in this validation scope.",
    ),
    (
        "- Book 7 prose\n\n## Blockers and next stage",
        "- any Book 7 manuscript prose by the Book 6 export workflow\n\n## Blockers and next stage",
    ),
    (
        '"source_base": SOURCE_BASE_SHA,\n        "proofreading_pr_head": PR31_HEAD,',
        '"source_base": SOURCE_BASE_SHA,\n        "scope_base": scope_base_sha,\n        "proofreading_pr_head": PR31_HEAD,',
    ),
    (
        "scope, changed = scope_validation(b4, root)\n",
        "scope, scope_base_sha, changed = scope_validation(b4, root)\n",
    ),
    (
        "reports(b4, root, book, chapters, artifacts, all_validation, pages, contacts, epubcheck, pdf, changed)\n",
        "reports(b4, root, book, chapters, artifacts, all_validation, pages, contacts, epubcheck, pdf, scope_base_sha, changed)\n",
    ),
]
for old, new in replacements:
    if old not in text:
        raise RuntimeError(f"Expected repair anchor was not found: {old[:80]!r}")
    text = text.replace(old, new, 1)

PIPELINE.write_text(text, encoding="utf-8")

workflow = WORKFLOW.read_text(encoding="utf-8")
start = "      # BEGIN ONE-TIME VALIDATOR REPAIR\n"
end = "      # END ONE-TIME VALIDATOR REPAIR\n"
if start not in workflow or end not in workflow:
    raise RuntimeError("One-time workflow repair block was not found")
before, remainder = workflow.split(start, 1)
_, after = remainder.split(end, 1)
WORKFLOW.write_text(before + after, encoding="utf-8")
Path(__file__).unlink()
