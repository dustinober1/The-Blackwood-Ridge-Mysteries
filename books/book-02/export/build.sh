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
  --toc --toc-depth=2 \
  --split-level=2 \
  --metadata title="The Botanical Confession" \
  --metadata author="Vesper Blythe" \
  --metadata lang="en" \
  -o "the-botanical-confession.epub"

echo "Built the-botanical-confession.epub"
