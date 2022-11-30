"""Generate the code reference pages and navigation."""

# pylint: disable=too-few-public-methods

from pathlib import Path
from typing import Union, List
import re

import yaml
import mkdocs_gen_files  # type: ignore


class MkdocsConfig:
    """A class for working with mkdocs configuration."""

    @staticmethod
    def load() -> dict:
        """
        A method for loading mkdocs configuration.

        Returns:
            A dictionary that contains the mkdocs configuration.
        """

        with open(Path(__file__).parent / "mkdocs.yml", "rt", encoding="utf8") as f_yml:
            return yaml.load(f_yml, Loader=yaml.FullLoader)


class Index:
    """A class for creating index file from README."""

    @staticmethod
    def generate(readme: Path, site: str, ipynbs: List[str]) -> None:
        """
        A method for generating the index file.

        Args:
            readme: README.md path.
            site: Site url.
            ipynbs: List of html links that are ipynb files.
        """

        with open(readme, "rt", encoding="utf8") as f_readme:
            content = f_readme.read()

        for match in re.finditer(
            rf"\[([^]]*)\]\(({site}/)([^]]*)(.html)([^]]*)?\)",
            content,
        ):
            if match[0] in ipynbs:
                content = content.replace(
                    match[0], f"[{match[1]}]({match[3]}.ipynb{match[5]})"
                )
            else:
                content = content.replace(
                    match[0], f"[{match[1]}]({match[3]}.md{match[5]})"
                )

        content = content.replace(f"{site}/", "")

        with mkdocs_gen_files.open("index.md", "w") as f_index:
            f_index.write(content)


class SectionIndex:
    """A class for creating section index files."""

    @staticmethod
    def _write_index_file(file: str, toc: list) -> None:
        """
        A method for writing table of contents into a section index file.

        Args:
            file: The section index file.
            toc: Items of the table of contents.
        """

        for item in toc:
            if isinstance(item, str):
                SectionIndex._write_str_index(file, item)
            elif isinstance(item, dict):
                SectionIndex._write_dict_index(file, item)
            else:
                raise NotImplementedError(f"{item}")

    @staticmethod
    def _write_str_index(file: str, item: str) -> None:
        """
        A method for writing an str toc item into a section index file.

        Args:
            file: The section index file.
            item: Item of the table of contents.
        """

        with mkdocs_gen_files.open(file, "a") as f_index:
            parts = item.split("/")
            part = parts[-1].replace(".md", "").capitalize()
            link = Path(item).relative_to(Path(file).parent)
            f_index.write(f"* [{part}]({link})\n")

    @staticmethod
    def _write_dict_index(file: str, item: dict) -> None:
        """
        A method for writing a dict toc item into a section index file.

        Args:
            file: The section index file.
            item: Item of the table of contents.
        """

        with mkdocs_gen_files.open(file, "a") as f_index:
            for key in item:
                if isinstance(item[key], str):
                    link = Path(item[key]).relative_to(Path(file).parent)
                    f_index.write(f"* [{key}]({link})\n")
                    continue
                if item[key] and isinstance(item[key], list):
                    if isinstance(item[key][0], str):
                        if item[key][0].endswith("index.md"):
                            link = Path(item[key][0]).relative_to(Path(file).parent)
                            f_index.write(f"* [{key}]({link})\n")
                            continue
                raise NotImplementedError(f"{item}")

    @staticmethod
    def generate(nav_item: Union[list, dict, str]) -> None:
        """
        A method for creating section indices for the navigation.

        Args:
            nav_item: Part of the navigation.
        """

        if isinstance(nav_item, list):
            if (
                nav_item
                and isinstance(nav_item[0], str)
                and nav_item[0].endswith("index.md")
            ):
                with mkdocs_gen_files.open(nav_item[0], "a") as f_index:
                    f_index.write("\n")
                SectionIndex._write_index_file(file=nav_item[0], toc=nav_item[1:])
            for item in nav_item:
                SectionIndex.generate(nav_item=item)
        elif isinstance(nav_item, dict):
            for key in nav_item:
                SectionIndex.generate(nav_item=nav_item[key])


class Reference:
    """A class for creating code reference."""

    @staticmethod
    def generate(folder: str) -> None:
        """
        A method for generate code reference.

        Args:
            folder: Reference destination folder.
        """

        for path in sorted(Path("src").rglob("*.py")):
            module_path = path.relative_to("src").with_suffix("")

            doc_path = path.relative_to("src").with_suffix(".md")
            full_doc_path = Path(folder, doc_path)

            parts = tuple(module_path.parts)

            if parts[-1] == "__init__":
                parts = parts[:-1]
                doc_path = doc_path.with_name("index.md")
                full_doc_path = full_doc_path.with_name("index.md")
            elif parts[-1] == "__main__":
                continue

            with mkdocs_gen_files.open(full_doc_path, "w") as f_md:
                item = ".".join(parts)
                f_md.write(f"::: {item}")

            mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path)


def main() -> None:
    """
    The main method.
    It prepares files for the documentation site.
    """

    config = MkdocsConfig.load()

    site_url = config["site_url"]
    if site_url.endswith("/"):
        site_url = site_url[:-1]

    index_ipynbs: List[str] = []

    SectionIndex.generate(nav_item=config["nav"])

    Reference.generate("reference")

    Index.generate(
        readme=Path(__file__).parent / ".." / ".." / "README.md",
        site=site_url,
        ipynbs=index_ipynbs,
    )


main()
