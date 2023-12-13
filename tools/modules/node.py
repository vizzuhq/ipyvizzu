# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pathlib import Path
from subprocess import PIPE, Popen
from typing import Union


class Node:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def node(strict: bool, script: Union[str, Path], *params: str) -> str:
        with Popen(
            ["yarn", "node", script, *params],
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
