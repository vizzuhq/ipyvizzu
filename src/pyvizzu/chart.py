import uuid
import pkgutil

from pyvizzu.animation import Animation, AnimationMerger, Snapshot
from pyvizzu.method import Animate, Feature, Store
from pyvizzu.template import DisplayTarget, DisplayTemplate, VIZZU


class Chart:
    def __init__(self, vizzu=VIZZU, width="800px", height="480px"):

        self._ids = {}
        self._ids["init"] = uuid.uuid4().hex[:7]
        self._ids["chart"] = uuid.uuid4().hex[:7]

        self._scroll_into_view = False

        self._js = {}
        self._js["calls"] = []
        self._js["showed"] = False

        self._set_pyvizzujs()
        self._set_chart(vizzu, width, height)

    def _set_pyvizzujs(self):
        pyvizzujs = pkgutil.get_data("pyvizzu", "templates/pyvizzu.js").decode("utf-8")
        self._display(
            self._display_template_class.PYVIZZUJS.format(pyvizzujs=pyvizzujs)
        )

    def _set_chart(self, vizzu, width, height):
        self._display(
            self._display_template_class.INIT.format(
                init_id=self._ids["init"],
                chart_id=self._ids["chart"],
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

    @property
    def _display_target(self):
        return DisplayTarget.MANUAL

    @property
    def _display_template_class(self):
        return DisplayTemplate

    @property
    def _snapshot_class(self):
        return Snapshot

    @property
    def scroll_into_view(self):
        return self._scroll_into_view

    @scroll_into_view.setter
    def scroll_into_view(self, scroll_into_view):
        self._scroll_into_view = bool(scroll_into_view)

    def animate(self, *animations: Animation, **options):
        if not animations:
            raise ValueError("No animation was set.")

        animation = self._merge_animations(animations)
        animate = Animate(animation, options)

        self._display(
            self._display_template_class.ANIMATE.format(
                display_target=self._display_target,
                chart_id=self._ids["chart"],
                scroll=str(self._scroll_into_view).lower(),
                **animate.dump(),
            )
        )

    @staticmethod
    def _merge_animations(animations):
        if len(animations) == 1:
            return animations[0]

        merger = AnimationMerger()
        for animation in animations:
            merger.merge(animation)

        return merger

    def feature(self, name, enabled):
        self._display(
            self._display_template_class.FEATURE.format(
                chart_id=self._ids["chart"],
                **Feature(name, enabled).dump(),
            )
        )

    def store(self):
        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            self._display_template_class.STORE.format(
                chart_id=self._ids["chart"], **Store(snapshot_id).dump()
            )
        )
        return self._snapshot_class(snapshot_id)

    def _display(self, javascript):
        assert not self._js["showed"], "cannot be used after chart displayed."
        self._js["calls"].append(javascript)

    def _repr_html_(self):
        assert not self._js["showed"], "cannot be used after chart displayed."
        self._js["showed"] = True
        script = "\n".join(self._js["calls"])
        return f'<div id="{self._ids["init"]}"><script>{script}</script></div>'

    def show(self):
        return self._repr_html_()