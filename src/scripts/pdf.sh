#!/bin/sh
set -e
. ./src/scripts/manuscriptFormatter.sh

outputType=$1
latexClass=$2

mkdir -p output/.tmp && cd .tmp-manuscript

formattedManuscript=$(manuscriptFormatter "$outputType")

## Add watermark modify template screen to include user data
if [ "$1" == "screen" ]
then
. ../src/scripts/addWatermark.sh "screen"
fi

# Process main section
echo "$formattedManuscript" | timeout 600 pandoc \
    --pdf-engine=xelatex \
    --template=../src/templates/"$outputType"/custom-"$latexClass".tex \
    --listings \
    -V documentclass="$latexClass" \
    -f markdown-implicit_figures \
    -o ./../output/.tmp/tmp_book_for_"$outputType".pdf && \

# Process book opening section
xelatex -output-directory ./../output/.tmp ../src/templates/"$outputType"/opening.tex && \

# Join opening and main section
gs \
    -q \
    -dNOPAUSE \
    -dBATCH \
    -sDEVICE=pdfwrite \
    -sOutputFile=./../output/book_for_"$outputType".pdf \
    ./../output/.tmp/opening.pdf ./../output/.tmp/tmp_book_for_"$outputType".pdf && \

rm -rf ../output/.tmp && \

## Reset watermark template screen
. ../src/scripts/addWatermark.sh "reset"

echo "PDF for $outputType successfully generated"
