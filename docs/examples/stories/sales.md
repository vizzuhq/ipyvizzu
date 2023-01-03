---
csv_url: ./sales/sales.csv
---

# Sales of Shoes

<div id="example_01"></div>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

data_frame = pd.read_csv("./sales/sales.csv", dtype={"tenure": str})
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

<script src="./sales/sales.js"></script>
