# Mercury (mljar)

You can use ipyvizzu in Mercury with the following restrictions:

- [x] Change the url of Vizzu (`vizzu`)
- [x] Change the width of the chart (`width`)
- [x] Change the height of the chart (`height`)
- [x] Use scroll into view (`scroll_into_view`=`True`)

Dislay restrictions:

- [ ] Display all animations after `_repr_html_` method called (`display`=`DisplayTarget.MANUAL`)
- [x] Display all animations after `show` method called (`display`=`DisplayTarget.MANUAL`)
- [x] Automatically display all animations after the first cell (`display`=`DisplayTarget.BEGIN`)
- [x] Automatically display all animations after the currently running cell (`display`=`DisplayTarget.ACTUAL`)
- [x] Automatically display all animations after the last running cell (`display`=`DisplayTarget.END`)
- [ ] Rerun any cell without rerun the first cell (`display`!=`DisplayTarget.MANUAL`)

## Installation

Add ipyvizzu to requirements.txt.

```
python-dotenv
pandas
mljar-mercury
ipyvizzu
```

## Example

Below you can see an example, place the following code blocks into notebook cells in order to try it in Mercury.

For more information regarding to how to use ipyvizzu please check [Tutorial chapter](../../tutorial.md) of our documentation site.

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
```

```python
# add data to Chart

data = Data()
data_frame = pd.read_csv(
    "https://github.com/vizzuhq/ipyvizzu/raw/main/"
    + "docs/examples/stories/titanic/titanic.csv"
)
data.add_data_frame(data_frame)

chart.animate(data)
```

```python
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
```

```python
# add style to Chart

chart.animate(Style({"title": {"fontSize": 35}}))
```

```python
# filter data by the selected gender to Chart

data_filter = Data.filter(f"record['Sex'] == '{gender}'")
chart.animate(data_filter)
```

```python
# display Chart with show method (display=DisplayTarget.MANUAL)

# chart.show()
```

## Try it!

Place the above code blocks into notebook cells in order to try it. [![Open in Mercury](https://raw.githubusercontent.com/mljar/mercury/main/docs/media/open_in_mercury.svg)](https://huggingface.co/spaces/veghdev/ipyvizzu-demo)
