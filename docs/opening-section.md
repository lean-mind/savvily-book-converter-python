# Opening section

> This configuration can be found in `opening.tex` inside src/templates/`<doc_type>`/.
>
> This portion includes everything from the book cover up to the table of contents.
>
> It consists of different subsections placed sequentially based on custom requirements.

This template uses the `datatool` package to read from a file named `pub-data` located in `resources/` within your book.
This is done in the following lines:

```latex
\usepackage{datatool}

\DTLsetseparator{ = }
\DTLloaddb[noheader, keys={key,value}]{publishing-data}{./resources/pub-data}
\newcommand{\valueOf}[1]{\DTLfetch{publishing-data}{key}{#1}{value}}
```

This creates a command `valueOf` with which we can read the wanted value from the file (given a `KEY = VALUE` structure, spaces matter).

It is used throughout the file like so: `\valueOf{Title}`

This allows us to achieve custom opening sections while following a general structure and allowing the final
users to modify legal and copyright information according to its needs without having to interact with LaTeX directly.

## Book Cover

The book cover is added by using this command:

```latex
\usepackage{wallpaper}
\begin{document}
  \ThisTileWallPaper{17.9cm}{23.5cm}{./resources/book-cover.png}
\end{document}
```

It generates a new page with a background image, so it is needs to be used following the example.

![book cover](resources/images/book-cover.png)

> The size image has to be equal to page size.

> It is necessary to add a `book-cover.png` in manuscript resources folder.

## Title page

Blank page with the book title.

We use a blank line to add space between title and page top border and help with formatting.

```latex
\begin{titlepage}
  {\large\phantom{blabla} \par}
  \vspace{1cm}
  {\huge\centering Fancy Book Title \par}
\end{titlepage}
```

## Half-title page

Blank page with the book title, note, author name and logo.

> It is necessary to add a `logo.png` in manuscript resources folder.

```latex
\begin{titlepage}\thispagestyle{empty}
  {\large\phantom{blabla} \par}
  \vspace{1cm}
  {\scshape\Huge\centering Book Title \par}
  \vspace{0.5cm}
  {\normalsize\centering Fancy Note \par}
  \vspace{1cm}
  {\large\centering Author \par}
  \vspace{8.5cm}
  \begin{center}
    {\includegraphics[scale=0.20]{./resources/logo.png}}
  \end{center}
\end{titlepage}
```

## Back half-title page

A page dedicated to copyright and other information.

```latex
\begin{titlepage}\thispagestyle{empty}
  \vspace*{\fill}
  {\normalsize © <Author name>, 2021 \par}
  {\normalsize © <Editorial Name>, S.L., 2022 \par}
  {\normalsize © Editor: <Editor name> \par}
  {\normalsize © Front cover ilustration: <Ilustrator name> \par}
  {\normalsize © Artistic direction: <Director name> \par}
  {\normalsize © Printing \par}
  {\normalsize Printed in <Country name> \par}
  {\normalsize <Printing company name> \par}
  {\normalsize ISBN: <ISBN number> \par}
  {\normalsize Legal deposit: <Deposit number> \par}
\end{titlepage}
```

## Dedication

We can modify the dedication position by adjusting page margins with `\newgeometry`.

```latex
\begin{titlepage}\thispagestyle{empty}
  \newgeometry{left=10.5cm, right=2cm, top=8.5cm, bottom=2.5cm}
  {\itshape\small\raggedleft Fancy dedication for whom this book is possible. \par}
  \restoregeometry
\end{titlepage}
```
