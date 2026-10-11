#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc is not installed."
  exit 1
fi

pandoc manuscript-combined.md \
  -f markdown \
  -t epub3 \
  --toc --toc-depth=1 \
  --metadata title="The Annotated Murder" \
  --metadata author="Vesper Blythe" \
  --metadata lang="en" \
  --epub-cover-image cover.jpeg \
  -o "the-annotated-murder.epub"

echo "Built the-annotated-murder.epub with embedded cover image"
