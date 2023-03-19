"""A module for generating pages."""

import os
from pathlib import Path
from typing import Union, Optional, List
import sys

import yaml
import mkdocs_gen_files  # type: ignore


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

sys.path.insert(0, str(MKDOCS_PATH / "modules"))

from context import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    chdir,
)
from vizzu import (  # pylint: disable=import-error, wrong-import-position, wrong-import-order
    Vizzu,
)


class MkdocsConfig:
    """A class for loading mkdocs configuration."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def _format_url(url: Optional[str]) -> Optional[str]:
        if url and url.endswith("/"):
            return url[:-1]
        return url

    @staticmethod
    def _format(config: dict) -> dict:
        if "site_url" in config:
            config["site_url"] = MkdocsConfig._format_url(config["site_url"])
        return config

    @staticmethod
    def load(config: Path) -> dict:
        """
        A method for loading mkdocs configuration from yaml file.

        Args:
            config: The path of the yaml configuration file.

        Returns:
            A dictionary that contains the mkdocs configuration.
        """

        with open(config, "rt", encoding="utf8") as f_yml:
            return MkdocsConfig._format(yaml.load(f_yml, Loader=yaml.FullLoader))


class IndexPages:
    """A class for creating navigation index files."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def _write_index_file(file: str, toc: list) -> None:
        for item in toc:
            if isinstance(item, str):
                IndexPages._write_str_index(file, item)
            elif isinstance(item, dict):
                IndexPages._write_dict_index(file, item)
            else:
                raise NotImplementedError(f"{item}")

    @staticmethod
    def _write_str_index(file: str, item: str) -> None:
        with mkdocs_gen_files.open(file, "a") as f_index:
            parts = item.split("/")
            part = parts[-1].replace(".md", "").capitalize()
            link = Path(os.path.relpath(item, Path(file).parent))
            f_index.write(f"* [{part}]({link})\n")

    @staticmethod
    def _write_dict_index(file: str, item: dict) -> None:
        with mkdocs_gen_files.open(file, "a") as f_index:
            for key in item:
                if isinstance(item[key], str):
                    link = Path(os.path.relpath(item[key], Path(file).parent))
                    f_index.write(f"* [{key}]({link})\n")
                    continue
                if item[key] and isinstance(item[key], list):
                    if isinstance(item[key][0], str):
                        if item[key][0].endswith("index.md"):
                            link = Path(
                                os.path.relpath(item[key][0], Path(file).parent)
                            )
                            f_index.write(f"* [{key}]({link})\n")
                            continue
                raise NotImplementedError(f"{item}")

    @staticmethod
    def generate(
        nav_item: Union[list, dict, str], skip: Optional[List[str]] = None
    ) -> None:
        """
        A method for creating section indices for the navigation.

        Args:
            nav_item: Part of the navigation.
            skip: List of index files to skip.
        """

        if isinstance(nav_item, list):
            if (
                nav_item
                and isinstance(nav_item[0], str)
                and nav_item[0].endswith("index.md")
            ):
                if not skip or nav_item[0] not in skip:
                    original = Path("docs", nav_item[0])
                    if original.exists():
                        mkdocs_gen_files.set_edit_path(nav_item[0], nav_item[0])
                    with mkdocs_gen_files.open(nav_item[0], "a") as f_index:
                        f_index.write("\n")
                    IndexPages._write_index_file(file=nav_item[0], toc=nav_item[1:])
            for item in nav_item:
                IndexPages.generate(nav_item=item, skip=skip)
        elif isinstance(nav_item, dict):
            for key in nav_item:
                IndexPages.generate(nav_item=nav_item[key], skip=skip)


class Page:
    """A class for creating a page from a file outside the docs folder."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate(src: Path, dst: str, pos: str, site: str, keep: bool = False) -> None:
        """
        A method for generating a page.

        Args:
            src: Source path.
            dst: Destination path.
            pos: Destination relative pos to the index.
            site: Site url.
            keep: Place the original content into a pre tag.
        """

        with open(src, "rt", encoding="utf8") as f_src:
            content = f_src.read()

        content = content.replace(f"{site}/latest/", pos).replace(f"{site}/latest", pos)

        if dst == "index.md":
            example = "./showcases/titanic/titanic.csv"
            content = content.replace(example, f"{site}/latest/{example[2:]}")

        content = Vizzu.set_version(content)

        if keep:
            content = f"<pre>{content}</pre>"

        mkdocs_gen_files.set_edit_path(dst, ".." / Path(dst).parent / Path(src).name)
        with mkdocs_gen_files.open(dst, "w") as f_dst:
            f_dst.write(content)


class Docs:
    """A class for creating docs pages."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def generate(skip: Optional[List[str]] = None) -> None:
        """
        A method for generating docs pages.

        Args:
            skip: List of file names to skip.
        """

        docs_path = REPO_PATH / "docs"
        for path in list(docs_path.rglob("*.md")) + list(docs_path.rglob("*.js")):
            if skip and path.name in skip:
                continue
            with open(path, "rt", encoding="utf8") as f_src:
                dst = path.relative_to(docs_path)
                content = f_src.read()
                if path.suffix == ".md":
                    content = Vizzu.set_version(content)
                    mkdocs_gen_files.set_edit_path(dst, dst)
                with mkdocs_gen_files.open(dst, "w") as f_dst:
                    f_dst.write(content)


def main() -> None:
    """
    The main method.
    It prepares files for the documentation site.
    """

    with chdir(REPO_PATH):
        config = MkdocsConfig.load(MKDOCS_PATH / "mkdocs.yml")

        Docs.generate()

        IndexPages.generate(nav_item=config["nav"], skip=["examples/index.md"])

        Page.generate(
            src=REPO_PATH / "README.md",
            dst="index.md",
            pos="./",
            site=config["site_url"],
        )

        Page.generate(
            src=REPO_PATH / "CONTRIBUTING.md",
            dst="CONTRIBUTING.md",
            pos="../",
            site=config["site_url"],
        )

        Page.generate(
            src=REPO_PATH / "CODE_OF_CONDUCT.md",
            dst="CODE_OF_CONDUCT.md",
            pos="../",
            site=config["site_url"],
        )

        Page.generate(
            src=REPO_PATH / "LICENSE",
            dst="LICENSE.md",
            pos="../",
            site=config["site_url"],
            keep=True,
        )


main()
