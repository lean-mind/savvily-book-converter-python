#!/bin/sh
set -e

. ./src/scripts/manuscriptFormatter.sh

outputType=$1
latexClass=$2

pathUserDetails="./src/user-details-for-watermark.txt"

while read -r line; do

  name=$(echo "$line" | cut -d ';' -f1)
  username="$(echo $name | sed 's/ /_/g')"

  if [ -d ./src/templates/"$outputType"/.tmp_template_"$username"/ ]; then
    rm -rf ./src/templates/"$outputType"/.tmp_template_"$username"/
  fi

  mkdir ./src/templates/$outputType/.tmp_template_"$username"/

  cp ./src/templates/"$outputType"/custom-"$latexClass".tex ./src/templates/"$outputType"/.tmp_template_"$username"/custom-"$latexClass"_"$username".tex

  cp ./src/templates/"$outputType"/opening.tex ./src/templates/"$outputType"/.tmp_template_"$username"/opening_"$username".tex

  mkdir -p output/.tmp_"$username" && cd .tmp-manuscript

  formattedManuscript=$(manuscriptFormatter "$outputType")

  ## Add watermark modify copy of template screen for each user
  if [ "$1" == "screen" ]
  then
    . ../src/scripts/addWatermark.sh "$line"
  fi

  # Process main section
  echo "$formattedManuscript" | timeout 600 pandoc \
      --pdf-engine=xelatex \
      --template=../src/templates/"$outputType"/.tmp_template_"$username"/custom-"$latexClass"_"$username".tex \
      --listings \
      -V documentclass="$latexClass" \
      -f markdown-implicit_figures \
      -o ./../output/.tmp_"$username"/tmp_book_for_"$outputType"_"$username".pdf && \

  # Process book opening section
  xelatex -output-directory ./../output/.tmp_"$username" ../src/templates/"$outputType"/.tmp_template_"$username"/opening_"$username".tex && \

  # Join opening and main section
  gs \
      -q \
      -dNOPAUSE \
      -dBATCH \
      -sDEVICE=pdfwrite \
      -sOutputFile=./../output/codigo_sostenible_for_"$outputType"_"$username".pdf \
      ./../output/.tmp_"$username"/opening_"$username".pdf ./../output/.tmp_"$username"/tmp_book_for_"$outputType"_"$username".pdf && \

  rm -rf ../src/templates/screen/.tmp_template_"$username"

  rm -rf ../output/.tmp_"$username" && \

  cd ..

  echo "PDF for $outputType successfully generated"

done < "$pathUserDetails"
