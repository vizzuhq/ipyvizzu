---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Single Line  to Line  II

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu.csv",
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
                "x": "Year",
                "y": {
                    "set": "Value 3 (+)",
                    "range": {"max": "6000000000"},
                },
                "size": "Country",
            },
            "title": "Single Line Chart",
            "geometry": "line",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"color": "Country", "size": None},
            "title": "Drill down",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"y": {"range": {"max": "auto"}}},
            "title": "Line Chart II",
        }
    )
)
```

<script src="./drilldown_aggregate_line.js"></script>
