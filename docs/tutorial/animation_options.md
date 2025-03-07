---
csv_url: ../../assets/data/music_data.csv
---

# Animation options

In `ipyvizzu` you can set the timing and duration of the animation. You can do
this either for the whole animation, or for animation groups such as the
elements moving along the x-axis or the y-axis, appearing or disappearing or
when the coordinate system is changed.

Let’s see first a simple example when a stacked column chart is grouped using
the default animation options.

<div id="tutorial_01"></div>

{% include-markdown "tutorial/assets/setup/setup_c.md" %}

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": ["Kinds"]},
                "x": {"attach": ["Kinds"]},
            }
        }
    )
)
```

We stack the columns, still with the default options.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"detach": ["Kinds"]},
                "y": {"attach": ["Kinds"]},
            }
        }
    )
)
```

Now we change the animation settings for the elements moving along the y-axis
and also the change in styles, more specifically when the labels on the markers
move from the center of the chart elements to the top of them.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"attach": ["Kinds"]},
                "y": {"detach": ["Kinds"]},
            }
        }
    ),
    y={"duration": 2, "delay": 2},
    style={"duration": 2, "delay": 4},
)
```

This is an example of changing the settings for the whole animation at once.

<div id="tutorial_04"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"detach": ["Kinds"]},
                "y": {"attach": ["Kinds"]},
            }
        }
    ),
    duration=1,
    easing="linear",
)
```

When the two settings are combined, `ipyvizzu` will use the general animation
options and spread the unique settings for specific groups proportionally. This
is why you can see the same animation as two steps before but happening much
quicker since the duration of the whole animation is set to 1 second.

<div id="tutorial_05"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"attach": ["Kinds"]},
                "y": {"detach": ["Kinds"]},
            }
        }
    ),
    duration=1,
    easing="linear",
    y={"duration": 2, "delay": 2},
    style={"duration": 2, "delay": 4},
)
```

The default unit for animation is seconds, but you can set other units.

<div id="tutorial_06"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"detach": ["Kinds"]},
                "y": {"attach": ["Kinds"]},
            }
        }
    ),
    duration="500ms",
)
```

<script src="../animation_options.js"></script>
