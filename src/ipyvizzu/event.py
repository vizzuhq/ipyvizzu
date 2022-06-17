"""A module used to work with events"""

import uuid


class EventHandler:
    """A class used to store an event handler's data"""

    def __init__(self, event, handler):
        self._id = uuid.uuid4().hex[:7]
        self._event = event
        self._handler = handler

    @property
    def id(self):  # pylint: disable=invalid-name
        """A property used to store an event handler's id"""
        return self._id

    @property
    def event(self):
        """A property used to store an event's name"""
        return self._event

    @property
    def handler(self):
        """A property used to store a handler's function body"""
        return self._handler
