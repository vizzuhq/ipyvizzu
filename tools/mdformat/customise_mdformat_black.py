"""Customise the installed mdformat-black package"""

import argparse
from pathlib import Path


def main() -> None:
    """
    The main method.
    It customises the installed mdformat-black package.
    """

    parser = argparse.ArgumentParser(
        prog="customise_mdformat_black.py",
        description="Customise the installed mdformat-black package",
    )
    parser.add_argument("-v", "--venv", type=str, required=True)
    parser.add_argument("-l", "--line_length", type=int, default=88)
    args = parser.parse_args()

    mdformat_black_original_code = (
        "return black.format_str(unformatted, mode=black.Mode())"
    )
    mdformat_black_new_code = (
        "return black.format_str("
        + "unformatted, "
        + f"mode=black.Mode(line_length={args.line_length})"
        + ")"
    )

    try:
        venv_path = Path(args.venv)
        mdformat_black_paths = list(venv_path.glob("**/mdformat_black/"))
        assert len(mdformat_black_paths) == 1, "not or multiple mdformat_black found"
        for mdformat_black_path in mdformat_black_paths:
            with open(
                mdformat_black_path / "__init__.py", "r", encoding="utf8"
            ) as file_handler:
                mdformat_black_code = file_handler.read()
            assert (
                mdformat_black_original_code in mdformat_black_code
                or mdformat_black_new_code in mdformat_black_code
            ), "mdformat_black code changed"
            with open(
                mdformat_black_path / "__init__.py", "w", encoding="utf8"
            ) as file_handler:
                file_handler.write(
                    mdformat_black_code.replace(
                        mdformat_black_original_code, mdformat_black_new_code
                    )
                )
    except Exception as exc:
        raise NotImplementedError(
            "the currently installed mdformat-black is not compatible with this script"
        ) from exc


main()
