"""A module for working with context."""

import os
from pathlib import Path
import sys
from typing import Union


if sys.version_info >= (3, 11):
    from contextlib import chdir  # pylint: disable=unused-import
else:
    from contextlib import contextmanager

    @contextmanager
    def chdir(path: Union[str, Path]):
        """
        A method for changing the current working directory upon entering
        and restoring the old one on exit.
        """

        old_wd = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(old_wd)
