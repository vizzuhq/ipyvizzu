# Sorting

ipyvizzu provides multiple options to sort data. By default, the data is sorted
by the order it is added to ipyvizzu. This is why we suggest to add temporal
data such as dates in chronological order - from oldest to newest.

You can also sort the elements by value, which will provide you with an
ascending order.

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
            "title": "Switch to ascending order...",
        }
    )
)

chart.animate(
    Config(
        {
            "sort": "byValue",
        }
    )
)
```

<div id="tutorial_01"></div>

If you want descending order instead, you have to set the reverse parameter to
true. When used without setting the sorting to byValue, the elements will be in
the opposite order than they are in the data set added to ipyvizzu.

```python
chart.animate(Config({"title": "...or descending order."}))

chart.animate(
    Config(
        {
            "reverse": True,
        }
    )
)
```

<div id="tutorial_02"></div>

This is how to switch back to the default sorting.

```python
chart.animate(Config({"title": "Let's get back to where we were"}))

chart.animate(
    Config(
        {
            "sort": "none",
            "reverse": False,
        }
    )
)
```

<div id="tutorial_03"></div>

When you have more than one dimension on a channel, their order determines how
the elements are grouped. For example, below - each set of bars is first
organized by `Genres`, and then we have one bar for each of `Kinds`.

```python
chart.animate(Config({"title": "With two discretes on one axis..."}))

chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": "Kinds"},
                "x": {"set": ["Genres", "Kinds"]},
            }
        }
    )
)
```

<div id="tutorial_04"></div>

When switching the order of dimensions on the x-axis ipyvizzu will rearrange
the elements according to this new logic.

**Note:** The legend is automatically removed during the animation.

```python
chart.animate(Config({"title": "...grouping is determined by their order."}))

chart.animate(
    Config(
        {
            "channels": {
                "x": {"set": ["Kinds", "Genres"]},
            }
        }
    )
)
```

<div id="tutorial_05"></div>

<script src="./sorting.js"></script>
