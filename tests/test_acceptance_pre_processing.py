import src.formatter.EpubFormatter as epubFormatter
import src.formatter.ScreenPDFFormatter as screenPdfFormatter
import src.formatter.PrintPDFFormatter as printPdfFormatter
import tests.expected_output_md as expected


class TestFormatter:
    def test_new_ebook_format(self):
        assert (epubFormatter.run("tests/sample-manuscript").read().decode() == expected.epub_format)

    def test_new_pdf_print_format(self):
        assert (printPdfFormatter.run("tests/sample-manuscript").read().decode() == expected.pdf_print)

    def test_new_pdf_screen_format(self):
        assert (screenPdfFormatter.run("tests/sample-manuscript").read().decode() == expected.pdf_screen)
