#!/bin/sh
set -e

cd ./output

pathUserDetails="../src/user-details-for-watermark.txt"

add_watermark_for_epub() {
  userInformation=$1
  name=$(echo $userInformation | cut -d ';' -f1)
  email=$(echo $userInformation | cut -d ';' -f2)
  dni=$(echo $userInformation | cut -d ';' -f3)
  find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' -E 's/<\/body>/<br\/><br\/><section class='\"section-user-data\"'><p>'"$name"'<\/p><p>'"$email"'<\/p><p>'"$dni"'<\/p><\/section>\n&/' {} \;
}

while read -r line; do
  name=$(echo "$line" | cut -d ';' -f1)
  username="$(echo $name | sed 's/ /_/g')"

  if [ -d ./epub-version-"$username"/ ]; then
    rm -rf ./epub-version-"$username"/
  fi

  cp ebook.epub codigo_sostenible_"$username".epub

  mv codigo_sostenible_"$username".epub codigo_sostenible_"$username".zip

  mkdir epub-version-"$username"

  mv codigo_sostenible_"$username".zip ./epub-version-"$username" && cd ./epub-version-"$username"

  unzip codigo_sostenible_"$username".zip && rm codigo_sostenible_"$username".zip

  cd ./EPUB/text/

  find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' -E 's/<pre title="([A-z]*#?)".*/<code class="language">\1<\/code>\n&/' {} \;

  add_watermark_for_epub "$line"

  cd ../..

  zip codigo_sostenible_"$username".zip -r EPUB META-INF mimetype

  mv codigo_sostenible_"$username".zip codigo_sostenible_"$username".epub

  mv codigo_sostenible_"$username".epub ../

  cd ..

  rm -rf ./epub-version-"$username"

  mkdir -p codigo_sostenible_"$username"

  mv codigo_sostenible_"$username".epub codigo_sostenible_"$username"

done < "$pathUserDetails"

cd ..
