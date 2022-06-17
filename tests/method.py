import unittest
import abc


class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestMethod:
            raise unittest.SkipTest()
        super(TestMethod, cls).setUpClass()

    @abc.abstractmethod
    def get_method(self):
        """
        Return Method()
        """

    @abc.abstractmethod
    def get_animate(self, chart_target, chart_anim_opts=None):
        """
        Return Animate(chart_target, chart_anim_opts)
        """

    @abc.abstractmethod
    def get_snapshot(self, snapshot_id):
        """
        Return Snapshot(snapshot_id)
        """

    @abc.abstractmethod
    def get_feature(self, name, enabled):
        """
        Return Feature(name, enabled)
        """

    @abc.abstractmethod
    def get_store(self, snapshot_id):
        """
        Return Store(snapshot_id)
        """

    def test_method(self):
        method = self.get_method()
        self.assertEqual(None, method.dump())

    def test_animate_without_option(self):
        animation = self.get_snapshot("abc1234")
        return self.get_animate(animation)

    def test_animate_with_option(self):
        animation = self.get_snapshot("abc1234")
        option = {"duration": 1, "easing": "linear"}
        return self.get_animate(animation, option)

    def test_feature(self):
        method = self.get_feature("tooltip", True)
        self.assertEqual({"name": '"tooltip"', "enabled": "true"}, method.dump())

    def test_store(self):
        method = self.get_store("abc1234")
        self.assertEqual({"id": "abc1234"}, method.dump())
