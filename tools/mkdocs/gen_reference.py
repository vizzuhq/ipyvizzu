"""A module for generating the code reference."""

from pathlib import Path

import mkdocs_gen_files  # type: ignore


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

        for path in sorted(Path("src").rglob("*.py")):
            module_path = path.relative_to("src").with_suffix("")

            doc_path = path.relative_to("src").with_suffix(".md")
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

    Reference.generate("reference")


main()
