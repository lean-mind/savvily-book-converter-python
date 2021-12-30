<br />
<div align="center">
  <a href="https://github.com/lean-mind/savvily-book-converter">
    <img src="resources/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Savvily Book Converter</h3>

  <p align="center">
    Easily convert your markdown manuscript into a pdf and/or epub book!
    <br />
    <a href="https://lean-mind.github.io/savvily-book-converter/#/"><strong>Explore the docs »</strong></a>
    <br />
    </p>
</div>

## Pre-Requisites

The easiest way to run this project is with Docker.

If you'd rather not use it (or can't), you'll have to install Latex and some other dependencies (see [below](#latex)).

## Docker

Get it [here](https://docs.docker.com/get-docker/)!

# Getting started

Clone the repo and `cd` into it:

```bash
git clone git@github.com:lean-mind/savvily-book-converter.git && cd codigo-sostenible-book-converter-format
```

Generate docker image:

```bash
docker build -t "savvily-book-generator" $PWD
```

If you are installing with docker now is a good time to build the image. Run:

`docker build -t "savvily-book-generator" $PWD`

Make sure you run this command from the project's root directory (where the Dockerfile is located) and do not change the name of the image (or do so in `convert.sh` as well).

You'll find two important directories under `src`, `scripts` and `templates`.

- These scripts are the ones doing the heavy lifting. Pre-processing ,rendering and merging is done here.
- In templates you'll find the relevant `.tex` files for each conversion type. Modify them at you own risk!

# How to run the project

## Docker

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
