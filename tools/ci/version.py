# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from contextlib import chdir
import json
from pathlib import Path
import sys


REPO_PATH = Path(__file__).parent / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"

sys.path.insert(0, str(TOOLS_PATH / "modules"))

from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class Version:
    @staticmethod
    def set_readme_version(restore: bool) -> None:
        with open("README.md", "r", encoding="utf8") as fh_readme:
            content = fh_readme.read()

        content = Vizzu.set_version(content, restore)

        with open("README.md", "w", encoding="utf8") as fh_readme:
            fh_readme.write(content)

    @staticmethod
    def set_src_version(restore: bool) -> None:
        for item in (REPO_PATH / "src").rglob("*.py"):
            with open(item, "r", encoding="utf8") as fh_item:
                content = fh_item.read()

            content = Vizzu.set_version(content, restore)

            with open(item, "w", encoding="utf8") as fh_item:
                fh_item.write(content)


def main() -> None:
    with chdir(REPO_PATH):
        restore = json.loads(sys.argv[1].lower())
        Version.set_readme_version(restore)
        Version.set_src_version(restore)


main()
