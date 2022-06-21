"""
A module used to postprocess
mocked test outputs
"""

import re
from unittest.mock import MagicMock


class Normalizer:
    """
    A class used to normalize
    mocked test outputs
    """

    def __init__(self):
        self.id1_pattern = re.compile(r"'[a-f0-9]{7}'", flags=re.MULTILINE)
        self.id2_pattern = re.compile(r"\"[a-f0-9]{7}\"", flags=re.MULTILINE)

    def normalize_id(self, output: str) -> str:
        """
        A method used to replace
        uuids found with a regular expression with "id"
        """

        normalized_output = output
        normalized_output = self.id1_pattern.sub("id", normalized_output)
        normalized_output = self.id2_pattern.sub("id", normalized_output)
        return normalized_output

    def normalize_output(self, output: MagicMock, start_index: int = 0) -> str:
        """
        A method used to merge and normalize
        mocked test outputs
        """

        output_items = []
        for block in output.call_args_list[start_index:]:
            output_items.append(block.args[0])
        return self.normalize_id("\n".join(output_items)).strip()
