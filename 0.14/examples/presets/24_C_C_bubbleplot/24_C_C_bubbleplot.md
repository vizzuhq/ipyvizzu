---
csv_url: ../../../assets/data/chart_types_eu.csv
---

# Bubble Plot

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
    Config.bubbleplot(
        {
            "x": "Value 4 (+/-)",
            "y": "Value 5 (+/-)",
            "color": "Joy factors",
            "dividedBy": "Country",
            "size": "Value 3 (+)",
            "title": "Bubble Plot",
        }
    )
)
```

<script src="./24_C_C_bubbleplot.js"></script>
