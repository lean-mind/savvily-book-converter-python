#!/bin/sh

ARGS=$(getopt --options psea --long "print,screen,epub,all" -- "$@")

case "$1" in
  -p|--print)
    mkdir -p manuscript && cp -r $2/* ./manuscript
    docker run -it --rm \
      --volume $PWD:/data \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      --entrypoint ./src/scripts/pdf_for_print.sh \
      docker-book-generator
    shift;;

  -s|--screen)
    mkdir -p manuscript && cp -r $2/* ./manuscript
    docker run -it --rm \
      --volume $PWD:/data \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      --entrypoint ./src/scripts/pdf_for_screen.sh \
      docker-book-generator
    shift;;

  -e|--epub)
    mkdir -p manuscript && cp -r $2/* ./manuscript
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
    ./convert.sh -p $2; ./convert.sh -s $2; ./convert.sh -e $2
    shift;;

  --)
    break;;

   *)
    printf "Unknown option %s\n" "$1"
    exit 1;;
esac

rm -rf manuscript
