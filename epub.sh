#!/bin/sh

cd codigo-sostenible/manuscript

find . -name "[0-9]*.txt" | sort -V | xargs               \
  pandoc                                                  \
    --toc                                                 \
    --css ../../epub.css                                  \
    --epub-cover-image ./resources/Codigo_Sostenible.png  \
    -o ./../../output/ebook.epub                          \
    ../../metadata.yml                                    \
&& echo "EPUB successfully generated"
