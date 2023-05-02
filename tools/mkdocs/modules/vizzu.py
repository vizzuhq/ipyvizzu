"""A module for working with Vizzu."""

from pathlib import Path
import re

from ipyvizzu import Chart


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

VIZZU_BACKEND_URL = ""
VIZZU_STYLEREF_BACKEND_URL = ""

IPYVIZZU_VERSION = ""
VIZZU_VERSION = ""

IPYVIZZU_SITE_URL = "https://ipyvizzu.vizzuhq.com"
VIZZU_SITE_URL = "https://lib.vizzuhq.com"
VIZZU_CDN_URL = "https://cdn.jsdelivr.net/npm/vizzu"


class Vizzu:
    """A class for working with Vizzu."""

    @staticmethod
    def get_vizzu_backend_url() -> str:
        """
        A static method for returning backend vizzu url.

        Returns:
            Backend vizzu url.
        """

        if VIZZU_BACKEND_URL:
            return VIZZU_BACKEND_URL
        version = Vizzu.get_vizzu_version()
        return f"{VIZZU_CDN_URL}@{version}/dist/vizzu.min.js"

    @staticmethod
    def get_vizzu_styleref_backend_url() -> str:
        """
        A static method for returning backend vizzu style reference url.

        Returns:
            Backend vizzu style reference url.
        """

        if VIZZU_STYLEREF_BACKEND_URL:
            return VIZZU_STYLEREF_BACKEND_URL
        version = Vizzu.get_vizzu_version()
        return f"{VIZZU_CDN_URL}@{version}/dist/vizzu.min.js"

    @staticmethod
    def get_vizzu_version() -> str:
        """
        A static method for returning vizzu major.minor version.

        Returns:
            Vizzu major.minor version.
        """

        if VIZZU_VERSION:
            return VIZZU_VERSION
        cdn = Chart.VIZZU
        return re.search(r"vizzu@([\d.]+)/", cdn).group(1)  # type: ignore

    @staticmethod
    def get_ipyvizzu_version() -> str:
        """
        A static method for returning ipyvizzu major.minor version.

        Returns:
            ipyvizzu major.minor version.
        """

        if IPYVIZZU_VERSION:
            return IPYVIZZU_VERSION
        with open(
            REPO_PATH / "setup.py",
            "r",
            encoding="utf8",
        ) as f_version:
            content = f_version.read()
            version = re.search(r"version=\"(\d+).(\d+).(\d+)\"", content)
            return f"{version.group(1)}.{version.group(2)}"  # type: ignore

    @staticmethod
    def set_version(content: str, restore: bool = False) -> str:
        """
        A static method for setting vizzu version in content.

        Args:
            content: Content to be modified.
            restore: A flag to restore the content.

        Returns:
            Modified content.
        """

        vizzu_version = Vizzu.get_vizzu_version()
        ipyvizzu_version = Vizzu.get_ipyvizzu_version()
        if not restore:
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/latest/",
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/",
            )
            content = content.replace(
                f"{VIZZU_SITE_URL}/latest/",
                f"{VIZZU_SITE_URL}/{vizzu_version}/",
            )
        else:
            content = content.replace(
                f"{IPYVIZZU_SITE_URL}/{ipyvizzu_version}/",
                f"{IPYVIZZU_SITE_URL}/latest/",
            )
            content = content.replace(
                f"{VIZZU_SITE_URL}/{vizzu_version}/",
                f"{VIZZU_SITE_URL}/latest/",
            )
        return content
