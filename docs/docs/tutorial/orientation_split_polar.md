# Orientation, split & polar

Now that you are familiar with the basic logic and operation of ipyvizzu, let's
dive in with some more advanced features that you can use to create animated
data stories and show the data from different perspectives.

Switching orientation means that you put a measure from one axis to the other
to see the data from a different perspective. This is once again a state you
should only use temporarily.

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
                "y": {"set": ["Popularity", "Kinds"]},
                "x": {"set": "Genres"},
                "label": {"attach": "Popularity"},
            },
            "color": {"attach": "Kinds"},
            "title": "Switch the orientation = arrange by other axis",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "detach": "Popularity",
                },
                "x": {
                    "attach": "Popularity",
                },
            }
        }
    )
)
```

<div id="tutorial_01"></div>

By turning the split parameter on, you can see stacked elements side-by-side,
which enables the comparison of the components.

```python
chart.animate(Config({"title": "Split stacked values = show side-by-side"}))

chart.animate(Config({"split": True}))
```

<div id="tutorial_02"></div>

Merging the components by turning the split parameter off.

```python
chart.animate(Config({"title": "Merge"}))

chart.animate(Config({"split": False}))
```

<div id="tutorial_03"></div>

We aggregate the data by removing the Genres dimension from the x-axis.

```python
chart.animate(Config({"title": "Aggregate"}))

chart.animate(
    Config(
        {
            "channels": {
                "x": {
                    "detach": "Genres",
                }
            }
        }
    )
)
```

<div id="tutorial_04"></div>

Switching from cartesian coordinates to polar. When doing so, it is worth
setting the axis range on the axis with the dimension so that the viewers can
easily compare the values shown. If you want to return to the default cartesian
coordinates, just set the coordSystem parameter to `cartesian`.

```python
chart.animate(Config({"title": "Polar coordinates"}))

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "range": {
                        "min": "-30%",
                    },
                },
            },
            "coordSystem": "polar",
        }
    )
)
```

<div id="tutorial_05"></div>

<script src="./01_10_orientation_split_polar.js"></script>
