---
csv_url: ../../../assets/data/chart_types_eu_data_6.csv
---

# Stacked Streamgraph to Split Area

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu_data_6.csv",
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
                "y": ["Value 3 (+)", "Country"],
                "color": "Country",
            },
            "title": "Stacked Streamgraph",
            "geometry": "area",
            "align": "center",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {"y": {"range": {"max": "100%"}}},
            "title": "Split Area Chart",
            "split": True,
            "align": "min",
        }
    )
)
```

<script src="./merge_split_area_stream_3dis_1con.js"></script>
