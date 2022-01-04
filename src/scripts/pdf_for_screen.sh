#!/bin/sh

mkdir -p output/tmp && cd manuscript

# Prepare markdown for processing
xelatex -output-directory ./../output/tmp ../src/templates/screen/starting.tex

# Prepare MD
# Sort all chapters and cat them to stdout
find . -maxdepth 1 -name "[0-9]*.txt" -o -name '[0-9]*.md' | sort -V | xargs  cat | \

# Ensure: h1 headers work, links respect md format, code block languages are passed as capitalized titles
sed -Ee 's:(^#):\n\1:' -Ee 's:] \(:](:g' -Ee 's:(```)(.+)$:\1{title=\u\2}:' | \

# Run Pandoc on stdin
pandoc \
    --pdf-engine=xelatex \
    --template=../src/templates/screen/custom-report.tex \
    --listings \
    -V documentclass=report \
    -f markdown-implicit_figures \
    -o ./../output/tmp/tmp_book_for_screen.pdf \

find ./closing/ -name "[0-9]*.txt" -o -name '[0-9]*.md' | sort -V | xargs  cat | \
# Ensure: h1 headers work, links respect md format, code block languages are passed as capitalized titles
sed -Ee 's:(^#):\n\1:' -Ee 's:] \(:](:g' -Ee 's:(```)(.+)$:\1{title=\u\2}:' | \

# Process md additional fragments
pandoc \
    --pdf-engine=xelatex\
    --template=../src/templates/screen/ending.tex\
    --listings -V documentclass=report\
    -f markdown-implicit_figures\
    -o ./../output/tmp/ending.pdf

# Join pdf fragments
gs \
  -q \
  -dNOPAUSE \
  -dBATCH \
  -sDEVICE=pdfwrite \
  -sOutputFile=./../output/book_for_screen.pdf \
  ./../output/tmp/starting.pdf ./../output/tmp/tmp_book_for_screen.pdf ./../output/tmp/ending.pdf
echo "PDF for screen successfully generated"

rm -rf ../output/tmp
