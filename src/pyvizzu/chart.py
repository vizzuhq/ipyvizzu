import uuid

from pyvizzu.animation import Animation, Snapshot, AnimationMerger
from pyvizzu.method import Animate, Feature, Store
from pyvizzu.template import DisplayTarget, DisplayTemplate


class Chart:
    """
    Wrapper over Vizzu Chart
    """

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
            DisplayTemplate.ANIMATE.format(
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
            DisplayTemplate.FEATURE.format(
                chart_id=self._chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self) -> Snapshot:
        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            DisplayTemplate.STORE.format(
                chart_id=self._chart_id, **Store(snapshot_id).dump()
            )
        )
        return Snapshot(snapshot_id)
