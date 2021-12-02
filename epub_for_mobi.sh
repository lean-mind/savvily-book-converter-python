#!/bin/sh

cd codigo-sostenible/manuscript

pandoc .tempBook\
    --toc                                                 \
    --css ../../epub.css                                  \
    --highlight-style ../../monochrome.theme              \
    --epub-cover-image ./resources/Codigo_Sostenible.png  \
    -o ./../../output/ebook_for_mobi.epub                 \
    ../../metadata.yml                                    \
&& echo "EPUB for MOBI successfully generated"
