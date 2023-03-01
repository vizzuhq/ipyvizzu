---
csv_url: ../../assets/data/music_data.csv
---

# Orientation, split & polar

Now that you are familiar with the basic logic and operation of `ipyvizzu`,
let's dive in with some more advanced features that you can use to create
animated data stories and show the data from different perspectives.

Switching orientation means that you put a measure from one axis to the other to
see the data from a different perspective. This is once again a state you should
only use temporarily.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config

    data_frame = pd.read_csv(
        "https://github.com/vizzuhq/ipyvizzu/raw/main/docs/assets/data/music_data.csv"
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()

    chart.animate(data)

    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Popularity", "Kinds"]},
                    "x": {"set": ["Genres"]},
                    "label": {"attach": ["Popularity"]},
                },
                "color": {"attach": ["Kinds"]},
            }
        )
    )
    ```

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "detach": ["Popularity"],
                },
                "x": {
                    "attach": ["Popularity"],
                },
            }
        }
    )
)
```

By turning the split parameter on, you can see stacked elements side-by-side,
which enables the comparison of the components.

<div id="tutorial_02"></div>

```python
chart.animate(Config({"split": True}))
```

Merging the components by turning the split parameter off.

<div id="tutorial_03"></div>

```python
chart.animate(Config({"split": False}))
```

We aggregate the data by removing the `Genres` dimension from the x-axis.

<div id="tutorial_04"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {
                    "detach": ["Genres"],
                }
            }
        }
    )
)
```

Switching from cartesian coordinates to polar. When doing so, it is worth
setting the axis range on the axis with the dimension so that the viewers can
easily compare the values shown. If you want to return to the default cartesian
coordinates, just set the `coordSystem` parameter to `'cartesian'`.

!!! info
    The range of the x-axis is automatically set to `max:133%` as this is the
    standard way to show radial charts.

<div id="tutorial_05"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "range": {
                        "min": "-30%",
                    },
                },
            },
            "coordSystem": "polar",
        }
    )
)
```

<script src="../orientation_split_polar.js"></script>
