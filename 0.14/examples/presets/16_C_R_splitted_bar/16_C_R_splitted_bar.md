---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Splitted Bar Chart

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
    Config.splittedBar(
        {
            "x": "Value 2 (+)",
            "y": "Year",
            "splittedBy": "Joy factors",
            "title": "Splitted Bar Chart",
        }
    )
)
```

<script src="./16_C_R_splitted_bar.js"></script>
