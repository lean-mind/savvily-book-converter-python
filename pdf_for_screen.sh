#!/bin/sh

cp -rf ./codigo-sostenible/manuscript/* .

chapters=$(cat Book.txt)

pandoc $chapters                                          \
       --pdf-engine=xelatex                               \
       --template=custom-report.tex                       \
       --listings                                         \
       -V documentclass=report                            \
       -o ./output/report.pdf

rm -rf ./*.txt ./resources
