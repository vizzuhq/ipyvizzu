---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Radial Bar Chart

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
                "x": "Value 2 (+)",
                "y": {
                    "set": ["Joy factors"],
                    "range": {"min": "-30%"},
                },
                "color": "Joy factors",
                "label": "Value 2 (+)",
            },
            "title": "Radial Bar Chart",
            "coordSystem": "polar",
        }
    )
)
```

<script src="./radial_rectangle_1dis_1con.js"></script>
