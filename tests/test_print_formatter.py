from formatter.PrintPDFFormatter import PrintPDFFormatter
import tests.fixtures.expected_output_md as expected
import pytest


class TestPrintFormatter:
    def test_link_to_footnote_single_line(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes("sample text [this is some linked text](this-is-a-url) more text")
        expected_output = (
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert actual_output == expected_output

    def test_link_to_footnote_single_line_starts_with_link(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes("[this is some linked text](this-is-a-url) more text")
        expected_output = (
            "this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert actual_output == expected_output

    def test_link_to_footnote_single_line_ends_with_link(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes("sample text [this is some linked text](this-is-a-url)")
        expected_output = (
            "sample text this is some linked text[^this-is-a-url]"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert actual_output == expected_output

    @pytest.mark.skip(reason="Currently broken, links in the same line are swallowed")
    def test_link_to_footnotes_two_links_one_line(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes(
            "sample text [this is some linked text](this-is-a-url) more text [and](another-url) after that"
        )
        expected_output = (
            "sample text this is some linked text[^this-is-a-url] more text and[^another-url] after that"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
            "[^another-url]: another-url"
            "\n"
        )
        assert actual_output == expected_output

    def test_link_to_footnotes_multi_line(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes(
            "some more text 1"
            "\n"
            "sample text [this is some linked text](this-is-a-url) more text"
            "\n"
            "some more text 2"
        )
        expected_output = (
            "some more text 1"
            "\n"
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n\n"
            "some more text 2"
        )
        assert actual_output == expected_output

    def test_link_to_footnotes_discard_images(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes("![image-name](image/path)")
        expected_output = "![image-name](image/path)"
        assert actual_output == expected_output

    def test_link_to_footnotes_multi_line_discard_images(self):
        formatter = PrintPDFFormatter()
        actual_output = formatter.turn_links_to_footnotes(
            "![an-image](path-to-image)"
            "\n"
            "some more text 1"
            "\n"
            "sample text [this is some linked text](this-is-a-url) more text"
            "\n"
            "some more text 2"
        )
        expected_output = (
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
        assert actual_output == expected_output
