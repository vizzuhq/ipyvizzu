import re
from nbconvert.preprocessors import Preprocessor


class NbPreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, index):

        if "source" in cell and cell.cell_type == "markdown":
            cell.source = re.sub(
                r"\[([^]]*)\]\(([^)]*)\.ipynb([^]]*)?\)",
                r"[\1](\2.html\3)",
                cell.source,
            )

        if "outputs" in cell and cell.cell_type == "code":
            for i, output in enumerate(cell.outputs):
                if "data" in output and "application/javascript" in output["data"]:
                    cell.outputs[i]["data"]["application/javascript"] = re.sub(
                        r"(// )(IpyVizzu._hide\(element\);|IpyVizzu._display\(this.elements\[chartId\], element\);)",  # pylint: disable=line-too-long
                        r"\2",
                        output["data"]["application/javascript"],
                    )

        return cell, resources
