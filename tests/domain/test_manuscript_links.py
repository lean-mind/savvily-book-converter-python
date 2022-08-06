from src.domain.Manuscript import Manuscript


class TestLinks:

    def test_links_are_corrected(self):
        broken_link = Manuscript("sample text [this is some linked text] (this-is-a-url) more text")
        fixed_link = broken_link.format_links()
        expected_fix = "sample text [this is some linked text](this-is-a-url) more text"
        assert str(fixed_link) == expected_fix
