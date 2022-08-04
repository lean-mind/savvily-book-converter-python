import src.formatter.legacy.LegacyBasicFormatter as basicFormatter
import src.formatter.legacy.LegacyPrintPDFFormatter as printPdfFormatter
import tests.fixtures.data.legacy_basic_format_md as legacy_format_fixture
import tests.fixtures.data.legacy_print_format_md as legacy_print_format_fixture


class TestFormatter:
    def test_new_ebook_format(self):
        assert (basicFormatter.run("tests/fixtures/sample-manuscript").read().decode() == legacy_format_fixture.content)

    def test_new_pdf_print_format(self):
        assert (printPdfFormatter.run("tests/fixtures/sample-manuscript").read().decode() == legacy_print_format_fixture.content)

    def test_new_pdf_screen_format(self):
        assert (basicFormatter.run("tests/fixtures/sample-manuscript").read().decode() == legacy_format_fixture.content)
