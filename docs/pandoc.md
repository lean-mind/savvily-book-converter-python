# Pandoc

You won't be able to use the main `convert.sh` script.

In stead, you'll have to manually run the individual script you are interested in (they can be found under `src/scripts`)

For these to work they must be invoked from the project's root, where they expect to find a directory called `manuscript`.

This directory must contain the full manuscript with the expected format and structure.

## TODO.Link to installation resources for dependencies

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
