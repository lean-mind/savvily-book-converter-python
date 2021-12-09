#!/bin/sh

cd codigo-sostenible/manuscript

# Prepare markdown for processing

# Sort all chapters and cat them to stdout
find . -name "[0-9]*.txt" | sort -V | xargs  cat |\

# Ensure: h1 headers work, links respect md format, code block languages are passed as capitalized titles
sed -Ee 's:(^#):\n\1:' \
    -Ee 's:] \(:](:g' \
    -Ee 's:(```)(.+)$:\1{title=\u\2}:' |\

# Run Pandoc on stdin
pandoc \
    --pdf-engine=xelatex                       \
    --template=../../custom-book.tex           \
    --listings                                 \
    -V documentclass=book                      \
    -f markdown-implicit_figures               \
    -o ./../../output/book_for_print.pdf       \
&& echo "PDF for print successfully generated"
