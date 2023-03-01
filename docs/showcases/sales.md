---
csv_url: ./sales.csv
---

# Sales of Shoes

<div class="showcase">
  <iframe  id="showcase" src='./main.html' width="100%" scrolling="no" frameborder="0"></iframe>
</div>
<script src="../../assets/javascripts/iframe/autoheight.js"></script>
<script src="../../assets/javascripts/iframe/click.js"></script>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

data_frame = pd.read_csv("./sales.csv")
data = Data()
data.add_data_frame(data_frame)

chart = Chart()

chart.animate(data)

chart.animate(
    Data.filter("record['Product'] == 'Shoes'"),
    Config(
        {
            "x": "Region",
            "y": ["Sales", "Product"],
            "label": "Sales",
            "color": "Product",
            "title": "Sales of Shoes",
        }
    ),
)

chart.animate(
    Data.filter(
        "record['Product'] == 'Shoes' || record['Product'] == 'Handbags'"
    ),
    Config({"title": "Sales of Shoes & Handbags"}),
    delay=1,
)

chart.animate(
    Data.filter("record['Product'] != 'Accessories'"),
    Config({"title": "Sales of Shoes, Handbags & Gloves"}),
    delay=1,
)

chart.animate(
    Data.filter(None),
    Config({"title": "Sales of All Products"}),
    delay=1,
)

chart.animate(
    Config(
        {
            "y": ["Revenue [$]", "Product"],
            "label": "Revenue [$]",
            "title": "Revenue of All Products",
        }
    ),
    delay=1,
)

chart.animate(
    Config({"x": ["Region", "Revenue [$]"], "y": "Product"}), delay=2
)

chart.animate(Config({"x": "Revenue [$]", "y": "Product"}))

chart.animate(
    Config({"coordSystem": "polar", "sort": "byValue"}), delay=1
)
```
