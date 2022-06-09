from ipyvizzu.template import DisplayTemplate
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

    @property
    def _display_template_class(self):
        return DisplayTemplate
