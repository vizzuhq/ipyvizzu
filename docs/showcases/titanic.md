---
csv_url: ./titanic.csv
---

# Passengers of the Titanic

<div class="showcase">
  <iframe  id="showcase" src='./main.html' width="100%" scrolling="no" frameborder="0"></iframe>
</div>
<script src="../../assets/javascripts/iframe/autoheight.js"></script>
<script src="../../assets/javascripts/iframe/click.js"></script>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config

data_frame = pd.read_csv(
    "https://github.com/vizzuhq/ipyvizzu/raw/main/docs/showcases/titanic/titanic.csv"
)
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
        {
            "x": ["Count", "Sex", "Survived"],
            "y": None,
            "coordSystem": "polar",
        }
    )
)
```
