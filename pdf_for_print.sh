#!/bin/sh

./pdf_cover.sh

mkdir output && cd codigo-sostenible/manuscript

find . -name "[0-9]*.txt" | sort -V | xargs				\
pandoc                                     				\
       --pdf-engine=xelatex                				\
       --template=../../custom-book.tex    				\
       --listings                          				\
       -V documentclass=book               				\
       -o ./../../output/bookWithoutCover.pdf 		\
&& echo "PDF for print successfully generated"

cd ../../

pdfunite ./output/cover.pdf ./output/bookWithoutCover.pdf ./output/book.pdf

rm ./output/cover.pdf
rm ./output/bookWithoutCover.pdf
