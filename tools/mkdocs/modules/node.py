"""A module for working with NodeJs."""

from pathlib import Path
from subprocess import PIPE, Popen
from typing import Union


class Node:
    """A class for working with NodeJs."""

    @staticmethod
    def node(strict: bool, script: Union[str, Path], *params: str) -> str:
        """
        A static method for running NodeJs commands.

        Args:
            strict: Check stderr too.
            script: Path of the NodeJs script.
            *params: Parameters of the NodeJs script.

        Returns:
            Command output.
        """

        return Node.run(strict, "node", script, *params)

    @staticmethod
    def npx(strict: bool, script: Union[str, Path], *params: str) -> str:
        """
        A static method for running NodeJs commands.

        Args:
            strict: Check stderr too.
            script: Path of the NodeJs script.
            *params: Parameters of the NodeJs script.

        Returns:
            Command output.
        """

        return Node.run(strict, "npx", script, *params)

    @staticmethod
    def run(strict: bool, exe: str, script: Union[str, Path], *params: str) -> str:
        """
        A static method for running NodeJs commands.

        Args:
            script: Path of the NodeJs script.
            exe: Type of the executable.
            strict: Check stderr too.
            *params: Parameters of the NodeJs script.

        Returns:
            Command output.
        """

        with Popen(
            [exe, script, *params],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        ) as node:
            outs, errs = node.communicate()

        if errs:
            print(errs.decode())

        if node.returncode or (strict and errs):
            raise RuntimeError(f"failed to run {Path(script).stem}")

        return outs.decode()
