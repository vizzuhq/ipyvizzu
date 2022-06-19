"""A module used to work with events"""

import uuid


class EventHandler:
    """A class used to store an event handler's data"""

    def __init__(self, event: str, handler: str):
        self._id = uuid.uuid4().hex[:7]
        self._event = event
        self._handler = " ".join(handler.split())

    @property
    def id(self) -> str:  # pylint: disable=invalid-name
        """A property used to store an event handler's id"""
        return self._id

    @property
    def event(self) -> str:
        """A property used to store an event's name"""
        return self._event

    @property
    def handler(self) -> str:
        """A property used to store a handler's function body"""
        return self._handler
