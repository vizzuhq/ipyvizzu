import fugue.api as fa  # type: ignore
import pandas as pd  # type: ignore
import unittest

# register the extension, not needed in practical use
import ipyvizzu.integrations.fugue  # noqa # pylint: disable-all


class TestFugue(unittest.TestCase):
    """
    A class for testing Fugue integration.
    """

    def test_fugue_extension_preset(self):
        """Test Fugue extension - preset"""
        df = pd.DataFrame(dict(a=list("abcde"), b=range(5)))
        fa.fugue_sql_flow(
            """
            SELECT * FROM df WHERE b<5

            OUTPUT USING vizzu:bar(x="a",y="b")
        """,
            df=df,
        ).run()

    def test_fugue_extension_timeline(self):
        """Test Fugue extension - timeline"""
        df = pd.DataFrame(dict(a=list("abcde"), b=range(5), c=[1, 1, 2, 2, 3]))
        fa.fugue_sql_flow(
            """
            SELECT * FROM df WHERE b<5

            OUTPUT USING vizzu:timeline_bar(
                by="c",
                config={"x":"b","y":"a",title="x %s"},
                duration=0.3
            )
        """,
            df=df,
        ).run()
