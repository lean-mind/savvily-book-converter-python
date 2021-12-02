#!/bin/sh

cd codigo-sostenible/manuscript

pandoc .tempBook\
    --pdf-engine=xelatex                       \
    --template=../../custom-report.tex         \
    --listings                                 \
    -V documentclass=report                    \
    -f markdown-implicit_figures               \
    -o ./../../output/book_for_screen.pdf      \
&& echo "PDF for screen successfully generated"
