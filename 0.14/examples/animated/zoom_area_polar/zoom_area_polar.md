---
csv_url: ../../../assets/data/chart_types_eu_data_6.csv
---

# Polar Stacked Area to Zoomed Polar Stacked Area

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
                "y": ["Value 3 (+)", "Country_code"],
                "color": "Country_code",
            },
            "title": "Polar Stacked Area",
            "geometry": "area",
            "coordSystem": "polar",
        }
    )
)

chart.animate(
    data.filter(
        """
  data_6.filter(record) 
  && record.Year < 12 && record.Year > 6
  """
    ),
    Config({"title": "Zoomed Polar Stacked Area"}),
)
```

<script src="./zoom_area_polar.js"></script>
