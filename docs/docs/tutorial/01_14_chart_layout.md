# Chart layout

ipyvizzu has three separate parts of the chart layout: the plot area that
contains the chart, the title containing the chart title on the top, and the
legend on the left. ipyvizzu automatically hides the legend when it’s
unnecessary to show it. When the title is not in use, ipyvizzu hides that part
automatically as well. Each of these parts have their own paddings on all four
sides that adjust to the chart size by default, but can also be set with the
appropriate settings in the style object. All size parameters can be set in
pixel, percentage and em.

We add different background colors to the parts of the layout to show how they
are aligned.

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style


data_frame = pd.read_csv("./music_data.csv")
data = Data()
data.add_data_frame(data_frame)


chart = Chart()

chart.animate(data)

chart.animate(
    Config(
        {
            "channels": {
                "y": {"set": ["Popularity", "Kinds"]},
                "x": {"set": "Genres"},
            },
            "label": {"attach": "Popularity"},
            "color": {"set": "Kinds"},
            "title": "Plot, title and legend background",
        }
    )
)

chart.animate(
    Style(
        {
            "title": {"backgroundColor": "#A0A0A0"},
            "plot": {"backgroundColor": "#D2D2D2"},
            "legend": {"backgroundColor": "#808080"},
        }
    )
)
```

<div id="tutorial_01"></div>

Setting the width of the legend.

```python
chart.animate(Config({"title": "Legend width"}))

chart.animate(Style({"legend": {"width": 50}}))
```

<div id="tutorial_02"></div>

Setting the legend width back to its default value.

```python
chart.animate(Style({"legend": {"width": None}}))
```

<div id="tutorial_03"></div>

Changing the title paddings. By default, the title is horizontally centered
above the chart. In this example, we set the title’s left padding, resulting in
the text moving to the right.

```python
chart.animate(Config({"title": "Title padding"}))

chart.animate(
    Style(
        {"title": {"paddingTop": 20, "paddingBottom": 20, "paddingLeft": 200}}
    )
)
```

<div id="tutorial_04"></div>

Setting the title paddings back to their default values.

```python
chart.animate(
    Style(
        {
            "title": {
                "paddingTop": None,
                "paddingBottom": None,
                "paddingLeft": None,
            }
        }
    )
)
```

<div id="tutorial_05"></div>

Changing the paddings of the plot area to position the plot. The texts on the
axes are drawn on the padding of the plot and not the plot itself.

```python
chart.animate(Config({"title": "Plot padding"}))

chart.animate(Style({"plot": {"paddingLeft": 100, "paddingRight": 100}}))
```

<div id="tutorial_06"></div>

Setting the plot paddings back to their default values.

```python
chart.animate(Style({"plot": {"paddingLeft": None, "paddingRight": None}}))
```

<div id="tutorial_07"></div>

<script src="./01_14_chart_layout.js"></script>
