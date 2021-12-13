#!/bin/sh

cd codigo-sostenible/manuscript

# Prepare book beginning and ending pages separately
pdflatex -output-directory ./../../output ../../starting.tex 
pdflatex -output-directory ./../../output ../../ending.tex 
rm ../../output/*.log ../../output/*.aux

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
    -o ./../../output/tmp_book_for_print.pdf       \
&& echo "PDF for print successfully generated"

pdfunite ./../../output/starting.pdf ./../../output/tmp_book_for_print.pdf ./../../output/ending.pdf ./../../output/book_for_print.pdf

rm ../../output/starting.pdf ../../output/ending.pdf ../../output/tmp_book_for_print.pdf
