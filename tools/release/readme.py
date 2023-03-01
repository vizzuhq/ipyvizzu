"""A module for setting versions in readme."""

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


class Readme:
    """A class for setting versions in readme."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def set_version() -> None:
        """A method for setting versions in readme."""

        with open("README.md", "r", encoding="utf8") as fh_readme:
            content = fh_readme.read()

        content = content.replace(
            f"{Vizzu.get_vizzulibdoc_url()}/raw/main/docs/readme/",
            f"{Vizzu.get_vizzulibsite_url()}/{Vizzu.get_vizzu_version()}/readme/",
        )
        content = content.replace(
            "https://github.com/vizzuhq/ipyvizzu/raw/main/docs",
            "https://ipyvizzu.vizzuhq.com/latest",
        )
        content = content.replace(
            "https://ipyvizzu.vizzuhq.com/latest",
            f"https://ipyvizzu.vizzuhq.com/{Vizzu.get_ipyvizzu_version()}",
        )

        with open("README.md", "w", encoding="utf8") as fh_readme:
            fh_readme.write(content)


def main() -> None:
    """
    The main method.
    It set versions in readme.
    """

    with chdir(REPO_PATH):
        Readme.set_version()


main()
