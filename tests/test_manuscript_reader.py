from infrastructure.ManuscriptReader import ManuscriptReader
import tests.fixtures.data.no_format_md as full_text


class TestReader:
    reader = ManuscriptReader()

    def test_files_are_sorted(self):
        sorted_chapters = self.reader.get_sorted_chapters("tests/fixtures/sample-manuscript")
        print(sorted_chapters)
        expected_files = ["01_chapter.md", "02_chapter.md", "3_empty_chap.md", "10_empty_chapter.md"]
        assert sorted_chapters == expected_files

    def test_whole_manuscript_is_read(self):
        manuscript_content = self.reader.readFrom("tests/fixtures/sample-manuscript")
        assert manuscript_content == full_text.content
