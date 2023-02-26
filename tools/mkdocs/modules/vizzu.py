"""A module for working with Vizzu."""

from pathlib import Path
import re


REPO_PATH = Path(__file__).parent / ".." / ".." / ".."
MKDOCS_PATH = REPO_PATH / "tools" / "mkdocs"
VIZZU_LIB_PATH = REPO_PATH / "vizzu-lib"


VIZZU_BACKEND_URL = ""
VIZZU_STYLE_REFERENCE_URL = ""
VIZZU_VERSION = ""
VIZZU_TEST_VERSION = ""
VIZZU_LIB_DOC_URL = ""
SHOWCASE_VIZZU_URL = ""
SHOWCASE_GITHUB_URL = ""
SHOWCASE_HOST_URL = ""


class Vizzu:
    """A class for working with Vizzu."""

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
    def get_full_version() -> list:
        """
        A static method for returning vizzu major.minor.patch version.

        Returns:
            Vizzu major.minor.patch version.
        """

        with open(
            VIZZU_LIB_PATH / "src" / "chart" / "main" / "version.cpp",
            "r",
            encoding="utf8",
        ) as f_version:
            content = f_version.read()
            version = re.search(r"version\(\s*(\d+),\s*(\d+),\s*(\d+)\s*\)", content)
            return [
                version.group(1),  # type: ignore
                version.group(2),  # type: ignore
                version.group(3),  # type: ignore
            ]

    @staticmethod
    def get_version() -> str:
        """
        A static method for returning vizzu major.minor version.

        Returns:
            Vizzu major.minor version.
        """

        if VIZZU_VERSION:
            return VIZZU_VERSION
        version_parts = Vizzu.get_full_version()
        return f"{version_parts[0]}.{version_parts[1]}"

    @staticmethod
    def get_test_version() -> str:
        """
        A static method for returning vizzu test version.

        Returns:
            Vizzu test version.
        """

        if VIZZU_TEST_VERSION:
            return VIZZU_TEST_VERSION
        version_parts = Vizzu.get_full_version()
        return f"{version_parts[0]}.{version_parts[1]}.{version_parts[2]}"

    @staticmethod
    def set_version(content: str) -> str:
        """
        A static method for setting vizzu version in content.

        Args:
            content: Content to be modified.

        Returns:
            Modified content.
        """

        version = Vizzu.get_version()
        content = content.replace(
            "https://cdn.jsdelivr.net/npm/vizzu@latest/",
            f"https://cdn.jsdelivr.net/npm/vizzu@{version}/",
        )
        content = content.replace(
            "https://lib.vizzuhq.com/latest/", f"https://lib.vizzuhq.com/{version}/"
        )
        return content

    @staticmethod
    def set_js_showcase_url(content: str) -> str:
        """
        A static method for setting vizzu version in showcase js content.

        Args:
            content: Content to be modified.

        Returns:
            Modified content.
        """

        version = Vizzu.get_version()
        vizzu_url = f"https://cdn.jsdelivr.net/npm/vizzu@{version}/dist/vizzu.min.js"
        if SHOWCASE_VIZZU_URL:
            vizzu_url = SHOWCASE_VIZZU_URL
        content = content.replace(
            "https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js", vizzu_url
        )
        return content

    @staticmethod
    def set_html_showcase_url(content: str) -> str:
        """
        A static method for setting version urls in showcase html content.

        Args:
            content: Content to be modified.

        Returns:
            Modified content.
        """

        version = Vizzu.get_version()
        github_url = f"{Vizzu.get_vizzulibdoc_url()}/tree/gh-pages"
        new_github_url = github_url
        if SHOWCASE_GITHUB_URL:
            new_github_url = SHOWCASE_GITHUB_URL
        content = content.replace(
            f"{github_url}/latest/",
            f"{new_github_url}/{version}/",
        )
        host_url = "https://lib.vizzuhq.com"
        new_host_url = host_url
        if SHOWCASE_HOST_URL:
            new_host_url = SHOWCASE_HOST_URL
        content = content.replace(f"{host_url}/latest/", f"{new_host_url}/{version}/")
        return content
