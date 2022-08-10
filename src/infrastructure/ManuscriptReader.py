import os
from infrastructure.ChapterSorter import ChapterSorter
from infrastructure.ChapterValidator import ChapterValidator


class ManuscriptReader:
    sorter = ChapterSorter()
    validator = ChapterValidator()

    def readFrom(self, path: str) -> str:
        manuscript_chapters = os.listdir(path)
        valid_chapters = self.validator.filter(manuscript_chapters)
        chapters_filenames = self.sorter.sort(valid_chapters)

        read_chapters = ""
        for file in chapters_filenames:
            with open(f"{path}/{file}", "r") as f:
                read_chapters += f.read()
        return read_chapters
