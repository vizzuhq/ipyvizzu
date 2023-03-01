---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Stacked Bubble Chart

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
    Config.stackedBubble(
        {
            "size": "Value 2 (+)",
            "color": "Joy factors",
            "stackedBy": "Country_code",
            "title": "Stacked Bubble Chart",
        }
    )
)
```

<script src="./62_W_R_stacked_bubble.js"></script>
