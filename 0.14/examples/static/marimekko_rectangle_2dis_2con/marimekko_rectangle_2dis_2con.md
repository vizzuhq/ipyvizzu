---
csv_url: ../../../assets/data/chart_types_eu_data_4.csv
---

# Marimekko Chart

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/chart_types_eu_data_4.csv",
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
                "x": ["Country", "Value 2 (+)"],
                "y": ["Joy factors", "Value 3 (+)"],
                "color": "Joy factors",
                "label": ["Country", "Value 2 (+)"],
            },
            "title": "Marimekko Chart",
            "align": "stretch",
            "orientation": "horizontal",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "label": {
                        "format": "dimensionsFirst",
                        "fontSize": "0.7em",
                    }
                }
            }
        }
    ),
)
```

<script src="./marimekko_rectangle_2dis_2con.js"></script>
