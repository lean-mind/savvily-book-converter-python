#!/bin/sh

./process_cover.sh

pandoc 8_errores.txt    \
    --pdf-engine=xelatex                           \
    --template=custom-report.tex                   \
    --listings                                     \
    -V documentclass=report                        \
    -o ./output/book.pdf

pdfunite ./output/cover.pdf ./output/book.pdf ./output/output.pdf
