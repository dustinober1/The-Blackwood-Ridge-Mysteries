#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
BOOK_DIR="$(cd .. && pwd)"
DIST="$PWD/dist"
PACKAGE_DIST="$BOOK_DIR/package/dist"

for command in python3 pandoc; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "ERROR: required command is not installed: $command" >&2
    exit 1
  fi
done

rm -rf "$DIST" "$PACKAGE_DIST"
mkdir -p "$DIST" "$PACKAGE_DIST"

python3 "$BOOK_DIR/package/generate-cover.py" \
  --output "$PACKAGE_DIST/The-Challenger-cover.jpg"

python3 assemble-retail.py \
  --source manuscript-combined.md \
  --output "$DIST/manuscript-retail.md"

export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1783814400}"

pandoc "$DIST/manuscript-retail.md" \
  --from=markdown+smart+raw_html \
  --to=epub3 \
  --toc --toc-depth=1 \
  --epub-title-page=false \
  --css=epub.css \
  --metadata-file=metadata.yaml \
  --epub-cover-image="$PACKAGE_DIST/The-Challenger-cover.jpg" \
  --output="$DIST/The-Challenger.epub"

cp "$PACKAGE_DIST/The-Challenger-cover.jpg" "$DIST/The-Challenger-cover.jpg"
cp "$BOOK_DIR/publish/listing.md" "$DIST/Book-3-listing-copy.md"
cp "$BOOK_DIR/publish/upload-package.md" "$DIST/README-FIRST.md"

python3 validate-release.py \
  --retail-md "$DIST/manuscript-retail.md" \
  --epub "$DIST/The-Challenger.epub" \
  --cover "$DIST/The-Challenger-cover.jpg" \
  --json "$DIST/release-manifest.json" \
  --markdown "$DIST/release-validation.md"

python3 - "$DIST" <<'PY'
from pathlib import Path
import sys
import zipfile

dist = Path(sys.argv[1])
output = dist / "The-Challenger-upload-package.zip"
include = [
    "The-Challenger.epub",
    "The-Challenger-cover.jpg",
    "Book-3-listing-copy.md",
    "README-FIRST.md",
    "release-manifest.json",
    "release-validation.md",
]
with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name in include:
        archive.write(dist / name, arcname=name)
print(output)
PY

printf '\nBook 3 upload package built successfully:\n'
find "$DIST" -maxdepth 1 -type f -printf '  %f\n' | sort
