# Streamlit

There is a new `Streamlit` component,
[streamlit-vizzu](https://github.com/vizzu-streamlit/streamlit-vizzu), that
allow you to interact with an `ipyvizzu` chart within a `Streamlit` app without
the chart being redrawn on every interaction.

## Features

The features of `ipyvizzu` that are available in `Streamlit` are marked with a
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

## Installation

Run the following command in your command line in order to install `ipyvizzu`
(visit [Installation chapter](../../installation.md) for more options and
details).

```sh
pip install ipyvizzu pandas streamlit
```

## Sample

Try `ipyvizzu` in `Streamlit` with the following sample.

```python
# import streamlit, pandas and ipyvizzu

from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


def create_chart():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

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

    # return generated html code

    return chart._repr_html_()


# generate Chart's html code

CHART = create_chart()


# display Chart

html(CHART, width=650, height=370)
```

Place the above code blocks into a python file (for example called
`ipyvizzu_example.py`) and run the following command in your command line in
order to try it.

```sh
streamlit run ipyvizzu_example.py
```

Check the [Tutorial](../../tutorial/index.md) for more info.
