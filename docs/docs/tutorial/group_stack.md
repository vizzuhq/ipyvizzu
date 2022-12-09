# Group/stack

The following example shows how to group and stack elements of a bar chart.

To get a stacked chart, you need to add a new dimension to the same channel
where the measure is: the y-axis. However, since doing only this would result
in multiple column chart elements with the same color stacked on top of each
other, we also add the same dimension to the color channel.

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
            "channels": {"y": {"set": "Popularity"}, "x": {"set": "Genres"}},
            "title": "Creating a stacked chart",
        }
    )
)

chart.animate(
    Config(
        {"channels": {"y": {"attach": "Kinds"}, "color": {"attach": "Kinds"}}}
    )
)
```

<div id="tutorial_01"></div>

By detaching this newly added dimension from the y-axis and attaching it to the
x-axis, you get a grouped bar chart in a way that is easy to follow for the
viewer.

```python
chart.animate(
    Config(
        {
            "title": "...then you can add it to another channel = group elements..."
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": "Kinds"},
                "x": {"attach": "Kinds"},
            },
        }
    )
)
```

<div id="tutorial_02"></div>

To stack a grouped chart, you just have to do the same thing the other way
around: detach the dimension from the x-axis and attach it to the y-axis.

```python
chart.animate(
    Config({"title": "...doing it the other way is how you stack your chart"})
)

chart.animate(
    Config(
        {
            "channels": {
                "y": {"attach": "Kinds"},
                "x": {"detach": "Kinds"},
            },
        }
    )
)
```

<div id="tutorial_03"></div>

<script src="./group_stack.js"></script>
