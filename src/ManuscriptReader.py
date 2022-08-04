import os
import re


class ManuscriptReader:
    def read(self, path: str) -> str:
        chapters_filenames = self.get_sorted_chapters(path)
        read_chapters = []
        for file in chapters_filenames:
            with open(f"{path}/{file}", "r") as f:
                read_chapters.append(self._list_to_string(f.readlines()))
        return self._list_to_string(read_chapters)

    def read_chapters(self, path: str, chapters_filenames: list) -> str:
        read_chapters = []
        for file in chapters_filenames:
            with open(f"{path}/{file}", "r") as f:
                read_chapters.append(self._list_to_string(f.readlines()))
        return self._list_to_string(read_chapters)

    def get_sorted_chapters(self, path: str) -> list:
        manuscript_chapters = os.listdir(path)
        index_separator = '_'
        valid_filenames = self._filter_valid_chapter_names(manuscript_chapters, index_separator)

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

    def _list_to_string(self, list: list) -> str:
        return "".join(list)
