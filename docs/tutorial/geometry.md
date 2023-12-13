---
csv_url: ../../assets/data/music_data.csv
---

# Geometry

In `ipyvizzu` you can set the geometric elements used to represent your data by
the geometry property within the config object. This is where the library shines
\- beautifully animating between the geometries!

Switching the geometry to area.

<div id="tutorial_01"></div>

{% include-markdown "tutorial/assets/setup/setup_b.md" %}

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
