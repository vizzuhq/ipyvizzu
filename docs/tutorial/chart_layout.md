---
csv_url: ../../assets/data/music_data.csv
---

# Chart layout

`ipyvizzu` has three separate parts of the chart layout: the plot area that
contains the chart, the title containing the chart title on the top, and the
legend on the left. `ipyvizzu` automatically hides the legend when it’s
unnecessary to show it. When the title is not in use, `ipyvizzu` hides that part
automatically as well. Each of these parts have their own paddings on all four
sides that adjust to the chart size by default, but can also be set with the
appropriate settings in the `Style` object. All size parameters can be set in
pixel, percentage and em.

We add different background colors to the parts of the layout to show how they
are aligned.

<div id="tutorial_01"></div>

{% include-markdown "tutorial/assets/setup/setup_c.md" %}

```python
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

Setting the width of the legend.

<div id="tutorial_02"></div>

```python
chart.animate(Style({"legend": {"width": 50}}))
```

Setting the legend width back to its default value.

<div id="tutorial_03"></div>

```python
chart.animate(Style({"legend": {"width": None}}))
```

Changing the title paddings. By default, the title is horizontally centered
above the chart. In this example, we set the title’s left padding, resulting in
the text moving to the right.

<div id="tutorial_04"></div>

```python
chart.animate(
    Style(
        {
            "title": {
                "paddingTop": 20,
                "paddingBottom": 20,
                "paddingLeft": 200,
            }
        }
    )
)
```

Setting the title paddings back to their default values.

<div id="tutorial_05"></div>

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

Changing the paddings of the plot area to position the plot. The texts on the
axes are drawn on the padding of the plot and not the plot itself.

<div id="tutorial_06"></div>

```python
chart.animate(
    Style({"plot": {"paddingLeft": 100, "paddingRight": 100}})
)
```

Setting the plot paddings back to their default values.

<div id="tutorial_07"></div>

```python
chart.animate(
    Style({"plot": {"paddingLeft": None, "paddingRight": None}})
)
```

<script src="../chart_layout.js"></script>
