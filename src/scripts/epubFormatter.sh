#!/bin/sh
set -e

cd ./output

mv ebook.epub ebook.zip

mkdir epub-version

mv ebook.zip ./epub-version && cd ./epub-version

unzip ebook.zip && rm ebook.zip

cd ./EPUB/text/

find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' -E 's/<pre title="([A-z]*#?)".*/<code class="language">\1<\/code>\n&/' {} \;

cp ../../../../src/user-details-for-watermark.txt .

add_watermark_for_epub() {
  pathUserDetails=./user-details.txt
  name=$(cut -d ';' -f1 $pathUserDetails)
  email=$(cut -d ';' -f2 $pathUserDetails)
  dni=$(cut -d ';' -f3 $pathUserDetails)
  find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' -E 's/<\/body>/<br\/><br\/><section class='\"section-user-data\"'><p>'"$name"'<\/p><p>'"$email"'<\/p><p>'"$dni"'<\/p><\/section>\n&/' {} \;
}

add_watermark_for_epub

cd ../..

zip ebook.zip -r EPUB META-INF mimetype

mv ebook.zip ebook.epub

mv ebook.epub ../

cd ..

rm -rf ./epub-version
