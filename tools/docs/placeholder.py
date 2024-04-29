# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pathlib import Path
import sys


REPO_PATH = Path(__file__).parent / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"
MKDOCS_PATH = TOOLS_PATH / "docs"


sys.path.insert(0, str(TOOLS_PATH / "modules"))

from chdir import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


PLACEHOLDER = """placeholders:
  IPYVIZZU_MINOR_VERSION: "{}"
  LIB_MINOR_VERSION: "{}"
settings:
  auto_placeholder_tables: false
"""


class Placeholder:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate() -> None:
        with open(
            MKDOCS_PATH / "placeholder-plugin.yaml", "w", encoding="utf8"
        ) as fh_config:
            ipyvizzu_version = Vizzu.get_ipyvizzu_version().split(".")
            ipyvizzu_minor = f"{ipyvizzu_version[0]}.{ipyvizzu_version[1]}"
            vizzu_version = Vizzu.get_vizzu_version().split(".")
            vizzu_minor = f"{vizzu_version[0]}.{vizzu_version[1]}"
            fh_config.write(PLACEHOLDER.format(ipyvizzu_minor, vizzu_minor))


def main() -> None:
    with chdir(REPO_PATH):
        Placeholder.generate()


main()
