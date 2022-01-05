# Manuscript Structure

In order to execute the conversion properly the <manuscript-dir> should follow this structure:

```
<manuscript-dir>
├── 0_Chapter.md
├── 1_Chapter.md
├── ...
├── resources
│   ├── book-cover-screen.png
│   ├── book-cover-print.png
│   ├── ...
├── closing
│   ├── 0_Thanks.md
│   ├── 1_Author.md
│   ├── 2_Bibliography.md
│   ├── 3_Savvily.md
│   ├── ...
├── ...
```

This directory can be located and named wherever and however you prefer.

> If you are not using docker **must** call your manuscript directory ".manuscript" and place it **exactly** at the projects root.

## Closing directory

The inclusion of a `/closing` directory is suggested but not strictly necessary.

You'll want to add to it the parts of the manuscript you expect to **not** be included in the Table of Contents.

## Chapter numeration

The chapters file names must begin with a number sequentially, for example:

- 0_fancyChapterName1.md
- 1_fancyChapterName2.md
- 2_fancyChapterName3.md

> Files not starting with a number will not be rendered.

Just like the chapters of your manuscript, you need to numerate the files in the `/closing` directory (if you choose to include one).

We suggest you follow the order in the example above, but this is ultimately up to you.

## Chapter beginning

Each chapter needs to begin with a `h1` heading to be included in table of contents.

Sections and subsections should follow suit.

## File types

At the moment the scripts accept both `.md` and `.txt`.

> File with any other termination will be not be rendered.

The ability to accept `.txt` is likely to be removed in the future and in any case you should provide a manuscript written strictly in common **markdown**.

## Manuscript constrains

- All files must be as LF.
- This list constructions is not allowed (list and inline code): * `Practices = Principles(Context)`
