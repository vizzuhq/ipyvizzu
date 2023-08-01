# Databricks

## Features

The features of `ipyvizzu` that are available in `Databricks` are marked with a
green check.

- [x]  Change the url of `Vizzu` (`vizzu`)
- [x]  Change the width of the `Chart` (`width`)
- [x]  Change the height of the `Chart` (`height`)
- [x]  Use scroll into view (`scroll_into_view`=`True`)

Display features:

- [x]  Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`)
- [ ]  Display all animations after `show` method called
  (`display`=`DisplayTarget.MANUAL`)
- [ ]  Automatically display all animations after the first cell
  (`display`=`DisplayTarget.BEGIN`)
- [ ]  Automatically display all animations after the currently running cell
  (`display`=`DisplayTarget.ACTUAL`)
- [ ]  Automatically display all animations after the last running cell
  (`display`=`DisplayTarget.END`)
- [ ]  Rerun any cell without rerun the first cell
  (`display`!=`DisplayTarget.MANUAL`)

Check [Chart settings chapter](../../tutorial/chart_settings.md) for more
details.

## Live example

[Open in Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/808850182010194/3745120999164565/1947355309752283/latest.html)

## Installation

Place the following code into a notebook cell in order to install `ipyvizzu`
(visit [Installation chapter](../../installation.md) for more options and
details).

```
!pip install ipyvizzu
```

## Sample

Try `ipyvizzu` in `Databricks` with the following sample.

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
df = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/latest/showcases/titanic/titanic.csv"
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


# display Chart with _repr_html_ method (display=DisplayTarget.MANUAL)

chart
```

Check the [Tutorial](../../tutorial/index.md) for more info.
