import pytest
from pdfminer.high_level import extract_text
from tests.pandoc_integration.fixtures.helpers.PdfHelper import PdfHelper

full_text = extract_text("output/python_print.pdf")
raw_pdf: list = [line for line in full_text.splitlines() if line]
helper = PdfHelper(raw_pdf)


class TestPrintOutput:
    def test_total_page_number(self):
        expected_number_of_pages: int = 19
        last_line: str = raw_pdf[-1]
        number_of_closing_blank_pages: int = 3
        actual_number_of_pages: int = int(last_line) + number_of_closing_blank_pages
        assert actual_number_of_pages == expected_number_of_pages

    def test_code_block_lang_tag_capitalized(self):
        all_code_block_lang_tags: list = [
            tag
            for tag in raw_pdf
            if tag.lower() in ["java", "python"]
        ]
        capitalized_lang_tags: list = [
            capitalized_tag
            for capitalized_tag in all_code_block_lang_tags
            if capitalized_tag[0].isupper()
        ]
        assert len(capitalized_lang_tags) == len(all_code_block_lang_tags)

    def test_lang_tag_precede_code_block(self):
        known_code_block_start: str = "if (61) {"
        code_block_position: int = raw_pdf.index(known_code_block_start)
        expected_code_block_lang_tag: str = "Java"
        actual_code_block_lang_tag: str = raw_pdf[code_block_position - 1]
        assert actual_code_block_lang_tag == expected_code_block_lang_tag

    def test_chapter_name_in_headers_of_odd_numbered_pages(self):
        for page_number in helper.get_page_numbers_of_headers_in_chapter(1):
            assert page_number % 2 != 0


class TestPrintLinks:
    def test_all_links_are_converted_to_footnotes(self):
        links_in_sample_md = 8
        links_in_pdf = helper.get_links_from_pdf()
        assert len(links_in_pdf) == links_in_sample_md

    @pytest.mark.skip(reason="Currently broken, links in references are not handled")
    def test_links_in_references_are_handled(self):
        known_broken_link_in_reference = "https://www.nyan.cat/"
        links_in_pdf = helper.get_links_from_pdf()
        known_broken_link_in_reference_from_pdf = [
            line
            for line in links_in_pdf
            if known_broken_link_in_reference in line
        ]
        assert len(known_broken_link_in_reference_from_pdf) == 0
