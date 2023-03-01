---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Bubble Plot to Bubble

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
                "x": ["Joy factors", "Value 6 (+/-)"],
                "y": "Value 5 (+/-)",
                "color": "Joy factors",
                "size": "Value 2 (+)",
                "label": "Country_code",
            },
            "title": "Bubble Plot",
            "geometry": "circle",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "x": None,
                "y": None,
                "size": ["Value 2 (+)", "Country_code"],
            },
            "title": "Stacked Bubble Chart",
        }
    )
)

chart.animate(
    Config(
        {"channels": {"size": "Value 2 (+)"}, "title": "Bubble Chart"}
    )
)
```

<script src="./relationship_comparison_circle_2_bubble_plot.js"></script>
