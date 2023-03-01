---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Lollipop Chart

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
    Config.lollipop(
        {"x": "Year", "y": "Value 1 (+)", "title": "Lollipop Chart"}
    )
)
```

<script src="./20_C_C_lollipop_chart.js"></script>
