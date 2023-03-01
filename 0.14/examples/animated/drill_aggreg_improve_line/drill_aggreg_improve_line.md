---
csv_url: ../../../assets/data/chart_types_eu_data_6.csv
---

# Single Line  to Line  I

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu_data_6.csv",
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
            "channels": {"x": "Year", "y": "Value 3 (+)"},
            "title": "Single Line Chart",
            "geometry": "line",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "y": ["Country", "Value 3 (+)"],
                "color": "Country",
            },
            "title": "Drill down",
            "geometry": "area",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"y": "Value 3 (+)"},
            "title": "Line Chart I",
            "geometry": "line",
        }
    )
)
```

<script src="./drill_aggreg_improve_line.js"></script>
