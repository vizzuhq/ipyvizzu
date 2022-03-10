import unittest
import pathlib
import json
import os


from unittest.mock import patch
from normalizer import Normalizer


class TestNotebook(unittest.TestCase):
    maxDiff = None

    exclude_list = {"data.ipynb"}

    @classmethod
    def setUpClass(cls):
        cls.project_dir = pathlib.Path(__file__).parent.parent
        cls.normalizer = Normalizer()

    def test(self):
        examples_dir = self.project_dir / "docs/examples"

        for path in examples_dir.glob("*.ipynb"):
            if path.name in self.exclude_list:
                continue

            with self.subTest(path=path):
                os.chdir(examples_dir)
                notebook = parse_notebook(path)
                for source, output in notebook:
                    display_html = patch("ipyvizzu.display_html").start()
                    exec(source)  # pylint: disable=exec-used
                    display_out = []
                    for block in display_html.call_args_list:
                        display_out.append(block.args[0])
                    self.assertEqual(
                        self.normalizer.normalize_id("\n".join(display_out)).strip(),
                        self.normalizer.normalize_id(output).strip(),
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
    outputs = "\n".join(parse_output(output) for output in cell["outputs"])
    return outputs


def parse_output(output):
    return "".join(output["data"].get("text/html", []))


def parse_source(cell):
    return "".join(cell["source"])
