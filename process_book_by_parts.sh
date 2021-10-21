#!/bin/sh

./process_cover.sh

cp -rf ./codigo-sostenible/manuscript/* .

pandoc ./codigo-sostenible/manuscript/0_pre.txt           \
       ./codigo-sostenible/manuscript/1_intro.txt         \
       ./codigo-sostenible/manuscript/2_flexible.txt      \
       ./codigo-sostenible/manuscript/3_sorpresa.txt      \
       ./codigo-sostenible/manuscript/4_cohesion.txt      \
       ./codigo-sostenible/manuscript/5_refactoring.txt   \
       ./codigo-sostenible/manuscript/6_principios.txt    \
       ./codigo-sostenible/manuscript/7_srp.txt           \
       ./codigo-sostenible/manuscript/8_errores.txt       \
       ./codigo-sostenible/manuscript/9_tipos.txt         \
       ./codigo-sostenible/manuscript/10_contexto.txt     \
       ./codigo-sostenible/manuscript/11_cierre.txt       \
      --pdf-engine=xelatex                                \
      --template=custom-book.tex                          \
      --listings                                          \
      -V documentclass=book                               \
      -o ./output/bookWithoutCover.pdf

rm -rf ./*.txt ./resources

pdfunite ./output/cover.pdf ./output/bookWithoutCover.pdf ./output/book.pdf
