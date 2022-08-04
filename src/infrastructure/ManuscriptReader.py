import os
from infrastructure.ChapterSorter import ChapterSorter


class ManuscriptReader:
    def readFrom(self, path: str) -> str:
        sorter = ChapterSorter()
        manuscript_chapters = os.listdir(path)
        chapters_filenames = sorter.sort(manuscript_chapters)

        read_chapters = ""
        for file in chapters_filenames:
            with open(f"{path}/{file}", "r") as f:
                read_chapters += f.read()
        return read_chapters
