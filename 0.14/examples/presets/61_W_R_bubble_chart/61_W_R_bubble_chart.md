---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Bubble Chart

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
    Config.bubble(
        {
            "size": "Value 5 (+/-)",
            "color": "Country_code",
            "title": "Bubble Chart",
        }
    )
)
```

<script src="./61_W_R_bubble_chart.js"></script>
