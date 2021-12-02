#!/bin/sh

cd codigo-sostenible/manuscript

pandoc .tempBook\
    --pdf-engine=xelatex                       \
    --template=../../custom-book.tex           \
    --listings                                 \
    -V documentclass=book                      \
    -f markdown-implicit_figures               \
    -o ./../../output/book_for_print.pdf       \
&& echo "PDF for print successfully generated"
