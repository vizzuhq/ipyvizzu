"""A module for generating the code reference."""

from pathlib import Path
import sys

import mkdocs_gen_files  # type: ignore

REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"
SRC_PATH = REPO_PATH / "src"


sys.path.insert(0, str(MKDOCS_PATH))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)


class Reference:
    """A class for generating the code reference."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate(folder: str) -> None:
        """
        A method for generating the code reference.

        Args:
            folder: The destination folder of the code reference.
        """

        for path in sorted(SRC_PATH.rglob("*.py")):
            module_path = path.relative_to(SRC_PATH).with_suffix("")

            doc_path = path.relative_to(SRC_PATH).with_suffix(".md")
            full_doc_path = Path(folder, doc_path)

            parts = tuple(module_path.parts)

            if parts[-1] == "__init__":
                parts = parts[:-1]
                doc_path = doc_path.with_name("index.md")
                full_doc_path = full_doc_path.with_name("index.md")
            elif parts[-1] == "__main__":
                continue

            mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path)
            with mkdocs_gen_files.open(full_doc_path, "w") as f_md:
                item = ".".join(parts)
                f_md.write(f"::: {item}")


def main() -> None:
    """
    The main method.
    It generates the code reference.
    """

    with chdir(REPO_PATH):
        Reference.generate("reference")


main()
