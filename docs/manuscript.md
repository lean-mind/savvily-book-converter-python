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
│   ├── pub-data
│   ├── ...
├── ...
```

This directory can be located and named wherever and however you prefer.

> If you are not using docker **must** call your manuscript directory ".manuscript" and place it **exactly** at the projects root.

## Chapter numeration

The chapters file names must begin with a number sequentially, for example:

- 0_fancyChapterName1.md
- 1_fancyChapterName2.md
- 2_fancyChapterName3.md

> Files not starting with a number will not be rendered.

## Chapter beginning

Each chapter needs to begin with a `h1` heading to be included in table of contents.

Sections and subsections should follow suit.

## File types

At the moment the scripts accept both `.md` and `.txt`.

> File with any other termination will be not be rendered.

The ability to accept `.txt` is likely to be removed in the future and in any case you should provide a manuscript written strictly in common **markdown**.

## Publisher data

You'll need to provide a file called `pub-data` within your `resources/` directory.
It shall contain a list of **necessary** fields to produce proper legal and copyright information within the opening
section of the book.

You can take the one provided as part of the sample-manuscript as reference.
The keys must be the same as the ones provided, but make sure to update the values with your specific information.

Also, consider that the given format must be respected:

- The keys **must** be named as they are.
- Keys and values **must** be separated by `[ = ]` (excluding brackets of course), spaces do matter.

## Manuscript constrains

- No references can contain links. This will break the link when processing a print-ready PDF.
- Referencing long URLs (which includes regular links for the print-ready version) will break the footnotes format.
Use URL shorteners like [bitly](https://bitly.com/).
- Code blocks are not exempt from link processing and reference conversion. Only links of the format `[0](1)` will be excluded. This
  means that:
    - The structure `[foo](bar)` inside a code block **will** be considered a link.
    - A code block containing a line with `[foo](bar)` **will** break for the print-ready PDF.
- No list item can contain inline code:

```
Good List:
- First item
* Second item

Bad List:
- `First item`
* `Second` item

```
