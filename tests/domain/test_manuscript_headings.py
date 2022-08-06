from src.domain.Manuscript import Manuscript


class TestHeadings:

    def test_h1(self):
        broken_heading = Manuscript("last paragraph.\n# New Chapter")
        fixed_heading = broken_heading.format_headings()
        expected_fix = "last paragraph.\n\n# New Chapter"
        assert str(fixed_heading) == expected_fix

    def test_h2(self):
        broken_headings = Manuscript("# last paragraph.\n## New Chapter")
        fixed_headings = broken_headings.format_headings()
        expected_fix = "\n# last paragraph.\n\n## New Chapter"
        assert str(fixed_headings) == expected_fix

    def test_h1_in_first_line(self):
        broken_headings = Manuscript("# last paragraph.\n# New Chapter")
        fixed_headings = broken_headings.format_headings()
        expected_fix = "\n# last paragraph.\n\n# New Chapter"
        assert str(fixed_headings) == expected_fix

    def test_discards_non_heading_elements(self):
        not_a_heading = Manuscript("En C# y Kotlin")
        formatted_manuscript = not_a_heading.format_headings()
        assert formatted_manuscript == not_a_heading
