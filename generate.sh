#!/bin/sh

ARGS=$(getopt --options psea --long "print,screen,epub,all" -- "$@")

mkdir -p output
mkdir -p manuscript && cp -r $2/* ./manuscript

case "$1" in
  -p|--print)
    docker run -it --rm \
      --volume $PWD:/data \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      --entrypoint ./src/scripts/pdf_for_print.sh \
      docker-book-generator
    shift;;

  -s|--screen)
    docker run -it --rm \
      --volume $PWD:/data \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      --entrypoint ./src/scripts/pdf_for_screen.sh \
      docker-book-generator
    shift;;

  -e|--epub)
    docker run -it --rm \
      --volume $PWD:/data \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      --entrypoint ./src/scripts/epub.sh \
      docker-book-generator
    docker run -it --rm \
      --volume $PWD:/data \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      --entrypoint ./src/scripts/epub_for_mobi.sh \
      docker-book-generator
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
