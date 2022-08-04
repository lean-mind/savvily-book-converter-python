from infrastructure.ManuscriptReader import ManuscriptReader
import tests.fixtures.data.no_format_md as full_text


class TestReader:
    reader = ManuscriptReader()

    def test_whole_manuscript_is_read(self):
        manuscript_content = self.reader.readFrom("tests/fixtures/sample-manuscript")
        assert manuscript_content == full_text.content
