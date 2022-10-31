"""A module for working with JavaScript events"""

import uuid


class EventHandler:
    """A class for representing an event handler."""

    def __init__(self, event: str, handler: str):
        """
        EventHandler constructor.

        It generates a uuid for the event handler,
        stores the event type and the body of the handler function.

        Args:
            event: The type of the event.
            handler: The body of the handler function.
        """

        self._id = uuid.uuid4().hex[:7]
        self._event = event
        self._handler = " ".join(handler.split())

    @property
    def id(self) -> str:  # pylint: disable=invalid-name
        """
        A property for storing an id.

        Returns:
            The uuid of the event handler.
        """

        return self._id

    @property
    def event(self) -> str:
        """
        A property for storing an event type.

        Returns:
            The type of the event.
        """

        return self._event

    @property
    def handler(self) -> str:
        """
        A property for storing an event handler function.

        Returns:
            The body of the handler function.
        """

        return self._handler
