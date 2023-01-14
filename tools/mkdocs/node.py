"""A module for working with NodeJs."""

from pathlib import Path
from subprocess import PIPE, Popen


class Node:
    """A class for working with NodeJs."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def run(script: str, *params: str) -> str:
        """
        A static method for running NodeJs commands.

        Args:
            script: Path of the NodeJs script.
            *params: Parameters of the NodeJs script.

        Returns:
            Command output.
        """

        with Popen(
            ["node", script, *params],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        ) as node:
            outs, errs = node.communicate()

        if node.returncode or errs:
            if errs:
                raise RuntimeError(errs.decode())
            raise RuntimeError(f"failed to run {Path(script).stem}")

        return outs.decode()
