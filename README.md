This project is used to convert Carlos Blé's book "Código Sostenible" to different formats.
It does the conversion from markdown files using Pandoc. This tool needs LaTeX to run.

# Project contents:

- ***codigo-sostenible*** (folder): It is a submodule linked to the repository that contains the markdown files with the book.


- ***JetBrains_Mono*** (folder): Contains needed fonts to run the project.


- ***output*** (folder): Contains the converted files.


- ***\*.tex*** (files): Contain the LaTeX templates with the custom styles used for the conversion.


- ***\epub.css***: Contains the style used to convert from markdown files to epub.


- ***metadata.yml***: Contains the metadata related to the book.


There are different scripts to convert from markdown files:

- "***process_book.sh***": This script converts the manuscript files to a pdf file (version to print).


- "***process_report.sh***": This script converts the manuscript files to a pdf file (digital version).


- "***process_ebook.sh***": This script converts the manuscript files to an epub file (eReaders version).


- "***process_cover.sh***": This script converts the book cover image to a pdf file.
  It is automatically run before any of the others scripts.


# How to clone this project including the submodule

Clone the repository with the command:

`git clone git@github.com:lean-mind/codigo-sostenible-book-converter-format.git`

Navigate into the root folder

`cd codigo-sostenible-book-converter-format`

Init and update the submodule:

`git submodule update --init --recursive`


# How to run this project

## Run with Docker (not available for MAC OS X - Apple Silicon)

Open your terminal in the root folder of the project (or where the _Dockerfile_ is located). 
Type the next command to create a docker image (the image will be created from the _Dockerfile_ configuration):

`docker build -t "DOCKER_IMAGE_NAME" .`

Now, run the image specifying the entrypoint (this is the script which will make the conversion):


Command for UNIX:
```Bash
docker run --rm --volume $PWD:/data --entrypoint "./nameOfTheScript.sh" DOCKER_IMAGE_NAME
```

Command for Windows:
```Bash
docker run --rm --volume $PWD\:/data --entrypoint "./nameOfTheScript.sh" DOCKER_IMAGE_NAME
```



## Run without Docker

### Install LaTeX in your system (MAC OS X)

Go to your terminal and type the next command to install Pandoc:

`brew install pandoc`

Once it has been installed it, type the next command to install LaTeX:

`brew install basictex`

Afterwards, install _poppler_ library to be able to render PDF with pdfunite:

`brew install poppler`

After that, apply changes with:

`eval "$(/usr/libexe.ae/path-helper)"`

Install the next libraries with the TeX Live Manager (tlmgr) as admin:

`sudo tlmgr install titlesec`

`sudo tlmgr install wallpaper`

`sudo tlmgr install incgraph`

`sudo tlmgr install roboto`

If you haven't got the font Jetbrains Mono, you need to install it. 
You can simply double click in the font file and follow the suggested steps.

### Run the script to start the conversion with:

`./nameOfTheScript.sh`

NOTE: In case there is some other library added to the project but it has not been included in this README.md,
when executing the command to make the conversion with Latex the terminal will ask you to install it.


### Known errors

#### Code line separator format mismatch

The terminal shows the following error:

```Bash
standard_init_linux.go:228: exec user process caused: no such file or directory
```

Solution: Use your favourite IDE to open the project and change the "line separator" format to LF.
(In Intellij IDEA: find that option in the tool-bar at the bottom right of the window.
