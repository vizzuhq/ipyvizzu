---
csv_url: ../../../assets/data/chart_types_eu_data_6.csv
---

# Stacked Column Chart

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
    Config.stackedColumn(
        {
            "x": "Country",
            "y": "Value 2 (+)",
            "stackedBy": "Joy factors",
            "title": "Stacked Column Chart",
        }
    )
)
```

<script src="./04_C_R_stacked_column.js"></script>
