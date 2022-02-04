#!/bin/sh

mkdir -p output && cd .manuscript || exit

# Prepare markdown for processing

#find . -name "[0-9]*.txt" | sort -V | xargs  cat 2>/dev/null |\
find . -maxdepth 1 -name "[0-9]*.txt" -o -name '[0-9]*.md' | sort -V | xargs  cat | \

# Ensure: h1 headers work, links respect md format, code block languages are passed as capitalized titles
sed -Ee 's:(^#):\n\1:' \
    -Ee 's:] \(:](:g' \
    -Ee 's:(```)(.+)$:\1{title=\u\2}:' \
    -Ee 's:\s\[\^:\[\^:g'|\

# Run Pandoc on stdin
pandoc \
    --toc \
    --epub-embed-font=/usr/share/fonts/Roboto-Bold.ttf \
    --css ../src/templates/epub/epub.css \
    --epub-cover-image ./resources/book-cover-print.png \
    -o ./../output/ebook.epub \
    --metadata-file ../src/templates/epub/metadata.yml \
&& echo "EPUB successfully generated"
