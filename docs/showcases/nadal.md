---
csv_url: ./nadal.csv
---

# Rafael Nadal's matches

<div class="showcase">
  <iframe  id="showcase" src="./main.html" width="100%" scrolling="no" frameborder="0"></iframe>
</div>
<script src="../../assets/javascripts/iframe/autoheight.js"></script>
<script src="../../assets/javascripts/iframe/click.js"></script>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

df = pd.read_csv(
    "https://xIPYVIZZU_MINOR_VERSIONx/showcases/nadal/nadal.csv",
    dtype={
        "Year": str,
        "Round": str,
        "Round2": str,
        "Order_GS": str,
        "Order_all": str,
        "Total_GS": str,
        "Top": str,
    },
)
data = Data()
data.add_df(df)

chart = Chart(display=DisplayTarget.END)
chart.animate(data)

chart.animate(
    data.filter("record.Year != 'Total'"),
    Config(
        {
            "x": "Year",
            "y": "Round2",
            "color": {
                "set": "Result_Num",
                "range": {"min": -1, "max": 1},
            },
            "size": None,
            "orientation": "horizontal",
            "geometry": "rectangle",
            "title": "Rafael Nadal's matches at the Roland Garros",
            "legend": "size",
        }
    ),
    Style(
        {
            "title": {
                "paddingTop": 50,
                "paddingBottom": 0,
            },
            "plot": {
                "marker": {
                    "borderWidth": 3,
                    "borderOpacity": 0,
                    "colorPalette": "#1EB55FFF #AD0000FF #AEAEAEFF",
                    "colorGradient": "#AEAEAEFF 0.000000, #AD0000FF 0.500000, #1EB55FFF 1.000000",
                },
                "paddingLeft": 20,
                "paddingBottom": "3.5em",
                "paddingTop": "2.5em",
                "xAxis": {"interlacing": {"color": "#ffffff00"}},
                "yAxis": {"label": {"fontSize": "120%"}},
            },
            "logo": {"width": 100},
        }
    ),
)

chart.animate(
    Config(
        {"lightness": "Won", "title": "Won 112 out of 116 (96.5%)"}
    ),
    Style(
        {"plot": {"marker": {"maxLightness": 0, "minLightness": 0.8}}}
    ),
    delay=4,
)

chart.animate(
    Config(
        {"lightness": "Lost", "title": "Lost 3 times, retired once"}
    ),
    delay=4,
)

chart.animate(
    Config({"lightness": None, "title": ""}),
    Style(
        {
            "plot": {
                "marker": {"maxLightness": None, "minLightness": None}
            }
        }
    ),
    delay=4,
)

chart.animate(
    Config(
        {
            "lightness": "3SetWin",
            "title": "90 wins (80%) in straight sets",
        }
    ),
    Style(
        {"plot": {"marker": {"maxLightness": 0, "minLightness": 0.8}}}
    ),
)

chart.animate(
    Config(
        {
            "lightness": "Straightwin",
            "title": "Won 4 titles without dropping a set",
        }
    ),
    delay=3,
)

chart.animate(
    Config({"lightness": None, "title": ""}),
    Style(
        {
            "plot": {
                "marker": {"maxLightness": None, "minLightness": None}
            }
        }
    ),
    delay=4,
)

chart.animate(
    Config(
        {
            "lightness": "Novak",
            "title": "Played the most times against Djokovic - 10 matches",
        }
    ),
    Style(
        {"plot": {"marker": {"maxLightness": 0, "minLightness": 0.8}}}
    ),
)

chart.animate(
    Config(
        {
            "lightness": "Roger",
            "title": "Second on this list is Federer - with 6 encounters",
        }
    ),
    delay=4,
)

chart.animate(
    Config(
        {
            "lightness": "Final",
            "title": "Rafa won all of his 14 finals",
        }
    ),
    delay=4,
)

chart.animate(
    data.filter("record.Year != 'Total' && record.Round == 'F'"),
    Config(
        {
            "y": {"set": "Round2", "range": {"max": 1, "min": -5}},
            "x": "Count",
            "lightness": None,
            "noop": "Year",
            "label": None,
            "title": "",
        }
    ),
    Style(
        {
            "plot": {
                "marker": {
                    "borderWidth": 0,
                    "colorPalette": "#C6652A #CDA02E #47B0FF #329564 #5C88F2 #91A9B5 #DBC4B1",
                    "maxLightness": None,
                    "minLightness": None,
                    "label": {
                        "position": "center",
                        "format": "dimensionsFirst",
                    },
                },
                "xAxis": {
                    "title": {"color": "#ffffff00"},
                    "label": {"color": "#ffffff00"},
                    "interlacing": {"color": "#ffffff00"},
                },
                "yAxis": {
                    "title": {"color": "#ffffff00"},
                    "label": {"color": "#ffffff00", "fontSize": None},
                },
            }
        }
    ),
    delay=3,
)

chart.animate(
    data.filter(
        """
        record.Year == "Total" &&
        record.Tournament == "Roland Garros" &&
        record.Player == "Nadal"
        """
    ),
    Config(
        {
            "noop": ["Level", "Round2"],
            "label": ["Player", "Tournament", "Count"],
            "y": {"set": ["Player", "Tournament"]},
        }
    ),
    duration=0,
)

chart.animate(Config({"noop": "Level"}), duration=0)

chart.animate(
    data.filter(
        "record.Year == 'Total' && record.Round == 'GS' && record.Top == '1'"
    ),
    Config(
        {
            "y": {
                "set": ["Player", "Tournament", "Level"],
                "range": {"max": None, "min": None},
            },
            "title": "Rafa won the same Grand Slam title the most times",
            "color": "Level",
            "legend": "color",
            "noop": None,
            "sort": "byValue",
        }
    ),
)

chart.animate(
    data.filter('record.Year == "Total" && record.Top == "1"'),
    Config(
        {
            "y": {
                "set": ["Player", "Tournament", "Level"],
                "range": {"max": 19, "min": 7},
            },
            "x": ["Count"],
            "title": "Winning the same ATP title - Rafa is 1st, 2nd, 3rd & 4th!",
        }
    ),
    delay=5,
)

chart.animate(
    data.filter(
        'record.Year == "Total" && record.Round == "GS" && record.Top == "1"'
    ),
    Config(
        {
            "y": {
                "set": ["Player", "Tournament", "Level"],
                "range": {"max": None, "min": None},
            },
            "x": ["Count"],
            "title": "",
            "color": "Level",
        }
    ),
    delay=5,
)

chart.animate(Config({"x": ["Count", "Total_GS"], "label": "Player"}))

chart.animate(
    data.filter("record.Year == 'Total' && record.Round == 'GS'"),
    Config(
        {
            "y": {
                "set": ["Player"],
                "range": {"max": None, "min": None},
            },
            "x": ["Count", "Tournament", "Level", "Total_GS"],
            "title": "Rafa also leads in the number of total Grand Slams won",
        }
    ),
)

chart.animate(
    Config({"label": ["Total_GS"]}),
    Style(
        {
            "plot": {
                "marker": {
                    "label": {
                        "position": "right",
                        "filter": "color(#666666FF)",
                    }
                }
            }
        }
    ),
)
```
