#!/bin/sh

cp -rf ./codigo-sostenible/manuscript/* .

chapters=$(cat Book.txt)

pandoc $chapters                                             \
       --toc                                                 \
       --css epub.css                                        \
       --epub-cover-image ./resources/Codigo_Sostenible.png  \
       -o ./output/ebook.epub metadata.yml

rm -rf ./*.txt ./resources