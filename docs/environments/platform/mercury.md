# Mercury/mljar

## Features

The features of `ipyvizzu` that are available in `Mercury/mljar` are marked with
a green check.

- [x] Change the url of `Vizzu` (`vizzu`)
- [x] Change the width of the `Chart` (`width`)
- [x] Change the height of the `Chart` (`height`)
- [x] Use scroll into view (`scroll_into_view`=`True`)

Dislay features:

- [ ] Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x] Display all animations after `show` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x] Automatically display all animations after the first cell
  (`display`=`DisplayTarget.BEGIN`)
- [x] Automatically display all animations after the currently running cell
  (`display`=`DisplayTarget.ACTUAL`)
- [x] Automatically display all animations after the last running cell
  (`display`=`DisplayTarget.END`)
- [ ] Rerun any cell without rerun the first cell
  (`display`!=`DisplayTarget.MANUAL`)

Check [Chart settings chapter](../../tutorial/chart_settings.md) for more
details.

## Installation

Add `ipyvizzu` to `requirements.txt`.

```
python-dotenv
pandas
mljar-mercury
ipyvizzu
```

## Sample

Try `ipyvizzu` in `Mercury/mljar` with the following sample.

```
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
# configure default choice

gender = "male"
```

```python
# import pandas and ipyvizzu

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


# initialize Chart

chart = Chart(
    width="640px", height="360px"
)  # or Chart(width="640px", height="360px", display=DisplayTarget.ACTUAL)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.BEGIN)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.END)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)


# add data to Chart

data = Data()
data_frame = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/latest/showcases/titanic/titanic.csv"
)
data.add_data_frame(data_frame)

chart.animate(data)


# add config to Chart

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


# add style to Chart

chart.animate(Style({"title": {"fontSize": 35}}))


# filter data by the selected gender to Chart

data_filter = Data.filter(f"record['Sex'] == '{gender}'")
chart.animate(data_filter)


# display Chart with show method (display=DisplayTarget.MANUAL)

# chart.show()
```

Check the [Tutorial](../../tutorial/index.md) for more info.
