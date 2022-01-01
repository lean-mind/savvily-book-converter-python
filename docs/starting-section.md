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

## Half-title

This is a page carrying nothing but the title.

It is necessary to add a blank line to add space between title and page top border.

```latex
\begin{titlepage}
  {\large\phantom{blabla} \par}
  \vspace{1cm}
  {\huge\centering Fancy Book Title \par}
\end{titlepage}
```

