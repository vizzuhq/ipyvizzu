<p align="center">
  <a href="https://github.com/vizzuhq/vizzu-lib">
    <img src="https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>ipyvizzu</b> - Jupyter notebook integration of Vizzu.</p>
  <p align="center">
    <a href="https://ipyvizzu.vizzuhq.com/doc.html">Tutorial</a>
    · <a href="http://ipyvizzu.vizzuhq.com/examples/examples.html">Examples</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu.svg)](https://badge.fury.io/py/ipyvizzu)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu/actions/workflows/cicd.yml)

# About The Project

ipyvizzu is the [Jupyter Notebook](https://jupyter.org/) integration of [Vizzu](https://github.com/vizzuhq/vizzu-lib). ipyvizzu enables data scientists and analysts to utilize animation for storytelling with data using Python.

Similar to Vizzu, which is a free, open-source Javascript/C++ library, ipyvizzu also utilizes a generic dataviz engine that generates many types of charts and seamlessly animates between them. It is designed for building animated data stories as it enables showing different perspectives of the data that the viewers can easily follow.

Main features:
- Designed with animation in focus;
- Defaults based on data visualization guidelines;
- Works with Pandas dataframe, also JSON and inline data input is available;
- Auto scrolling to keep the actual chart in position while executing multiple cells.

# Installation

ipyvizzu requires `IPython` and `pandas` packages.
However you can use it only in Jupyter Notebook therefore `notebook` project has to be installed.

```sh
pip install ipyvizzu
pip install notebook
```
You can also use ipyvizzu by locally installing Vizzu, you can find more info about this in the [documentation](https://ipyvizzu.vizzuhq.com/doc.html)

# Usage

ipyvizzu only works in Jupiter Notebook environment.
A notebook cell may contain the following code snippet resulting in the animation below.

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config

data_frame = pd.read_csv("titanic.csv")
data = Data()
data.add_data_frame(data_frame)

chart = Chart(width="640px", height="360px")

chart.animate(data)

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

<p align="center">
  <img src="https://github.com/vizzuhq/ipyvizzu/raw/main/docs/assets/ipyvizzu-promo.gif" alt="ipyvizzu" />
</p>

Visit our [documentation](https://ipyvizzu.vizzuhq.com/doc.html) site for more details and a step-by-step tutorial into ipyvizzu,
or check out the [example gallery](http://ipyvizzu.vizzuhq.com/examples/examples.html).

# Tools Support

ipyvizzu can also be used in a wide variety of environments! Check out the examples below to see the supported functions:

- [Colab example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/colab.md) and interactive demo [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19H4etDPuSyJ3LNJbshsfEAnxxwjJgZgq?usp=sharing)

- [Databricks example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/databricks.md)

- [DataCamp example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/datacamp.md)

- [Deepnote example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/deepnote.md) and interactive demo [![View in Deepnote](https://deepnote.com/static/buttons/view-in-deepnote.svg)](https://deepnote.com/workspace/david-andras-vegh-bc03-79fd3a98-abaf-40c0-8b52-9f3e438a73fc/project/ipyvizzu-demo-dff3c2c3-f212-434e-8fa1-23d843c52fe3/%2Fipyvizzu_demo.ipynb)

- [JupyterLite example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/jupyterlite.md)

- [Kaggle example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/kaggle.md) and interactive demo [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/dvidandrsvgh/ipyvizzu-demo)

- [Mercury example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/mercury.md) and interactive demo [![Open in Mercury](https://raw.githubusercontent.com/mljar/mercury/main/docs/media/open_in_mercury.svg)](https://huggingface.co/spaces/veghdev/ipyvizzu-demo)

- [Mode example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/mode.md)

- [Panel example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/panel.md)

- [Streamlit example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/streamlit.md)

- [VSCode Python example](https://github.com/vizzuhq/ipyvizzu/blob/main/docs/examples/environments/vscode.md)


# Contributing

We welcome contributions to the project, visit our [contributing guide](https://github.com/vizzuhq/ipyvizzu/blob/main/CONTRIBUTING.md) for further info.

# Contact

* Join our Slack if you have any questions or comments: [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
* Drop us a line at hello@vizzuhq.com
* Follow us on twitter: [https://twitter.com/VizzuHQ](https://twitter.com/VizzuHQ)

# License

Copyright © 2022 [Vizzu Kft.](https://vizzuhq.com).

Released under the [Apache 2.0 License](https://github.com/vizzuhq/ipyvizzu/blob/main/LICENSE).
