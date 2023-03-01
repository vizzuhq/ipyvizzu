---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Grouped Column Chart

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
                "x": ["Joy factors", "Country"],
                "y": "Value 5 (+/-)",
                "color": "Joy factors",
                "label": "Value 5 (+/-)",
            },
            "title": "Grouped Column Chart",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "label": {
                        "fontSize": 6,
                        "orientation": "vertical",
                        "angle": -3.14,
                    }
                }
            }
        }
    ),
)
```

<script src="./column_grouped_rectangle_negative_2dis_1con.js"></script>
