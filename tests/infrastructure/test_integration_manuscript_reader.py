from infrastructure.ManuscriptReader import ManuscriptReader
import tests.infrastructure.fixtures.reader_dummy_manuscript_full_md as full_text


class TestReader:
    reader = ManuscriptReader()

    def test_whole_manuscript_is_read(self):
        manuscript_content = self.reader.readFrom("tests/infrastructure/fixtures/reader-dummy-manuscript")
        assert manuscript_content == full_text.content
