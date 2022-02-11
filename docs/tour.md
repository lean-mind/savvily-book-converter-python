# Project Tour

At the project root you'll find the `Dockerfile` and the `convert.sh` script.

## convert.sh

We went over how to use the script [here](/#how-to-run-the-project).

Basically it works by launching a `docker run` command based on the given flags and path.
You'll see it uses some other scripts, we'll go over them later.

It also makes a hidden temporary copy of the manuscript and cleans after itself.

## src/

You'll find two important directories under `src/`: `scripts/` and `templates/`.

- In `scripts/` you'll see the above-mentioned scripts. These are the ones doing the heavy lifting. Pre-processing, rendering and merging (if necessary) is done here.
- In `templates/` you'll find the relevant files for each conversion type, `.tex` for the [PDFs](basic-commands) and `.css`, `.yml` and `.theme` [e-pubs](epub).

## scripts/

### manuscriptFormatter.sh

Processes the manuscript to ensure Pandoc compliance and to facilitate our requirements.

There is a lot of `sed` and regex going on here:

- First it uses `find`, `sort` and `xargs` to organize the manuscript and feed it to `sed`.
- The stream goes through a couple of `sed` commands to ensure proper formatting.
- When rendering a print-ready PDF, there is a separate `sed` command which converts links to references (it looks rather scary but its just Groupings and a lot of escaped parentheses).

### pdf.sh

Takes the output from the previous script and passes it to Pandoc.

It also processes separately the opening section of the book (using `xelatex` directly) and merges the resulting PDFs (with the help of `ghostscript`).

### epub.sh

It passes the output from the formatting script mentioned above to Pandoc with the relevant settings and `css` to
produce an epub according to our styleguides.
