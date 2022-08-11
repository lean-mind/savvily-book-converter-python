import pytest
from src.domain.Manuscript import Manuscript


class TestLinksToFootnotes:

    def test_single_line(self):
        line_with_a_link = Manuscript("sample text [this is some linked text](this-is-a-url) more text")
        line_with_ref = line_with_a_link.turn_links_to_footnotes()
        expected_ref_format = (
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert str(line_with_ref) == expected_ref_format

    def test_single_line_starts_with_link(self):
        line_starts_with_link = Manuscript("[this is some linked text](this-is-a-url) more text")
        line_with_ref = line_starts_with_link.turn_links_to_footnotes()
        expected_ref_format = (
            "this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert str(line_with_ref) == expected_ref_format

    def test_single_line_ends_with_link(self):
        line_ends_with_link = Manuscript("sample text [this is some linked text](this-is-a-url)")
        line_with_ref = line_ends_with_link.turn_links_to_footnotes()
        expected_ref_format = (
            "sample text this is some linked text[^this-is-a-url]"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
        )
        assert str(line_with_ref) == expected_ref_format

    def test_discard_images(self):
        line_with_image = Manuscript("![image-name](image/path)")
        unformatted_line = line_with_image.turn_links_to_footnotes()
        assert str(unformatted_line) == str(line_with_image)

    def test_multi_line(self):

        lines_with_link = Manuscript(
            "some more text 1"
            "\n"
            "sample text [this is some linked text](this-is-a-url) more text"
            "\n"
            "some more text 2"
        )
        lines_with_ref = lines_with_link.turn_links_to_footnotes()
        expected_ref_format = (
            "some more text 1"
            "\n"
            "sample text this is some linked text[^this-is-a-url] more text"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n\n"
            "some more text 2"
        )
        assert str(lines_with_ref) == expected_ref_format

    def test_multi_line_discard_images(self):

        lines_with_image_and_link = Manuscript(
            "![an-image](path-to-image)"
            "\n"
            "some more text 1"
            "\n"
            "sample text [this is some linked text](this-is-a-url) more text"
            "\n"
            "some more text 2"
        )
        lines_with_image_and_ref = lines_with_image_and_link.turn_links_to_footnotes()
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
        assert str(lines_with_image_and_ref) == expected_ref_format

    @pytest.mark.skip(reason="Currently broken, links in the same line are swallowed")
    def test_two_links_one_line(self):
        line_with_two_links = Manuscript(
            "sample text [this is some linked text](this-is-a-url) more text [and yet](another-url) after that"
        )
        line_with_two_refs = line_with_two_links.turn_links_to_footnotes()
        expected_ref_format = (
            "sample text this is some linked text[^this-is-a-url] more text and yet[^another-url] after that"
            "\n\n"
            "[^this-is-a-url]: this-is-a-url"
            "\n"
            "[^another-url]: another-url"
            "\n"
        )
        assert str(line_with_two_refs) == expected_ref_format
