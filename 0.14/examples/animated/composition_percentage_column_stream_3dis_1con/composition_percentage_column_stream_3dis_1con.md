---
csv_url: ../../../assets/data/chart_types_eu_data_14.csv
---

# Column  to 100% Column

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu_data_14.csv",
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
                "y": ["Value 2 (+)", "Country"],
                "noop": "Country",
            },
            "title": "Column Chart",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "y": {"range": {"max": "100%"}},
                "color": "Country",
                "noop": None,
            },
            "title": "Split Column Chart",
            "split": True,
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"y": {"range": {"max": "auto"}}},
            "title": "Stacked Column Chart",
            "split": False,
        }
    )
)

chart.animate(
    Config({"title": "100% Column Chart", "align": "stretch"})
)
```

<script src="./composition_percentage_column_stream_3dis_1con.js"></script>
