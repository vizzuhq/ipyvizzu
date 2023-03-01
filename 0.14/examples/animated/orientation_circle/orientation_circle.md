---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Dot Plot to Dot Plot with Other Orientation

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
                "y": "Joy factors",
                "lightness": "Joy factors",
                "noop": "Year",
            },
            "title": "Dot Plot",
            "geometry": "circle",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "x": "Year",
                "y": "Value 5 (+/-)",
                "noop": "Joy factors",
            },
            "title": "Dot Plot with Other Orientation",
        }
    )
)
```

<script src="./orientation_circle.js"></script>
