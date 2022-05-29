from pyvizzu.animation import Animation as PyvizzuAnimation
from pyvizzu.animation import PlainAnimation as PyvizzuPlainAnimation
from pyvizzu.animation import InferType as PyvizzuInferType
from pyvizzu.animation import Data as PyvizzuData
from pyvizzu.animation import Config as PyvizzuConfig
from pyvizzu.animation import Style as PyvizzuStyle
from pyvizzu.animation import Snapshot as PyvizzuSnapshot
from pyvizzu.animation import AnimationMerger as PyvizzuAnimationMerger

from stpyvizzu.template import DisplayTemplate


Animation = PyvizzuAnimation

PlainAnimation = PyvizzuPlainAnimation

InferType = PyvizzuInferType

Data = PyvizzuData

Config = PyvizzuConfig

Style = PyvizzuStyle


class Snapshot(PyvizzuSnapshot):
    def _set_classes(self):
        self._classes["DisplayTemplate"] = DisplayTemplate


AnimationMerger = PyvizzuAnimationMerger
