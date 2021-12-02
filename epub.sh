#!/bin/sh

cd codigo-sostenible/manuscript

pandoc .tempBook\
    --toc                                                 \
    --css ../../epub.css                                  \
    --epub-cover-image ./resources/Codigo_Sostenible.png  \
    -o ./../../output/ebook.epub                          \
    ../../metadata.yml                                    \
&& echo "EPUB successfully generated"
