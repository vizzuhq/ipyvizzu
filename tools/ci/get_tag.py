# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from contextlib import chdir
from pathlib import Path
import re
import sys
import requests

REPO_PATH = Path(__file__).parent / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"

sys.path.insert(0, str(TOOLS_PATH / "modules"))

from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)

OWNER = "vizzuhq"
REPO = "vizzu-lib"


if __name__ == "__main__":
    with chdir(REPO_PATH):
        API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/tags"

        vizzu_version = Vizzu.get_vizzu_version()

        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        tags = response.json()
        patch_versions = [
            int(
                re.search(
                    rf"^v{re.escape(vizzu_version)}\.(\d+)", tag["name"]  # type: ignore
                ).group(1)
            )
            for tag in tags
            if re.search(rf"^v{re.escape(vizzu_version)}\.(\d+)", tag["name"])
        ]
        latest_patch_version = max(patch_versions)

        CHECKOUT_REF = f"v{vizzu_version}.{latest_patch_version}"
        print(CHECKOUT_REF)
