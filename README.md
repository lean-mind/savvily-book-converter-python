<br />
<div align="center">
  <a href="https://github.com/lean-mind/savvily-book-converter-python">
    <img src="docs/resources/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Savvily Book Converter [Python]</h3>

  <p align="center">
    Easily convert your markdown manuscript into a pdf and/or epub book!
    <br />
    <a href="https://lean-mind.github.io/savvily-book-converter-python/#/"><strong>Explore the docs »</strong></a>
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

To format the Markdown, Pandoc uses [Latex](https://www.latex-project.org/).
Latex is a composition text system and it counts with endless format configurations.

Full documentation can also be found [here](https://lean-mind.github.io/savvily-book-converter-python/#/).

## Prerequisites

The easiest way to run this project is with Docker.

If you'd rather not use it (or can't), you'll have to install Latex and some other dependencies (see [the
documentation](https://lean-mind.github.io/savvily-book-converter-python/#/)).

## Getting started

1. Clone the repo and `cd` into it:

```
git clone git@github.com:lean-mind/savvily-book-converter-python.git savvily && cd savvily
```

2. Build the Docker Image with:

```
docker build -t "savvily-book-generator" $PWD
```

3. Output should be found in the `output` directory.

## Config

You'll find a file called `pub-data`.
It contains a list of **necessary** fields to produce proper legal and copyright information within the opening
section of the book.

It has some sample data by default but make sure to update this with your specific information.

Also, consider that the given format must be respected:

- The keys **must** be named as they are.
- Keys and values **must** be separated by `[ = ]` (excluding brackets of course), spaces do matter.

## Usage

From the project root directory:

`./convert.sh FLAG [MANUSCRIPT_PATH]`

The script expects both a flag determining the wanted output format and a path (relative or absolute) to your [manuscript](manuscript).

If no path is given the output will be generated under the sample book under `sample-manuscript/`

The available flags are:

```
-p or --print --> Generates a pdf for printing
-s or --screen --> Generates a pdf for screen viewing
-e or --epub --> Generates an epub (standard and mobi-redy)
-a or --all --> All of the above
```

If you are not using docker, check the [docs](https://lean-mind.github.io/savvily-book-converter-python/#/) to see how to run
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
├── ...
```

Keep in mind that the Chapters name **must** follow the format `number_name` for the script to work!

For more information regarding this, check the [docs](https://lean-mind.github.io/savvily-book-converter-python/#/manuscript).
