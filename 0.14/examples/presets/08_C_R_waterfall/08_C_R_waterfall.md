---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Waterfall Chart

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
    Config.waterfall(
        {
            "x": "Year",
            "y": "Value 5 (+/-)",
            "title": "Waterfall Chart",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "colorGradient": "#ff001b 0,#ff001b 0.5,#7e79e8 0.5,#7e79e8 1",
                    "label": {"position": "top"},
                }
            }
        }
    ),
)
```

<script src="./08_C_R_waterfall.js"></script>
