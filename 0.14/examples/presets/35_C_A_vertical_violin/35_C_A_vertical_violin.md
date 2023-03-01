---
csv_url: ../../../assets/data/music_industry_history_1.csv
---

# Vertical Violin Graph

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    data_frame = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.14/assets/data/music_industry_history_1.csv",
        dtype={"Year": str, "Timeseries": str},
    )
    data = Data()
    data.add_data_frame(data_frame)

    chart = Chart()
    chart.animate(data)
    ```

```python
chart.animate(
    Config.verticalViolin(
        {
            "x": "Revenue [m$]",
            "y": "Year",
            "splittedBy": "Format",
            "title": "Vertical Violin Graph",
        }
    ),
    Style(
        {"plot": {"xAxis": {"interlacing": {"color": "#ffffff00"}}}}
    ),
)
```

<script src="./35_C_A_vertical_violin.js"></script>
