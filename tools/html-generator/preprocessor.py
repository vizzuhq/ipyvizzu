from nbconvert.preprocessors import Preprocessor
import re


class NbPreprocessor(Preprocessor):

    def preprocess_cell(self, cell, resources, index):

        if 'source' in cell and cell.cell_type == "markdown":
            cell.source = re.sub(r"\[([^]]*)\]\(([^)]*)\.ipynb([^]]*)?\)",r"[\1](\2.html\3)", cell.source)

        return cell, resources