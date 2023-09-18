---
csv_url: ../../assets/data/music_data.csv
---

# Events

You can register handlers for various events. There are pointer events (`click`,
`pointeron`), animation events (`begin`, `update`, `complete`), and rendering
events that are called before rendering the chart elements. Handlers can be
registered/unregistered with the `on`, `off` method pair.

!!! note
    Currently `on` method only accept handler's `JavaScript` expression as
    string. The event can be accessed via the `event` object, see the examples
    below.

We are registering a handler for the `click` event which will show an alert
block with information about the clicked marker.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config

    df = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.csv"
    )
    data = Data()
    data.add_df(df)

    chart = Chart()

    chart.animate(data)

    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Popularity", "Kinds"]},
                    "x": {"set": ["Genres"]},
                    "color": {"set": ["Kinds"]},
                    "label": {"set": ["Popularity"]},
                },
            }
        )
    )
    ```

```python
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
logo_draw_handler = "event.preventDefault();"

logo_draw = chart.on("logo-draw", logo_draw_handler)
```

Unregistering the previously registered handler.

```python
chart.off(logo_draw)
```

You can also add a background image to the chart using the `preventDefault`
method.

<div id="tutorial_04"></div>

```python
bgimage_draw_handler = """
if (!window.bgImage) {
    window.bgImage = new Image();
    // base64 converted image
    window.bgImage.src = 'data:image/gif;base64,R0lGODlhAwACAPIAAJLf6q/i7M/r8un0+PT6+/n8/QAAAAAAACH5BAQAAAAALAAAAAADAAIAAAMEWBMkkAA7';
}
event.renderingContext.drawImage(window.bgImage, 0, 0,
    event.data.rect.size.x, event.data.rect.size.y);
event.preventDefault();
"""

bgimage_draw = chart.on("background-draw", bgimage_draw_handler)

chart.animate(Config({"title": "Add background image"}))
```

!!! note
    Place the `chart.on` call before the `chart.animate` call from where you
    want to replace the background image.

Unregistering the previously registered handler.

```python
chart.off(bgimage_draw)
```

<script src="../events.js"></script>
