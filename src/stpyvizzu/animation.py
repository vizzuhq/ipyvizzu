from stpyvizzu.template import DisplayTemplate
from pyvizzu.animation import Snapshot as PyvizzuSnapshot

# pylint: disable=unused-import

from pyvizzu.animation import Animation
from pyvizzu.animation import PlainAnimation
from pyvizzu.animation import InferType
from pyvizzu.animation import Data
from pyvizzu.animation import Config
from pyvizzu.animation import Style
from pyvizzu.animation import AnimationMerger


class Snapshot(PyvizzuSnapshot):

    # pylint: disable=abstract-method

    def __init__(self, name: str):
        self._classes["DisplayTemplate"] = DisplayTemplate
        super().__init__(name)
