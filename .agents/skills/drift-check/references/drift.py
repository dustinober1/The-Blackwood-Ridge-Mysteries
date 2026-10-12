#!/usr/bin/env python3
"""Book-level drift audit: what per-chapter gates cannot see.

The average chapter is fine; the trend is not. This script measures nine
proxies across a list of chapter files, in order, and flags trends.

Fiction:

  pet words      content words hot in one chapter or concentrating in the back half
  negation pivot negation constructions per 1k words, first vs second half
  opener formula first-word clusters across chapters (serialized-recap habit)
  closer dies    pairwise similarity of chapter-final sentences (stamped closers)
  specifics      proper-noun-ish tokens per 1k words, as a trend (texture thinning)

Non-fiction (print for any book; interpretation routes by project type):

  claim density    assertion sentences per 1k words (falling = drift to summary)
  evid/claim       evidence sentences (examples, data, quotes, citations) per claim
  abstraction      abstract-noun endings per 1k vs concrete anchors per 1k
  re-definitions   terms whose definition pattern appears again in a later chapter

These are proxies that correlate with the reader-experience problem, not
measurements of it. The skill that calls this owns interpretation; the script
only reports numbers and candidate clusters.

    python3 drift.py Chapter-001.md Chapter-002.md ...
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import Counter

STOP = set("""a an and the this that these those there here it its he she they them his
her their him of to in on at by for with from as is are was were be been being am do does
did have has had will would could should can may might must not no nor so if but or and
then than when while where what which who whom whose how why all any both each few more
most other some such only own same too very just now one two three i you we us our your
my me up out off over under again further once about into through during before after
above below between because until against itself himself herself themselves myself
yourself""".split())

WORD = re.compile(r"[A-Za-z][A-Za-z']+")

SENTENCE = re.compile(r"(?<=[.!?])\s+")

ABSTRACT_ENDING = re.compile(
    r"(?:tion|sion|ment|ness|ity|ance|ence|ism|acy|ship|hood|ology)$", re.I
)

EVIDENCE_MARK = re.compile(
    r"""\d|%|["“”]|e\.g\.|i\.e\.|for example|for instance|according to
    |such as|\(\s*[A-Z][a-zA-Z]+(?:\s+et\s+al\.)?,?\s*\d{4}\s*\)|\[\d+\]
    |study|studies|survey|census|per\s+cent|percent""",
    re.I | re.X,
)

# The defined TERM, not the subject: "X is a thekgi", "X — a thekgi",
# "known as thekgi", "called thekgi". One capture group per alternative.
DEFINITION = re.compile(
    r"""\b[A-Za-z][\w-]{2,}(?:\s+[a-z][\w-]{2,}){0,2}\s+
        (?:is|are)\s+(?:a|an|the)?\s*([a-z][\w-]{2,}(?:\s+[a-z][\w-]{2,}){0,1})\b
        |\b[a-z][\w-]{2,}(?:\s+[a-z][\w-]{2,}){0,2}\s+[—–-]\s+(?:a|an|the)?\s*([A-Za-z][\w-]{2,})\b
        |\bknown\s+as\s+(?:a|an|the)?\s*([A-Za-z][\w-]{2,})
        |\b(?:called|termed|named)\s+([A-Za-z][\w-]{2,})""",
    re.I | re.X,
)


def split_words(text: str) -> list[str]:
    return WORD.findall(text)


def body_lines(path: Path) -> tuple[str, list[str]]:
    """Title (first # heading or filename) and prose lines with headings/fences stripped."""
    title = path.stem
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            if title == path.stem:
                title = line.lstrip("#").strip()
            continue
        if line in ("---", "```", "***"):
            continue
        if re.match(r"^[-*] \[", line):  # checkbox apparatus
            continue
        lines.append(line)
    return title, lines


def first_words(lines: list[str], n: int = 6) -> str:
    for line in lines:
        words = split_words(line)
        if len(words) >= 3:
            return " ".join(words[:n])
    return "(none)"


def last_sentence(lines: list[str]) -> str:
    for line in reversed(lines):
        sentences = re.split(r"(?<=[.!?])\s+", line)
        for sentence in reversed(sentences):
            if len(split_words(sentence)) >= 4:
                return sentence
    return "(none)"


def jaccard(a: str, b: str) -> float:
    aw = {w for w in split_words(a.lower()) if w not in STOP}
    bw = {w for w in split_words(b.lower()) if w not in STOP}
    if not aw or not bw:
        return 0.0
    return len(aw & bw) / len(aw | bw)


def skeleton(a: str) -> tuple[str, ...]:
    """The stop-word frame of a sentence: same frame + fresh nouns = a die."""
    return tuple(w for w in split_words(a.lower()) if w in STOP)


def skeleton_match(a: str, b: str) -> float:
    sa, sb = skeleton(a), skeleton(b)
    if len(sa) < 4 or len(sb) < 4 or set(sa) != set(sb):
        return 0.0
    return 1.0


def cluster_pairs(pairs: list[tuple[int, int, float, str]]) -> list[list[int]]:
    """Union-find the flagged pairs into clusters."""
    parent: dict[int, int] = {}

    def find(x: int) -> int:
        while parent.setdefault(x, x) != x:
            x = parent[x] = parent[parent[x]]
        return x

    for i, j, _, _ in pairs:
        parent[find(i)] = find(j)
    groups: dict[int, list[int]] = {}
    for node in sorted(parent):
        groups.setdefault(find(node), []).append(node)
    return sorted(groups.values(), key=lambda g: (-len(g), g[0]))


def main() -> None:
    paths = [Path(p) for p in sys.argv[1:]]
    if len(paths) < 2:
        print("need at least 2 chapter files, in order")
        raise SystemExit(2)

    chapters = []
    defined_terms: dict[str, list[int]] = {}
    for idx, path in enumerate(paths, 1):
        title, lines = body_lines(path)
        text = " ".join(lines)
        words = split_words(text)
        low = [w.lower() for w in words]
        n = max(len(low), 1)
        neg = len(re.findall(r"\b(?:is|are|was|were|does|do|did)\s+not\b|\bn't\b|\bnever\b|\bno one\b|\bnobody\b", text, re.I))
        # Proper-noun-ish = a capitalized, non-stop word that does not start a
        # sentence. Word tokens carry no punctuation, so check the raw text.
        caps = 0
        for m in re.finditer(r"[A-Z][A-Za-z']+", text):
            if m.group(0).lower() in STOP:
                continue
            prev = text[: m.start()].rstrip()
            if prev and not re.search(r"[.!?][\"”']?$", prev):
                caps += 1
        sentences = [s for s in SENTENCE.split(text) if len(split_words(s)) >= 3]
        claims, evidence = 0, 0
        for sent in sentences:
            evid = bool(EVIDENCE_MARK.search(sent))
            evidence += evid
            if len(split_words(sent)) >= 6 and not sent.rstrip().endswith("?") and not evid:
                claims += 1
        abstract = sum(1 for w in low if ABSTRACT_ENDING.search(w) and w not in STOP)
        concrete = caps + sum(1 for w in words if w.isdigit())
        for m in DEFINITION.finditer(text):
            term = next((g for g in m.groups() if g), None)
            if term and len(split_words(term)) <= 3 and term.lower() not in STOP:
                defined_terms.setdefault(term.lower(), []).append(idx)
        chapters.append({
            "title": title,
            "k": n / 1000.0,
            "neg": neg / (n / 1000.0),
            "spec": caps / (n / 1000.0),
            "claims": claims / (n / 1000.0),
            "evid": evidence,
            "abs": abstract / (n / 1000.0),
            "conc": concrete / (n / 1000.0),
            "open": first_words(lines),
            "close": last_sentence(lines),
            "words": Counter(w for w in low if w not in STOP and len(w) > 3),
        })

    total_words = sum(len(split_words(" ".join(body_lines(p)[1]))) for p in paths)
    book_freq = Counter()
    for c in chapters:
        book_freq.update(c["words"])

    print(f"Drift audit — {len(chapters)} chapters, ~{total_words:,} words\n")
    print(f"{'ch':>4} {'words':>6} {'neg/1k':>7} {'spec/1k':>8}  opener")
    for i, c in enumerate(chapters, 1):
        print(f"{i:>4} {int(c['k']*1000):>6} {c['neg']:>7.1f} {c['spec']:>8.1f}  {c['open'][:48]}")

    half = len(chapters) // 2
    front_neg = sum(c["neg"] for c in chapters[:half]) / max(half, 1)
    back_neg = sum(c["neg"] for c in chapters[half:]) / max(len(chapters) - half, 1)
    front_spec = sum(c["spec"] for c in chapters[:half]) / max(half, 1)
    back_spec = sum(c["spec"] for c in chapters[half:]) / max(len(chapters) - half, 1)
    print(f"\nNegation-pivot density: front half avg {front_neg:.1f}/1k vs back half {back_neg:.1f}/1k"
          f"  {'— RISING (house style calcifying)' if back_neg > front_neg * 1.3 else ''}")
    print(f"Specifics density:      front half avg {front_spec:.1f}/1k vs back half {back_spec:.1f}/1k"
          f"  {'— FALLING (texture thinning)' if back_spec < front_spec * 0.7 else ''}")

    print("\nPet-word candidates (hot in one chapter ≥3× book rate, or ≥70% back-half):")
    found = False
    for word, total in book_freq.most_common(400):
        if total < 8:
            continue
        per_ch = [(i + 1, c["words"].get(word, 0)) for i, c in enumerate(chapters)]
        hot = [(i, cnt) for i, cnt in per_ch if cnt >= 3 and cnt >= 3 * total / len(chapters)]
        back_share = sum(cnt for i, cnt in per_ch if i > half) / total
        if hot or back_share >= 0.7:
            found = True
            detail = (f"hot in ch{hot[0][0]} ({hot[0][1]}×)" if hot
                      else f"{back_share:.0%} of uses in back half")
            print(f"  {word!r}: {total}× — {detail}")
    if not found:
        print("  none")

    print("\nOpener clusters (shared first 2 words, ≥3 chapters):")
    found = False
    opener_pairs = Counter(" ".join(c["open"].split()[:2]).lower() for c in chapters)
    for prefix, cnt in opener_pairs.most_common(5):
        if cnt >= 3:
            found = True
            members = [i + 1 for i, c in enumerate(chapters)
                       if " ".join(c["open"].split()[:2]).lower() == prefix]
            print(f"  {prefix!r}: chapters {members}")
    if not found:
        print("  none — openers vary")

    print("\nCloser die candidates:")
    found = False
    pairs = []
    for i in range(len(chapters)):
        for j in range(i + 1, len(chapters)):
            a, b = chapters[i]["close"], chapters[j]["close"]
            sim = jaccard(a, b)
            if sim >= 0.45:
                pairs.append((i, j, sim, "verbatim"))
            elif skeleton_match(a, b):
                pairs.append((i, j, 1.0, "same frame, fresh nouns"))
    for cluster in cluster_pairs(pairs):
        found = True
        members = ", ".join(f"ch{m+1}" for m in cluster)
        kind = next(kind for i, j, _, kind in pairs if i in cluster and j in cluster)
        print(f"  {members}  ({kind})")
        for n in cluster[:3]:
            print(f"    {chapters[n]['close'][:90]}")
    if not found:
        print("  none — closers vary")

    half = len(chapters) // 2

    def halves(key: str) -> tuple[float, float]:
        front = chapters[:half] or chapters[:1]
        back = chapters[half:] or chapters[-1:]
        avg = lambda chs: sum(c[key] for c in chs) / len(chs)
        return avg(front), avg(back)

    print()
    print("Non-fiction proxies (interpretation routes by project type — see the skill):")
    print(f"{'ch':>4} {'claims/1k':>10} {'evid':>5} {'evid/claim':>11} {'abs/1k':>7} {'conc/1k':>8}")
    for i, c in enumerate(chapters, 1):
        ratio = c["evid"] / max(c["claims"] * c["k"], 0.001)
        print(f"{i:>4} {c['claims']:>10.1f} {c['evid']:>5.0f} {ratio:>11.2f} {c['abs']:>7.1f} {c['conc']:>8.1f}")

    f_claims, b_claims = halves("claims")
    flag = "  — FALLING (drifting from argument toward summary)" if b_claims < f_claims * 0.7 else ""
    print(f"\nClaim density: front half avg {f_claims:.1f}/1k vs back half {b_claims:.1f}/1k{flag}")

    f_evid = sum(c["evid"] for c in chapters[:half] or chapters[:1]) / max(
        sum(c["claims"] * c["k"] for c in chapters[:half] or chapters[:1]), 0.001)
    b_evid = sum(c["evid"] for c in chapters[half:] or chapters[-1:]) / max(
        sum(c["claims"] * c["k"] for c in chapters[half:] or chapters[-1:]), 0.001)
    flag = "  — FALLING (assertions going unsupported)" if b_evid < f_evid * 0.7 else ""
    print(f"Evidence-to-claim ratio: front half {f_evid:.2f} vs back half {b_evid:.2f}{flag}")

    f_abs, b_abs = halves("abs")
    f_conc, b_conc = halves("conc")
    flags = []
    if b_abs > f_abs * 1.3:
        flags.append(f"abstract nouns rising ({f_abs:.1f} → {b_abs:.1f}/1k)")
    if b_conc < f_conc * 0.7:
        flags.append(f"concrete anchors falling ({f_conc:.1f} → {b_conc:.1f}/1k)")
    ladder = "  — NARROWING: " + "; ".join(flags) if flags else ""
    print(f"Abstraction ladder: abstract/1k {f_abs:.1f} vs {b_abs:.1f}, concrete anchors/1k {f_conc:.1f} vs {b_conc:.1f}{ladder}")

    reintroduced = {t: chs for t, chs in defined_terms.items() if len(chs) >= 2}
    if reintroduced:
        print("Reintroduced definitions (term defined again in a later chapter):")
        for term, chs in sorted(reintroduced.items()):
            print(f"  {term!r}: defined in ch{', ch'.join(map(str, chs))}")
    else:
        print("Reintroduced definitions: none")


if __name__ == "__main__":
    main()
