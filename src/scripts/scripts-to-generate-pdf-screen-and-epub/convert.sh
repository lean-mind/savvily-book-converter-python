#!/bin/sh
set -e

cd ../../..

if [ $# -ge 1 ]; then
  if [ -d "./manuscript" ]; then
    manuscript="./manuscript"
  else
    echo "The manuscript folder doesn't exist"
    echo "The manuscript folder should contain a resources folder and files with .txt or .md extension \n"

    echo "Please place the manuscript folder in the project root \n"
    exit 1
  fi
else
    echo "Wrong input"
    exit 1
fi

name="$2"
email="$3"

case "$1" in
  -s| --screen) scriptToRun="./src/scripts/scripts-to-generate-pdf-screen-and-epub/pdf.sh screen report "\"$name\"" "$email"" ;;

  -e| --epub) scriptToRun="./src/scripts/scripts-to-generate-pdf-screen-and-epub/epub.sh" format="epub";;

   *) printf "Unknown option %s\n" "$1" ; exit 1;;
esac

if [ -d .tmp-manuscript ]; then
  rm -rf .tmp-manuscript
fi

mkdir -p .tmp-manuscript && cp -r "$manuscript"/* ./.tmp-manuscript

docker run --rm \
  --volume "$PWD":/data \
  -u "$(id -u "$USER"):$(id -g "$USER")" \
  savvily-book-generator \
  "$scriptToRun"

rm -rf .tmp-manuscript

if [ "$format" = "epub" ]; then
  . ./src/scripts/scripts-to-generate-pdf-screen-and-epub/epubFormatter.sh "$name" "$email"
fi

. ./src/scripts/wrapBooks.sh
