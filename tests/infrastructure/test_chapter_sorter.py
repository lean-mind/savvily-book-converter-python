from src.infrastructure.ChapterSorter import ChapterSorter


class TestSorter:
    sorter = ChapterSorter()

    def test_chapters_are_sorted_by_index(self):
        sorted_chapters = self.sorter.sort(["01_chapter.md", "10_chapter.md", "02_chapter.md",
                                           "3_chapter.md", "1_chapter.md", "21_chapter.md"])
        expected_files = [
            "01_chapter.md",
            "1_chapter.md",
            "02_chapter.md",
            "3_chapter.md",
            "10_chapter.md",
            "21_chapter.md"]
        assert sorted_chapters == expected_files
