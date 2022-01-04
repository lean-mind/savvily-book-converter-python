# Code block

Code block are being rendered using the [listings package](https://texdoc.org/serve/listings.pdf/0)

When searching for documentation or information regarding code blocks, please use the keyword `listings` and thank us later.

## Define colors

```latex
\definecolor{color-variable-name}{HTML}{F5F5F5}
```

## Basic configuration

All style configuration regarding code blocks has to be set inside the `\lstdefinestyle` command as follows:

```latex
\lstdefinestyle{listing_style_name}{
  ...
}
```

## Caption

When setting a caption it is necessary to keep in mind two types of configurations:
1. Caption configuration

```latex
\DeclareCaptionFormat{listing}{{\textwidth+17pt\relax}\vskip1pt#1#2#3}
\captionsetup[lstlisting]{
    format=listing,
    singlelinecheck=false,
    labelformat={empty},
    margin=0pt,
    font={tt, it, scriptsize, color=listing-language},
    labelsep=space,
    labelfont=bf,
    justification=raggedleft
}
```

2. Listing configuration related to caption. 

The following commands for example belong to the `listings` package but set the caption position:

```latex
...
    aboveskip        = 1.0em,
    belowskip        = 0.1em,
    abovecaptionskip = 0em,
    belowcaptionskip = 0.4em
...
```
