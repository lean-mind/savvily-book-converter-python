# Project Tour

At the project root you'll find the `Dockerfile` and the `convert.sh` script.

## convert.sh

We went over how to use the script [here](/#how-to-run-the-project).

Basically it works by launching a `docker run` command based on the given flags and path.
You'll see it uses some other scripts, we'll go over them later.

It also makes a temporary copy of the manuscript and cleans after itself.

## src/

You'll find two important directories under `src`, `scripts` and `templates`.

- In `scripts` you'll see the above-mentioned scripts. These are the ones doing the heavy lifting. Pre-processing, rendering and merging (if necessary) is done here.
- In `templates`, you'll find the relevant files for each conversion type, `.tex` for the [PDFs](basic-commands) and `.css`, `.yml` and `.theme` [e-pubs](epub).

