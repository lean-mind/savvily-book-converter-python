#!/bin/sh

cd codigo-sostenible/manuscript

find . -name "[0-9]*.txt" | sort -V | xargs 			\
pandoc   																					\
		--pdf-engine=xelatex                    			\
		--template=../../custom-report.tex      			\
		--listings                              			\
		-V documentclass=report                 			\
		-o ./../../output/book_for_screen.pdf 				\
&& echo "PDF for screen successfully generated"
