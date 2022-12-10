# Without coordinates & noop channel

Certain chart types have neither measures nor dimensions on the axes such as
treemaps and bubble charts. This is a case when the noop channel comes in handy
for grouping and stacking elements in these kinds of charts.

To get to a treemap, we have to detach all dimensions and the measure from the
axes and put two of them on the size channel, whereas the other dimension is
still on the color channel.

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config


data_frame = pd.read_csv("./music_data.csv")
data = Data()
data.add_data_frame(data_frame)


chart = Chart()

chart.animate(data)

chart.animate(
    Config(
        {
            "channels": {
                "y": {"set": ["Kinds", "Popularity"]},
                "x": {"set": "Genres"},
                "label": {"attach": "Popularity"},
            },
            "color": {"set": "Kinds"},
            "title": "Treemap",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "set": None,
                },
                "x": {
                    "set": None,
                },
                "size": {
                    "attach": ["Genres", "Popularity"],
                },
            }
        }
    )
)
```

<div id="tutorial_01"></div>

Getting from a treemap to a bubble chart is simply by changing the geometry to
circle. This bubble chart is stacked by the Type dimension that is on the size
channel - this is why the bubbles are in separate, small groups.

```python
chart.animate(Config({"title": "Bubble chart - stacked"}))

chart.animate(
    Config(
        {
            "geometry": "circle",
        }
    )
)
```

<div id="tutorial_02"></div>

In order to show all bubbles as one group, we use the noop (no operations)
channel for the Genres dimension. The noop channel enables us to have a
dimension on the chart, that doesn’t affect any parameter of the elements, only
their count.

```python
chart.animate(
    Config({"title": "Bubble chart - grouped - using the noop channel"})
)

chart.animate(
    Config(
        {
            "channels": {
                "size": {"detach": "Genres"},
                "noop": {"set": "Genres"},
            }
        }
    )
)
```

<div id="tutorial_03"></div>

<script src="./without_coordinates_noop_channel.js"></script>
