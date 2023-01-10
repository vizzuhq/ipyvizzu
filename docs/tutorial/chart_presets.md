---
csv_url: ../data/music_data.csv
---

# Chart presets

Throughout this tutorial, we have shown you how to create charts with `ipyvizzu`
using a chart type-agnostic, uniform way without being limited to a predefined
set of available charts. But sometimes, when you know the chart type you want to
use, it is easier to start with that and skip configuring it from scratch. For
this reason, `ipyvizzu` provides preset chart configurations for many known
chart types. See the [preset gallery](../examples/presets/index.html) for all
available presets.

Use the methods of the presets static property of the `Config` class to build a
chart based on a preset. These methods return chart configuration objects that
can be passed to the `animate` method. For example, this is how to create a
stacked bubble chart using its preset.

<div id="tutorial_01"></div>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style


data_frame = pd.read_csv("../data/music_data.csv")
data = Data()
data.add_data_frame(data_frame)


chart = Chart()

chart.animate(data)

chart.animate(
    Config(
        {
            "title": "Using a preset",
        }
    )
)

chart.animate(
    Config.stackedBubble(
        {
            "size": "Popularity",
            "color": "Kinds",
            "stackedBy": "Genres",
        }
    )
)
```

Presets will override all channels, removing all previously set series from the
chart. Using a preset will also explicitly set most chart configuration
parameters. Exceptions to this are the `legend`, `title`, `reverse`, and `sort`
properties that can be set while using a preset. Here's an example of a preset
where chart elements are sorted by value.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "title": "Set sorting for a chart preset",
        }
    )
)

chart.animate(
    Config.radialStackedBar(
        {
            "angle": "Popularity",
            "radius": "Genres",
            "stackedBy": "Kinds",
            "sort": "byValue",
        }
    )
)
```

As you will see, the preset doesn't override the previously configured sorting
and wouldn't affect the rest of the chart config parameters mentioned above
either.

Presets will affect chart configuration, but you might also want to set the
style or the underlying data.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "title": "Setting style for a preset",
        }
    )
)

chart.animate(
    Config.radialBar(
        {
            "angle": "Popularity",
            "radius": "Genres",
        }
    ),
    Style({"plot.xAxis.interlacing.color": "#ffffff00"}),
)
```

<script src="./chart_presets.js"></script>
