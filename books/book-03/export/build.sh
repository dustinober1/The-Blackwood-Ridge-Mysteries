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
  --json "$DIST/validation.json" \
  --markdown "$DIST/release-validation.md"

python3 create_upload_package.py "$DIST"

printf '\nBook 3 upload package built successfully:\n'
find "$DIST" -maxdepth 1 -type f -printf '  %f\n' | sort
