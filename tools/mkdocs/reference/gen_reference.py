"""A module for generating the code reference."""

from pathlib import Path
import sys

import mkdocs_gen_files  # type: ignore

import ipyvizzu


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"


sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class Reference:
    """A class for generating the code reference."""

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

            if parts[-1] == "__main__":
                continue
            if parts[-1] == "__init__":
                parts = parts[:-1]
                doc_path = doc_path.with_name("index.md")
                full_doc_path = full_doc_path.with_name("index.md")

            item = ".".join(parts)
            if item == "ipyvizzu":
                mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path)
                with mkdocs_gen_files.open(full_doc_path, "w") as f_md:
                    f_md.write(f"# {item}\n")
                    f_md.write(f"{ipyvizzu.__doc__}\n")
            else:
                mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path)
                with mkdocs_gen_files.open(full_doc_path, "w") as f_md:
                    item = ".".join(parts)
                    f_md.write(f"::: {item}")

    @staticmethod
    def generate_version_script(file: str) -> None:
        """
        A method for generating an external JavaScript file that sets vizzu-lib version.

        Args:
            file: The destination file.
        """

        with mkdocs_gen_files.open(file, "w") as f_js:
            vizzulibsite_url = Vizzu.get_vizzulibsite_url()
            vizzu_version = Vizzu.get_vizzu_version()
            f_js.write(
                f"""
document.addEventListener("DOMContentLoaded", (event) => {{
  if (window.location.href.includes("/reference/")) {{
    const links = document.links;
    for (let i = 0; i < links.length; i++) {{
      if (
        links[i].hostname !== window.location.hostname &&
        links[i].href.includes("{vizzulibsite_url}")
      ) {{
        links[i].href = links[i].href.replace("latest", "{vizzu_version}");
      }}
    }}
  }}
}});
            """
            )


def main() -> None:
    """
    The main method.
    It generates the code reference.
    """

    with chdir(REPO_PATH):
        Reference.generate("reference")
        Reference.generate_version_script("assets/javascripts/codereflinks.js")


main()
