# Mercury

You can use ipyvizzu in Mercury with the following restrictions:

| Function                                                                                   | Supported          |
| ------------------------------------------------------------------------------------------ | ------------------ |
| Rerun individual cells without rerun the chart initialization cell (if display!="manual")  | :x:                |
|                                                                                            |                    |
| Constructor arguments:                                                                     |                    |
| Change the url of Vizzu (vizzu)                                                            | :white_check_mark: |
| Change the width of the chart (width)                                                      | :white_check_mark: |
| Change the height of the chart (height)                                                    | :white_check_mark: |
| Automatically display all animations after the constructor's cell (display="begin")        | :white_check_mark: |
| Automatically display animation after the currently running cell (display="actual")        | :white_check_mark: |
| Automatically display all animations after the last running cell (display="end")           | :white_check_mark: |
| Manually display all animations after `show()` method called (display="manual")            | :white_check_mark: |
| Manually display all animations after `_repr_html_()` method called (display="manual")     | :x:                |
|                                                                                            |                    |
| Properties:                                                                                |                    |
| Scroll into view (scroll_into_view=True)                                                   | :white_check_mark: |

Try ipyvizzu with this working example below (it is not necessary to put the code into different cells):

```
# cell 0
# configure application

---
title: ipyvizzu demo
description: ipyvizzu mercury demo
show-code: False
params:
params:
    gender:
        input: select
        label: select the gender
        choices: [male, female]
        multi: False
---
```

```python
# cell 1
# configure default value

gender = 'male'
```

```python
# cell 2
# import pandas and ipyvizzu and initialize chart

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

chart = Chart(width="640px", height="360px")
# chart = Chart(width="640px", height="360px", display=DisplayTarget.BEGIN)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.ACTUAL)  # default
# chart = Chart(width="640px", height="360px", display=DisplayTarget.END)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)
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
# filter data by the selected gender

data_filter = Data.filter(f"record['Sex'] == '{gender}'")
chart.animate(data_filter)
```

```python
# cell 6
# display chart with show() method if display=DisplayTarget.MANUAL

# chart.show()
```
