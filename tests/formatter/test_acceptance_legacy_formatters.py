import src.formatter.legacy.LegacyBasicFormatter as basicFormatter
import src.formatter.legacy.LegacyPrintPDFFormatter as printPdfFormatter
import tests.formatter.fixtures.legacy_epub_format_md as epub_format_md
import tests.formatter.fixtures.legacy_screen_pdf_format_md as screen_pdf_format_md
import tests.formatter.fixtures.legacy_print_pdf_format_md as print_pdf_format_md


class TestFormatter:
    def test_legacy_ebook_format(self):
        assert (basicFormatter.run("tests/formatter/fixtures/sample-manuscript").read().decode() == epub_format_md.content)

    def test_legacy_pdf_print_format(self):
        assert (printPdfFormatter.run("tests/formatter/fixtures/sample-manuscript").read().decode() == print_pdf_format_md.content)

    def test_legacy_pdf_screen_format(self):
        assert (basicFormatter.run("tests/formatter/fixtures/sample-manuscript").read().decode() == screen_pdf_format_md.content)
