# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from ipyvizzu import Data

from tests.test_data import DataWithAssets


class TestDataJson(DataWithAssets):
    def test_from_json(self) -> None:
        data = Data.from_json(self.asset_dir / "in_json.json")
        self.assertEqual(
            self.ref_pd_series,
            data.build(),
        )
