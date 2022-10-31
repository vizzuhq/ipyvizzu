"""A module for preprocessing notebook files."""

import re
from nbconvert.preprocessors import Preprocessor  # type: ignore


class NbPreprocessor(Preprocessor):
    """
    A class for preprocessing notebook cells before converting them to another format.
    """

    def preprocess_cell(self, cell, resources, index):
        """
        Overrides Preprocessor.preprocess_cell method.
        In markdown cells, it replaces the alignment format and ipynb links with html links.
        In code cells, it sets IpyVizzu.nbconvert value to true.
        """

        if "source" in cell and cell.cell_type == "markdown":
            cell.source = re.sub(
                r"\[([^]]*)\]\(([^)]*)\.ipynb([^]]*)?\)",
                r"[\1](\2.html\3)",
                cell.source,
            )

            cell.source = re.sub(
                r"\<p align\=\"center\"",
                '<p style="text-align: center"',
                cell.source,
            )

        if "outputs" in cell and cell.cell_type == "code":
            for i, output in enumerate(cell.outputs):
                if "data" in output and "application/javascript" in output["data"]:
                    cell.outputs[i]["data"]["application/javascript"] = re.sub(
                        r"(IpyVizzu.nbconvert = )(false)(;)",
                        r"\1true\3",
                        output["data"]["application/javascript"],
                    )

        return cell, resources
