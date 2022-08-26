from infrastructure.ChapterValidator import ChapterValidator


class TestValidator:
    validator = ChapterValidator()

    def test_chapters_wtith_valid_format_and_markdown_extension_are_valid(self):
        assert self.validator.is_valid_name("01_chapter.md") is True

    def test_chapters_wtith_valid_format_and_text_extension_are_valid(self):
        assert self.validator.is_valid_name("1_chapter.txt") is True

    def test_chapters_wtith_no_index_are_invalid(self):
        assert self.validator.is_valid_name("chapter.md") is False

    def test_chapters_wtith_no_index_separator_are_invalid(self):
        assert self.validator.is_valid_name("01chapter.md") is False

    def test_chapters_wtith_no_name_are_invalid(self):
        assert self.validator.is_valid_name("01.md") is False

    def test_chapters_wtith_no_extension_are_invalid(self):
        assert self.validator.is_valid_name("01_chapter") is False

    def test_filter_discards_only_invalid_filenames(self):
        valid_chapters = self.validator.filter([
            "01_chapter.md",
            "1_chapter.txt",
            "chapter.md",
            "01chapter.md",
            "01.md",
            "dorectory",
            "image.png"
        ])
        assert valid_chapters == ["01_chapter.md", "1_chapter.txt"]
