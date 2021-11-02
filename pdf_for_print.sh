#!/bin/sh

./pdf_cover.sh

cp -rf ./codigo-sostenible/manuscript/* .

chapters=$(cat Book.txt)

pandoc $chapters                                           \
       --pdf-engine=xelatex                                \
       --template=custom-book.tex                          \
       --listings                                          \
       -V documentclass=book                               \
       -o ./output/bookWithoutCover.pdf

rm -rf ./*.txt ./resources

pdfunite ./output/cover.pdf ./output/bookWithoutCover.pdf ./output/book.pdf

rm ./output/cover.pdf
rm ./output/bookWithoutCover.pdf