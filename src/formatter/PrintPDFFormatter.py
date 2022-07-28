from formatter.BasicFormatter import BasicFormatter
import re


class PrintPDFFormatter:

    def turn_links_to_footnotes(self, raw_manuscript: str):

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

        return re.sub(link_regex, turn_to_footnote, raw_manuscript)

    def run(self, raw_manuscript: str):
        formatter = BasicFormatter()
        test = formatter.run(raw_manuscript)
        return self.turn_links_to_footnotes(test)
