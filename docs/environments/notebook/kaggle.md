# Kaggle

## Features

The features of `ipyvizzu` that are available in `Kaggle` are marked with a
green check.

- [x]  Change the url of `Vizzu` (`vizzu`)
- [x]  Change the width of the `Chart` (`width`)
- [x]  Change the height of the `Chart` (`height`)
- [x]  Use scroll into view (`scroll_into_view`=`True`)

Display features:

- [x]  Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x]  Display all animations after `show` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x]  Automatically display all animations after the first cell
  (`display`=`DisplayTarget.BEGIN`)
- [x]  Automatically display all animations after the currently running cell
  (`display`=`DisplayTarget.ACTUAL`)
- [x]  Automatically display all animations after the last running cell
  (`display`=`DisplayTarget.END`)
- [x]  Rerun any cell without rerun the first cell
  (`display`!=`DisplayTarget.MANUAL`)

Check [Chart settings chapter](../../tutorial/chart_settings.md) for more
details.

## Live example

[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/dvidandrsvgh/ipyvizzu-demo)

## Installation

Place the following code into a notebook cell in order to install `ipyvizzu`
(visit [Installation chapter](../../installation.md) for more options and
details).

```
!pip install ipyvizzu pandas
```

## Sample

Try `ipyvizzu` in `Kaggle` with the following sample.

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
df = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/xIPYVIZZU_MINOR_VERSIONx/showcases/titanic/titanic.csv"
)
data.add_df(df)

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

# chart.show()
# chart
```

Check the [Tutorial](../../tutorial/index.md) for more info.
