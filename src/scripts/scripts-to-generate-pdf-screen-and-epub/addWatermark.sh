#!/bin/sh
set -e

#username="$(echo $name | sed 's/ /_/g')"

username="$(echo "$2" | sed 's/\([A-z]*\).*/\1/')" # user_surname@gmail.com -> user_surname
email="$(echo "$2" | sed 's/_/\\\\_/g')" # user1_surname@gmail.com -> user1\\_surname@gmail.com
name="$1"

add_watermark_to_template_copy_of_pdf_screen() {
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} name}}/\\textsf{\\textbf{\\color{darkgray} '"$name"'}}/' ../src/templates/screen/.tmp_template_"$username"/custom-report_"$username".tex
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} email}}/\\textsf{\\textbf{\\color{darkgray} '"$email"'}}/' ../src/templates/screen/.tmp_template_"$username"/custom-report_"$username".tex

  sed -i 's/\\textsf{\\textbf{\\color{darkgray} name}}/\\textsf{\\textbf{\\color{darkgray} '"$name"'}}/' ../src/templates/screen/.tmp_template_"$username"/opening_"$username".tex
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} email}}/\\textsf{\\textbf{\\color{darkgray} '"$email"'}}/' ../src/templates/screen/.tmp_template_"$username"/opening_"$username".tex
}

add_watermark_to_template_copy_of_pdf_screen

