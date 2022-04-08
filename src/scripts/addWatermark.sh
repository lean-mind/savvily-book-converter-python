#!/bin/sh
set -e

pathUserDetails=../src/user-details-for-watermark.txt
name=$(cut -d ';' -f1 $pathUserDetails)
email=$(cut -d ';' -f2 $pathUserDetails)
dni=$(cut -d ';' -f3 $pathUserDetails)

add_watermark_for_pdf_screen() {
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} name}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$name"'}}}/' ../src/templates/screen/custom-report.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} email}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$email"'}}}/' ../src/templates/screen/custom-report.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} dni}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$dni"'}}}/' ../src/templates/screen/custom-report.tex

  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} name}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$name"'}}}/' ../src/templates/screen/opening.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} email}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$email"'}}}/' ../src/templates/screen/opening.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} dni}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$dni"'}}}/' ../src/templates/screen/opening.tex
}

reset_watermark_for_pdf_screen() {
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$name"'}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} name}}}/' ../src/templates/screen/custom-report.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$email"'}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} email}}}/' ../src/templates/screen/custom-report.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$dni"'}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} dni}}}/' ../src/templates/screen/custom-report.tex

  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$name"'}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} name}}}/' ../src/templates/screen/opening.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$email"'}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} email}}}/' ../src/templates/screen/opening.tex
  sed -i 's/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} '"$dni"'}}}/\\rotatebox{0}{\\textsf{\\textbf{\\color{darkgray} dni}}}/' ../src/templates/screen/opening.tex
}

if [ "$1" == "screen" ]
then
  add_watermark_for_pdf_screen
fi

if [ "$1" == "reset" ]
then
  reset_watermark_for_pdf_screen
fi

