import re


class ChapterSorter:
    def sort(self, chapter_names: list) -> list:
        index_separator = '_'
        valid_filenames = self._filter_valid_chapter_names(chapter_names, index_separator)

        def chapters_indexes_as_integers(valid_filename):
            chapter_index = valid_filename.split(index_separator)[0]
            return int(chapter_index)

        return sorted(valid_filenames, key=chapters_indexes_as_integers)

    def _filter_valid_chapter_names(self, chapters: list, separator: str) -> list:
        chapter_index = r'^(\d+)'
        index_separator = '_'
        chapter_name = r'.*'
        markdown_ext = '.md'
        text_ext = '.txt'
        valid_md = re.compile(f"{chapter_index}{index_separator}{chapter_name}{markdown_ext}")
        valid_txt = re.compile(f"{chapter_index}{index_separator}{chapter_name}{text_ext}")
        return [
            chapter_filename for chapter_filename in chapters
            if valid_md.match(chapter_filename) or valid_txt.match(chapter_filename)
        ]
