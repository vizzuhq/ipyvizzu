"""A module for generating the style reference."""

from pathlib import Path
import sys

import mkdocs_gen_files


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"
GEN_PATH = MKDOCS_PATH / "style"


sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from node import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Node,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
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

        content = Node.node(
            True,
            GEN_PATH / "gen_style_reference.mjs",
            Vizzu.get_vizzu_styleref_backend_url(),
        )
        with mkdocs_gen_files.open(dst, "a") as f_index:
            f_index.write(f"\n{content}\n")


def main() -> None:
    """
    The main method.
    It generates the style reference.
    """

    with chdir(REPO_PATH):
        StyleReference.generate(dst="tutorial/style.md")


main()
