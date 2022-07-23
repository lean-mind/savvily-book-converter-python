<br />
<div align="center">
  <a href="https://github.com/lean-mind/savvily-book-converter-python">
    <img src="resources/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Savvily Book Converter</h3>

  <p align="center">
    Easily convert your markdown manuscript into a pdf and/or epub book!
  </p>
</div>

# Getting started

## A note about Docker

The following instructions will rely on docker to run the project and generate the documents.

This is by far the easiest way to interact with the project, but if you want (or need) to do it the hard way, have a look over [here](pandoc).

## Docker

Get it [here](https://docs.docker.com/get-docker/)!

Remember to configure it to [start on boot](https://docs.docker.com/engine/install/linux-postinstall/#configure-docker-to-start-on-boot) and to make it [manageable](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for non-root users.

## Install

Clone the repo and `cd` into it:

```bash
git clone git@github.com:lean-mind/savvily-book-converter-python.git savvily && cd savvily
```

Generate docker image:

```bash
docker build -t "savvily-book-generator" $PWD
```

Make sure to run this command from the project's root directory and do not change the name of the image (or do so in `convert.sh` as well).

## How to run the project

From the project root directory:

`./convert.sh FLAG [MANUSCRIPT_PATH]`

The script expects both a flag determining the wanted output format and a path (relative or absolute) to your [manuscript](manuscript).
If no path is given the output will be generated under the sample book under `fixtures/sample-manuscript/`

The available flags are:

```
-p or --print --> Generates a pdf for printing
-s or --screen --> Generates a pdf for screen viewing
-e or --epub --> Generates an epub
-a or --all --> All of the above
```

You'll find the output in the `output/` directory.
