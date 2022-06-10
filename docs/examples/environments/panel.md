# Panel

ipyvizzu is partially supported in Panel.
You can use it with the following restrictions:

| Function                                                                                   | Supported          |
| ------------------------------------------------------------------------------------------ | ------------------ |
| Rerun individual cells without rerun the chart initialization cell (if display!="manual")  | :x:                |
|                                                                                            |                    |
| Constructor arguments:                                                                     |                    |
| Change the url of vizzu (vizzu)                                                            | :white_check_mark: |
| Change the width of the chart (width)                                                      | :white_check_mark: |
| Change the height of the chart (height)                                                    | :white_check_mark: |
| Automatically display all animations after the constructor's cell (display="begin")        | :x:                |
| Automatically display animation after the currently running cell (display="actual")        | :x:                |
| Automatically display all animations after the last running cell (display="end")           | :x:                |
| Manually display all animations after `show()` method called (display="manual")            | :x:                |
| Manually display all animations after `_repr_html_()` method called (display="manual")     | :white_check_mark: |
|                                                                                            |                    |
| Properties:                                                                                |                    |
| Scroll into view (scroll_into_view=True)                                                   | :white_check_mark: |

Try ipyvizzu with this working example below:

Create ipyvizzu_demo.py:

```python
# ipyvizzu_demo.py

# import panel, pandas and ipyvizzu

import panel as pn
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style


def create_chart():

    # initialize chart

    chart = Chart(width="640px", height="360px", display="manual")


    # add data

    data = Data()
    data_frame = pd.read_csv("https://github.com/vizzuhq/ipyvizzu/raw/main/docs/examples/stories/titanic/titanic.csv")
    data.add_data_frame(data_frame)

    chart.animate(data)


    # add config

    chart.animate(Config({"x": "Count", "y": "Sex", "label": "Count","title":"Passengers of the Titanic"}))
    chart.animate(Config({"x": ["Count","Survived"], "label": ["Count","Survived"], "color": "Survived"}))
    chart.animate(Config({"x": "Count", "y": ["Sex","Survived"]}))


    # add style

    chart.animate(Style({"title": {"fontSize": 35}}))


    return chart


CHART = create_chart()

pn.extension(sizing_mode="stretch_width", template="fast")

pn.state.template.param.update(
    title="ipyvizzu",
)

pn.pane.Markdown(
"""
# Panel demo with ipyvizzu
"""
).servable()

pn.pane.HTML(CHART, height=370, sizing_mode="stretch_both").servable()
```

Install dependencies and run ipyvizzu_demo.py with Panel.

```sh
pip install ipyvizzu pandas panel

panel serve ipyvizzu_demo.py  # --autoreload
```