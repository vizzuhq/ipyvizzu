# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import sys
import io
from contextlib import redirect_stdout
import pathlib
import unittest
import pandas as pd  # type: ignore


from tests.normalizer import Normalizer


if sys.version_info >= (3, 7):
    import fugue.api as fa  # type: ignore
    import ipyvizzu.integrations.fugue  # register the extension  # pylint: disable=unused-import

    class TestFugue(unittest.TestCase):
        def test_fugue_extension_preset(self) -> None:
            ref = pathlib.Path(__file__).parent / "assets" / "fugue_preset.txt"
            with open(ref, "r", encoding="utf8") as f_ref:
                ref_content = f_ref.read()
            df = pd.DataFrame({"a": list("abcde"), "b": range(5)})
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                fa.fugue_sql_flow(
                    """
                    SELECT * FROM df WHERE b<5

                    OUTPUT USING vizzu:bar(x="a",y="b")
                """,
                    df=df,
                ).run()
            self.assertEqual(
                Normalizer().normalize_id("\n".join(stdout.getvalue().split("\n")[1:])),
                ref_content,
            )

        def test_fugue_extension_timeline(self) -> None:
            ref = pathlib.Path(__file__).parent / "assets" / "fugue_timeline.txt"
            with open(ref, "r", encoding="utf8") as f_ref:
                ref_content = f_ref.read()
            df = pd.DataFrame({"a": list("abcde"), "b": range(5), "c": [1, 1, 2, 2, 3]})
            stdout = io.StringIO()
            with redirect_stdout(stdout):
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
            self.assertEqual(
                Normalizer().normalize_id("\n".join(stdout.getvalue().split("\n")[1:])),
                ref_content,
            )

else:
    # TODO: remove once support for Python 3.6 is dropped
    pass
