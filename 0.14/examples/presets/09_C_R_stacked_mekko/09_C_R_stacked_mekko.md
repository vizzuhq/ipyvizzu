---
csv_url: ../../../assets/data/chart_types_eu_data_4.csv
---

# Stacked Mekko Chart

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu_data_4.csv",
        dtype={"Year": str, "Timeseries": str},
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()
    chart.animate(data)
    ```

```python
chart.animate(
    Config.mekko(
        {
            "x": "Value 1 (+)",
            "y": "Value 2 (+)",
            "stackedBy": "Joy factors",
            "groupedBy": "Country",
            "title": "Stacked Mekko Chart",
        }
    )
)
```

<script src="./09_C_R_stacked_mekko.js"></script>
