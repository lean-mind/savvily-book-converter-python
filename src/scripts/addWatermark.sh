#!/bin/sh
set -e

pathUserDetails=../src/user-details-for-watermark.txt
name=$(cut -d ';' -f1 $pathUserDetails)
email=$(cut -d ';' -f2 $pathUserDetails)
dni=$(cut -d ';' -f3 $pathUserDetails)

username="$(echo $name | sed 's/ /_/g')"

add_watermark_to_template_copy_of_pdf_screen() {
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} name}}/\\textsf{\\textbf{\\color{darkgray} '"$name"'}}/' ../src/templates/screen/.tmp_template_"$username"/custom-report_"$username".tex
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} email}}/\\textsf{\\textbf{\\color{darkgray} '"$email"'}}/' ../src/templates/screen/.tmp_template_"$username"/custom-report_"$username".tex
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} dni}}/\\textsf{\\textbf{\\color{darkgray} '"$dni"'}}/' ../src/templates/screen/.tmp_template_"$username"/custom-report_"$username".tex

  sed -i 's/\\textsf{\\textbf{\\color{darkgray} name}}/\\textsf{\\textbf{\\color{darkgray} '"$name"'}}/' ../src/templates/screen/.tmp_template_"$username"/opening_"$username".tex
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} email}}/\\textsf{\\textbf{\\color{darkgray} '"$email"'}}/' ../src/templates/screen/.tmp_template_"$username"/opening_"$username".tex
  sed -i 's/\\textsf{\\textbf{\\color{darkgray} dni}}/\\textsf{\\textbf{\\color{darkgray} '"$dni"'}}/' ../src/templates/screen/.tmp_template_"$username"/opening_"$username".tex
}

add_watermark_to_template_copy_of_pdf_screen

