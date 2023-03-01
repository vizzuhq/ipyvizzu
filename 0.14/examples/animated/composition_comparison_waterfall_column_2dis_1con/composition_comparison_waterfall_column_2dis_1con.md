---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Waterfall  to Column

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
                "color": {
                    "set": ["Value 5 (+/-)"],
                    "range": {"min": "-45", "max": "45"},
                },
                "noop": "Country",
                "label": "Value 5 (+/-)",
            },
            "title": "Waterfall Chart",
            "legend": "color",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "colorGradient": "#3d51b8 0,#6389ec 0.15,#9fbffa 0.35,#d5d7d9 0.5,#f4b096 0.65,#e36c56 0.85,#ac1727 1",
                    "label": {"position": "top"},
                }
            }
        }
    ),
)

chart.animate(
    Config(
        {"channels": {"y": "Value 5 (+/-)"}, "title": "Column Chart"}
    )
)
```

<script src="./composition_comparison_waterfall_column_2dis_1con.js"></script>
