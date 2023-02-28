"""A module for working with Vizzu."""

from pathlib import Path
import re

from ipyvizzu import Chart


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"

VIZZU_VERSION = ""
VIZZU_BACKEND_URL = ""
VIZZU_STYLE_REFERENCE_URL = ""
VIZZU_LIB_SITE_URL = ""
VIZZU_LIB_DOC_URL = ""


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
        return "https://lib.vizzuhq.com/"

    @staticmethod
    def get_vizzulibdoc_url() -> str:
        """
        A static method for returning vizzu lib doc url.

        Returns:
            Backend vizzu lib doc url.
        """

        if VIZZU_LIB_DOC_URL:
            return VIZZU_LIB_DOC_URL
        return "https://github.com/vizzuhq/vizzu-lib-doc"

    @staticmethod
    def get_backend_url() -> str:
        """
        A static method for returning backend vizzu url.

        Returns:
            Backend vizzu url.
        """

        if VIZZU_BACKEND_URL:
            return VIZZU_BACKEND_URL
        version = Vizzu.get_version()
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
        version = Vizzu.get_version()
        return f"https://cdn.jsdelivr.net/npm/vizzu@{version}/dist/vizzu.min.js"

    @staticmethod
    def get_version() -> str:
        """
        A static method for returning vizzu major.minor version.

        Returns:
            Vizzu major.minor version.
        """

        if VIZZU_VERSION:
            return VIZZU_VERSION
        cdn = Chart.VIZZU
        return re.search(r"vizzu@([\d.]+)/", cdn).group(1)  # type: ignore
