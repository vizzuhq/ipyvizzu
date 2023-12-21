"""A module for storing version number."""

import sys


__version__ = "0.17.0"
__version_info__ = tuple(map(int, __version__.split(".")))

PYENV = sys.version_info
