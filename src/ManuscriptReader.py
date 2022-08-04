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
        manuscript = os.listdir(path)
        digits = re.compile(r'(\d+)')
        separator = re.compile('_')
        filenames = [file for file in manuscript if re.match(r"\d+_.*\.md|\d+_.*\.txt", file)]

        def preceding_digits_as_integers(filename):
            filename_index = separator.split(filename)[0]
            return int(filename_index)

        return sorted(filenames, key=preceding_digits_as_integers)

    def _list_to_string(self, list: list) -> str:
        return "".join(list)
