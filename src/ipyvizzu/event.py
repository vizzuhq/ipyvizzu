"""A module for working with javascript events"""

import uuid


class EventHandler:
    """
    A class for representing an event handler.
    It generates a uuid for the event handler,
    stores event type in the _event instance variable and
    stores body of the event handler function in the _handler instance variable.
    """

    def __init__(self, event: str, handler: str):
        self._id = uuid.uuid4().hex[:7]
        self._event = event
        self._handler = " ".join(handler.split())

    @property
    def id(self) -> str:  # pylint: disable=invalid-name
        """A property for storing uuid"""

        return self._id

    @property
    def event(self) -> str:
        """A property for storing event type"""

        return self._event

    @property
    def handler(self) -> str:
        """A property for storing body of the event handler function"""

        return self._handler
