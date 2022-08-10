import re


class PdfHelper:
    def __init__(self, raw_pdf):
        self.raw_pdf = raw_pdf

    def get_links_from_pdf(self) -> list:
        link_pattern = r"(.*[http][https]://.*)"
        return self._filter_list_by_pattern(self.raw_pdf, link_pattern)

    def get_page_numbers_of_headers_in_chapter(self, chapter_number: int) -> list:
        page_numbers_preceding_pages_with_headers: list = [
            self.raw_pdf[index - 1]
            for index, line in enumerate(self.raw_pdf)
            if line == self._get_heading_from_manuscript_for_chapter(1).upper()
        ]
        page_numbers_with_headers: list = [
            int(page_number) + 1
            for page_number in page_numbers_preceding_pages_with_headers
        ]
        return page_numbers_with_headers

    def _get_heading_from_manuscript_for_chapter(self, chapter_number: int) -> str:
        heading_pattern = r"# (.*)\n"
        with open(f"tests/pandoc_integration/fixtures/sample-manuscript/0{chapter_number}_chapter.md", "r") as f:
            lines = f.readlines()
        return self._filter_list_by_pattern(lines, heading_pattern)[0]

    def _get_links_from_manuscript_for_chapter(self, chapter_number: int) -> list:
        link_pattern = r".*(http://.*)\)"
        with open(f"tests/pandoc_integration/fixtures/sample-manuscript/0{chapter_number}_chapter.md", "r") as f:
            lines = f.readlines()
        return self._filter_list_by_pattern(lines, link_pattern)

    def _filter_list_by_pattern(self, lst: list, pattern: str) -> list:
        return [
            re.match(pattern, line).group(1)
            for line in lst
            if re.match(pattern, line)
        ]
