from src.domain.Manuscript import Manuscript
import tests.fixtures.data.new_print_format_md as new_print_format_fixture
import tests.fixtures.data.legacy_basic_format_md as legacy_format_fixture
import tests.fixtures.data.no_format_md as full_text_fixture


class TestManuscript:

    def test_epub_format(self):
        broken_md = Manuscript(full_text_fixture.content)
        formatted_md = broken_md.epub_format()
        assert str(formatted_md) == legacy_format_fixture.content

    def test_screen_pdf_format(self):
        broken_md = Manuscript(full_text_fixture.content)
        formatted_md = broken_md.screen_pdf_format()
        assert str(formatted_md) == legacy_format_fixture.content

    def test_print_pdf_format(self):
        broken_md = Manuscript(full_text_fixture.content)
        formatted_md = broken_md.print_pdf_format()
        assert str(formatted_md) == new_print_format_fixture.content
