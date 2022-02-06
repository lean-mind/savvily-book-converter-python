#!/bin/sh

manuscriptFormatter(){
  # Sort all chapters and cat their content to stdout
  processedManuscript=$(find . -maxdepth 1 -name "[0-9]*.txt" -o -name '[0-9]*.md' | sort -V | xargs  cat | \
  # Ensure:
  # correct h1 headers
  # links respect md format
  # code block languages are passed as capitalized titles
  # refs have no separation with previous word
  sed -Ee 's:(^#):\n\1:' \
      -Ee 's:] \(:](:g' \
      -Ee 's:(```)(.+)$:\1{title=\u\2}:' \
      -Ee 's:\s\[\^:\[\^:g')

  if [ "$1" = "print" ]; then
    # All non-images links ([some](text)) are converted to footnotes, uses the links as refs to avoid spaces and duplicates
    processedManuscript=$(echo "$processedManuscript" | \
      sed -E "/!.*/! s:(.+?)\[(.+?)\]\(([^)]+)\)(.+?):\1\2[^\3]\4\n\n[^\3]\: \3\n:g")
  fi

  echo "$processedManuscript"
}
