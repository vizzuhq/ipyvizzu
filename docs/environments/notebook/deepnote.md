# Deepnote

## Features

The features of `ipyvizzu` that are available in `Deepnote` are marked with a
green check.

- [x] Change the url of `Vizzu` (`vizzu`)
- [x] Change the width of the `Chart` (`width`)
- [x] Change the height of the `Chart` (`height`)
- [x] Use scroll into view (`scroll_into_view`=`True`)

Dislay features:

- [x] Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x] Display all animations after `show` method called
  (`display`=`DisplayTarget.MANUAL`)
- [ ] Automatically display all animations after the first cell
  (`display`=`DisplayTarget.BEGIN`)
- [ ] Automatically display all animations after the currently running cell
  (`display`=`DisplayTarget.ACTUAL`)
- [ ] Automatically display all animations after the last running cell
  (`display`=`DisplayTarget.END`)
- [ ] Rerun any cell without rerun the first cell
  (`display`!=`DisplayTarget.MANUAL`)

Check [Chart settings chapter](../../tutorial/chart_settings.md) for more
details.

## Live example

[![View in Deepnote](https://deepnote.com/static/buttons/view-in-deepnote.svg)](https://deepnote.com/workspace/david-andras-vegh-bc03-79fd3a98-abaf-40c0-8b52-9f3e438a73fc/project/ipyvizzu-demo-dff3c2c3-f212-434e-8fa1-23d843c52fe3/%2Fipyvizzu_demo.ipynb)

## Installation

Place the following code into a notebook cell in order to install `ipyvizzu`
(visit [Installation chapter](../../installation.md) for more options and
details).

```
!pip install ipyvizzu
```

## Sample

Try `ipyvizzu` in `Deepnote` with the following sample.

```python
# import pandas and ipyvizzu

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


# initialize Chart

chart = Chart(
    width="640px", height="360px", display=DisplayTarget.MANUAL
)


# add data to Chart

data = Data()
data_frame = pd.read_csv(
    "https://github.com/vizzuhq/ipyvizzu/raw/main/"
    + "docs/examples/stories/titanic/titanic.csv"
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


# display Chart with show or _repr_html_ method (display=DisplayTarget.MANUAL)

chart.show()
# chart
```

Check the [Tutorial](../../tutorial/index.md) for more info.
