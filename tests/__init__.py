"""ipyvizzu test modules."""

import sys

sys.path.insert(0, "./src")


from ipyvizzu import (  # pylint: disable=wrong-import-position
    Animate,
    AnimationMerger,
    Chart,
    ChartProperty,
    Config,
    Data,
    EventHandler,
    EventOff,
    EventOn,
    Feature,
    Keyframe,
    Log,
    Method,
    PlainAnimation,
    RawJavaScript,
    RawJavaScriptEncoder,
    Snapshot,
    AnimationSnapshot,
    Store,
    Style,
)
