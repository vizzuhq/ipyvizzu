---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Distribution Plot to Scatter Plot

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
                "x": "Joy factors",
                "y": "Value 5 (+/-)",
                "color": "Joy factors",
                "noop": "Country_code",
            },
            "title": "Distribution Plot",
            "geometry": "circle",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "x": ["Joy factors", "Value 6 (+/-)"],
                "label": "Country_code",
            },
            "title": "Scatter Plot",
        }
    )
)
```

<script src="./distribution_relationship_dotplot_dotplot.js"></script>
