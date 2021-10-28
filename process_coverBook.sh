#!/bin/sh

pdflatex --output-directory=./output ./coverBook.tex

rm ./output/coverBook.log
rm ./output/coverBook.aux
