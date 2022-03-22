#!/bin/sh
set -e

cd ./output

mv ebook.epub ebook.zip

mkdir epub-version

mv ebook.zip ./epub-version && cd ./epub-version

unzip ebook.zip && rm ebook.zip

cd ./EPUB/text/

find . -maxdepth 1 -name "ch*.xhtml" -exec sed -i '' 's/<pre title="\([A-z]*\)".*/<code class="language">\1<\/code>\n&/' {} \;

cd ../..

zip ebook.zip -r EPUB META-INF mimetype

mv ebook.zip ebook.epub

mv ebook.epub ../

cd ..

rm -rf ./epub-version
