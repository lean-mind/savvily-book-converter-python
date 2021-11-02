#!/bin/sh

pdflatex --output-directory=./output ./cover.tex

rm ./output/cover.log
rm ./output/cover.aux
