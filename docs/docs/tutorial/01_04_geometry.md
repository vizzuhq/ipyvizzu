# Geometry

In ipyvizzu you can set the geometric elements used to represent your data
by the geometry property within the config object. This is where the library
shines - beautifully animating between the geometries!

Switching the geometry to area.

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
            "title": "Geometry",
            "channels": {"y": {"set": "Popularity"}, "x": {"set": "Genres"}},
        }
    )
)

chart.animate(Config({"title": "Geometry: area", "geometry": "area"}))
```

<div id="tutorial_01"></div>

Drawing a line chart.

```python
chart.animate(Config({"title": "Geometry: line", "geometry": "line"}))
```

<div id="tutorial_02"></div>

Switching the geometry to circle.
This setting is the most useful when used together with the size channel,
as shown in the next chapter of the tutorial.

```python
chart.animate(Config({"title": "Geometry: circle", "geometry": "circle"}))
```

<div id="tutorial_03"></div>

Rectangle geometry is the default setting in ipyvizzu,
used for most common charts like bar and column charts.

```python
chart.animate(
    Config(
        {"title": "Geometry: rectangle - default", "geometry": "rectangle "}
    )
)
```

<div id="tutorial_04"></div>

<script src="./01_04_geometry.js"></script>
