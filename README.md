Easily convert you markdown manuscript to a pdf and/or epub book!

Full documentation can be found [here](https://lean-mind.github.io/codigo-sostenible-book-converter-format/).

# Pre-Requisites

The easiest way to run this project is with Docker.

If you'd rather not use it (or can't), you'll have to install Latex and some other dependencies (see [below](#latex)).

## Docker

Get it [here](https://docs.docker.com/get-docker/)!

<a name="latex"/>

## Without Docker

### LaTeX

Make sure you have both `pandoc` and `basictex` installed and working on your system.

Install the next libraries with the TeX Live Manager (tlmgr) as admin:

```shell
tlmgr update --self && tlmgr install tocloft && tlmgr install emptypage && tlmgr install footmisc && tlmgr install titlesec && tlmgr install wallpaper && tlmgr install roboto && tlmgr install incgraph && tlmgr install tcolorbox && tlmgr install environ
```

### Ghostscript

The scripts use Ghostscript to do a final merge of the complete book (if converting to PDF), make sure its installed and available in your systems `PATH`.

### Sed

GNU's version of sed is needed for the book to render properly.

Ensure you have the right version on your machine (Busybox, BSD, Alpine Linux and Mac OS users might have to install a different version).

An easy way to check if you sed flavour is causing issues is to have a look at the code block's language tags.

If you see `\uLANGUAGE_NAME` with no capitalization, you'll need to install the GNU version.

# Getting started

Clone the repo and `cd` into it:

`git clone git@github.com:lean-mind/savvily-book-converter.git && cd codigo-sostenible-book-converter-format`

You can ignore the `docs` directory.

If you are installing without docker, you'll notice the Dockerfile contains the same dependencies you had to install.

**That** is your reference in case of dependency issues.

If you are installing with docker now is a good time to build the image. Run:

`docker build -t "savvily-book-generator" $PWD`

Make sure you run this command from the project's root directory (where the Dockerfile is located) and do not change the name of the image (or do so in `convert.sh` as well).

# How to run the project

## With Docker

From the project root directory:

`./convert.sh [FLAG] [MANUSCRIPT_PATH]`

The script expects **both** a flag determining the wanted output format **and** a path (relative or absolute) to the manuscript.

The available flags are:

```
-p or --print --> Generates a pdf for printing
-s or --screen --> Generates a pdf for screen viewing
-e or --epub --> Generates an epub (standard and mobi-redy)
-a or --all --> All of the above
```

You'll find the output in the `output` directory.

## Without Docker

You won't be able to use the main `convert.sh` script.

In stead, you'll have to manually run the individual script you are interested in (they can be found under `src/scripts`)

For these to work they must be invoked from the project's root, where they expect to find a directory called `manuscript`.

This directory must contain the full manuscript with the expected format and structure.

## Manuscript Structure

## TODO.Link to installation resources for dependencies
