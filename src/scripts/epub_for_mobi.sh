#!/bin/sh

cd codigo-sostenible/manuscript

# Prepare markdown for processing

# Sort all chapters and cat them to stdout (Ignore "xargs: 'cat' terminated by signal 13" known bug)
find . -name "[0-9]*.txt" | sort -V | xargs  cat 2>/dev/null |\

# Ensure: h1 headers work, links respect md format, code block languages are passed as capitalized titles
sed -Ee 's:(^#):\n\1:' \
    -Ee 's:] \(:](:g' \
    -Ee 's:(```)(.+)$:\1{title=\u\2}:' |\

# Run Pandoc on stdin
pandoc \
    --toc                                                 \
    --css ../../src/templates/epub/epub.css                                  \
    --highlight-style ../../src/templates/epub/monochrome.theme              \
    --epub-cover-image ./resources/Codigo_Sostenible.png  \
    -o ./../../output/ebook_for_mobi.epub                 \
    --metadata-file ../../src/templates/epub/metadata.yml                    \
&& echo "EPUB for MOBI successfully generated"
