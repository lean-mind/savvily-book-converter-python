#!/bin/sh

cp -rf ./codigo-sostenible/manuscript/* .

chapters=$(cat Book.txt)

pandoc $chapters                                             \
       --toc                                                 \
       --css epub.css                                        \
       --highlight-style monochrome.theme                    \
       --epub-cover-image ./resources/Codigo_Sostenible.png  \
       -o ./output/ebookMonochrome.epub metadata.yml

rm -rf ./*.txt ./resources