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
├── autor.md
├── agradecimientos.md
├── bibliografia.md
├── savvily.md
```

> If you are not using docker to convert the document you need to call your manuscript directory
> "manuscript".

## Chapter numeration

The chapters file names must begin with a number sequentially, for example:
- 0_fancyChapterName1.md
- 1_fancyChapterName2.md
- 2_fancyChapterName3.md

## Chapter beginning

The chapters need to be started with a heading 1 to be included in table of contents.
