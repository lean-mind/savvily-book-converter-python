from src.domain.Manuscript import Manuscript


class TestLangTags:

    def test_without_context(self):
        broken_lang_tag = Manuscript("```java")
        fixed_lang_tag = broken_lang_tag.format_lang_tags()
        expected_fix = "```{title=Java}"
        assert str(fixed_lang_tag) == expected_fix

    def test_with_context(self):
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
