---
csv_url: ../data/music_data.csv
---

# Channels & legend

Besides the x-axis and the y-axis, there are five more channels in ipyvizzu you
can use to visualize your data. Similarly to the axes you can put any number of
dimensions and/or one measure to a channel. In the following example the four
most commonly used channels are shown. The fifth, noop channel is introduced
later in the
[Without coordinates & noop channel](./without_coordinates_noop_channel.md)
chapter.

Data on the label channel will be written on the markers on the chart. ipyizzu
automatically determines the best way to position these labels, but you can set
them differently with the style object introduced in the
[Color palette & fonts](./color_palette_fonts.md) chapter.

<div id="tutorial_01"></div>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config


data_frame = pd.read_csv("../data/music_data.csv")
data = Data()
data.add_data_frame(data_frame)


chart = Chart()

chart.animate(data)

chart.animate(
    Config(
        {
            "channels": {"y": {"set": "Popularity"}, "x": {"set": "Genres"}},
            "title": "Label",
        }
    )
)

chart.animate(Config({"channels": {"label": {"attach": "Popularity"}}}))
```

The lightness channel sets the lightness of the markers. In this case the same
measure (Popularity) is added to it that is on the y-axis, meaning that columns’
height and lightness represent the same values. The legend for the lightness
channel is turned on using the legend property.

**Note:** This is an example when we explicitly instruct ipyvizzu to show the
legend. By default ipyvizzu automatically shows/hides the legend when it's
necessary. You can also turn it off with the `legend`: `None` command or set
back to automatic mode with `legend`: `auto`.

<div id="tutorial_02"></div>

```python
chart.animate(Config({"title": "Lightness - legend on"}))

chart.animate(
    Config(
        {
            "channels": {"lightness": {"attach": "Popularity"}},
            "legend": "lightness",
        }
    )
)
```

The color channel sets the color of the markers. The same dimension (Genres) is
put on it that is on the x-axis resulting in each bar having a different color.
If a measure is put on the color channel, a color range will be used.

**Note:** The value on the lightness channel is removed in this step as it
doesn’t make sense to use it together with the color channel in this case.

<div id="tutorial_03"></div>

```python
chart.animate(Config({"title": "Color"}))

chart.animate(
    Config(
        {
            "channels": {"color": {"attach": "Genres"}},
            "legend": "color",
        }
    )
)
```

The size channel sets the size of the markers if the geometry is circle - where
size sets the radius of the circles - or line - where size determines line
width. It is ignored when using rectangle or area geometry. This is why we
change the geometry to circle in the example.

<div id="tutorial_04"></div>

```python
chart.animate(Config({"title": "Size - change of geometry required"}))

chart.animate(
    Config(
        {
            "channels": {"size": {"set": "Popularity"}},
            "geometry": "circle",
        }
    )
)
```

<script src="./channels_legend.js"></script>
