import subprocess
import sys
import logging
from os import makedirs, chdir
import formatter.ScreenPDFFormatter as screenPdfFormatter

logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.DEBUG)


def __pandoc_command(manuscript_path: str) -> list:
    engine = "--pdf-engine=xelatex"
    template = "--template=src/pandoc-templates/screen/custom-report.tex"
    figures = "markdown-implicit_figures"
    resources = f"--resource-path={manuscript_path}"
    output = ".tmp-manuscript/chapters.pdf"

    return ["timeout", "600", "pandoc", engine, template, "--listings",
            "-V", "documentclass=report", "-f", figures, "-o", output, resources]


def __compile_chapters(manuscript_path: str):
    logging.info(" === COMPILING screen pdf chapters ===")

    formatted_stream = screenPdfFormatter.run(manuscript_path)
    subprocess.run(__pandoc_command(manuscript_path), stdin=formatted_stream, check=True)


# TODO.check pathing within template to avoid cd
def __compile_opnening():
    logging.info(" === COMPILING screen pdf opening ===")

    chdir(".tmp-manuscript")
    xelatex_command = ["xelatex", "-output-directory", ".", "../src/pandoc-templates/screen/opening.tex"]
    subprocess.run(xelatex_command)
    chdir("../")


def __join_sections(output_name: str):
    logging.info(" === Joining screen pdf opening and chapters ===")

    output = f"-sOutputFile=output/{output_name}.pdf"
    ghostscript_command = ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
                           output, ".tmp-manuscript/opening.pdf", ".tmp-manuscript/chapters.pdf"]
    subprocess.run(ghostscript_command)


def __compile_pdf_from(manuscript_path: str):
    __compile_chapters(manuscript_path)
    __compile_opnening()
    __join_sections("python_screen")


if __name__ == "__main__":
    try:
        makedirs("output", exist_ok=True)
        manuscript_path = sys.argv[1]
        __compile_pdf_from(manuscript_path)
        logging.info(" === DONE generating screen pdf ===")
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        logging.error(f" === Pandoc command failed! === \n{e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f" === Something went wrong! === \n{e}")
        sys.exit(1)
