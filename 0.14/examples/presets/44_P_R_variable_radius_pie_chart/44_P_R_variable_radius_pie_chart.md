---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Variable Radius Pie Chart

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
    Config.variableRadiusPie(
        {
            "angle": "Value 2 (+)",
            "radius": "Value 1 (+)",
            "by": "Joy factors",
            "title": "Variable Radius Pie Chart",
        }
    )
)
```

<script src="./44_P_R_variable_radius_pie_chart.js"></script>
