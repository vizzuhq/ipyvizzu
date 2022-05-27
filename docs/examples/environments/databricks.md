# databricks

You can use ipyvizzu in databricks with the following restrictions:

| Function                                                                                | Supported          |
| --------------------------------------------------------------------------------------- | ------------------ |
| Constructor arguments:                                                                  |                    |
| Change the url of vizzu (vizzu)                                                         | :white_check_mark: |
| Change the width of the chart (width)                                                   | :white_check_mark: |
| Change the height of the chart (height)                                                 | :white_check_mark: |
| Automatically display all animations after the constructor's cell (display="begin")     | :x:                |
| Automatically display animation after the currently running cell (display="actual")     | :x:                |
| Automatically display all animations after the last running cell (display="end")        | :x:                |
| Manually display all animations after `show()` method called (display="manual")         | :x:                |
| Manually display all animations after `_repr_html_()` method called (display="manual")  | :white_check_mark: |
|                                                                                         |                    |
| Properties:                                                                             |                    |
| Scroll into view (scroll_into_view=True)                                                | :white_check_mark: |
|                                                                                         |                    |
| Rerun cells without rerun the chart initialization cell                                 | :x:                |

Try ipyvizzu with this working example below (it is not necessary to put the code into different cmds):

```python
# cmd 1
# install ipyvizzu

!pip install ipyvizzu
```

```python
# cmd 2
# import pandas and ipyvizzu and initialize chart

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

chart = Chart(width="640px", height="360px", display="manual")
```

```python
# cmd 3
# add data

data = Data()
data_frame = pd.read_csv('https://github.com/vizzuhq/ipyvizzu/raw/main/docs/examples/stories/titanic/titanic.csv')
data.add_data_frame(data_frame)

chart.animate(data)
```

```python
# cmd 4
# add config

chart.animate(Config({"x": "Count", "y": "Sex", "label": "Count","title":"Passengers of the Titanic"}))
chart.animate(Config({"x": ["Count","Survived"], "label": ["Count","Survived"], "color": "Survived"}))
chart.animate(Config({"x": "Count", "y": ["Sex","Survived"]}))
```

```python
# cmd 5
# add style

chart.animate(Style({"title": {"fontSize": 35}}))
```

```python
# cmd 6
# display chart with _repr_html_() method

chart
```
