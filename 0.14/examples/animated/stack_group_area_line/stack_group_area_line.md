---
csv_url: ../../../assets/data/tutorial.csv
---

# Stacked Area  to Line

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
                "y": {
                    "set": ["Values 1", "Categ. Parent"],
                    "range": {"max": "400"},
                },
                "label": "Values 1",
                "color": "Categ. Parent",
            },
            "title": "Stacked Area Chart",
            "geometry": "area",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"y": "Values 1"},
            "title": "Line Chart",
            "geometry": "line",
        }
    )
)

chart.animate(Config({"channels": {"y": {"range": {"max": "auto"}}}}))
```

<script src="./stack_group_area_line.js"></script>
