#!/bin/sh

cd codigo-sostenible/manuscript

find . -name "[0-9]*.txt" | sort -V | xargs				\
pandoc                                     				\
       --pdf-engine=xelatex                				\
       --template=../../custom-book.tex    				\
       --listings                          				\
       -V documentclass=book               				\
       -f markdown-implicit_figures               \
       -o ./../../output/book_for_print.pdf 			        \
&& echo "PDF for print successfully generated"
