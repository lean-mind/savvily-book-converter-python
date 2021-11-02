#!/bin/sh

./pdf_cover.sh

cp -rf ./codigo-sostenible/manuscript/* .

chapters=$(cat Book.txt)

pandoc $chapters                                          \
       --pdf-engine=xelatex                               \
       --template=custom-report.tex                       \
       --listings                                         \
       -V documentclass=report                            \
       -o ./output/reportWithoutCover.pdf

rm -rf ./*.txt ./resources

pdfunite ./output/cover.pdf ./output/reportWithoutCover.pdf ./output/report.pdf

rm ./output/cover.pdf
rm ./output/reportWithoutCover.pdf