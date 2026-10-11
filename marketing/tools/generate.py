#!/usr/bin/env python3
"""Render marketing post specs to PNG social cards via typst.

Usage:
  python3 marketing/tools/generate.py all
  python3 marketing/tools/generate.py 001-welcome-to-the-ridge 005-case-file-wren
  python3 marketing/tools/generate.py all --ppi 288    # 2x review proofs

Pipeline per post: if the spec declares an `art:` block, ridge_art renders
the background SVG; then typst compiles marketing/templates/<template>.typ
with the spec as a sys.input. Specs live in marketing/posts/ and carry the
card copy plus the caption, hashtags, and alt text for each platform.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POSTS = ROOT / "marketing" / "posts"
TEMPLATES = ROOT / "marketing" / "templates"
GENERATED = ROOT / "marketing" / "generated"
ART = GENERATED / "art"

sys.path.insert(0, str(Path(__file__).parent))
import ridge_art


def parse_spec(slug):
    """Extract the fields the driver needs; typst reads the full spec itself."""
    text = (POSTS / f"{slug}.yaml").read_text(encoding="utf-8")
    tm = re.search(r"^template:\s*([\w-]+)\s*$", text, re.M)
    if not tm:
        raise SystemExit(f"{slug}: missing `template:`")
    art = None
    am = re.search(r"^art:\n((?:[ \t]+\S.*\n)+)", text, re.M)
    if am:
        block = am.group(1)
        sm = re.search(r"\bstyle:\s*([\w-]+)", block)
        sd = re.search(r"\bseed:\s*(\d+)", block)
        if sm:
            art = {"style": sm.group(1), "seed": int(sd.group(1)) if sd else 1}
    return tm.group(1), art


def build(slug, ppi=144):
    template, art = parse_spec(slug)
    args = [
        "typst", "compile",
        f"--root={ROOT}",
        "--format=png",
        f"--ppi={ppi}",
        f"--input=spec=/marketing/posts/{slug}.yaml",
    ]
    if art:
        ART.mkdir(parents=True, exist_ok=True)
        (ART / f"{slug}.svg").write_text(ridge_art.render(art["style"], art["seed"]), encoding="utf-8")
        args.append(f"--input=art=/marketing/generated/art/{slug}.svg")
    out = GENERATED / f"{slug}.png"
    args += [str(TEMPLATES / f"{template}.typ"), str(out)]
    subprocess.run(args, check=True)
    return out


def main():
    argv = sys.argv[1:]
    ppi = 144
    if "--ppi" in argv:
        i = argv.index("--ppi")
        ppi = int(argv[i + 1])
        del argv[i:i + 2]
    slugs = argv
    if not slugs or slugs == ["all"]:
        slugs = sorted(p.stem for p in POSTS.glob("*.yaml"))
    for slug in slugs:
        out = build(slug, ppi)
        print(f"ok {slug} -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
