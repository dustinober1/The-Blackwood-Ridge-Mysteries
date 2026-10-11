#!/usr/bin/env python3
"""Persona review toolkit for The Blackwood Ridge Mysteries.

Parses the persona library (docs/reader-personas/personas.md) and the
reader-facing manuscript exports (books/book-NN/export/manuscript-combined.md)
into a manifest used to run chapter-by-chapter persona reviews.

Usage:
    python3 tools/persona_toolkit.py manifest            # write tools/persona-review-manifest.json
    python3 tools/persona_toolkit.py chapters book-02    # print chapter boundary table
    python3 tools/persona_toolkit.py personas            # print persona summary table
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PERSONAS_MD = REPO / "docs" / "reader-personas" / "personas.md"
MANIFEST_OUT = REPO / "tools" / "persona-review-manifest.json"

GROUP_HEADER_RE = re.compile(r"^## ([A-Z]) — (.+?) \((\d+)\)\s*$")
PERSONA_START_RE = re.compile(r"^\*\*([A-Z]\d{2})\s+(.+?)\*\*\s*(.*)$")
FIELD_RE = re.compile(r"\*([A-Za-z][A-Za-z /-]*?):\*\s*")
BOOK_NUM_RE = re.compile(r"book-(\d+)")
NUMBERED_CHAPTER_RE = re.compile(r"^# Chapter (\d+)\s+—\s+(.+?)\s*$")


def parse_personas(path=PERSONAS_MD):
    """Parse personas.md into structured entries.

    Returns (groups, personas). Each persona dict:
      group, id, name, entry, loves, hates, checks, rates, extra (dict of other
      *Key:* fields), body (raw text after the bold name), full_text.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    groups = []
    personas = []
    current_group = None
    current = None
    body_lines = []

    def flush():
        nonlocal current, body_lines
        if current is None:
            return
        body = "\n".join(body_lines).strip()
        current["body"] = body
        _extract_fields(current)
        current["full_text"] = (
            f"{current['id']} {current['name']}. {body}"
        )
        personas.append(current)
        current = None
        body_lines = []

    for line in lines:
        gm = GROUP_HEADER_RE.match(line)
        if gm:
            flush()
            current_group = {
                "letter": gm.group(1),
                "name": gm.group(2),
                "count": int(gm.group(3)),
                "note": "",
            }
            groups.append(current_group)
            continue
        if current_group and line.startswith("> ") and not personas and current is None:
            current_group["note"] = (current_group["note"] + " " + line[2:].strip()).strip()
            continue
        pm = PERSONA_START_RE.match(line)
        if pm:
            flush()
            current = {
                "group": current_group["letter"],
                "group_name": current_group["name"],
                "id": pm.group(1),
                "name": pm.group(2).strip(),
            }
            rest = pm.group(3).strip()
            body_lines = [rest] if rest else []
            continue
        if current is not None:
            if line.strip() == "---":
                continue
            body_lines.append(line)
    flush()
    return groups, personas


def _extract_fields(persona):
    """Pull *Key:* fields out of the body text."""
    body = persona["body"]
    marks = list(FIELD_RE.finditer(body))
    fields = {}
    for i, m in enumerate(marks):
        key = m.group(1).strip().lower().replace(" / ", "_").replace(" ", "_")
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        value = body[m.end():end].strip()
        fields[key] = value
    for key in ("entry", "loves", "hates", "checks", "rates"):
        persona[key] = fields.get(key, "")
    persona["extra_fields"] = {k: v for k, v in fields.items()
                              if k not in ("entry", "loves", "hates", "checks", "rates")}


