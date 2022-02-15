import unittest
import pathlib
import json
import re

from unittest.mock import patch


class TestNotebook(unittest.TestCase):
    maxDiff = None

    exclude_list = {"data.ipynb"}

    @classmethod
    def setUpClass(cls):
        cls.div_pattern = re.compile(r"myVizzu_\d+", flags=re.MULTILINE)

    @classmethod
    def normalize_div_id(cls, output):
        normalized_output = cls.div_pattern.sub("myVizzu", output, count=2)
        return normalized_output

    @patch("ipyvizzu.display_html")
    def test(self, display_html):
        for path in pathlib.Path("docs/examples").glob("*.ipynb"):
            if path.name in self.exclude_list:
                continue

            with self.subTest(path=path):
                notebook = parse_notebook(path)
                for source, output in notebook:
                    exec(source)
                    self.assertEqual(
                        self.normalize_div_id(display_html.call_args.args[0]),
                        self.normalize_div_id(output),
                    )


def parse_notebook(path):
    with path.open() as fp:
        notebook = json.load(fp)

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