"""A module for setting versions before release."""

import json
from pathlib import Path
import sys


REPO_PATH = Path(__file__).parent / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"


sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class Version:
    """A class for setting versions before release."""

    @staticmethod
    def set_readme_version(restore: bool) -> None:
        """A method for setting versions in readme."""

        with open("README.md", "r", encoding="utf8") as fh_readme:
            content = fh_readme.read()

        content = Vizzu.set_version(content, restore)

        with open("README.md", "w", encoding="utf8") as fh_readme:
            fh_readme.write(content)

    @staticmethod
    def set_src_version(restore: bool) -> None:
        """A method for setting versions in src docstring."""

        for item in (REPO_PATH / "src").rglob("*.py"):
            with open(item, "r", encoding="utf8") as fh_item:
                content = fh_item.read()

            content = Vizzu.set_version(content, restore)

            with open(item, "w", encoding="utf8") as fh_item:
                fh_item.write(content)


def main() -> None:
    """
    The main method.
    It set versions before release.
    """

    with chdir(REPO_PATH):
        restore = json.loads(sys.argv[1].lower())
        Version.set_readme_version(restore)
        Version.set_src_version(restore)


main()
