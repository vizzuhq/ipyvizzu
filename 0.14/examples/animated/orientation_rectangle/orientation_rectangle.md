---
csv_url: ../../../assets/data/tutorial.csv
---

# Stacked Column  to Bar

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/tutorial.csv",
        dtype={"Year": str, "Timeseries": str},
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()
    chart.animate(data)
    ```

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": "Timeseries",
                "y": ["Values 1", "Categ. Parent"],
                "color": "Categ. Parent",
                "label": "Values 1",
            },
            "title": "Stacked Column Chart",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"x": "Values 1", "y": "Categ. Parent"},
            "title": "Bar Chart",
        }
    )
)
```

<script src="./orientation_rectangle.js"></script>
