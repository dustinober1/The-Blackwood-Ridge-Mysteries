#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc is not installed."
  echo "Install it first:"
  echo "  brew install pandoc     (macOS)"
  echo "  apt-get install pandoc  (Debian/Ubuntu)"
  exit 1
fi

pandoc manuscript-combined.md \
  -f markdown \
  -t epub3 \
  --toc --toc-depth=1 \
  --metadata title="Murder Most Annotated" \
  --metadata author="Vesper Blythe" \
  --metadata lang="en" \
  -o "murder-most-annotated.epub"

echo "Built murder-most-annotated.epub"
