---
csv_url: ./titanic/titanic.csv
---

# Passengers of the Titanic

<div id="example_01"></div>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config

data_frame = pd.read_csv("./titanic/titanic.csv")
data = Data()
data.add_data_frame(data_frame)

chart = Chart()

chart.animate(data)

chart.animate(
    Config(
        {
            "x": "Count",
            "y": "Sex",
            "label": "Count",
            "title": "Passengers of the Titanic",
        }
    )
)
chart.animate(
    Config(
        {
            "x": ["Count", "Survived"],
            "label": ["Count", "Survived"],
            "color": "Survived",
        }
    )
)
chart.animate(Config({"x": "Count", "y": ["Sex", "Survived"]}))

chart.animate(
    Config(
        {"x": ["Count", "Sex", "Survived"], "y": None, "coordSystem": "polar"}
    )
)
```

<script src="./titanic/titanic.js"></script>
