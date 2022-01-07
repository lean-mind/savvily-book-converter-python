# Table of contents

This section is also known as Index and is currently being generated between the [opening section](opening-section) and the first chapter of the book.

## Basic configuration

The table of content is generated based on headings.

> chapter = h1 | #
>
> section = h2 | ##
>
> subsection = h3 | ###

And is set with these commands:

```latex
\usepackage{titletoc}
\titlecontents{chapter}[0em]
    {\vspace{0em}
    {\normalfont\bfseries}
    {}
    {\enspace\dotfill\contentspage}

\titlecontents{section}[0em]
    {\vspace{-0.5em}}
    {\normalfont\sffamily\relax}
    {}
    {\enspace\small\dotfill\contentspage}

\titlecontents{subsection}[0em]
    {\vspace{-0.7em}}
    {}
    {}
    {\enspace\small\dotfill\contentspage}
```

## Dots

The dot density (between the chapter names and corresponding page numbers) can be configured with this command.

```latex
\usepackage{tocloft}
\renewcommand\cftdotsep{5}
```

## Indent

The default indent is removed with this command.

```latex
\setlength{\cftsecindent}{-8pt}
\setlength{\cftsubsecindent}{4pt}
```

## Hyperlinks

Add clickable links to the Table of Contents by simply including this package:

```latex
\usepackage[hidelinks]{hyperref}
```

## Numeration

These commands delete the chapter numeration from the table of content.

```latex
\makeatletter
\renewcommand{\cftchappresnum}{\begin{lrbox}{\@tempboxa}}
\renewcommand{\cftchapaftersnum}{\end{lrbox}}
\makeatother
\makeatletter
\renewcommand{\cftsecpresnum}{\begin{lrbox}{\@tempboxa}}
\renewcommand{\cftsecaftersnum}{\end{lrbox}}
\makeatother
\makeatletter
\renewcommand{\cftsubsecpresnum}{\begin{lrbox}{\@tempboxa}}
\renewcommand{\cftsubsecaftersnum}{\end{lrbox}}
\makeatother
```
