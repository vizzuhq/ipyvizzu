# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import re
import sys
from typing import Optional
from unittest.mock import MagicMock


class Normalizer:
    def __init__(self) -> None:
        self.id1_pattern = re.compile(r"'[a-f0-9]{7}'", flags=re.MULTILINE)
        self.id2_pattern = re.compile(r"\\'[a-f0-9]{7}\\'", flags=re.MULTILINE)
        self.id3_pattern = re.compile(r"\"[a-f0-9]{7}\"", flags=re.MULTILINE)

    def normalize_id(self, output: str) -> str:
        normalized_output = output
        normalized_output = self.id1_pattern.sub("id", normalized_output)
        normalized_output = self.id2_pattern.sub("id", normalized_output)
        normalized_output = self.id3_pattern.sub("id", normalized_output)
        return normalized_output

    def normalize_output(
        self, output: MagicMock, start_index: int = 0, end_index: Optional[int] = None
    ) -> str:
        output_items = []
        if not end_index:
            end_index = len(output.call_args_list)
        for block in output.call_args_list[start_index:end_index]:
            if sys.version_info >= (3, 8):
                args = block.args
            else:
                # TODO: remove once support for Python 3.7 is dropped
                args, _ = block
            output_items.append(args[0])
        return self.normalize_id("\n".join(output_items)).strip()
