"""
A test module used to test
the method module
"""

import unittest

from ipyvizzu import Method, Animate, Feature, Store, Snapshot


class TestMethod(unittest.TestCase):
    """
    A test class used to test
    methods
    """

    def test_method(self) -> None:
        """
        A test method used to test
        Method()
        """

        method = Method()
        self.assertEqual(None, method.dump())

    def test_animate_without_option(self) -> None:
        """
        A test method used to test
        Animate() with animation and without option
        """

        animation = Snapshot("abc1234")
        method = Animate(animation)
        self.assertEqual(
            {
                "chart_target": "'abc1234'",
                "chart_anim_opts": "undefined",
            },
            method.dump(),
        )

    def test_animate_with_option(self) -> None:
        """
        A test method used to test
        Animate() with animation and option
        """

        animation = Snapshot("abc1234")
        option = {"duration": 1, "easing": "linear"}
        method = Animate(animation, option)
        self.assertEqual(
            {
                "chart_target": "'abc1234'",
                "chart_anim_opts": '{"duration": 1, "easing": "linear"}',
            },
            method.dump(),
        )

    def test_feature(self) -> None:
        """
        A test method used to test
        Feature()
        """

        method = Feature("tooltip", True)
        self.assertEqual({"name": '"tooltip"', "enabled": "true"}, method.dump())

    def test_store(self) -> None:
        """
        A test method used to test
        Store()
        """

        method = Store("abc1234")
        self.assertEqual({"id": "abc1234"}, method.dump())
