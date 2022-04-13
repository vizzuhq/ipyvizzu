import json

from ipyvizzu.animation import PlainAnimation


class Method:
    _data = None

    def dump(self):
        return self._data


class Animate(Method):
    def __init__(self, chart_target, chart_anim_opts=None):
        self._data = {
            "chart_target": chart_target.dump(),
            "chart_anim_opts": PlainAnimation(chart_anim_opts).dump()
            if chart_anim_opts
            else "undefined",
        }


class Feature(Method):
    def __init__(self, name, enabled):
        self._data = {"name": json.dumps(name), "enabled": json.dumps(enabled)}


class Store(Method):
    def __init__(self, snapshot_id):
        self._data = {"id": snapshot_id}
