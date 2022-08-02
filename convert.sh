#!/bin/sh
set -e

if [ $# -eq 1 ]; then
  echo "Sorry, I need a valid manuscript path to work"
  exit 1
elif [ $# -eq 2 ]; then
  manuscript=$2
else
  echo "Wrong input"
  exit 1
fi

case "$1" in
-p | --print) scriptToRun="python3 -B src/pdf-print.py .tmp-manuscript" ;;
-lp | --legacy-print) scriptToRun="python3 -B src/pdf-print.py legacy .tmp-manuscript" ;;

\
  -s | --screen) scriptToRun="python3 -B src/pdf-screen.py .tmp-manuscript" ;;
-ls | --legacy-screen) scriptToRun="python3 -B src/pdf-screen.py legacy .tmp-manuscript" ;;

\
  -e | --epub) scriptToRun="python3 -B src/epub.py .tmp-manuscript" ;;
-le | --legacy-epub) scriptToRun="python3 -B src/epub.py legacy .tmp-manuscript" ;;

\
  -a | --all)
  ./convert.sh -e ".tmp-manuscript"
  ./convert.sh -p ".tmp-manuscript"
  ./convert.sh -s ".tmp-manuscript"
  exit
  ;;
-la | --legacy-all)
  ./convert.sh -le ".tmp-manuscript"
  ./convert.sh -lp ".tmp-manuscript"
  ./convert.sh -ls ".tmp-manuscript"
  exit
  ;;

\
  *)
  printf "Unknown option %s\n" "$1"
  exit 1
  ;;
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
