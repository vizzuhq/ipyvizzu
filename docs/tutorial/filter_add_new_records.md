# Filtering & adding new records

Filtering enables you to zoom in or out within a chart, allowing the viewer to
focus on certain selected elements, or get more context. You can also add new
records to the data on the chart which makes it easy to work with real-time
sources.

!!! note
    Currently `filter` and `set_filter` methods only accept JavaScript
    expression as string. The data fields can be accessed via the `record`
    object, see the examples below.

We add two items from the `Genres` dimension - using the `||` operator - to the
filter, so the chart elements that belong to the other two items will vanish
from the chart.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config

    df = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.csv"
    )
    data1 = Data()
    data1.add_data_frame(df)

    chart = Chart()

    chart.animate(data1)

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
filter1 = Data.filter(
    "record['Genres'] == 'Pop' || record['Genres'] == 'Metal'"
)

chart.animate(filter1)
```

Now we add a cross-filter that includes items from both the `Genres` and the
`Kinds` dimensions. This way we override the filter from the previous state. If
we weren't update the filter, `ipyvizzu` would use it in subsequent states.

<div id="tutorial_02"></div>

```python
filter2 = Data.filter(
    "(record['Genres'] == 'Pop' || record['Genres'] == 'Metal')"
    + " && record['Kinds'] == 'Smooth'"
)

chart.animate(filter2)
```

Switching the filter off to get back to the original view.

<div id="tutorial_03"></div>

```python
chart.animate(Data.filter(None))
```

Here we add another record to the data set and update the chart accordingly.

<div id="tutorial_04"></div>

```python
records = [
    ["Soul", "Hard", 91],
    ["Soul", "Smooth", 57],
    ["Soul", "Experimental", 115],
]

data2 = Data()
data2.add_records(records)

chart.animate(data2)
```

!!! info
    Combining this option with the [store](./shorthands_store.md) function makes
    it easy to update previously configured states with fresh data since this
    function saves the config and style parameters of the chart into a variable
    but not the data.

<script src="../filter_add_new_records.js"></script>
