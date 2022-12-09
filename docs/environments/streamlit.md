# Streamlit

You can use ipyvizzu in Streamlit with the following restrictions:

- [x] Change the url of Vizzu (`vizzu`)
- [x] Change the width of the chart (`width`)
- [x] Change the height of the chart (`height`)
- [x] Use scroll into view (`scroll_into_view`=`True`)

Dislay restrictions:

- [x] Display all animations after `_repr_html_` method called (`display`=`DisplayTarget.MANUAL`)
- [ ] Display all animations after `show` method called (`display`=`DisplayTarget.MANUAL`)
- [ ] Automatically display all animations after the first cell (`display`=`DisplayTarget.BEGIN`)
- [ ] Automatically display all animations after the currently running cell (`display`=`DisplayTarget.ACTUAL`)
- [ ] Automatically display all animations after the last running cell (`display`=`DisplayTarget.END`)
- [ ] Rerun any cell without rerun the first cell (`display`!=`DisplayTarget.MANUAL`)

## Installation

Run the following command in your command line in order to install ipyvizzu (for more installation options and details see [Installation chapter](../installation.md) of our documentation site).

```sh
pip install ipyvizzu streamlit
```

## Example

Below you can see an example, place the following code blocks into a python file in order to try it in Streamlit.

For more information regarding to how to use ipyvizzu-story please check [Tutorial chapter](../tutorial/index.md) of our documentation site.

```python
# import streamlit, pandas and ipyvizzu

from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


def create_chart():

    # initialize Chart

    chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)

    # create and add data to Chart

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

    # return generated html code

    return chart._repr_html_()


# generate Chart's html code

CHART = create_chart()


# display Chart

html(CHART, width=650, height=370)
```

## Try it!

Place the above code blocks into a python file (for example called `ipyvizzu_example.py`)
and run the following command in your command line in order to try it.

```sh
streamlit run ipyvizzu_example.py
```
