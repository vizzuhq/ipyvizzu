---
csv_url: ../../assets/data/music_data.csv
---

# Events

You can register handlers for various events. There are mouse events (`click`,
`mouseon`), animation events (`begin`, `update`, `complete`), and rendering
events that are called before rendering the chart elements. Handlers can be
registered/unregistered with the `on`, `off` method pair.

!!! note
    Currently `on` method only accept handler's JavaScript expression as string.
    The event can be accessed via the `event` object, see the examples below.

We are registering a handler for the `click` event which will show an alert
block with information about the clicked marker.

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
            },
            "label": {"attach": "Popularity"},
            "color": {"set": "Kinds"},
            "title": "Click event added to markers",
        }
    )
)

click_handler = "alert(JSON.stringify(event.data));"

click = chart.on("click", click_handler)
```

Unregistering the previously registered handler.

```python
chart.off(click)
```

Here we override the axis label color for `Jazz` to red and all others to gray.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "title": "Changing the canvas context before label draw",
        }
    )
)

label_draw_handler = (
    "event.renderingContext.fillStyle ="
    + " (event.data.text === 'Jazz') ? 'red' : 'gray';"
)

label_draw = chart.on("plot-axis-label-draw", label_draw_handler)
```

Unregistering the previously registered handler.

```python
chart.off(label_draw)
```

The default behaviour of all events can be blocked by calling the event's
`preventDefault` method. Here we block the drawing of the `Vizzu` logo in the
bottom right corner of the chart.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "title": "Prevent default behavior",
        }
    )
)

logo_draw_handler = "event.preventDefault();"

logo_draw = logo_chart.on("logo-draw", logo_draw_handler)
```

Unregistering the previously registered handler.

```python
chart.off(logo_draw)
```

<script src="../events.js"></script>
