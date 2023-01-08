# Mode

You can use ipyvizzu in Mode with the following restrictions:

- [x] Change the url of Vizzu (`vizzu`)
- [x] Change the width of the chart (`width`)
- [x] Change the height of the chart (`height`)
- [x] Use scroll into view (`scroll_into_view`=`True`)

Dislay restrictions:

- [x] Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`)
- [ ] Display all animations after `show` method called
  (`display`=`DisplayTarget.MANUAL`)
- [ ] Automatically display all animations after the first cell
  (`display`=`DisplayTarget.BEGIN`)
- [ ] Automatically display all animations after the currently running cell
  (`display`=`DisplayTarget.ACTUAL`)
- [ ] Automatically display all animations after the last running cell
  (`display`=`DisplayTarget.END`)
- [ ] Rerun any cell without rerun the first cell
  (`display`!=`DisplayTarget.MANUAL`)

## Installation

Place the following code into a notebook cell in order to install ipyvizzu
(visit [Installation chapter](../../installation.md) for more options and
details).

```
!pip install ipyvizzu -t "/tmp" > /dev/null 2>&1
```

## Example

Below you can see an example, place the following code blocks into notebook
cells in order to try it in Mode.

For more information regarding to how to use ipyvizzu please check
[Tutorial chapter](../../tutorial/index.md) of our documentation site.

```python
# import pandas and ipyvizzu

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


# initialize Chart

chart = Chart(
    width="640px", height="360px", display=DisplayTarget.MANUAL
)
```

```python
# add data to Chart

data = Data()
data_frame = pd.read_csv(
    "https://github.com/vizzuhq/ipyvizzu/raw/main/"
    + "docs/examples/stories/titanic/titanic.csv"
)
data.add_data_frame(data_frame)

chart.animate(data)
```

```python
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
```

```python
# add style to Chart

chart.animate(Style({"title": {"fontSize": 35}}))
```

```python
# display Chart with _repr_html_ method (display=DisplayTarget.MANUAL)

chart
```

## Try it!

Place the above code blocks into notebook cells in order to try it.
