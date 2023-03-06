"""A module for working with Vizzu."""

from pathlib import Path
import re

from ipyvizzu import Chart


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

IPYVIZZU_VERSION = ""
VIZZU_VERSION = ""
VIZZU_BACKEND_URL = ""
VIZZU_STYLE_REFERENCE_URL = ""
VIZZU_LIB_SITE_URL = ""


class Vizzu:
    """A class for working with Vizzu."""

    @staticmethod
    def get_vizzulibsite_url() -> str:
        """
        A static method for returning vizzu site doc url.

        Returns:
            Backend vizzu lib site url.
        """

        if VIZZU_LIB_SITE_URL:
            return VIZZU_LIB_SITE_URL
        return "https://lib.vizzuhq.com"

    @staticmethod
    def get_backend_url() -> str:
        """
        A static method for returning backend vizzu url.

        Returns:
            Backend vizzu url.
        """

        if VIZZU_BACKEND_URL:
            return VIZZU_BACKEND_URL
        version = Vizzu.get_vizzu_version()
        return f"https://cdn.jsdelivr.net/npm/vizzu@{version}/dist/vizzu.min.js"

    @staticmethod
    def get_style_reference_url() -> str:
        """
        A static method for returning style reference vizzu url.

        Returns:
            Style reference vizzu url.
        """

        if VIZZU_STYLE_REFERENCE_URL:
            return VIZZU_STYLE_REFERENCE_URL
        version = Vizzu.get_vizzu_version()
        return f"https://cdn.jsdelivr.net/npm/vizzu@{version}/dist/vizzu.min.js"

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
    def set_version(content: str) -> str:
        """
        A static method for setting vizzu version in content.

        Args:
            content: Content to be modified.

        Returns:
            Modified content.
        """

        vizzu_version = Vizzu.get_vizzu_version()
        ipyvizzu_version = Vizzu.get_ipyvizzu_version()
        content = content.replace(
            "https://ipyvizzu.vizzuhq.com/latest/",
            f"https://ipyvizzu.vizzuhq.com/{ipyvizzu_version}/",
        )
        content = content.replace(
            "https://lib.vizzuhq.com/latest/",
            f"https://lib.vizzuhq.com/{vizzu_version}/",
        )
        return content
