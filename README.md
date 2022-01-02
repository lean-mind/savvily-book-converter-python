<br />
<div align="center">
  <a href="https://github.com/lean-mind/savvily-book-converter">
    <img src="docs/resources/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Savvily Book Converter</h3>

  <p align="center">
    Easily convert your markdown manuscript into a pdf and/or epub book!
    <br />
    <a href="https://lean-mind.github.io/savvily-book-converter/#/"><strong>Explore the docs »</strong></a>
    <br />
    </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#prerequisites">Prerequisites</a>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#manuscript_structure">Manuscript</a></li>
  </ol>
</details>

## About The Project

This project make use of [Pandoc](https://pandoc.org/). This is a conversion tool that
provide us the capacity of transform a specific Markdown document to other formats
like pdf or epub.

Full documentation can also be found [here](https://lean-mind.github.io/savvily-book-converter/#/).

## Prerequisites

The easiest way to run this project is with Docker.

If you'd rather not use it (or can't), you'll have to install Latex and some other dependencies (see [the
documentation](https://lean-mind.github.io/savvily-book-converter/#/)).

## Getting started

1. Clone the repo and `cd` into it:

```
git clone git@github.com:lean-mind/savvily-book-converter.git && cd savvily-book-converter
```

2. Build the Docker Image with:

```
docker build -t "savvily-book-generator" $PWD
```

3. Output should be found in the `output` directory.

## Usage

From the project root directory:

```
./convert.sh [FLAG] [MANUSCRIPT_PATH]
```

The script expects **both** a flag determining the wanted output format **and** a path (relative or absolute) to the manuscript.

The available flags are:

```
-p or --print --> Generates a pdf for printing
-s or --screen --> Generates a pdf for screen viewing
-e or --epub --> Generates an epub (standard and mobi-redy)
-a or --all --> All of the above
```

If you are not using docker, check the [docs](https://lean-mind.github.io/savvily-book-converter/#/) to see how to run
the project.

## Manuscript Structure

The Manuscript should follow this structure:

```
<manuscript-dir>
├── 0_Chapter.md
├── 1_Chapter.md
├── ...
├── resources
│   ├── book-cover-screen.png
│   ├── book-cover-print.png
│   ├── ...
├── autor.md
├── agradecimientos.md
├── bibliografia.md
├── savvily.md
```

Keep in mind that the Chapters name **must** follow the format `number_name` for the script to work!

For more information regarding this, check the [docs](https://lean-mind.github.io/savvily-book-converter/#/manuscript).
