---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Splitted Column Chart

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
    Config.splittedColumn(
        {
            "x": "Year",
            "y": "Value 2 (+)",
            "splittedBy": "Joy factors",
            "title": "Splitted Column Chart",
        }
    )
)
```

<script src="./05_C_R_splitted_column.js"></script>
