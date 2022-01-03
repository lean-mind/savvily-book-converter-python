# Basic latex commands

## Document structure

Latex use a layout as base [document structure](https://en.wikibooks.org/wiki/LaTeX/Document_Structure).
It is needed to be declared at the beginning of latex file.

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

## Add margin between lines

```latex
{\normalsize Top line \par}
\vspace{1cm}
{\normalsize Bottom line \par}
```

## Center

```latex
\begin{center}
    {\includegraphics[scale=0.20]{./resources/logo.png}}
\end{center}
```

## Move all to bottom

```latex
\begin{titlepage}\thispagestyle{empty}
  \vspace*{\fill}
  {\normalsize This text will appear on bottom \par}
\end{titlepage}
```
