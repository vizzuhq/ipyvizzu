---
csv_url: ../../assets/data/music_data.csv
---

# Geometry

In `ipyvizzu` you can set the geometric elements used to represent your data by
the geometry property within the config object. This is where the library shines
\- beautifully animating between the geometries!

Switching the geometry to area.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/music_data.csv"
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()

    chart.animate(data)

    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Popularity"]},
                    "x": {"set": ["Genres"]},
                },
            }
        )
    )
    ```

```python
chart.animate(Config({"geometry": "area"}))
```

Drawing a line chart.

<div id="tutorial_02"></div>

```python
chart.animate(Config({"geometry": "line"}))
```

Switching the geometry to circle. This setting is the most useful when used
together with the size channel, as shown in the next chapter of the tutorial.

<div id="tutorial_03"></div>

```python
chart.animate(Config({"geometry": "circle"}))
```

Rectangle geometry is the default setting in `ipyvizzu`, used for most common
charts like bar and column charts.

<div id="tutorial_04"></div>

```python
chart.animate(
    Config(
        {
            "geometry": "rectangle ",
        }
    )
)
```

<script src="../geometry.js"></script>
