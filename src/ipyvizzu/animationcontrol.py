"""A module for working with animation control."""

from typing import Union, Callable

from ipyvizzu.template import DisplayTemplate


class AnimationControl:
    """
    A class for controlling animations.
    """

    def __init__(self, prev_id: str, last_id: str, display_method: Callable):
        """
        AnimationControl constructor.

        Args:
            prev_id: Id of the previous animation promise.
            last_id: Id of the animation to be controlled.
            display_method: Displaying function.
        """

        self._ids = ", ".join([f"'{prev_id}'", f"'{last_id}'"])
        self._display = display_method

    def cancel(self) -> None:
        """Cancels the animation, will reject the animation promise."""

        self._display(
            DisplayTemplate.CONTROL.format(
                method=self.cancel.__name__,
                params=self._ids,
            )
        )

    def pause(self) -> None:
        """Pauses the controlled animation."""

        self._display(
            DisplayTemplate.CONTROL.format(
                method=self.pause.__name__,
                params=self._ids,
            )
        )

    def play(self) -> None:
        """Plays/resumes playing of the controlled animation."""

        self._display(
            DisplayTemplate.CONTROL.format(
                method=self.play.__name__,
                params=self._ids,
            )
        )

    def reverse(self) -> None:
        """Changes the direction of the controlled animation."""

        self._display(
            DisplayTemplate.CONTROL.format(
                method=self.reverse.__name__,
                params=self._ids,
            )
        )

    def seek(self, value: Union[int, str]) -> None:
        """
        Seeks the animation to the position specified by time or progress percentage.

        Args:
            value: The position specified by time or progress percentage.
        """

        params = ", ".join([self._ids, f"'{value}'"])
        self._display(
            DisplayTemplate.CONTROL.format(
                method=self.seek.__name__,
                params=params,
            )
        )

    def stop(self) -> None:
        """Stops the current animation seeking it back to its start position."""

        self._display(
            DisplayTemplate.CONTROL.format(
                method=self.stop.__name__,
                params=self._ids,
            )
        )
