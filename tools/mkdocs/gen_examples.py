import pathlib
import re
from subprocess import PIPE, Popen

import mkdocs_gen_files


class VizzuLib:

    version = "0.6"
    url = f"https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/{version}/content"


class Examples:

    datafiles = {}

    datafile_re = re.compile(r"test_data\/(\w*).mjs")
    title_re = re.compile(r"title\:\s'(.*)'")


class GenExamples:
    def __init__(self, name, src, dst) -> None:
        self._name = name
        self._src = src
        self._dst = dst

    @staticmethod
    def get_content(item):
        with open(item, "r") as fh_item:
            return fh_item.read()

    @staticmethod
    def generate_example_data(datafile):
        with open(
            f"./vizzu-lib/test/integration/test_data/{datafile}.mjs",
            "r",
        ) as fh_data:
            datacontent = fh_data.read()
        with mkdocs_gen_files.open(f"javascripts/{datafile}.js", "w") as fh_data:
            fh_data.write(datacontent)

    def generate_example_js(self, item, datafile, title=None):
        js_type = "js"
        if title:
            js_type = "md"

        command = [
            "node",
            f"./tools/mkdocs/mjs2{js_type}.mjs",
            f"../../{item}",
            datafile,
        ]
        if js_type == "md":
            command.append(title)

        p = Popen(
            command,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        )
        outs, errs = p.communicate()

        if p.returncode or errs:
            if errs:
                raise RuntimeError(errs.decode())
            raise RuntimeError(f"failed to run mjs2{js_type}")

        content = outs.decode()
        with mkdocs_gen_files.open(
            f"{self._dst}/{item.stem}.{js_type}", "w"
        ) as f_example:
            f_example.write(content)

    def generate_example(self, item, datafile, title):
        self.generate_example_js(item, datafile, title)
        self.generate_example_js(item, datafile)
        if datafile not in Examples.datafiles:
            Examples.datafiles[datafile] = True
            GenExamples.generate_example_data(datafile)

    def generate(self):
        with mkdocs_gen_files.open(f"{self._dst}/index.md", "a") as fh_index:
            meta = """---\nhide:\n  - toc\n---"""
            fh_index.write(f"{meta}\n\n")

            fh_index.write(f"# {self._name}\n")

            src = pathlib.Path(f"./vizzu-lib/{self._src}")
            for item in sorted(src.iterdir()):
                if item.is_file() and item.suffix == ".mjs":
                    fh_index.write(
                        "["
                        + "![Image title]"
                        + f"({VizzuLib.url}/{self._dst}/{item.stem}.png)"
                        + "{ class='example-gallery' }"
                        + "]"
                        + f"(./{item.stem}.md)\n"
                    )

                    content = GenExamples.get_content(item)
                    datafile = " ".join(re.findall(Examples.datafile_re, content))
                    title = " ".join(re.findall(Examples.title_re, content))

                    self.generate_example(item, datafile, title)


def main() -> None:

    presets = GenExamples(
        "Preset charts",
        "test/integration/test_cases/web_content/preset",
        "examples/presets",
    )
    presets.generate()


main()
