---
name: compile-manuscript
description: "Compile and stitch drafted chapter files into a continuous, publication-ready manuscript with customizable front matter, scene breaks, table of contents, and export formatting. Use when user says 'compile manuscript', 'export book', 'stitch chapters', 'generate full book file', or 'create publication draft'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: cross-cutting
---

# Compile Manuscript

Assembles individual chapter markdown files from `Chapters/Book-N/` into a single, cohesive manuscript file formatted for beta readers, agents, or typesetting engines (Pandoc, Word, PDF, ePub).

## Features

- **Sequential Stitching:** Sorts and concatenates `Chapter-001.md` through `Chapter-NNN.md`.
- **Scene Break Standardization:** Normalizes inconsistent scene breaks (`* * *`, `#`, `---`, blank lines) into standardized typographic markers.
- **Front & Back Matter Integration:**
  - Title page, author attribution, copyright notice.
  - Dedication, epigraph, acknowledgments.
  - Table of Contents generator.
- **Export Formats:**
  - Standard markdown export (`export/manuscript-combined.md`).
  - Clean reader-facing format (strips internal craft comments/metadata).

## Output

Outputs compiled manuscript to:
`Chapters/Book-N/export/manuscript-combined.md` or `books/book-NN/export/manuscript-combined.md`.
