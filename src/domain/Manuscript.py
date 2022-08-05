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

    def basic_format(self):
        return Manuscript(self.text) \
            .format_links() \
            .format_references() \
            .format_headings() \
            .format_lang_tags()

    def turn_links_to_footnotes(self):
        link_regex = re.compile(r"""
            (.*|)           # group before link, '|' for lines starting with link
            \[(....+?)\]    # group link text, anything between the first '[' and the first ']' of the line
            \(([^)]+)\)     # group link url, anything between the first '(' and the first ')' of the line
            (.*)            # group after link
        """, flags=re.VERBOSE)

        def turn_to_footnote(match):
            text_before_ref = match.group(1)
            referenced_text = match.group(2)
            reference_url = match.group(3)
            text_after_ref = match.group(4)

            # Discard lines that start with !, aka images
            if match.group(0).startswith('!'):
                return match.group(0)
            else:
                return (
                    f"{text_before_ref}{referenced_text}[^{reference_url}]{text_after_ref}"
                    "\n\n"
                    f"[^{reference_url}]: {reference_url}"
                    "\n"
                )

        return Manuscript(re.sub(link_regex, turn_to_footnote, self.text))

    def print_pdf_format(self):
        return Manuscript(self.text) \
            .basic_format() \
            .turn_links_to_footnotes()

    def __str__(self):
        return self.text
