# Animation options

In ipyvizzu you can set the timing and duration of the animation. You can do
this either for the whole animation, or for animation groups such as the
elements moving along the x-axis or the y-axis, appearing or disappearing or
when the coordinate system is changed.

Let’s see first a simple example when a stacked column chart is grouped using
the default animation options.

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
            },
            "label": {"attach": "Popularity"},
            "color": {"set": "Kinds"},
            "title": "Default options - step 1",
        }
    )
)

chart.animate(
    Config({"channels": {"y": {"detach": "Kinds"}, "x": {"attach": "Kinds"}}})
)
```

<div id="tutorial_01"></div>

We stack the columns, still with the default options.

```python
chart.animate(Config({"title": "Default options - step 2"}))

chart.animate(
    Config({"channels": {"x": {"detach": "Kinds"}, "y": {"attach": "Kinds"}}})
)
```

<div id="tutorial_02"></div>

Now we change the animation settings for the elements moving along the y-axis
and also the change in styles, more specifically when the labels on the markers
move from the center of the chart elements to the top of them.

```python
chart.animate(
    Config({"title": "Custom animation settings for specific groups"})
)

chart.animate(
    Config(
        {"channels": {"y": {"detach": "Kinds"}, "x": {"attach": "Kinds"}}}
    ),
    y={"duration": 2, "delay": 2},
    style={"duration": 2, "delay": 4},
)
```

<div id="tutorial_03"></div>

This is an example of changing the settings for the whole animation at once.

```python
chart.animate(Config({"title": "Custom options for the whole animation"}))

chart.animate(
    Config(
        {"channels": {"x": {"detach": "Kinds"}, "y": {"attach": "Kinds"}}}
    ),
    duration=1,
    easing="linear",
)
```

<div id="tutorial_04"></div>

When the two settings are combined, ipyvizzu will use the general animation
options and spread the unique settings for specific groups proportionally. This
is why you can see the same animation as two steps before but happening much
quicker since the duration of the whole animation is set to 1 second.

```python
chart.animate(Config({"title": "Custom settings for both"}))

chart.animate(
    Config(
        {"channels": {"y": {"detach": "Kinds"}, "x": {"attach": "Kinds"}}}
    ),
    duration=1,
    easing="linear",
    y={"duration": 2, "delay": 2},
    style={"duration": 2, "delay": 4},
)
```

<div id="tutorial_05"></div>

The default unit for animation is seconds, but you can set other units.

```python
chart.animate(Config({"title": "Set unit"}))

chart.animate(
    Config(
        {"channels": {"x": {"detach": "Kinds"}, "y": {"attach": "Kinds"}}}
    ),
    duration="500ms",
)
```

<div id="tutorial_06"></div>

<script src="./animation_options.js"></script>
