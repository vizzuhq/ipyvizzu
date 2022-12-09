# Aggregate/drill-down

These features basically mean that you add or remove an additional dimension
to/from an axis or another channel. As you can see below, there are some
important things to keep in mind when you use them.

Let’s stack together the elements by putting the Genres dimension from the
x-axis to the y-axis. At the end of this phase, there are chart elements with
the same color stacked on top of each other, which is something you would want
to avoid.

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
            "title": "Stack",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "attach": "Genres",
                },
                "x": {"set": None},
            }
        }
    )
)
```

<div id="tutorial_01"></div>

By taking the Genres off of the y-axis, only one chart element remains for
every color, and Vizzu automatically calculates and shows the aggregate value
of the elements.

**Note:** Instead of taking the unwanted dimension down from the chart, Genres
could have been added to the lightness channel to differentiate the chart
elements.

```python
chart.animate(Config({"title": "Aggregate element"}))

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "detach": "Genres",
                },
            }
        }
    )
)
```

<div id="tutorial_02"></div>

To drill-down, the same dimension is put back on the y-axis, which results in a
state that we suggest you to only use temporarily when in transition.

```python
chart.animate(Config({"title": "Drill-down"}))

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "attach": "Genres",
                },
            }
        }
    )
)
```

<div id="tutorial_03"></div>

We group the elements by putting once again the Genres dimension on the x-axis.

```python
chart.animate(Config({"title": "Group"}))

chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "detach": "Genres",
                },
                "x": {
                    "set": "Genres",
                },
            }
        }
    )
)
```

<div id="tutorial_04"></div>

<script src="./aggregate_drilldown.js"></script>
