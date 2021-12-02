#!/bin/sh

ARGS=$(getopt --options psea --long "print,screen,epub,all" -- "$@")

mkdir -p output

# Prepare markdown for processing

# Sort all chapters and cat them to stdout
find codigo-sostenible/manuscript/ -name "[0-9]*.txt" | sort -V | xargs  cat |\
# Ensure: h1 headers work, links respect md format, code block languages are passed as capitalized titles
sed -Ee 's:(^#):\n\1:' \
    -Ee 's:] \(:](:g' \
    -Ee 's:(```)(.+)$:\1{title=\u\2}:' > codigo-sostenible/manuscript/.tempBook 

case "$1" in
  -p|--print)
    docker run --rm \
      --volume $PWD:/data \
      --entrypoint ./pdf_for_print.sh \
      docker-book-generator
    rm codigo-sostenible/manuscript/.tempBook
    shift;;

  -s|--screen)
    docker run --rm \
      --volume $PWD:/data \
      --entrypoint ./pdf_for_screen.sh \
      docker-book-generator
    rm codigo-sostenible/manuscript/.tempBook
    shift;;

  -e|--epub)
    docker run --rm \
      --volume $PWD:/data \
      --entrypoint ./epub.sh \
      docker-book-generator
    docker run --rm \
      --volume $PWD:/data \
      --entrypoint ./epub_for_mobi.sh \
      docker-book-generator
    rm codigo-sostenible/manuscript/.tempBook
    shift;;

  -a|--all)
    ./generate.sh -p; ./generate.sh -s; ./generate.sh -e
    shift;;

  --)
    break;;

   *)
    printf "Unknown option %s\n" "$1"
    exit 1;;
esac
