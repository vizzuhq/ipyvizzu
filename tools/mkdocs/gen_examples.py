"""Generate the example gallery."""

# pylint: disable=too-few-public-methods

import pathlib
import re
from subprocess import PIPE, Popen
from typing import List, Dict, Optional

import mkdocs_gen_files


class VizzuLib:
    """A class for providing vizzu-lib related information."""

    version = "0.6"
    url = f"https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/{version}/content"


class Examples:
    """A class for providing example related information."""

    datafiles: Dict[str, bool] = {}

    datafile_re = re.compile(r"test_data\/(\w*).mjs")
    title_re = re.compile(r"title\:\s'(.*)'")


class GenExamples:
    """A class for generating examples."""

    def __init__(self, name: str, src: str, dst: str, video: bool = False) -> None:
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
    def _get_content(item: pathlib.Path) -> str:
        with open(item, "r", encoding="utf8") as fh_item:
            return fh_item.read()

    def _create_index(self) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            meta = """---\nhide:\n  - toc\n---"""
            fh_index.write(f"{meta}\n\n")
            fh_index.write(f"# {self._name}\n")

    def _add_image(self, item: pathlib.Path, title: str) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            fh_index.write(
                "["
                + f"![{title}]"
                + f"({VizzuLib.url}/{self._dst}/{item.stem}.png)"
                + "{ class='example-gallery' }"
                + "]"
                + f"(./{item.stem}.md)\n"
            )

    def _add_video(self, item: pathlib.Path, title: str) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            fh_index.write(
                "<div>"
                + f"<a href='./{item.stem}.html' title='{title}'>"
                + "<video nocontrols autoplay muted loop class='example-gallery'"
                + f"src='{VizzuLib.url}/{self._dst}/{item.stem}.mp4'"
                + " type='video/mp4'></video>"
                + "</a>"
                + "</div>\n"
            )

    @staticmethod
    def _generate_example_data(datafile: str) -> None:
        if datafile not in Examples.datafiles:
            Examples.datafiles[datafile] = True
            with open(
                f"./vizzu-lib/test/integration/test_data/{datafile}.mjs",
                "r",
                encoding="utf8",
            ) as fh_data:
                datacontent = fh_data.read()
            with mkdocs_gen_files.open(f"javascripts/{datafile}.js", "w") as fh_data:
                fh_data.write(datacontent)

    def _generate_example_js(
        self, item: pathlib.Path, datafile: str, title: Optional[str] = None
    ) -> None:
        js_type = "js"
        if title:
            js_type = "md"

        command: List[str] = [
            "node",
            f"./tools/mkdocs/mjs2{js_type}.mjs",
            f"../../{item}",
            datafile,
        ]
        if title:
            command.append(title)

        with Popen(
            command,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        ) as node:
            outs, errs = node.communicate()

        if node.returncode or errs:
            if errs:
                raise RuntimeError(errs.decode())
            raise RuntimeError(f"failed to run mjs2{js_type}")

        content = outs.decode()
        with mkdocs_gen_files.open(
            f"{self._dst}/{item.stem}.{js_type}", "w"
        ) as f_example:
            f_example.write(content)

    def _generate_example(self, item: pathlib.Path, datafile: str, title: str) -> None:
        self._generate_example_js(item, datafile, title)
        self._generate_example_js(item, datafile)
        GenExamples._generate_example_data(datafile)

    def generate(self) -> None:
        """A method for generating examples."""

        self._create_index()

        src = pathlib.Path(f"./vizzu-lib/{self._src}")
        items = list(src.rglob("*.mjs"))
        items.sort(key=lambda f: f.stem)
        for item in items:
            if not self._allowed or self._allowed.get(item.stem, False):
                content = GenExamples._get_content(item)

                datafiles = re.findall(Examples.datafile_re, content)
                if not datafiles or len(datafiles) > 1:
                    raise ValueError("failed to find datafile")
                datafile = "".join(datafiles)

                titles = re.findall(Examples.title_re, content)
                if not titles:
                    raise ValueError("failed to find title")
                title = ", ".join(titles)

                if self._video:
                    self._add_video(item, title)
                else:
                    self._add_image(item, title)

                self._generate_example(item, datafile, title)


def main() -> None:
    """
    The main method.
    It generates the example gallery.
    """

    presets = GenExamples(
        "Preset charts",
        "test/integration/test_cases/web_content/preset",
        "examples/presets",
    )
    presets.generate()

    static = GenExamples(
        "Static charts",
        "test/integration/test_cases/web_content/sample_static",
        "examples/static",
    )
    static.generate()

    animated = GenExamples(
        "Animated charts",
        "test/integration/test_cases/web_content/templates",
        "examples/animated",
        video=True,
    )
    animated.allow(
        [
            "composition_percentage_area_stream_3dis_1con",
            "composition_percentage_column_3dis_1con",
            "composition_percentage_column_stream_3dis_1con",
            "composition_comparison_pie_coxcomb_column_2dis_2con",
            "merge_split_area_stream_3dis_1con",
            "merge_split_bar",
            "merge_split_radial_stacked_rectangle_2dis_1con",
            "orientation_circle",
            "orientation_marimekko_rectangle_2dis_2con",
            "pie_donut2_rectangle_1dis_1con",
            "relationship_comparison_circle_2_bubble_plot",
            "relationship_total_bubble_plot_column",
            "stack_group_area_line",
            "stack_group_circle",
            "stack_group_treemap",
            "total_element_bubble_2_bar",
            "total_element_bubble_column",
            "total_time_area_column",
            "total_time_bar_line",
            "treemap_radial",
            "zoom_area",
        ]
    )
    animated.generate()


main()
