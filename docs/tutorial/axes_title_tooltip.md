---
csv_url: ../../assets/data/music_data.csv
---

# Axes, title, tooltip

To build a chart with `ipyvizzu`, you have to add data series to the channels.
Channels will be explained more in-depth later, but for now, think of channels
as different elements of the chart we can bind data to. The simplest and most
often used channels are the x and y-axes.

The first step is to create a simple column chart, adding one of the dimensions
from the data set we added in the previous chapter (`Genres`) to the x-axis and
the measure (`Popularity`) to the y-axis using the set property.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, ChartProperty, Data, Config

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.csv"
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()

    chart.animate(data)
    ```

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"set": ["Popularity"]},
                "x": {"set": ["Genres"]},
            }
        }
    )
)
```

In the next step, the chart is rearranged by putting both series on the y-axis
using once again the set property, resulting in a single column chart.
`ipyvizzu` automatically animates between the initial state and this one.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"set": ["Popularity", "Genres"]},
                "x": {"set": None},
            }
        }
    )
)
```

Instead of set, you can use attach and detach to add or remove series to/from
the channels.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": ["Popularity"]},
                "x": {"attach": ["Popularity"]},
            }
        }
    )
)
```

Using attach & detach makes it easier to build your animated charts
step-by-step, however you either have to keep in mind what you had on which
channel in the previous step or add the following code to access the actual
configuration of the chart.

Add the following code to log the actual configuration of the chart in the
browser console.

```python
chart.log(ChartProperty.CONFIG)
```

Setting the chart title with the title command.

<div id="tutorial_04"></div>

```python
chart.animate(Config({"title": "My first chart"}))
```

Switching on the tooltips that appear on the chart elements when the user hovers
over them with their mouse by adding the (`"tooltip"`, `True`) parameters to the
`chart.feature` method.

<div id="tutorial_05"></div>

```python
chart.feature("tooltip", True)
```

<script src="../axes_title_tooltip.js"></script>
