---
csv_url: ../../assets/data/music_data.csv
---

# Aggregate/drill-down

These features basically mean that you add or remove an additional dimension
to/from an axis or another channel.

Let’s aggregate together the elements by getting the `Genres` dimension off the
x-axis. By taking it off of the chart, only one chart element remains for every
color, and `ipyvizzu` automatically calculates and shows the aggregate value of
the elements.

<div id="tutorial_01"></div>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config


data_frame = pd.read_csv("../../assets/data/music_data.csv")
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
                "x": {"set": None},
            }
        }
    )
)
```

To drill-down, the same dimension is put back on the x-axis.

<div id="tutorial_02"></div>

```python
chart.animate(Config({"title": "Drill-down"}))

chart.animate(
    Config(
        {
            "channels": {
                "x": {
                    "attach": "Genres",
                },
            }
        }
    )
)
```

<script src="../aggregate_drilldown.js"></script>
