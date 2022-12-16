<p align="center">
  <a href="https://github.com/vizzuhq/ipyvizzu">
    <img src="https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>ipyvizzu</b> Build animated charts in many environments with a simple Python syntax</p>
  <p align="center">
    <a href="https://ipyvizzu.vizzuhq.com/doc.html">Tutorial</a>
    · <a href="http://ipyvizzu.vizzuhq.com/examples/examples.html">Examples</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu.svg)](https://badge.fury.io/py/ipyvizzu)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipyvizzu.svg)](https://anaconda.org/conda-forge/ipyvizzu)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu/actions/workflows/cicd.yml)

# About The Project

ipyvizzu is an animated charting tool for [Jupyter](https://jupyter.org),
[Google Colab](https://colab.research.google.com),
[Databricks](https://docs.databricks.com/notebooks),
[Kaggle](https://www.kaggle.com/code) and [Deepnote](https://deepnote.com)
notebooks among other platforms. ipyvizzu enables data scientists and analysts
to utilize animation for storytelling with data using Python. It's built on the
open-source Javascript/C++ charting library
[Vizzu](https://github.com/vizzuhq/vizzu-lib)

**There is a new extension of ipyvizzu,
[ipyvizzu-story](https://github.com/vizzuhq/ipyvizzu-story)** with which the
animated charts can be presented right from the notebooks. Since
ipyvizzu-story's syntax is a bit different to ipyvizzu's, we suggest you to
start from the [ipyvizzu-story repo](https://github.com/vizzuhq/ipyvizzu-story)
if you're interested in using animated charts to present your findings live or
to share your presentation as an HTML file.

Similarly to Vizzu, ipyvizzu utilizes a generic dataviz engine that generates
many types of charts and seamlessly animates between them. It is designed for
building animated data stories as it enables showing different perspectives of
the data that the viewers can easily follow.

Main features:

- Designed with animation in focus;
- Defaults based on data visualization guidelines;
- Works with Pandas dataframe, while also JSON and inline data input is
  available;
- Auto scrolling feature to keep the actual chart in position while executing
  multiple cells.

# Installation

ipyvizzu requires the `IPython`, `jsonschema` and `pandas` packages.

```sh
pip install ipyvizzu
```

You can also use ipyvizzu by locally installing Vizzu, you can find more info
about this in the [documentation](https://ipyvizzu.vizzuhq.com/doc.html)

# Usage

You can create the animation below with the following code snippet.

<p align="center">
  <img src="https://github.com/vizzuhq/ipyvizzu/raw/main/docs/assets/ipyvizzu-promo.gif" alt="ipyvizzu" />
</p>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config

data_frame = pd.read_csv(
    "https://raw.githubusercontent.com/vizzuhq/ipyvizzu/main/docs/examples/stories/titanic/titanic.csv"
)
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

# Documentation

Visit our [documentation](https://ipyvizzu.vizzuhq.com/doc.html) site for more
details and a step-by-step tutorial into ipyvizzu or check out our
[example gallery](http://ipyvizzu.vizzuhq.com/examples/examples.html).

## Environment support

ipyvizzu can be used in a wide variety of environments, visit
[Environments chapter](https://vizzuhq.github.io/ipyvizzu/docs/environments/index.html)
of our documentation site for more details.

- Jupyter/IPython
  - [Jupyter Notebook](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/jupyternotebook.html)
  - [Colab](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/colab.html)
    [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19H4etDPuSyJ3LNJbshsfEAnxxwjJgZgq?usp=sharing)
  - [Databricks](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/databricks.html)
  - [DataCamp](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/datacamp.html)
  - [Deepnote](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/deepnote.html)
    [![View in Deepnote](https://deepnote.com/static/buttons/view-in-deepnote.svg)](https://deepnote.com/workspace/david-andras-vegh-bc03-79fd3a98-abaf-40c0-8b52-9f3e438a73fc/project/ipyvizzu-demo-dff3c2c3-f212-434e-8fa1-23d843c52fe3/%2Fipyvizzu_demo.ipynb)
  - [JupyterLab](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/jupyterlab.html)
  - [JupyterLite](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/jupyterlite.html)
  - [Kaggle](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/kaggle.html)
    [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/dvidandrsvgh/ipyvizzu-demo)
  - [Mercury/mljar](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/mercury.html)
    [![Open in Mercury](https://raw.githubusercontent.com/mljar/mercury/main/docs/media/open_in_mercury.svg)](https://huggingface.co/spaces/veghdev/ipyvizzu-demo)
  - [Mode](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/mode.html)
  - [Noteable](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/noteable.html)
  - [Voilà](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/voila.html)
  - [VSCode Python](https://vizzuhq.github.io/ipyvizzu/docs/environments/jupyter/vscode.html)
- [Streamlit](https://vizzuhq.github.io/ipyvizzu/docs/environments/streamlit.html)
- [Panel](https://vizzuhq.github.io/ipyvizzu/docs/environments/panel.html)

# Extensions

- [ipyvizzu-story](https://github.com/vizzuhq/ipyvizzu-story) adds presentation
  controls to present data stories live or to share them as an interactive HTML
  file.

# Contributing

We welcome contributions to the project, visit our contributing
[guide](https://github.com/vizzuhq/ipyvizzu/blob/main/CONTRIBUTING.md) for
further info.

# Contact

- Join our Slack if you have any questions, comments or you need some assistance
  in using our tools:
  [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
- Drop us a line at hello@vizzuhq.com
- Follow us on Twitter: [VizzuHQ](https://twitter.com/VizzuHQ)

# License

Copyright © 2022 [Vizzu Kft.](https://vizzuhq.com).

Released under the
[Apache 2.0 License](https://github.com/vizzuhq/ipyvizzu/blob/main/LICENSE).
