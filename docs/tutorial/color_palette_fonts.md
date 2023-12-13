---
csv_url: ../../assets/data/music_data.csv
---

# Color palette & fonts

This and the next chapter provide a quick intro to the styling of the charts.
You can either use the `style` property like in the following examples or use
`CSS`. By using `CSS`, it's easier to set the same style for multiple charts on
one page or re-use style settings. `CSS` parameter usage is disabled by default
and can be enabled by `chart.feature("cssProperties", True)`.

The font sizes automatically adjust to the chart size to help readability, and
can also be set separately or for specific groups.

The color palette is changed to the colors we add here. The order of the
dimension’s items in the data set determine which color belongs to which item as
the colors are added one-by-one. If you want to use the same setting via `CSS`,
you should add
`--vizzu-plot-marker-colorPalette: #9355e8FF #123456FF #BDAF10FF;`.

<div id="tutorial_01"></div>

{% include-markdown "tutorial/assets/setup/setup_c.md" %}

```python
chart.animate(
    Style(
        {
            "plot": {
                "marker": {
                    "colorPalette": "#9355e8FF #123456FF #BDAF10FF"
                }
            }
        }
    )
)
```

The actual style settings of the chart can be logged in the browser console via
the `STYLE` property.

```python
chart.log(ChartProperty.STYLE)
```

Changing the title font size will only affect the title; all other font sizes
remain the same. `CSS` version: `--vizzu-title-fontSize: 50;`.

<div id="tutorial_02"></div>

```python
chart.animate(Style({"title": {"fontSize": 50}}))
```

This is how to set the font size back to its default value.

<div id="tutorial_03"></div>

```python
chart.animate(Style({"title": {"fontSize": None}}))
```

In case you change the font size of the whole chart with the top-level
`fontSize` parameter then every font on the chart will grow/shrink
proportionally. The size refers to the font size of the axis labels by default.

<div id="tutorial_04"></div>

```python
chart.animate(Style({"fontSize": 20}))
```

You can reset styles to default on any levels by setting them to `None`.

<div id="tutorial_05"></div>

```python
chart.animate(Style(None))
```

For information on all available style parameters see the [Style](./style.md)
chapter.

<script src="../color_palette_fonts.js"></script>
