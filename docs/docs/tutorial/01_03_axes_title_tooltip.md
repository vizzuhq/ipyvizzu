# Axes, title, tooltip

To build a chart with ipyvizzu, you have to add data series to the channels.

The first step is to create a simple column chart, adding one of the dimensions (Genre) to the x-axis and the measure (Popularity) to the y-axis using the set property.

```python
from ipyvizzu import Chart, ChartProperty, Data, Config


chart = Chart()

data = Data.from_json("./music_data.json")

chart.animate(data)

chart.animate(
    Config({"channels": {"y": {"set": "Popularity"}, "x": {"set": "Genres"}}})
)
```

<div id="tutorial_01_03_01"></div>
<button type="button" id="tutorial_01_03_01_replay">Replay</button>

In the next step, the chart is rearranged by putting both series on the y-axis using once again the set property, resulting in a single column chart. Vizzu automatically animates between the initial state and this one.

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

<div id="tutorial_01_03_02"></div>
<button type="button" id="tutorial_01_03_02_replay">Replay</button>

Instead of set, you can use attach and detach to add or remove series to/from the channels.

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": "Popularity"},
                "x": {"attach": "Popularity"},
            }
        }
    )
)
```

<div id="tutorial_01_03_03"></div>
<button type="button" id="tutorial_01_03_03_replay">Replay</button>

Using attach & detach makes it easier to build your animated charts step-by-step, however you either have to keep in mind what you had on which channel in the previous step or add the following code to access the actual configuration of the chart.

**Note:** Add the following code to log the actual configuration of the chart in the browser console.

```python
chart.log(ChartProperty.CONFIG)
```

Setting the chart title with the title command.

```python
chart.animate(Config({"title": "My first chart"}))
```

<div id="tutorial_01_03_04"></div>
<button type="button" id="tutorial_01_03_04_replay">Replay</button>

Switching on the tooltips that appear on the chart elements when the user hovers over them with their mouse by adding the (tooltip, true) parameters to the chart.feature method.

```python
chart.feature("tooltip", True)
```

<div id="tutorial_01_03_05"></div>
<button type="button" id="tutorial_01_03_05_replay">Replay</button>

<script src="./01_03_axes_title_tooltip.js"></script>
