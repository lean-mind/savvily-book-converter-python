# Table of contents

This section is generated between starting section and first book chapter.

## Basic configuration

The table of content is generated based on headings.

> chapter = h1 | #
> section = h2 | ##
> subsection = h3 | ###

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

The dot density can be configured with this command.

```latex
\usepackage{tocloft}
\renewcommand\cftdotsep{5}
```

## Indent

The indent is removed with this command.

```latex
\setlength{\cftsecindent}{-8pt}
\setlength{\cftsubsecindent}{4pt}
```

## Hyperlinks

To add hyperlinks to table of content it is only needed to use this package.

```latex
\usepackage[hidelinks]{hyperref}
```
