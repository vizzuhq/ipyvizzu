# Flask

## Features

The features of `ipyvizzu` that are available in `Flask` are marked with a green
check.

- [x]  Change the url of `Vizzu` (`vizzu`)
- [x]  Change the width of the `Chart` (`width`)
- [x]  Change the height of the `Chart` (`height`)
- [x]  Use scroll into view (`scroll_into_view`=`True`)

Display features:

- [ ]  Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`) \*
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

\*you can display the `Chart` in other ways, see the sample below

## Installation

Run the following command in your command line in order to install `ipyvizzu`
(visit [Installation chapter](../../installation.md) for more options and
details).

```sh
pip install ipyvizzu pandas flask
```

## Sample

Try `ipyvizzu` in `Flask` with the following sample.

```python
# import flask, pandas and ipyvizzu

import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

from flask import Flask, render_template


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


# display Chart

app = Flask(__name__)
html = chart._repr_html_()


@app.route("/")
def vizzu():
    return render_template("vizzu.html", mychart=html)
```

Place the above code blocks into a python file (for example called
`application.py`), create the html template (`templates/vizzu.html`) with the
following content

```html
<!DOCTYPE html>
<html>
 <body>
  <div class="container">
   <iframe frameborder="0" height="480px" scrolling="no" src="data:text/html, {{ mychart }}" width="800px">
   </iframe>
  </div>
 </body>
</html>

```

and run the following command in your command line in order to try it.

```sh
flask --app application run
```

Check the [Tutorial](../../tutorial/index.md) for more info.
