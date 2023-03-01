---
csv_url: ../../../assets/data/chart_types_eu_data_14.csv
---

# Stacked Column  to Split Column

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
                "color": "Country",
            },
            "title": "Stacked Column Chart",
        }
    )
)

chart.animate(
    Config({"title": "100% Stacked Column Chart", "align": "stretch"})
)

chart.animate(
    Config(
        {
            "channels": {"y": {"range": {"max": "100%"}}},
            "title": "Split Column Chart",
            "align": "min",
            "split": True,
        }
    )
)
```

<script src="./composition_percentage_column_3dis_1con.js"></script>
