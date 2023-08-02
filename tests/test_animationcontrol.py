# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest
import unittest.mock

from ipyvizzu import Style

from tests.test_chart import TestChart


class TestAnimationControl(TestChart):
    def test_must_be_called_after_animate(self) -> None:
        with self.assertRaises(AssertionError):
            self.chart.control.seek("50%")

    def test_cancel(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.cancel()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'cancel', id, id);",
            )

    def test_pause(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.pause()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'pause', id, id);",
            )

    def test_play(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.play()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'play', id, id);",
            )

    def test_reverse(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.reverse()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'reverse', id, id);",
            )

    def test_seek(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.seek("50%")
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'seek', id, id, '50%');",
            )

    def test_stop(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.stop()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'stop', id, id);",
            )

    def test_store(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.control.store()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'store', id, id, id);",
            )
