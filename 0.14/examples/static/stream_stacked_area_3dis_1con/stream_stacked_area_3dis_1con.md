---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Stacked Streamgraph

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
                "x": ["Year", "Joy factors"],
                "y": ["Value 3 (+)", "Country_code"],
                "color": "Country_code",
            },
            "title": "Stacked Streamgraph",
            "geometry": "area",
            "align": "center",
        }
    )
)
```

<script src="./stream_stacked_area_3dis_1con.js"></script>
