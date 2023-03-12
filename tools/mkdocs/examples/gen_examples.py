"""A module for generating the example gallery."""

import os
from pathlib import Path
import re
import sys
from typing import List, Dict, Optional

import mkdocs_gen_files


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"
GEN_PATH = MKDOCS_PATH / "examples"
VIZZU_LIB_PATH = REPO_PATH / "vizzu-lib"
WEB_CONTENT_PATH = (
    VIZZU_LIB_PATH / "test" / "integration" / "test_cases" / "web_content"
)
TEST_DATA_PATH = VIZZU_LIB_PATH / "test" / "integration" / "test_data"
STATIC_EXAMPLES_PATH = WEB_CONTENT_PATH / "static"
ANIMATED_EXAMPLES_PATH = WEB_CONTENT_PATH / "animated"
PRESET_EXAMPLES_PATH = WEB_CONTENT_PATH / "presets"
SHOWCASES_PATH = REPO_PATH / "docs" / "showcases"
JS_ASSETS_PATH = "assets/javascripts"


sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from node import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Node,
)
from md import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Md,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class GenExamples:
    """A class for generating examples."""

    datafiles: Dict[str, bool] = {}

    datafile_re = re.compile(r"test_data\/(\w*).mjs")
    dataname_re = re.compile(r"import\s*\{\s*(.*)\s*}")
    title_re = re.compile(r"title\:\s'(.*)'")

    def __init__(self, name: str, src: Path, dst: str, video: bool = False) -> None:
        self._name = name
        self._src = src
        self._dst = dst

        self._video = video

        self._allowed: Dict[str, bool] = {}

    def allow(self, items: List[str]) -> None:
        """
        A method for setting alllowed examples.

        Args:
            items: Allowed examples list.
        """

        for item in items:
            self._allowed[item] = True

    @staticmethod
    def _get_content(item: Path) -> str:
        with open(item, "r", encoding="utf8") as fh_item:
            return fh_item.read()

    def _create_index(self, js_assets_path) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            meta = """---\nhide:\n  - toc\n---"""
            fh_index.write(f"{meta}\n\n")
            fh_index.write(f"# {self._name}\n")
            fh_index.write(f'<script src="{js_assets_path}/thumbs.js"></script>\n')

    def _add_image(self, item: Path, title: str) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            url = f"{Vizzu.get_vizzulibsite_url()}/{Vizzu.get_vizzu_version()}/{self._dst}"
            fh_index.write(
                "["
                + f"![{title}]"
                + f"({url}/{item.stem}.png)"
                + "{ class='image-gallery' }"
                + "]"
                + f"(./{item.stem}.md)\n"
            )

    def _add_video(self, item: Path, title: str) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            url = f"{Vizzu.get_vizzulibsite_url()}/{Vizzu.get_vizzu_version()}/{self._dst}"
            fh_index.write(
                f"<a href='./{item.stem}/' title='{title}'>"
                + "<video nocontrols autoplay muted loop class='image-gallery'"
                + f"src='{url}/{item.stem}.mp4'"
                + " type='video/mp4'></video>"
                + "</a>\n"
            )

    @staticmethod
    def _generate_example_data(datafile: str, dataname: str) -> None:
        datakey = "_".join([datafile, dataname])
        if dataname == "data":
            datakey = datafile
        if datakey not in GenExamples.datafiles:
            GenExamples.datafiles[datakey] = True

            datacontent = GenExamples._get_content(TEST_DATA_PATH / f"{datafile}.mjs")
            with mkdocs_gen_files.open(f"assets/data/{datafile}.js", "w") as fh_data:
                fh_data.write(datacontent)

            content = Node.node(
                True,
                GEN_PATH / "mjs2csv.mjs",
                f"{TEST_DATA_PATH}/{datafile}.mjs",
                dataname,
            )
            with mkdocs_gen_files.open(f"assets/data/{datakey}.csv", "w") as f_example:
                f_example.write(content)

    def _generate_example_js(
        self, item: Path, datafile: str, dataname: str, title: Optional[str] = None
    ) -> None:
        params = [str(item), str(TEST_DATA_PATH), datafile, dataname]

        dst_type = "js"
        if title:
            dst_type = "md"
            params.append(title)

        content = Node.node(True, GEN_PATH / f"mjs2{dst_type}.mjs", *params)
        if dst_type == "md":
            content = Vizzu.set_version(content)
            content = Md.format(content)
            with mkdocs_gen_files.open(
                f"{self._dst}/{item.stem}.{dst_type}", "w"
            ) as f_example:
                f_example.write(content)
        else:
            with mkdocs_gen_files.open(
                f"{self._dst}/{item.stem}/{item.stem}.{dst_type}", "w"
            ) as f_example:
                f_example.write(content)

    def _generate_example(
        self, item: Path, datafile: str, dataname: str, title: str
    ) -> None:
        self._generate_example_js(item, datafile, dataname, title)
        self._generate_example_js(item, datafile, dataname)
        GenExamples._generate_example_data(datafile, dataname)

    def generate(self) -> None:
        """A method for generating examples."""

        self._create_index("../../" + JS_ASSETS_PATH)
        src = self._src
        items = list(src.rglob("*.mjs"))
        items.sort(key=lambda f: f.stem)
        for item in items:
            if not self._allowed or self._allowed.get(item.stem, False):
                content = GenExamples._get_content(item)

                datafiles = re.findall(GenExamples.datafile_re, content)
                if not datafiles or len(datafiles) > 1:
                    raise ValueError("failed to find datafile")
                datafile = "".join(datafiles)

                datanames = re.findall(GenExamples.dataname_re, content)
                if not datanames or len(datanames) > 1:
                    raise ValueError("failed to find dataname")
                dataname = "".join(datanames)
                dataname = dataname.strip()

                titles = re.findall(GenExamples.title_re, content)
                if not titles:
                    raise ValueError("failed to find title")
                title = titles[0]
                if len(titles) > 1:
                    title = " to ".join([title, titles[-1]])
                    title = title.replace("Chart", "")

                if self._video:
                    self._add_video(item, title)
                else:
                    self._add_image(item, title)

                self._generate_example(item, datafile, dataname, title)


