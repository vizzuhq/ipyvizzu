---
csv_url: ../../../assets/data/infinite_data.csv
---

# Pie  to Coxcomb

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/infinite_data.csv",
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
                "x": ["Value 1", "Joy factors"],
                "color": "Joy factors",
                "label": "Value 1",
            },
            "title": "Pie Chart",
            "coordSystem": "polar",
        }
    )
)

chart.animate(
    Config(
        {
            "channels": {
                "x": [
                    "Value 1",
                    "Joy factors",
                    "Region",
                    "Country code",
                ],
                "label": None,
            }
        }
    ),
    duration="500ms",
)

chart.animate(
    Config(
        {
            "channels": {
                "x": [
                    "Value 1",
                    "Joy factors",
                    "Region",
                    "Country code",
                ],
                "y": {"set": "Value 3", "range": {"min": "-60%"}},
            },
            "title": "Coxcomb Chart",
        }
    )
)
```

<script src="./composition_comparison_pie_coxcomb_column_2dis_2con.js"></script>
