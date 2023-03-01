---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Stacked Column Chart

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
    Config(
        {
            "channels": {
                "x": "Country",
                "y": ["Joy factors", "Value 2 (+)"],
                "color": "Joy factors",
                "label": "Value 2 (+)",
            },
            "title": "Stacked Column Chart",
        }
    ),
    Style(
        {
            "plot": {
                "xAxis": {"label": {"angle": 2.3}},
                "marker": {
                    "label": {
                        "fontSize": 7,
                        "orientation": "vertical",
                        "angle": -3.14,
                    }
                },
            }
        }
    ),
)
```

<script src="./column_stacked_rectangle_negative_2dis_1con.js"></script>
