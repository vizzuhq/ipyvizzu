import uuid
import pkgutil

from pyvizzu.animation import Animation, AnimationMerger
from pyvizzu.method import Animate, Feature, Store
from pyvizzu.template import DisplayTarget, DisplayTemplate, VIZZU


class Chart:
    def __init__(self, vizzu=VIZZU, width="800px", height="480px"):
        self._init_id = uuid.uuid4().hex[:7]
        self._chart_id = uuid.uuid4().hex[:7]

        self._display_target = DisplayTarget.MANUAL
        self._set_display_template()
        self._calls = []
        self._showed = False

        self._scroll_into_view = False

        pyvizzujs = pkgutil.get_data("pyvizzu", "templates/pyvizzu.js").decode("utf-8")
        self._display(self._display_template.PYVIZZUJS.format(pyvizzujs=pyvizzujs))

        self._display(
            self._display_template.INIT.format(
                init_id=self._init_id,
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

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
            self._display_template.ANIMATE.format(
                display_target=self._display_target,
                chart_id=self._chart_id,
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
            self._display_template.FEATURE.format(
                chart_id=self._chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self):
        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            self._display_template.STORE.format(
                chart_id=self._chart_id, **Store(snapshot_id).dump()
            )
        )
        return snapshot_id

    def _set_display_template(self):
        self._display_template = DisplayTemplate

    def _display(self, javascript):
        assert not self._showed, "cannot be used after chart displayed."
        self._calls.append(javascript)

    def _repr_html_(self):
        assert not self._showed, "cannot be used after chart displayed."
        self._showed = True
        script = "\n".join(self._calls)
        return f'<div id="{self._init_id}"><script>{script}</script></div>'

    def show(self):
        return self._repr_html_()
