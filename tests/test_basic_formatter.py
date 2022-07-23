from formatter.BasicFormatter import BasicFormatter
import tests.fixtures.expected_output_md as expected


class TestBasicFormatter:
    def test_link_format(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_links("[this is some linked text] (this is a url)")
        expected_output = "[this is some linked text](this is a url)"
        assert actual_output == expected_output

    def test_reference_format(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_references(" [^reference-text]:")
        expected_output = "[^reference-text]:"
        assert actual_output == expected_output

    def test_headings_format(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_headings("last paragraph.\n# New Chapter")
        expected_output = "last paragraph.\n\n# New Chapter"
        assert actual_output == expected_output

    def test_language_tags_format(self):
        formatter = BasicFormatter()
        actual_output = formatter.check_lang_tags("```java")
        expected_output = "```{title=Java}"
        assert actual_output == expected_output
