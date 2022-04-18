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

  cp ebook.epub ebook_"$username".epub

  mv ebook_"$username".epub ebook_"$username".zip

  mkdir epub-version-"$username"

  mv ebook_"$username".zip ./epub-version-"$username" && cd ./epub-version-"$username"

  unzip ebook_"$username".zip && rm ebook_"$username".zip

  cd ./EPUB/text/

  find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' -E 's/<pre title="([A-z]*#?)".*/<code class="language">\1<\/code>\n&/' {} \;

  add_watermark_for_epub "$line"

  cd ../..

  zip ebook_"$username".zip -r EPUB META-INF mimetype

  mv ebook_"$username".zip ebook_"$username".epub

  mv ebook_"$username".epub ../

  cd ..

  rm -rf ./epub-version-"$username"

done < "$pathUserDetails"
