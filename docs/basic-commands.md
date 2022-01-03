# Basic latex commands

## Document structure

Latex uses a base [document structure](https://en.wikibooks.org/wiki/LaTeX/Document_Structure) as a layout.

It is needed to be declared at the beginning of latex file, like so:

```latex
\documentclass[10pt]{book}
```

## Set font

```latex
\usepackage[sfdefault]{roboto}
```

## Add blank page

```latex
\newpage\phantom{blabla}\thispagestyle{empty}
```

## Set spacing between two lines

```latex
{\normalsize Top line \par}
\vspace{1cm}
{\normalsize Bottom line \par}
```

## Center an image

```latex
\begin{center}
    {\includegraphics[scale=0.20]{./resources/logo.png}}
\end{center}
```

## Move text to the bottom of the page

```latex
\begin{titlepage}\thispagestyle{empty}
  \vspace*{\fill}
  {\normalsize This text will appear on bottom \par}
\end{titlepage}
```

## Remove numeration from chapters

```latex
\titleformat{\chapter}{\normalfont\Huge\bfseries}{}{0pt}{}
\titleformat{\section}{\normalfont\Large\bfseries}{}{0pt}{}
\titleformat{\subsection}{\normalfont\large\bfseries}{}{0pt}{}
```

## Set custom page number initialization

```latex
\setcounter{page}{9}
```
