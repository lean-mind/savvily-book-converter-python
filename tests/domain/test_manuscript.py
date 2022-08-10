from src.domain.Manuscript import Manuscript
import tests.domain.fixtures.snapshots_v1_0.print_pdf_format_md as print_pdf_format
import tests.domain.fixtures.snapshots_v1_0.screen_pdf_format_md as screen_pdf_format
import tests.domain.fixtures.snapshots_v1_0.epub_format_md as epub_format
import tests.domain.fixtures.unformatted_md as unformatted_md


class TestManuscript:

    def test_epub_format(self):
        broken_md = Manuscript(unformatted_md.content)
        formatted_md = broken_md.epub_format()
        assert str(formatted_md) == epub_format.content

    def test_screen_pdf_format(self):
        broken_md = Manuscript(unformatted_md.content)
        formatted_md = broken_md.screen_pdf_format()
        assert str(formatted_md) == screen_pdf_format.content

    def test_print_pdf_format(self):
        broken_md = Manuscript(unformatted_md.content)
        formatted_md = broken_md.print_pdf_format()
        assert str(formatted_md) == print_pdf_format.content
