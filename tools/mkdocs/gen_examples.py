"""A module for generating the example gallery."""

from pathlib import Path
import re
from subprocess import PIPE, Popen
from typing import List, Dict, Optional

import mdformat
import mkdocs_gen_files

from ipyvizzu import Chart


SET_PARENT_STYLE: str = """
<script>
const currentScript = document.currentScript;
document.addEventListener("DOMContentLoaded", (event) => {
  const parentContainer = currentScript.nextElementSibling;
  parentContainer.style.display = "flex";
  parentContainer.style["flex-wrap"] = "wrap";
  parentContainer.style.justifyContent = "center";
});
</script>
"""


class VizzuLib:
    """A class for providing vizzu-lib related information."""

    @staticmethod
    def version() -> str:
        """
        A method for returning vizzu-lib version.

        Returns:
            Version of vizzu-lib.
        """

        cdn = Chart.VIZZU
        return re.search(r"vizzu@([\d.]+)/", cdn).group(1)  # type: ignore

    @staticmethod
    def url() -> str:
        """
        A method for returning vizzu-lib doc url.

        Returns:
            Doc url of vizzu-lib.
        """

        version = VizzuLib.version()
        return (
            f"https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/{version}/content"
        )


class GenExamples:
    """A class for generating examples."""

    datafiles: Dict[str, bool] = {}

    datafile_re = re.compile(r"test_data\/(\w*).mjs")
    title_re = re.compile(r"title\:\s'(.*)'")

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
    def _get_content(item: Path) -> str:
        with open(item, "r", encoding="utf8") as fh_item:
            return fh_item.read()

    def _create_index(self) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            meta = """---\nhide:\n  - toc\n---"""
            fh_index.write(f"{meta}\n\n")
            fh_index.write(f"# {self._name}\n")
            fh_index.write(SET_PARENT_STYLE)

    def _add_image(self, item: Path, title: str) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            fh_index.write(
                "["
                + f"![{title}]"
                + f"({VizzuLib.url()}/{self._dst}/{item.stem}.png)"
                + "{ class='image-gallery' }"
                + "]"
                + f"(./{item.stem}.md)\n"
            )

    def _add_video(self, item: Path, title: str) -> None:
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            fh_index.write(
                f"<a href='./{item.stem}.html' title='{title}'>"
                + "<video nocontrols autoplay muted loop class='image-gallery'"
                + f"src='{VizzuLib.url()}/{self._dst}/{item.stem}.mp4'"
                + " type='video/mp4'></video>"
                + "</a>\n"
            )

    @staticmethod
    def _run_node(script: str, *params: str) -> str:
        with Popen(
            ["node", script, *params],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        ) as node:
            outs, errs = node.communicate()

        if node.returncode or errs:
            if errs:
                raise RuntimeError(errs.decode())
            raise RuntimeError(f"failed to run {Path(script).stem}")

        return outs.decode()

    @staticmethod
    def _generate_example_data(datafile: str) -> None:
        if datafile not in GenExamples.datafiles:
            GenExamples.datafiles[datafile] = True

            with open(
                f"./vizzu-lib/test/integration/test_data/{datafile}.mjs",
                "r",
                encoding="utf8",
            ) as fh_data:
                datacontent = fh_data.read()
            with mkdocs_gen_files.open(f"data/{datafile}.js", "w") as fh_data:
                fh_data.write(datacontent)

            content = GenExamples._run_node(
                "./tools/mkdocs/mjs2csv.mjs",
                f"../../vizzu-lib/test/integration/test_data/{datafile}.mjs",
            )
            with mkdocs_gen_files.open(f"data/{datafile}.csv", "w") as f_example:
                f_example.write(content)

    def _generate_example_js(
        self, item: Path, datafile: str, title: Optional[str] = None
    ) -> None:
        params = [f"../../{item}", datafile]

        dst_type = "js"
        if title:
            dst_type = "md"
            params.append(title)

        content = GenExamples._run_node(f"./tools/mkdocs/mjs2{dst_type}.mjs", *params)
        if dst_type == "md":
            content = mdformat.text(  # type: ignore
                content,
                options={"wrap": 80, "end-of-line": "keep", "line-length": 70},
                extensions={"gfm", "tables", "footnote", "frontmatter", "configblack"},
                codeformatters={
                    "python",
                    "bash",
                    "sh",
                    "json",
                    "toml",
                    "yaml",
                    "javascript",
                    "js",
                    "css",
                    "html",
                    "xml",
                },
            )

        with mkdocs_gen_files.open(
            f"{self._dst}/{item.stem}.{dst_type}", "w"
        ) as f_example:
            f_example.write(content)

    def _generate_example(self, item: Path, datafile: str, title: str) -> None:
        self._generate_example_js(item, datafile, title)
        self._generate_example_js(item, datafile)
        GenExamples._generate_example_data(datafile)

    def generate(self) -> None:
        """A method for generating examples."""

        self._create_index()
        src = Path(f"./vizzu-lib/{self._src}")
        items = list(src.rglob("*.mjs"))
        items.sort(key=lambda f: f.stem)
        for item in items:
            if not self._allowed or self._allowed.get(item.stem, False):
                content = GenExamples._get_content(item)

                datafiles = re.findall(GenExamples.datafile_re, content)
                if not datafiles or len(datafiles) > 1:
                    raise ValueError("failed to find datafile")
                datafile = "".join(datafiles)

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

                self._generate_example(item, datafile, title)


class GenRealLifeExamples(GenExamples):
    """A class for generating real life examples index page."""

    def __init__(self, name: str, src: str, dst: str) -> None:
        super().__init__(name, src, dst, True)

    def generate(self) -> None:
        """A method for overwriting GenExamples.generate method."""

        self._create_index()
        src = Path(self._src)
        items = list(src.rglob("*.md"))
        items.sort(key=lambda f: f.stem)
        for item in items:
            with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
                fh_index.write(
                    f"<a href='./{item.stem}.html' title=''>"
                    + "<video nocontrols autoplay muted loop class='image-gallery'"
                    + f"src='{VizzuLib.url()}/{self._dst}/{item.stem}.mp4'"
                    + " type='video/mp4'></video>"
                    + "</a>\n"
                )


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

    real = GenRealLifeExamples(
        "Real life examples",
        "./docs/examples/stories/",
        "examples/stories",
    )
    real.generate()


main()
