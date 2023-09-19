---
csv_url: ../../assets/data/music_data.csv
---

# Animation control & keyframes

Using the `control` property provided by the chart you can play, pause, stop,
seek or reverse the animations.

In this step, we seek forward to `50%` of progress after the animation starts.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Keyframe

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
chart.animate(
    Config(
        {
            "channels": {
                "x": {"attach": ["Kinds"]},
                "y": {"detach": ["Kinds"]},
            },
        }
    )
)
chart.control.seek("50%")
```

You can also control the initial position and play state of the animation
through the keyword arguments of the animate method.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"detach": ["Kinds"]},
                "y": {"attach": ["Kinds"]},
            },
        }
    ),
    playState="paused",
    position=0.5,
)
chart.control.play()
```

You may want to control multiple animations as a single one.

You can do this by boundling them together and passing them to a single
`animate` call. To do this, you need to create a `Keyframe` object from the
arguments of every single `animate` call and then passing them into a single
`animate` call.

<div id="tutorial_03"></div>

```python
chart.animate(
    Keyframe(
        Config(
            {
                "channels": {
                    "x": {"attach": ["Kinds"]},
                    "y": {"detach": ["Kinds"]},
                },
            }
        ),
        duration=0.5,
    ),
    Keyframe(
        Config(
            {
                "channels": {
                    "x": {"detach": ["Kinds"]},
                    "y": {"attach": ["Kinds"]},
                }
            }
        ),
        duration=1,
    ),
)
```

<script src="../animation_control_keyframes.js"></script>
