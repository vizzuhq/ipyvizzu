import uuid


class EventHandler:
    def __init__(self, event, handler):
        self._id = uuid.uuid4().hex[:7]
        self._event = event
        self._handler = handler

    @property
    def id(self):  # pylint: disable=invalid-name
        return self._id

    @property
    def event(self):
        return self._event

    @property
    def handler(self):
        return self._handler
