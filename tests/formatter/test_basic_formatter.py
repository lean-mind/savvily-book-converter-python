from src.formatter.BasicFormatter import BasicFormatter
import tests.fixtures.data.legacy_basic_format_md as legacy_format_fixture
import tests.fixtures.data.no_format_md as full_text_fixture


class TestBasicFormatter:
    formatter = BasicFormatter()

    def test_link_format(self):
        broken_link = "sample text [this is some linked text] (this-is-a-url) more text"
        fixed_link = self.formatter.check_links(broken_link)
        expected_fix = "sample text [this is some linked text](this-is-a-url) more text"
        assert fixed_link == expected_fix

    def test_reference_format(self):
        broken_ref = "sample text [^reference-text]: more text"
        fixed_ref = self.formatter.check_references(broken_ref)
        expected_fix = "sample text[^reference-text]: more text"
        assert fixed_ref == expected_fix

    def test_reference_format_omits_links(self):
        working_link_no_ref = "sample text [link text](link-url) more text"
        unchanged_link = self.formatter.check_references(working_link_no_ref)
        assert unchanged_link == working_link_no_ref

    def test_headings_format_h1(self):
        broken_heading = "last paragraph.\n# New Chapter"
        fixed_heading = self.formatter.check_headings(broken_heading)
        expected_fix = "last paragraph.\n\n# New Chapter"
        assert fixed_heading == expected_fix

    def test_headings_format_h2(self):
        broken_headings = "# last paragraph.\n## New Chapter"
        fixed_headings = self.formatter.check_headings(broken_headings)
        expected_fix = "\n# last paragraph.\n\n## New Chapter"
        assert fixed_headings == expected_fix

    def test_headings_format_h1_in_first_line(self):
        broken_headings = "# last paragraph.\n# New Chapter"
        fixed_headings = self.formatter.check_headings(broken_headings)
        expected_fix = "\n# last paragraph.\n\n# New Chapter"
        assert fixed_headings == expected_fix

    def test_headings_format_discards_non_heading_elements(self):
        not_a_heading = "En C# y Kotlin"
        fixed_headings = self.formatter.check_headings(not_a_heading)
        assert fixed_headings == not_a_heading

    def test_language_tags_format_simple_case(self):
        broken_lang_tag = "```java"
        fixed_lang_tag = self.formatter.check_lang_tags(broken_lang_tag)
        expected_fix = "```{title=Java}"
        assert fixed_lang_tag == expected_fix

    def test_language_tags_format_complex_case(self):
        fixed_lang_tag_with_code_block = self.formatter.check_lang_tags("""
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
        assert fixed_lang_tag_with_code_block == expected_fix

    def test_whole_formatter(self):
        formatted_md = self.formatter.run(full_text_fixture.content)
        assert formatted_md == legacy_format_fixture.content
