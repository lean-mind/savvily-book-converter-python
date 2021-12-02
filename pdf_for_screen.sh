#!/bin/sh

cd codigo-sostenible/manuscript

find . -name "[0-9]*.txt" | sort -V | xargs  cat |\
sed -Ee 's/(^#)/\n\1/' -Ee 's/(```)(.+)$/\1{title="\2"}/' -Ee 's/(\[.+\]) (\(.+\))/\1\2/' |\
  pandoc \
    --pdf-engine=xelatex                       \
    --template=../../custom-report.tex         \
    --listings                                 \
    -V documentclass=report                    \
    -f markdown-implicit_figures               \
    -o ./../../output/book_for_screen.pdf      \
&& echo "PDF for screen successfully generated"
