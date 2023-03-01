---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Polar Area Chart

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
                "x": "Year",
                "y": {
                    "set": ["Value 2 (+)"],
                    "range": {"max": "130%"},
                },
                "label": "Value 2 (+)",
            },
            "title": "Polar Area Chart",
            "geometry": "area",
            "coordSystem": "polar",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "label": {
                        "orientation": "tangential",
                        "angle": -1.57,
                    }
                }
            }
        }
    ),
)
```

<script src="./spiderweb_area_1dis_1con.js"></script>
