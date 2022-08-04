import pytest
from src.domain.Manuscript import Manuscript
import tests.fixtures.data.new_print_format_md as new_print_format_fixture
import tests.fixtures.data.legacy_basic_format_md as legacy_format_fixture
import tests.fixtures.data.no_format_md as full_text_fixture


class TestManuscript:

    class TestLinkFormat:

        def test_link_format(self):
            broken_link = Manuscript("sample text [this is some linked text] (this-is-a-url) more text")
            fixed_link = broken_link.format_links()
            expected_fix = "sample text [this is some linked text](this-is-a-url) more text"
            assert str(fixed_link) == expected_fix

    class TestReferenceFormat:

        def test_reference_format(self):
            broken_ref = Manuscript("sample text [^reference-text]: more text")
            fixed_ref = broken_ref.format_references()
            expected_fix = "sample text[^reference-text]: more text"
            assert str(fixed_ref) == expected_fix

        def test_reference_format_omits_links(self):
            working_link_no_ref = Manuscript("sample text [link text](link-url) more text")
            unchanged_link = working_link_no_ref.format_references()
            assert str(unchanged_link) == str(working_link_no_ref)

    class TestHeadingFormat:

        def test_headings_format_h1(self):
            broken_heading = Manuscript("last paragraph.\n# New Chapter")
            fixed_heading = broken_heading.format_headings()
            expected_fix = "last paragraph.\n\n# New Chapter"
            assert str(fixed_heading) == expected_fix

        def test_headings_format_h2(self):
            broken_headings = Manuscript("# last paragraph.\n## New Chapter")
            fixed_headings = broken_headings.format_headings()
            expected_fix = "\n# last paragraph.\n\n## New Chapter"
            assert str(fixed_headings) == expected_fix

        def test_headings_format_h1_in_first_line(self):
            broken_headings = Manuscript("# last paragraph.\n# New Chapter")
            fixed_headings = broken_headings.format_headings()
            expected_fix = "\n# last paragraph.\n\n# New Chapter"
            assert str(fixed_headings) == expected_fix

    class TestLangTagFormat:

        def test_language_tags_format_simple_case(self):
            broken_lang_tag = Manuscript("```java")
            fixed_lang_tag = broken_lang_tag.format_lang_tags()
            expected_fix = "```{title=Java}"
            assert str(fixed_lang_tag) == expected_fix

        def test_language_tags_format_complex_case(self):
            broken_lang_tag_with_code_block = Manuscript("""
                Some pre-code block text

                ```python
                if (61) {
                    motherboard_dv(website + -2);
                } else {
                    win(down_it_white, right * mms_dos, binary_firewire_page);
                }
                ```
                Some post-code block text
            """)
            fixed_lang_tag_with_code_block = broken_lang_tag_with_code_block.format_lang_tags()

            expected_fix = """
                Some pre-code block text

                ```{title=Python}
                if (61) {
                    motherboard_dv(website + -2);
                } else {
                    win(down_it_white, right * mms_dos, binary_firewire_page);
                }
                ```
                Some post-code block text
            """
            assert str(fixed_lang_tag_with_code_block) == expected_fix

    class TestLinksToFootnotes:

        def test_link_to_footnote_single_line(self):
            line_with_a_link = Manuscript("sample text [this is some linked text](this-is-a-url) more text")
            line_with_ref = line_with_a_link.turn_links_to_footnotes()
            expected_ref_format = (
                "sample text this is some linked text[^this-is-a-url] more text"
                "\n\n"
                "[^this-is-a-url]: this-is-a-url"
                "\n"
            )
            assert str(line_with_ref) == expected_ref_format

        def test_link_to_footnote_single_line_starts_with_link(self):
            line_starts_with_link = Manuscript("[this is some linked text](this-is-a-url) more text")
            line_with_ref = line_starts_with_link.turn_links_to_footnotes()
            expected_ref_format = (
                "this is some linked text[^this-is-a-url] more text"
                "\n\n"
                "[^this-is-a-url]: this-is-a-url"
                "\n"
            )
            assert str(line_with_ref) == expected_ref_format

        def test_link_to_footnote_single_line_ends_with_link(self):
            line_ends_with_link = Manuscript("sample text [this is some linked text](this-is-a-url)")
            line_with_ref = line_ends_with_link.turn_links_to_footnotes()
            expected_ref_format = (
                "sample text this is some linked text[^this-is-a-url]"
                "\n\n"
                "[^this-is-a-url]: this-is-a-url"
                "\n"
            )
            assert str(line_with_ref) == expected_ref_format

        def test_link_to_footnotes_discard_images(self):
            line_with_image = Manuscript("![image-name](image/path)")
            unformatted_line = line_with_image.turn_links_to_footnotes()
            assert str(unformatted_line) == str(line_with_image)

        def test_link_to_footnotes_multi_line(self):

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

        def test_link_to_footnotes_multi_line_discard_images(self):

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
        def test_link_to_footnotes_two_links_one_line(self):
            line_with_two_links = Manuscript(
                "sample text [this is some linked text](this-is-a-url) more text [and](another-url) after that"
            )
            line_with_two_refs = line_with_two_links.turn_links_to_footnotes()
            expected_ref_format = (
                "sample text this is some linked text[^this-is-a-url] more text and[^another-url] after that"
                "\n\n"
                "[^this-is-a-url]: this-is-a-url"
                "\n"
                "[^another-url]: another-url"
                "\n"
            )
            assert str(line_with_two_refs) == expected_ref_format

    class TestBasicFormat:

        def test_basic_format(self):
            broken_md = Manuscript(full_text_fixture.content)
            formatted_md = broken_md.basic_format()
            assert str(formatted_md) == legacy_format_fixture.content

    class TestPrintPdfFormat:
        def test_print_pdf_format(self):
            broken_md = Manuscript(full_text_fixture.content)
            formatted_md = broken_md.print_pdf_format()
            assert str(formatted_md) == new_print_format_fixture.content
