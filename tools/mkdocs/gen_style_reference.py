"""A module for generating the style reference."""

import sys

import mkdocs_gen_files

from ipyvizzu import Chart  # pylint: disable=unused-import


sys.path.insert(0, "./tools/mkdocs")

from node import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Node,
)


class StyleReference:
    """A class for generating the style reference."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate(dst: str) -> None:
        """
        A method for generating the style reference.

        Args:
            dst: Destination path.
        """

        content = Node.run(
            "./tools/mkdocs/styles/gen_style_reference.mjs",
            "https://vizzu-lib-main.storage.googleapis.com/lib/vizzu.min.js",  # Chart.VIZZU
        )
        with mkdocs_gen_files.open(dst, "a") as f_index:
            f_index.write(f"\n{content}\n")


def main() -> None:
    """
    The main method.
    It generates the style reference.
    """

    StyleReference.generate(dst="tutorial/style.md")


main()
