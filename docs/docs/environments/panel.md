# Panel

You can use ipyvizzu in Panel with the following restrictions:

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
pip install ipyvizzu panel
```

## Example

Below you can see an example, place the following code blocks into a python file in order to try it in Panel.

For more information regarding to how to use ipyvizzu-story please check [Tutorial chapter](../tutorial.md) of our documentation site.

```python
# import panel, pandas and ipyvizzu

import panel as pn
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


def create_chart():

    # initialize chart

    chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)

    # create and add data to Chart

    data = Data()
    data_frame = pd.read_csv(
        "https://github.com/vizzuhq/ipyvizzu/raw/main/docs/examples/stories/titanic/titanic.csv"
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

    # return Chart

    return chart


# create Chart

CHART = create_chart()


# display Chart

pn.extension(sizing_mode="stretch_width", template="fast")

pn.state.template.param.update(
    title="ipyvizzu",
)

pn.pane.Markdown(
    """
# Panel demo with ipyvizzu
"""
).servable()

pn.pane.HTML(CHART, height=370, sizing_mode="stretch_both").servable()
```

## Try it!

Place the above code blocks into a python file (for example called `ipyvizzu_example.py`)
and run the following command in your command line in order to try it.

```sh
panel serve ipyvizzu_example.py  # --autoreload
```
