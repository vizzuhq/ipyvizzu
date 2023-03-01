"""A module for working with mdformat."""

import mdformat


class Md:
    """A class for working with mdformat."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def format(content: str) -> str:
        """
        A static method for formatting markdown content.

        Args:
            content: Markdown content.

        Returns:
            Formatted content.
        """

        return mdformat.text(  # type: ignore
            content,
            options={"wrap": 80, "end-of-line": "keep", "line-length": 70},
            extensions={
                "gfm",
                "tables",
                "footnote",
                "frontmatter",
                "configblack",
                "admonition",
            },
            codeformatters={
                "python",
                "bash",
                "sh",
                "json",
                "toml",
                "yaml",
                "javascript",
                "js",
                "css",
                "html",
                "xml",
            },
        )
