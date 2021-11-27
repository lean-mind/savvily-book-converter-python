#!/bin/sh

cd codigo-sostenible/manuscript

find . -name "[0-9]*.txt" | sort -V | xargs               \
  pandoc                                                  \
    --toc                                                 \
    --css ../../epub.css                                  \
    --highlight-style ../../monochrome.theme              \
    --epub-cover-image ./resources/Codigo_Sostenible.png  \
    -o ./../../output/ebook_for_mobi.epub                 \
    ../../metadata.yml                                    \
&& echo "EPUB for MOBI successfully generated"
