# Page style

The page style make use of [fancyhdr](http://tug.ctan.org/tex-archive/macros/latex/contrib/fancyhdr/fancyhdr.pdf)
package. This package is used to apply style to page header and footer.

## Config

This config allows to show the title chapter on odd pages with position on right side.

Otherwise, it changes the footer number page to a small size.

```latex
\usepackage{fancyhdr}
\pagestyle{fancy}

\fancypagestyle{MyStyle}{
    \fancyhf{}
    \fancyhead[LE]{\footnotesize\color{gray}\rightmark}
    \fancyhead[RO]{\footnotesize\color{gray}\leftmark}
    \renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{##1}}{}}
    \renewcommand{\sectionmark}[1]{\markright{##1}}
    \fancyfoot[C]{\fontfamily{\sfdefault} \thepage}
}

\renewcommand{\headrulewidth}{0pt}
\renewcommand*{\thepage}{\footnotesize\arabic{page}}
```
