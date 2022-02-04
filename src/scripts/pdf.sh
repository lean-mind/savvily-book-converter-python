#!/bin/sh

outputType=$1

mkdir -p output/.tmp && cd .manuscript || exit

if [ "$outputType" = "print" ]; then
  latexClass="book"

  # Pre-process main section for printing
  # Sort all chapters and cat them to stdout
  preProcess=$(find . -maxdepth 1 -name "[0-9]*.txt" -o -name '[0-9]*.md' | sort -V | xargs  cat | \
  # Ensure: correct h1 headers, links respect md format, code block languages are passed as capitalized titles, refs have
  # no separation with previous word
  sed -Ee 's:(^#):\n\1:' -Ee 's:] \(:](:g' -Ee 's:(```)(.+)$:\1{title=\u\2}:' -Ee 's:\s\[\^:\[\^:g' | \
  # All non-images links ([some](text)) are converted to footnotes, takes the links as refs to avoid spaces and duplicates
  sed -E '/!.*/! s:(.+?)\[(.+?)\]\(([^)]+)\)(.+?):\1\2[^\3]\4\n\n\n[^\3]\: \3\n:g')

elif [ "$outputType" = "screen" ]; then
  latexClass="report"

  # Pre-process main section for screen PDF
  # Sort all chapters and cat them to stdout
  preProcess=$(find . -maxdepth 1 -name "[0-9]*.txt" -o -name '[0-9]*.md' | sort -V | xargs  cat | \
  # Ensure: correct h1 headers, links respect md format, code block languages are passed as capitalized titles, refs have
  # no separation with previous word
  sed -Ee 's:(^#):\n\1:' -Ee 's:] \(:](:g' -Ee 's:(```)(.+)$:\1{title=\u\2}:' -Ee 's:\s\[\^:\[\^:g')

fi

# Process main section
echo "${preProcess}" | pandoc \
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

echo "PDF for $outputType successfully generated"
