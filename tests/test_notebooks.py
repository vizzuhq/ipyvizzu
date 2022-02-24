import unittest
import pathlib
import json
import re
import os

from unittest.mock import patch


class TestNotebook(unittest.TestCase):
    maxDiff = None

    exclude_list = {"data.ipynb"}

    @classmethod
    def setUpClass(cls):
        cls.div_pattern = re.compile(r"myVizzu_\d+", flags=re.MULTILINE)
        cls.project_dir = pathlib.Path(__file__).parent.parent

    @classmethod
    def normalize_div_id(cls, output):
        normalized_output = cls.div_pattern.sub("myVizzu", output, count=2)
        return normalized_output

    @patch("ipyvizzu.display_html")
    def test(self, display_html):
        examples_dir = self.project_dir / "docs/examples"

        for path in examples_dir.glob("*.ipynb"):
            if path.name in self.exclude_list:
                continue

            with self.subTest(path=path):
                os.chdir(examples_dir)
                notebook = parse_notebook(path)
                for source, output in notebook:
                    exec(source)  # pylint: disable=exec-used
                    self.assertEqual(
                        self.normalize_div_id(display_html.call_args.args[0]),
                        self.normalize_div_id(output),
                    )


def parse_notebook(path):
    with path.open() as file_desc:
        notebook = json.load(file_desc)

    return [
        (
            parse_source(cell),
            parse_outputs(cell),
        )
        for cell in notebook["cells"]
        if cell["cell_type"] == "code" and cell["source"]
    ]


def parse_outputs(cell):
    outputs = "".join(parse_output(output) for output in cell["outputs"])
    return outputs


def parse_output(output):
    return "".join(output["data"].get("text/html", []))


def parse_source(cell):
    return "".join(cell["source"])