def parse_book(book_dir):
    """Parse one book's manuscript-combined.md into chapter line ranges."""
    book_dir = REPO / "books" / book_dir if not book_dir.startswith("/") else Path(book_dir)
    mpath = book_dir / "export" / "manuscript-combined.md"
    lines = mpath.read_text(encoding="utf-8").splitlines()
    title = ""
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
    m = BOOK_NUM_RE.search(str(book_dir))
    number = int(m.group(1)) if m else 0

    numbered = [NUMBERED_CHAPTER_RE.match(ln) for ln in lines]
    if any(numbered):
        style = "numbered"
        heads = [(i + 1, NUMBERED_CHAPTER_RE.match(ln).group(1), NUMBERED_CHAPTER_RE.match(ln).group(2))
                 for i, ln in enumerate(lines) if NUMBERED_CHAPTER_RE.match(ln)]
    else:
        style = "named"
        toc_titles = _toc_titles(lines)
        heads = []
        for i, ln in enumerate(lines):
            if ln.startswith("## ") and ln[3:].strip() in toc_titles:
                heads.append((i + 1, None, ln[3:].strip()))

    chapters = []
    for idx, (start, num, ctitle) in enumerate(heads):
        end = heads[idx + 1][0] - 1 if idx + 1 < len(heads) else len(lines)
        # Trim trailing back-matter for the final chapter when a known back-matter
        # heading follows (e.g. "# A Note from the Author", "# Thank you for reading").
        chapters.append({
            "num": int(num) if num else idx + 1,
            "title": ctitle,
            "start": start,
            "end": end,
        })

    # Back matter starts at the first top-level heading after the last
    # chapter that is not a chapter heading (e.g. "# A Note from the
    # Author", "# Thank you for reading").
    back_start = len(lines) + 1
    if chapters:
        for i in range(chapters[-1]["start"], len(lines)):
            if lines[i].startswith("# ") and not NUMBERED_CHAPTER_RE.match(lines[i]):
                back_start = i + 1
                break
        chapters[-1]["end"] = min(chapters[-1]["end"], back_start - 1)

    front_end = chapters[0]["start"] - 1 if chapters else len(lines)
    return {
        "dir": str(book_dir.relative_to(REPO)),
        "title": title,
        "number": number,
        "manuscript": str(mpath.relative_to(REPO)),
        "total_lines": len(lines),
        "chapter_style": style,
        "front_matter": {"start": 1, "end": front_end},
        "chapters": chapters,
        "back_matter": {"start": back_start, "end": len(lines)} if back_start <= len(lines) else None,
    }


def _toc_titles(lines):
    """Collect bullet titles under the '# Contents' heading."""
    titles = set()
    in_toc = False
    for ln in lines:
        if ln.startswith("# Contents"):
            in_toc = True
            continue
        if in_toc:
            if ln.startswith("# "):
                break
            t = re.match(r"^-\s+(.+?)\s*$", ln)
            if t:
                titles.add(t.group(1).strip())
    return titles


def build_manifest(book_ids=("book-02", "book-03", "book-04", "book-05")):
    groups, personas = parse_personas()
    books = {b: parse_book(b) for b in book_ids}
    manifest = {
        "source_personas": str(PERSONAS_MD.relative_to(REPO)),
        "books": books,
        "groups": groups,
        "personas": personas,
    }
    MANIFEST_OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "manifest"
    if cmd == "manifest":
        m = build_manifest()
        print(f"wrote {MANIFEST_OUT.relative_to(REPO)}: "
              f"{len(m['personas'])} personas, {len(m['groups'])} groups, "
              f"{len(m['books'])} books")
    elif cmd == "chapters":
        book = argv[2]
        b = parse_book(book)
        print(f"{book}: {b['title']} ({b['total_lines']} lines, style={b['chapter_style']})")
        for c in b["chapters"]:
            print(f"  ch {c['num']:>2}  lines {c['start']:>5}-{c['end']:>5}  {c['title']}")
        if b["back_matter"]:
            print(f"  back matter lines {b['back_matter']['start']}-{b['back_matter']['end']}")
    elif cmd == "personas":
        _, personas = parse_personas()
        for p in personas:
            print(f"{p['id']} [{p['group']}] {p['name']} | entry={p['entry'] or '(none)'}")
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
