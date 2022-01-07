#!/bin/sh

if [ $# -lt 2 ]; then
    echo "I need both a flag and a path!"
    exit 1
fi

case "$1" in
  -p|--print)
    mkdir -p .manuscript && cp -r "$2"/* ./.manuscript
    docker run -it --rm \
      --volume "$PWD":/data \
      -u "$(id -u "$USER"):$(id -g "$USER")" \
      --entrypoint ./src/scripts/pdf_for_print.sh \
      savvily-book-generator
    shift;;

  -s|--screen)
    mkdir -p .manuscript && cp -r "$2"/* ./.manuscript
    docker run -it --rm \
      --volume "$PWD":/data \
      -u "$(id -u "$USER"):$(id -g "$USER")" \
      --entrypoint ./src/scripts/pdf_for_screen.sh \
      savvily-book-generator
    shift;;

  -e|--epub)
    mkdir -p .manuscript && cp -r "$2"/* ./.manuscript
    docker run -it --rm \
      --volume "$PWD":/data \
      -u "$(id -u "$USER"):$(id -g "$USER")" \
      --entrypoint ./src/scripts/epub.sh \
      savvily-book-generator
    docker run -it --rm \
      --volume "$PWD":/data \
      -u "$(id -u "$USER"):$(id -g "$USER")" \
      --entrypoint ./src/scripts/epub_for_mobi.sh \
      savvily-book-generator
    shift;;

  -a|--all)
    ./convert.sh -p "$2"; ./convert.sh -s "$2"; ./convert.sh -e "$2"
    shift;;

   *)
    printf "Unknown option %s\n" "$1"
    exit 1;;
esac

rm -rf .manuscript
