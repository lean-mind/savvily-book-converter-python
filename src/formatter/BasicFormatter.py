import re


class BasicFormatter:

    def check_links(self, raw_manuscript: str):
        return raw_manuscript.replace("] (", "](")

    def check_references(self, raw_manuscript: str):
        return raw_manuscript.replace(" [^", "[^")

    def check_headings(self, raw_manuscript: str):
        return re.sub(r"#(.*)", r"\n#\1", raw_manuscript)

    def check_lang_tags(self, raw_manuscript: str):
        def format_and_capitalize(match):
            code_block_tag = match.group(1)
            capitalized_lang_tag = match.group(2).capitalize()
            return code_block_tag + r"{title=" + capitalized_lang_tag + r"}"

        code_block_tag_expression = r"(```)(.+)"
        return re.sub(code_block_tag_expression, format_and_capitalize, raw_manuscript)

    def run(self, raw_manuscript: str):
        return self.check_links(self.check_references(self.check_headings(self.check_lang_tags(raw_manuscript))))
