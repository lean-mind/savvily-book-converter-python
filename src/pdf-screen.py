import subprocess
import sys
import logging
from os import makedirs, chdir
import formatter.legacy.LegacyBasicFormatter as basicFormatter
from formatter.BasicFormatter import BasicFormatter
from ManuscriptReader import ManuscriptReader

logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def __pandoc_command(manuscript_path: str) -> list:
    engine = "--pdf-engine=xelatex"
    template = "--template=src/pandoc-templates/screen/custom-report.tex"
    figures = "markdown-implicit_figures"
    resources = f"--resource-path={manuscript_path}"
    output = ".tmp-manuscript/chapters.pdf"

    return ["timeout", "600", "pandoc", engine, template, "--listings",
            "-V", "documentclass=report", "-f", figures, "-o", output, resources]


def __compile_chapters(manuscript_path: str):
    logging.info(" === COMPILING Screen PDF chapters ===")

    reader = ManuscriptReader()
    full_manuscript = reader.readFrom(manuscript_path)
    new_formatter = BasicFormatter()
    formatted_manuscript = new_formatter.run(full_manuscript)
    subprocess.run(__pandoc_command(manuscript_path), input=formatted_manuscript.encode(), check=True)


# TODO.check pathing within template to avoid cd
def __compile_opnening():
    logging.info(" === COMPILING Screen PDF opening ===")

    xelatex_command = ["xelatex", "-output-directory", ".", "../src/pandoc-templates/screen/opening.tex"]
    chdir(".tmp-manuscript")
    xelatex_output = subprocess.run(xelatex_command, stdout=subprocess.PIPE)
    chdir("../")

    logging.info(f"XeLaTeX output:\n\n{xelatex_output.stdout.decode()}")


def __join_sections(output_name: str):
    logging.info(" === Joining Screen PDF opening and chapters ===")

    output = f"-sOutputFile=output/{output_name}.pdf"
    ghostscript_command = ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
                           output, ".tmp-manuscript/opening.pdf", ".tmp-manuscript/chapters.pdf"]
    subprocess.run(ghostscript_command)


def __compile_pdf_from(manuscript_path: str):
    __compile_chapters(manuscript_path)
    __compile_opnening()
    __join_sections("python_screen")


def __legacy_compile(manuscript_path: str):
    logging.info(" === COMPILING Screen PDF chapters ===")

    formatted_stream = basicFormatter.run(manuscript_path)
    subprocess.run(__pandoc_command(manuscript_path), stdin=formatted_stream, check=True)
    __compile_opnening()
    __join_sections("legacy_python_screen")


if __name__ == "__main__":
    try:
        makedirs("output", exist_ok=True)
        mode = sys.argv[1]
        manuscript_path = sys.argv[-1]
        if mode == 'legacy':
            print(" === LEGACY MODE ===")
            __legacy_compile(manuscript_path)
        else:
            __compile_pdf_from(manuscript_path)
        logging.info(" === DONE generating Screen PDF ===")
        print(" === DONE generating Screen PDF ===")
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        logging.error(f" === Pandoc command failed! === \n{e}")
        print(f" === Pandoc command failed! === \n{e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f" === Something went wrong! === \n{e}")
        print(f" === Something went wrong! === \n{e}")
        sys.exit(1)
