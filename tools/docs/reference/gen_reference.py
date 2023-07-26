# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pathlib import Path
import sys
from types import ModuleType

import mkdocs_gen_files  # type: ignore

import ipyvizzu

REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
TOOLS_PATH = REPO_PATH / "tools"
MKDOCS_PATH = TOOLS_PATH / "docs"

sys.path.insert(0, str(TOOLS_PATH / "modules"))

from chdir import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
    VIZZU_SITE_URL,
)


class Reference:
    @staticmethod
    def generate(package: ModuleType, folder: str) -> None:
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
            if item == package.__name__:
                mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path)
                with mkdocs_gen_files.open(full_doc_path, "w") as f_md:
                    f_md.write(f"{package.__doc__}\n")
                    for item in package.__all__:
                        f_md.write(f"::: {package.__name__}.{item}\n")
                        f_md.write("    options:\n")
                        f_md.write("      show_root_members_full_path: false\n")
            else:
                mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path)
                with mkdocs_gen_files.open(full_doc_path, "w") as f_md:
                    f_md.write(f"::: {item}")

    @staticmethod
    def generate_version_script(file: str) -> None:
        with mkdocs_gen_files.open(file, "w") as f_js:
            vizzu_version = Vizzu.get_vizzu_version()
            f_js.write(
                f"""
document.addEventListener("DOMContentLoaded", (event) => {{
  if (window.location.href.includes("/reference/")) {{
    const links = document.links;
    for (let i = 0; i < links.length; i++) {{
      if (
        links[i].hostname !== window.location.hostname &&
        links[i].href.includes("{VIZZU_SITE_URL}")
      ) {{
        links[i].href = links[i].href.replace("latest", "{vizzu_version}");
      }}
    }}
  }}
}});
            """
            )


def main() -> None:
    with chdir(REPO_PATH):
        Reference.generate(ipyvizzu, "reference")
        Reference.generate_version_script("assets/javascripts/codereflinks.js")


main()
