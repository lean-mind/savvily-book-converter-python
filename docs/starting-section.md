# Starting section

> This configuration can be found in starting.tex files.
> This is the beginning of the book until table of contents.
> Contains different subsections placed sequentially customized based on requirements.

## Book Cover

The book cover is added by using this command.

```latex
\usepackage{wallpaper}
\ThisTileWallPaper{17.9cm}{23.5cm}{./resources/Codigo_Sostenible_Print.png}
```

This command generates a new page with a background image, so it is needed to be used between commands `\begin` and `\end`.

```latex
\begin{document}
  \ThisTileWallPaper{17.9cm}{23.5cm}{./resources/Codigo_Sostenible_Print.png}
\end{document}
```

![book cover](resources/images/book-cover.PNG)

## Title page

This is a page carrying nothing but the title.

It is necessary to add a blank line to add space between title and page top border.

```latex
\begin{titlepage}
  {\large\phantom{blabla} \par}
  \vspace{1cm}
  {\huge\centering Fancy Book Title \par}
\end{titlepage}
```


## Half-title page

This is a page carrying book title, note, author and logo.

> It is necessary to add a logo.png in manuscript resources folder.

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

This is a page which is used to add all information related to the book.

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

We can custom the dedication position by adjusting `\newgeometry` margins.

```latex
\begin{titlepage}\thispagestyle{empty}
  \newgeometry{left=10.5cm, right=2cm, top=8.5cm, bottom=2.5cm}
  {\itshape\small\raggedleft Fancy dedication for whom this book is possible. \par}
  \restoregeometry
\end{titlepage}
```
