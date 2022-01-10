#!/bin/sh

if [ $# -lt 2 ]; then
    echo "I need both a flag and a path!"
    exit 1
fi

case "$1" in
  -p) scriptToRun="./src/scripts/pdf.sh print book" ;;

  -s) scriptToRun="./src/scripts/pdf.sh screen report" ;;

  -e) scriptToRun="./src/scripts/epub.sh" ;;

   *) printf "Unknown option %s\n" "$1" ; exit 1;;
esac

mkdir -p .manuscript && cp -r "$2"/* ./.manuscript

docker run -it --rm \
  --volume "$PWD":/data \
  -u "$(id -u "$USER"):$(id -g "$USER")" \
  savvily-book-generator \
  $scriptToRun

rm -rf .manuscript
