import subprocess
import sys
import logging
from os import makedirs
import formatter.legacy.LegacyBasicFormatter as basicFormatter
from infrastructure.ManuscriptReader import ManuscriptReader
from domain.Manuscript import Manuscript

logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.DEBUG)


def __pandoc_command(manuscript_path: str, legacy_mode: bool = False) -> list:
    metadata = "--metadata-file=src/pandoc-templates/epub/metadata.yml"
    resources = f"--resource-path={manuscript_path}"
    if legacy_mode:
        output = "--output=output/legacy_ebook.epub"
    else:
        output = "--output=output/ebook.epub"
    css = "--css=src/pandoc-templates/epub/epub.css"
    cover_image = f"--epub-cover-image={manuscript_path}/resources/book-cover-print.png"
    font = "--epub-embed-font=/usr/share/fonts/Roboto-Bold.ttf"

    return ["timeout", "600", "pandoc", font, css, cover_image, output, metadata, resources]


def __compile_epub_from(manuscript_path: str):
    logging.info(" === COMPILING Epub ===")

    reader = ManuscriptReader()
    full_manuscript = reader.readFrom(manuscript_path)
    manuscript = Manuscript(full_manuscript)
    formatted_manuscript = manuscript.epub_format()
    subprocess.run(__pandoc_command(manuscript_path), input=formatted_manuscript.as_encoded_string(), check=True)


def __legacy_compile(manuscript_path: str):
    logging.info(" === COMPILING Epub ===")

    formatted_stream = basicFormatter.run(manuscript_path)
    subprocess.run(__pandoc_command(manuscript_path, True), stdin=formatted_stream, check=True)


if __name__ == "__main__":
    try:
        makedirs("output", exist_ok=True)
        mode = sys.argv[1]
        manuscript_path = sys.argv[-1]
        if mode == 'legacy':
            print(" === LEGACY MODE ===")
            __legacy_compile(manuscript_path)
        else:
            __compile_epub_from(manuscript_path)
        logging.info(" === DONE generating Epub ===")
        print(" === DONE generating Epub ===")
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        logging.error(f" === Pandoc command failed! === \n{e}")
        print(f" === Pandoc command failed! === \n{e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f" === Something went wrong! === \n{e}")
        print(f" === Something went wrong! === \n{e}")
        sys.exit(1)
