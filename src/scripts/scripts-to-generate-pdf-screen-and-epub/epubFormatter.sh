#!/bin/sh
set -e

cd ./output

add_watermark_for_epub() {
  name="$1"
  email="$2"
  if [ -z "$name" ]; then
    name="$(echo $email | sed 's/\(.*\)\@.*/\1/')"
  fi
  find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' -E 's/<\/body>/<br\/><br\/><section class='\"section-user-data\"'><p>'"$name"'<\/p><p>'"$email"'<\/p><p>'"$dni"'<\/p><\/section>\n&/' {} \;
}

#name=$(echo "$line" | cut -d ';' -f1)
#username="$(echo $name | sed 's/ /_/g')"
username="$(echo $email | sed 's/\(.*\)\@.*/\1/')" # user_surname@gmail.com -> user_surname

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

add_watermark_for_epub "$1" "$2"

cd ../..

zip codigo_sostenible_"$username".zip -r EPUB META-INF mimetype

mv codigo_sostenible_"$username".zip codigo_sostenible_"$username".epub

mv codigo_sostenible_"$username".epub ../

cd ..

rm -rf ./epub-version-"$username"

mkdir -p codigo_sostenible_"$username"

mv codigo_sostenible_"$username".epub codigo_sostenible_"$username"

cd ..
