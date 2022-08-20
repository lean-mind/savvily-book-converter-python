from dataclasses import dataclass
import re


@dataclass
class Manuscript:
    text: str

    def format_links(self):
        return Manuscript(self.text.replace("] (", "]("))

    def format_references(self):
        return Manuscript(self.text.replace(" [^", "[^"))

    def format_headings(self):
        heading = re.compile(r"^(#.*)", flags=re.MULTILINE)
        new_line_before_match = r"\n\1"
        return Manuscript(re.sub(heading, new_line_before_match, self.text))

    def format_lang_tags(self):
        def format_and_capitalize(match):
            code_block_tag = match.group(1)
            capitalized_lang_tag = match.group(2).capitalize()
            return f"{code_block_tag}{{title={capitalized_lang_tag}}}"

        code_block_tag_expression = re.compile(r"(```)(.+)")
        return Manuscript(re.sub(code_block_tag_expression, format_and_capitalize, self.text))

    def turn_links_to_footnotes(self):
        link_regex = re.compile(r"""
            # group before link, anything before the last '[' of the line, except for '!' (discard images)
            ^([^!]*)
            # group link text, anything 4 or more chars long between the last '[' of the line and the following ']'
            \[(.{4,}?)\]
            # group link url, anything between the last '(' of the line and the following ')'
            \((.+?)\)
            # group after link, anything between the last ')' and EOL
            (.*$)
        """, flags=re.VERBOSE | re.MULTILINE)

        parsed_text = self.text
        while re.search(link_regex, parsed_text):
            def build_footnote(match):
                text_before_ref = match.group(1)
                referenced_text = match.group(2)
                reference_url = match.group(3)
                text_after_ref = match.group(4)
                return (
                    f"{text_before_ref}{referenced_text}[^{reference_url}]{text_after_ref}"
                    "\n\n"
                    f"[^{reference_url}]: {reference_url}"
                    "\n"
                )
            parsed_text = re.sub(link_regex, build_footnote, parsed_text)

        return Manuscript(parsed_text)

    def screen_pdf_format(self):
        return Manuscript(self.text) \
            .format_links() \
            .format_references() \
            .format_headings() \
            .format_lang_tags()

    def epub_format(self):
        return Manuscript(self.text) \
            .format_links() \
            .format_references() \
            .format_headings() \
            .format_lang_tags()

    def print_pdf_format(self):
        return Manuscript(self.text) \
            .screen_pdf_format() \
            .turn_links_to_footnotes()

    def as_encoded_string(self):
        return str(self).encode()

    def __str__(self):
        return self.text
