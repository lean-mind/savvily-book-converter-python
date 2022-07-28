from ManuscriptReader import ManuscriptReader
import tests.fixtures.data.no_format_md as full_text
import tests.fixtures.data.no_format_ch_01 as ch_01


class TestReader:
    reader = ManuscriptReader("tests/fixtures/sample-manuscript")

    def test_files_are_sorted(self):
        sorted_chapters = self.reader.get_sorted_chapters()
        expected_files = ["01_chapter.md", "02_chapter.md"]
        assert sorted_chapters == expected_files

    def test_whole_manuscript_is_read(self):
        manuscript_content = self.reader.read()
        assert manuscript_content == full_text.content

    def test_slected_chapters_are_read(self):
        selected_chapters = self.reader.read_chapters(["01_chapter.md"])
        assert selected_chapters == ch_01.content
