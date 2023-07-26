# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pathlib import Path
import re

import ipyvizzu


REPO_PATH = Path(__file__).parent / ".." / ".."

VIZZU_BACKEND_URL = ""
VIZZU_STYLEREF_BACKEND_URL = ""

IPYVIZZU_VERSION = ""
VIZZU_VERSION = ""

IPYVIZZU_SITE_URL = "https://ipyvizzu.vizzuhq.com"
VIZZU_SITE_URL = "https://lib.vizzuhq.com"
VIZZU_CDN_URL = "https://cdn.jsdelivr.net/npm/vizzu"


class Vizzu:
    _ipyvizzu_version = ""
    _vizzu_version = ""

    @staticmethod
    def get_vizzu_backend_url() -> str:
        if VIZZU_BACKEND_URL:
            return VIZZU_BACKEND_URL
        version = Vizzu.get_vizzu_version()
        return f"{VIZZU_CDN_URL}@{version}/dist/vizzu.min.js"

    @staticmethod
    def get_vizzu_styleref_backend_url() -> str:
        if VIZZU_STYLEREF_BACKEND_URL:
            return VIZZU_STYLEREF_BACKEND_URL
        version = Vizzu.get_vizzu_version()
        return f"{VIZZU_CDN_URL}@{version}/dist/vizzu.min.js"

    @staticmethod
    def get_vizzu_version() -> str:
        if VIZZU_VERSION:
            return VIZZU_VERSION
        if not Vizzu._vizzu_version:
            cdn = ipyvizzu.Chart.VIZZU
            Vizzu._vizzu_version = re.search(r"vizzu@([\d.]+)/", cdn).group(1)  # type: ignore
        return Vizzu._vizzu_version

    @staticmethod
    def get_ipyvizzu_version() -> str:
        if IPYVIZZU_VERSION:
            return IPYVIZZU_VERSION
        if not Vizzu._ipyvizzu_version:
            version = ipyvizzu.__version__
            Vizzu._ipyvizzu_version = re.search(r"(\d+.\d+).\d+", version).group(1)  # type: ignore
        return Vizzu._ipyvizzu_version

    @staticmethod
    def set_version(content: str, restore: bool = False) -> str:
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
