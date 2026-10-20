#!/bin/sh
# Points every page at style.css?v=<hash of style.css>, so browsers fetch the
# new stylesheet with a new page instead of pairing it with a cached old one
# (GitHub Pages lets browsers keep files for 10 minutes). Run after editing style.css.
cd "$(dirname "$0")/.." || exit 1
v=$(shasum style.css | cut -c1-8)
for f in index.html faq/index.html privacy/index.html support/index.html; do
  sed -i '' -E "s#href=\"((\.\./)?style\.css)(\?v=[0-9a-f]+)?\"#href=\"\1?v=$v\"#" "$f"
done
echo "style.css?v=$v"
