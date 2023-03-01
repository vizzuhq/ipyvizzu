---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Polar Scatter Plot

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
    Config.polarScatter(
        {
            "angle": "Value 3 (+)",
            "radius": "Value 2 (+)",
            "dividedBy": "Country",
            "title": "Polar Scatter Plot",
        }
    )
)
```

<script src="./53_P_C_polar_scatter.js"></script>
