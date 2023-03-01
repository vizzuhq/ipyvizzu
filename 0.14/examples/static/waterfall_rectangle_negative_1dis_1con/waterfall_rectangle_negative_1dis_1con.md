---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Waterfall Chart

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
                "y": ["Year", "Value 5 (+/-)"],
                "label": "Value 5 (+/-)",
            },
            "title": "Waterfall Chart",
            "legend": None,
        }
    ),
    Style({"plot": {"marker": {"label": {"position": "top"}}}}),
)
```

<script src="./waterfall_rectangle_negative_1dis_1con.js"></script>
