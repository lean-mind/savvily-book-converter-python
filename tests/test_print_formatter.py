from formatter.PrintPDFFormatter import PrintPDFFormatter
import tests.fixtures.data.new_print_format_md as new_print_format_fixture
import tests.fixtures.data.no_format_md as full_text_fixture
import pytest


class TestPrintFormatter:
    formatter = PrintPDFFormatter()

    def test_link_to_footnote_single_line(self):
        line_with_a_link = "sample text [this is some linked text](this-is-a-url) more text"
        line_with_ref = self.formatter.turn_links_to_footnotes(line_with_a_link)
        expected_ref_format = (
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert line_with_ref == expected_ref_format

    def test_link_to_footnote_single_line_starts_with_link(self):
        line_starts_with_link = "[this is some linked text](this-is-a-url) more text"
        line_with_ref = self.formatter.turn_links_to_footnotes(line_starts_with_link)
        expected_ref_format = (
            "this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert line_with_ref == expected_ref_format

    def test_link_to_footnote_single_line_ends_with_link(self):
        line_ends_with_link = "sample text [this is some linked text](this-is-a-url)"
        line_with_ref = self.formatter.turn_links_to_footnotes(line_ends_with_link)
        expected_ref_format = (
            "sample text this is some linked text[^this-is-a-url]"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert line_with_ref == expected_ref_format

    @pytest.mark.skip(reason="Currently broken, links in the same line are swallowed")
    def test_link_to_footnotes_two_links_one_line(self):
        line_with_two_links = "sample text [this is some linked text](this-is-a-url) more text [and](another-url) after that"
        line_with_two_refs = self.formatter.turn_links_to_footnotes(line_with_two_links)
        expected_ref_format = (
            "sample text this is some linked text[^this-is-a-url] more text and[^another-url] after that"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
            "[^another-url]: another-url"
            "\n"
        )
        assert line_with_two_refs == expected_ref_format

    def test_link_to_footnotes_multi_line(self):

        lines_with_ref = self.formatter.turn_links_to_footnotes(
            "some more text 1"
            "\n"
            "sample text [this is some linked text](this-is-a-url) more text"
            "\n"
            "some more text 2"
        )
        expected_ref_format = (
            "some more text 1"
            "\n"
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n\n"
            "some more text 2"
        )
        assert lines_with_ref == expected_ref_format

    def test_link_to_footnotes_discard_images(self):
        line_with_image = "![image-name](image/path)"
        unformatted_line = self.formatter.turn_links_to_footnotes(line_with_image)
        assert unformatted_line == line_with_image

    def test_link_to_footnotes_multi_line_discard_images(self):

        lines_with_image_and_ref = self.formatter.turn_links_to_footnotes(
            "![an-image](path-to-image)"
            "\n"
            "some more text 1"
            "\n"
            "sample text [this is some linked text](this-is-a-url) more text"
            "\n"
            "some more text 2"
        )
        expected_ref_format = (
            "![an-image](path-to-image)"
            "\n"
            "some more text 1"
            "\n"
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n\n"
            "some more text 2"
        )
        assert lines_with_image_and_ref == expected_ref_format

    def test_whole_formatter(self):
        formatted_md = self.formatter.run(full_text_fixture.content)
        assert formatted_md == new_print_format_fixture.content
