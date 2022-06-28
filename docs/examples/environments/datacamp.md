# databricks

You can use ipyvizzu in databricks with the following restrictions:

| Function                                                                                   | Supported          |
| ------------------------------------------------------------------------------------------ | ------------------ |
| Rerun individual cells without rerun the chart initialization cell (if display!="manual")  | :white_check_mark: |
|                                                                                            |                    |
| Constructor arguments:                                                                     |                    |
| Change the url of Vizzu (vizzu)                                                            | :white_check_mark: |
| Change the width of the chart (width)                                                      | :white_check_mark: |
| Change the height of the chart (height)                                                    | :white_check_mark: |
| Automatically display all animations after the constructor's cell (display="begin")        | :white_check_mark: |
| Automatically display animation after the currently running cell (display="actual")        | :white_check_mark: |
| Automatically display all animations after the last running cell (display="end")           | :white_check_mark: |
| Manually display all animations after `show()` method called (display="manual")            | :white_check_mark: |
| Manually display all animations after `_repr_html_()` method called (display="manual")     | :white_check_mark: |
|                                                                                            |                    |
| Properties:                                                                                |                    |
| Scroll into view (scroll_into_view=True)                                                   | :white_check_mark: |

Try ipyvizzu with this working example below (it is not necessary to put the code into different cells):

```python
# cell 1
# install ipyvizzu

!pip install ipyvizzu
```

```python
# cell 2
# import pandas and ipyvizzu and initialize chart

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

chart = Chart(width="640px", height="360px")
# chart = Chart(width="640px", height="360px", display="begin")
# chart = Chart(width="640px", height="360px", display="actual")  # default
# chart = Chart(width="640px", height="360px", display="end")
# chart = Chart(width="640px", height="360px", display="manual")
```

```python
# cell 3
# add data

data = Data()
data_frame = pd.read_csv("https://github.com/vizzuhq/ipyvizzu/raw/main/docs/examples/stories/titanic/titanic.csv")
data.add_data_frame(data_frame)

chart.animate(data)
```

```python
# cell 4
# add config

chart.animate(Config({"x": "Count", "y": "Sex", "label": "Count","title":"Passengers of the Titanic"}))
chart.animate(Config({"x": ["Count","Survived"], "label": ["Count","Survived"], "color": "Survived"}))
chart.animate(Config({"x": "Count", "y": ["Sex","Survived"]}))
```

```python
# cell 5
# add style

chart.animate(Style({"title": {"fontSize": 35}}))
```

```python
# cell 6
# display chart with show() or _repr_html_() method if display="manual"

# chart.show()
# chart
```
