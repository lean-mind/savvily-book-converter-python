#!/bin/sh
. ./src/scripts/markdownFormatter.sh

mkdir -p output && cd .manuscript || exit

formattedPandocInput=$(markdownFormatter "ebook")

# Run Pandoc on formatted input
echo "$formattedPandocInput" | pandoc \
    --toc \
    --epub-embed-font=/usr/share/fonts/Roboto-Bold.ttf \
    --css ../src/templates/epub/epub.css \
    --epub-cover-image ./resources/book-cover-print.png \
    -o ./../output/ebook.epub \
    --metadata-file ../src/templates/epub/metadata.yml && \

echo "EPUB successfully generated"
