# Code block

Code block are being configurated [listing package](https://texdoc.org/serve/listings.pdf/0)

All information in web related with code blocks is finding as `listings`.

## Define colors

```latex
\definecolor{color-variable-name}{HTML}{F5F5F5}
```

## Basic configuration

All style configuration have to be set inside `\lstdefinestyle` command as follows.

```latex
\lstdefinestyle{listing_style_name}{
  ...
}
```

## Caption

To configure caption it is necessary to keep in mind two types of configurations:
1. Caption configuration
2. Listing configuration related to caption

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

Listing configuration related to caption position.

```latex
...
    aboveskip        = 1.0em,
    belowskip        = 0.1em,
    abovecaptionskip = 0em,
    belowcaptionskip = 0.4em
...
```
