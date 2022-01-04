# Headers and Footers

We are using the [fancyhdr](http://tug.ctan.org/tex-archive/macros/latex/contrib/fancyhdr/fancyhdr.pdf) package to style headers and footers.

## Configuration

This configuration shows the chapter title on the right side of odd pages.

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
```

This on the other hand, sets the page number in the footer to a smaller size.

```
\renewcommand*{\thepage}{\footnotesize\arabic{page}}
```
