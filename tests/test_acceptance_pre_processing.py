import src.formatter.EpubFormatter as epubFormatter
import src.formatter.ScreenPDFFormatter as screenPdfFormatter
import src.formatter.PrintPDFFormatter as printPdfFormatter
import tests.fixtures.data.legacy_basic_format_md as legacy_format_fixture
import tests.fixtures.data.legacy_print_format_md as legacy_print_format_fixture


class TestFormatter:
    def test_new_ebook_format(self):
        assert (epubFormatter.run("tests/fixtures/sample-manuscript").read().decode() == legacy_format_fixture.content)

    def test_new_pdf_print_format(self):
        assert (printPdfFormatter.run("tests/fixtures/sample-manuscript").read().decode() == legacy_print_format_fixture.content)

    def test_new_pdf_screen_format(self):
        assert (screenPdfFormatter.run("tests/fixtures/sample-manuscript").read().decode() == legacy_format_fixture.content)
