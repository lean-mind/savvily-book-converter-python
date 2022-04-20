#!/bin/sh
set -e


cd ./output

for i in */; do 
  numberOfFiles=$(ls "${i%/}" | wc -l )
  if [ $numberOfFiles = 2 ]; then
    zip -r "${i%/}.zip" "$i"
    rm -r "${i%/}"
  fi
done \
