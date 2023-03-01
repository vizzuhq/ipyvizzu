---
csv_url: ../../../assets/data/chart_types_eu_data_3.csv
---

# Nested Donut Chart

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu_data_3.csv",
        dtype={"Year": str, "Timeseries": str},
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()
    chart.animate(data)
    ```

```python
chart.animate(
    Config.nestedDonut(
        {
            "angle": "Value 2 (+)",
            "stackedBy": "Joy factors",
            "radius": "Country",
            "title": "Nested Donut Chart",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "rectangleSpacing": "0",
                    "borderWidth": 1,
                    "borderOpacity": 0,
                }
            }
        }
    ),
)
```

<script src="./52_P_R_nested_donut.js"></script>
