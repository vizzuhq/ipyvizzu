---
csv_url: ../../assets/data/music_data.csv
---

# Shorthands & Store

To assist you with the development we added various shorthands that will make
your code more compact.

We also added store functions, which enable you to save either a chart state or
a whole animation into a variable that you can reuse later instead of setting up
that state or animation once again.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.csv"
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()

    chart.animate(data)

    chart.animate(
        Config(
            {
                "title": "Store function",
                "channels": {
                    "y": {"set": ["Popularity", "Kinds"]},
                    "x": {"set": ["Genres"]},
                },
                "label": {"attach": ["Popularity"]},
                "color": {"set": ["Kinds"]},
            }
        )
    )
    ```

```python
chart.animate(
    Config(
        {
            "align": "stretch",
        }
    )
)
```

Let's save this state by calling the `store` function.

```python
snapshot = chart.store()
```

If you set/attach/detach just one series on a channel, you don't have to put
that series into an array. Also, let's save this animation by calling the
`store` method of the `control` chart object.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                # "x": { "attach": [ "Kinds" ] },
                "x": {"attach": "Kinds"},
                # "y": { "detach": [ "Kinds" ] },
                "y": {"detach": "Kinds"},
            },
            "align": "none",
        }
    )
)

animation = chart.control.store()
```

If you use set on a channel and no other options like range, you don't have to
express that channel as an object. If you only set one series on a channel you
can simply write the series' name after the channel name.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                # "y": { "set": [ "Kinds", "Popularity" ] },
                "y": ["Kinds", "Popularity"],
                # "x": { "set": [ "Genres" ] },
                "x": "Genres",
            }
        }
    )
)
```

In any case, you can simply omit the `channel` object, `ipyvizzu` will
automatically recognize the channels by their names.

<div id="tutorial_04"></div>

```python
chart.animate(
    Config(
        {
            # "channels": {
            "y": "Kinds",
            "x": ["Genres", "Popularity"]
            # }
        }
    )
)
```

Instead of creating nested objects, you can set the styles like this.

<div id="tutorial_05"></div>

```python
chart.animate(
    Style(
        {
            # "plot": { "xAxis": { "label": { "fontSize": "150%" } } },
            "plot.xAxis.label.fontSize": "150%",
            "title.backgroundColor": "#A0A0A0",
        }
    )
)
```

This is how you can reuse a previously stored animation.

<div id="tutorial_06"></div>

```python
chart.animate(animation)
```

You can also get back to a state that you previously stored.

<div id="tutorial_07"></div>

```python
chart.animate(snapshot)
```

<script src="../shorthands_store.js"></script>
