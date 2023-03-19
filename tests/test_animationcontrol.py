"""A module for testing the ipyvizzu.animationcontrol module."""

import unittest
import unittest.mock

from tests import Style
from tests.test_chart import TestChart


class TestAnimationControl(TestChart):
    """A class for testing AnimationControl class."""

    def test_must_be_called_after_animate(self) -> None:
        """
        A method for testing AnimationControl msut be called after animate.

        Raises:
            AssertionError: If AssertionError is not occurred.
        """

        with self.assertRaises(AssertionError):
            self.chart.previous.seek("50%")

    def test_cancel(self) -> None:
        """
        A method for testing AnimationControl.cancel method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.cancel()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'cancel', id, id);",
            )

    def test_pause(self) -> None:
        """
        A method for testing AnimationControl.pause method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.pause()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'pause', id, id);",
            )

    def test_play(self) -> None:
        """
        A method for testing AnimationControl.play method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.play()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'play', id, id);",
            )

    def test_reverse(self) -> None:
        """
        A method for testing AnimationControl.reverse method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.reverse()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'reverse', id, id);",
            )

    def test_seek(self) -> None:
        """
        A method for testing AnimationControl.seek method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.seek("50%")
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'seek', id, id, '50%');",
            )

    def test_stop(self) -> None:
        """
        A method for testing AnimationControl.stop method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.stop()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'stop', id, id);",
            )

    def test_store(self) -> None:
        """
        A method for testing AnimationControl.store method.

        Raises:
            AssertionError: If the normalized output is not correct.
        """

        with unittest.mock.patch(self.mock) as output:
            self.chart.animate(Style(None))
            self.chart.previous.store()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "window.ipyvizzu.control(element, 'store', id, id, id);",
            )
