---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Scatter Plot

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
                "x": "Value 6 (+/-)",
                "y": "Value 5 (+/-)",
                "noop": "Year",
                "label": "Year",
            },
            "title": "Scatter Plot",
            "geometry": "circle",
        }
    )
)
```

<script src="./scatterplot_circle_negative_1dis_2con.js"></script>
