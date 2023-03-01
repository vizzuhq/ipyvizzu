---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Stacked Radial Bar Chart

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
                "x": ["Country", "Value 2 (+)"],
                "y": {"set": ["Year"], "range": {"min": "-20%"}},
                "color": "Country",
                "lightness": "Year",
            },
            "title": "Stacked Radial Bar Chart",
            "coordSystem": "polar",
        }
    )
)
```

<script src="./radial_stacked_rectangle_2dis_1con.js"></script>
