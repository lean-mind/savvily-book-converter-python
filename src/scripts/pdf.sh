#!/bin/sh
set -e
. ./src/scripts/manuscriptFormatter.sh

outputType=$1
latexClass=$2

cp ./src/user-details-for-watermark.txt ./.tmp-manuscript

pathUserDetails=./.tmp-manuscript/user-details-for-watermark.txt

name=$(cut -d ';' -f1 $pathUserDetails)
username="$(echo $name | sed 's/ /_/g')"

if [ -d ./src/templates/"$outputType"/.tmp_template_"$username"/ ]; then
  rm -rf ./src/templates/"$outputType"/.tmp_template_"$username"/
fi

mkdir ./src/templates/$outputType/.tmp_template_"$username"/

cp ./src/templates/"$outputType"/custom-"$latexClass".tex ./src/templates/"$outputType"/.tmp_template_"$username"/custom-"$latexClass"_"$username".tex

cp ./src/templates/"$outputType"/opening.tex ./src/templates/"$outputType"/.tmp_template_"$username"/opening_"$username".tex

mkdir -p output/.tmp && cd .tmp-manuscript

formattedManuscript=$(manuscriptFormatter "$outputType")

## Add watermark modify copy of template screen for each user
if [ "$1" == "screen" ]
then
  . ../src/scripts/addWatermark.sh
fi

# Process main section
echo "$formattedManuscript" | timeout 600 pandoc \
    --pdf-engine=xelatex \
    --template=../src/templates/"$outputType"/.tmp_template_"$username"/custom-"$latexClass"_"$username".tex \
    --listings \
    -V documentclass="$latexClass" \
    -f markdown-implicit_figures \
    -o ./../output/.tmp/tmp_book_for_"$outputType"_"$username".pdf && \

# Process book opening section
xelatex -output-directory ./../output/.tmp ../src/templates/"$outputType"/.tmp_template_"$username"/opening_"$username".tex && \

# Join opening and main section
gs \
    -q \
    -dNOPAUSE \
    -dBATCH \
    -sDEVICE=pdfwrite \
    -sOutputFile=./../output/book_for_"$outputType"_"$username".pdf \
    ./../output/.tmp/opening_"$username".pdf ./../output/.tmp/tmp_book_for_"$outputType"_"$username".pdf && \

rm -rf ../output/.tmp && \

rm -rf ../src/templates/screen/.tmp_template_"$username"

echo "PDF for $outputType successfully generated"
