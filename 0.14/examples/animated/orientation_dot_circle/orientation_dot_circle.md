---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Scatter Plot to Dot Plot

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
                "x": "Value 5 (+/-)",
                "y": "Value 6 (+/-)",
                "noop": "Joy factors",
                "lightness": "Year",
            },
            "title": "Scatter Plot",
            "geometry": "circle",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"x": "Year"},
            "title": "Dot Plot",
            "legend": "lightness",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"x": "Value 5 (+/-)", "y": "Value 6 (+/-)"},
            "title": "Scatter Plot",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"y": "Joy factors", "noop": None},
            "title": "Dot Plot",
        }
    )
)
```

<script src="./orientation_dot_circle.js"></script>
