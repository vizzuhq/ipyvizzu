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
    Config.scatter(
        {
            "x": "Value 6 (+/-)",
            "y": "Value 5 (+/-)",
            "dividedBy": "Year",
            "title": "Scatter Plot",
        }
    )
)
```

<script src="./22_C_C_scatter.js"></script>
