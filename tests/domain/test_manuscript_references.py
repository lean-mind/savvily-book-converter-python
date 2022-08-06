from src.domain.Manuscript import Manuscript


class TestReferences:

    def test_references_are_corrected(self):
        broken_ref = Manuscript("sample text [^reference-text]: more text")
        fixed_ref = broken_ref.format_references()
        expected_fix = "sample text[^reference-text]: more text"
        assert str(fixed_ref) == expected_fix

    def test_discards_links(self):
        working_link_no_ref = Manuscript("sample text [link text](link-url) more text")
        unchanged_link = working_link_no_ref.format_references()
        assert str(unchanged_link) == str(working_link_no_ref)
