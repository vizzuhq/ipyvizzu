"""A module for generating vizzu url for snippets."""

from pathlib import Path
import sys

import mkdocs_gen_files


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"


sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class VizzuUrl:
    """A class for generating vizzu url for snippets."""

    # pylint: disable=too-few-public-methods

    TEMPLATE = 'const vizzu = "{vizzu}";\n\nexport default vizzu;\n'

    @staticmethod
    def generate(dst: str) -> None:
        """
        A method for generating vizzu url for snippets.

        Args:
            dst: The destination file.
        """

        with mkdocs_gen_files.open(dst, "w") as f_vizzu:
            f_vizzu.write(VizzuUrl.TEMPLATE.format(vizzu=Vizzu.get_backend_url()))


def main() -> None:
    """
    The main method.
    It generates vizzu url for snippets.
    """

    with chdir(REPO_PATH):
        VizzuUrl.generate("assets/javascripts/vizzu.js")


main()
