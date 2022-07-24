from formatter.BasicFormatter import BasicFormatter
import tests.fixtures.expected_output_md as expected


class TestBasicFormatter:
    def test_link_format(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_links("sample text [this is some linked text] (this-is-a-url) more text")
        expected_output = "sample text [this is some linked text](this-is-a-url) more text"
        assert actual_output == expected_output

    def test_reference_format(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_references("sample text [^reference-text]: more text")
        expected_output = "sample text[^reference-text]: more text"
        assert actual_output == expected_output

    def test_reference_format_omits_links(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_references("sample text [link text](link-url) more text")
        expected_output = "sample text [link text](link-url) more text"
        assert actual_output == expected_output

    def test_headings_format_h1(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_headings("last paragraph.\n# New Chapter")
        expected_output = "last paragraph.\n\n# New Chapter"
        assert actual_output == expected_output

    def test_headings_format_h2(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_headings("# last paragraph.\n## New Chapter")
        expected_output = "\n# last paragraph.\n\n## New Chapter"
        assert actual_output == expected_output

    def test_headings_format_h1_in_first_line(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_headings("# last paragraph.\n# New Chapter")
        expected_output = "\n# last paragraph.\n\n# New Chapter"
        assert actual_output == expected_output

    def test_language_tags_format_simple_case(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_lang_tags("```java")
        expected_output = "```{title=Java}"
        assert actual_output == expected_output

    def test_language_tags_format_complex_case(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_lang_tags("""
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

        expected_output = """
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
        assert actual_output == expected_output

    def test_whole_formatter(self):
        formatter = BasicFormatter()
        actual_output = formatter.run(expected.default)
        expected_output = expected.basic_format
        assert actual_output == expected_output
