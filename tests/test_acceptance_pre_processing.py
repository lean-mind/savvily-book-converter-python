import src.formatter.EpubFormatter as epubFormatter
import src.formatter.ScreenPDFFormatter as screenPdfFormatter
import src.formatter.PrintPDFFormatter as printPdfFormatter
import tests.fixtures.expected_output_md as expected


class TestFormatter:
    def test_new_ebook_format(self):
        assert (epubFormatter.run("tests/fixtures/sample-manuscript").read().decode() == expected.basic_format)

    def test_new_pdf_print_format(self):
        assert (printPdfFormatter.run("tests/fixtures/sample-manuscript").read().decode() == expected.pdf_print_format)

    def test_new_pdf_screen_format(self):
        assert (screenPdfFormatter.run("tests/fixtures/sample-manuscript").read().decode() == expected.basic_format)