class GenShowcases(GenExamples):
    """A class for generating showcases index page."""

    def __init__(self, name: str, src: Path, dst: str) -> None:
        super().__init__(name, src, dst, True)

    def generate(self) -> None:
        """A method for overwriting GenExamples.generate method."""

        self._create_index("../" + JS_ASSETS_PATH)
        src = self._src
        items = list(src.rglob("*.js")) + list(src.rglob("main.html"))
        for item in items:
            content = GenExamples._get_content(item)
            content = Vizzu.set_version(content)
            with mkdocs_gen_files.open(
                self._dst + "/" + os.path.relpath(item, SHOWCASES_PATH), "w"
            ) as fh_js:
                fh_js.write(content)

        items = list(src.rglob("*.md"))
        items.sort(key=lambda f: f.stem)
        url = f"{Vizzu.get_vizzulibsite_url()}/{Vizzu.get_vizzu_version()}/{self._dst}"
        for item in items:
            with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
                fh_index.write(
                    f"<a href='./{item.stem}/' title=''>"
                    + "<video nocontrols autoplay muted loop class='image-gallery'"
                    + f"src='{url}/{item.stem}.mp4'"
                    + " type='video/mp4'></video>"
                    + "</a>\n"
                )


def main() -> None:
    """
    The main method.
    It generates the example gallery.
    """

    with chdir(REPO_PATH):
        presets = GenExamples(
            "Preset charts",
            PRESET_EXAMPLES_PATH,
            "examples/presets",
        )
        presets.generate()

        static = GenExamples(
            "Static charts",
            STATIC_EXAMPLES_PATH,
            "examples/static",
        )
        static.generate()

        animated = GenExamples(
            "Animated charts",
            ANIMATED_EXAMPLES_PATH,
            "examples/animated",
            video=True,
        )
        animated.generate()

        real = GenShowcases(
            "Showcases",
            SHOWCASES_PATH,
            "showcases",
        )
        real.generate()


main()
