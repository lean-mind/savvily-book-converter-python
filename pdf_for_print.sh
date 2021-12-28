#!/bin/sh

mkdir output/tmp
cd codigo-sostenible/manuscript

# Prepare book beginning and ending pages separately
xelatex -output-directory ./../../output/tmp ../../print/starting.tex

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
    --template=../../print/custom-book.tex           \
    --listings                                 \
    -V documentclass=book                      \
    -f markdown-implicit_figures               \
    -o ./../../output/tmp/tmp_book_for_print.pdf

pandoc --pdf-engine=xelatex --template=../../print/ending.tex --listings -V documentclass=book -f markdown-implicit_figures -o ./../../output/tmp/ending.pdf agradecimientos.txt autor.txt bibliografia.txt savvily.txt

gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=./../../output/book_for_print.pdf ./../../output/tmp/starting.pdf ./../../output/tmp/tmp_book_for_print.pdf ./../../output/tmp/ending.pdf && echo "PDF for print successfully generated"

rm -rf ../../output/tmp
