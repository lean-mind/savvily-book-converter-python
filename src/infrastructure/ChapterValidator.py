import re


class ChapterValidator:
    def is_valid_name(self, filename: str) -> bool:
        index_separator = '_'
        chapter_index = r'^(\d+)'
        index_separator = '_'
        chapter_name = r'.*'
        markdown_ext = '.md'
        text_ext = '.txt'

        valid_md = re.compile(f"{chapter_index}{index_separator}{chapter_name}{markdown_ext}")
        valid_txt = re.compile(f"{chapter_index}{index_separator}{chapter_name}{text_ext}")

        if valid_md.match(filename) or valid_txt.match(filename):
            return True
        else:
            return False
