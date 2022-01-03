# Starting section

> This configuration can be found in `starting.tex`.
> 
> This portion includes everything from the book cover up to the table of contents.
> 
> It consists of different subsections placed sequentially based on custom requirements.

## Book Cover

The book cover is added by using this command.

```latex
\usepackage{wallpaper}
\ThisTileWallPaper{17.9cm}{23.5cm}{./resources/book-cover.png}
```

This command generates a new page with a background image, so it is needs to be used like so:

```latex
\begin{document}
  \ThisTileWallPaper{17.9cm}{23.5cm}{./resources/book-cover.png}
\end{document}
```

![book cover](resources/images/book-cover.png)

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

A page dedicated to copyright and other such legal information.

```latex
\begin{titlepage}\thispagestyle{empty}
  \vspace*{\fill}
  {\normalsize © <Author name>, 2021 \par}
  {\normalsize © <Editorial Name>, S.L., 2022 \par}
  {\normalsize © Editor: <Editor name> \par}
  {\normalsize © Front cover ilustration: <Ilustrator name> \par}
  {\normalsize © Artistic direction: <Director name> \par}
  {\normalsize © Printing \par}
  {\normalsize Printed in Spain – Printed in <Country name> \par}
  {\normalsize <Printing company name> \par}
  {\normalsize ISBN: <ISBN number> \par}
  {\normalsize Legal deposit: <Deposit number> \par}
\end{titlepage}
```

## Dedication

We can modify the dedication positioning by adjusting its margins with `\newgeometry`.

```latex
\begin{titlepage}\thispagestyle{empty}
  \newgeometry{left=10.5cm, right=2cm, top=8.5cm, bottom=2.5cm}
  {\itshape\small\raggedleft Fancy dedication for whom this book is possible. \par}
  \restoregeometry
\end{titlepage}
```
