"""A module for working with mkdocs config."""

from pathlib import Path
from typing import Optional

import yaml


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
