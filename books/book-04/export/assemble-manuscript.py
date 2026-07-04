#!/usr/bin/env python3
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parents[1]
MANUSCRIPT_DIR = BOOK_DIR / 'manuscript'
OUTPUT = BOOK_DIR / 'export' / 'manuscript-combined.md'

CHAPTERS = [
    (1, 'Smoke Under Town Hall', 'ch-01.md'),
    (2, 'The Salvage Table', 'ch-02.md'),
    (3, 'A Shelf That Lied Twice', 'ch-03.md'),
    (4, "The Predecessor's Hand", 'ch-04.md'),
    (5, 'Water Lines', 'ch-05.md'),
    (6, 'Bad Procedure', 'ch-06.md'),
    (7, 'The Ash Index', 'ch-07.md'),
    (8, 'The Box Asked For', 'ch-08.md'),
]

FRONT_MATTER = r'''# The Archive Fire

**Vesper Blythe**

*The Blackwood Ridge Mysteries, Book 4*

\newpage

**The Archive Fire**

Copyright © 2026 Vesper Blythe

All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without prior written permission from the author, except for brief quotations used in reviews.

This is a work of fiction. Names, characters, places, and incidents are products of the author's imagination or are used fictitiously. Any resemblance to actual persons, living or dead, events, or locales is entirely coincidental.

First edition: July 2026
'''

CONTENTS = r'''\newpage

# Contents

- Chapter 1 — Smoke Under Town Hall
- Chapter 2 — The Salvage Table
- Chapter 3 — A Shelf That Lied Twice
- Chapter 4 — The Predecessor's Hand
- Chapter 5 — Water Lines
- Chapter 6 — Bad Procedure
- Chapter 7 — The Ash Index
- Chapter 8 — The Box Asked For
'''

CHAPTER_TEMPLATE = r'''\newpage

# Chapter {n} — {title}

{body}
'''


def strip_chapter_front_matter(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == '---':
        for idx in range(1, len(lines)):
            if lines[idx].strip() == '---':
                lines = lines[idx + 1:]
                break
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith('# '):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    return '\n'.join(lines).rstrip()


def main():
    parts = [FRONT_MATTER.strip(), CONTENTS.strip()]
    for n, title, filename in CHAPTERS:
        source = (MANUSCRIPT_DIR / filename).read_text(encoding='utf-8')
        body = strip_chapter_front_matter(source)
        parts.append(CHAPTER_TEMPLATE.format(n=n, title=title, body=body).strip())
    OUTPUT.write_text('\n\n'.join(parts).rstrip() + '\n', encoding='utf-8')
    print(f'Wrote {OUTPUT.relative_to(BOOK_DIR.parent.parent)}')


if __name__ == '__main__':
    main()
