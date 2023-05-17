<p align="center">
  <a href="https://ipyvizzu.vizzuhq.com/latest/">
    <img src="https://lib.vizzuhq.com/latest/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>ipyvizzu</b> - Build animated charts in Jupyter Notebook and similar environments with a simple Python syntax</p>
  <p align="center">
    <a href="https://ipyvizzu.vizzuhq.com/latest/">Documentation</a>
    · <a href="https://ipyvizzu.vizzuhq.com/latest/examples/">Examples</a>
    · <a href="https://ipyvizzu.vizzuhq.com/latest/reference/ipyvizzu/">Code reference</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu.svg)](https://badge.fury.io/py/ipyvizzu)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipyvizzu.svg)](https://anaconda.org/conda-forge/ipyvizzu)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu/actions/workflows/cicd.yml)

# ipyvizzu

## About The Project

`ipyvizzu` is an animated charting tool for [Jupyter](https://jupyter.org),
[Google Colab](https://colab.research.google.com),
[Databricks](https://docs.databricks.com/notebooks),
[Kaggle](https://www.kaggle.com/code) and [Deepnote](https://deepnote.com)
notebooks among other platforms. `ipyvizzu` enables data scientists and analysts
to utilize animation for storytelling with data using `Python`. It's built on
the open-source `JavaScript`/`C++` charting library
[Vizzu](https://github.com/vizzuhq/vizzu-lib).

**There is a new extension of `ipyvizzu`,
[ipyvizzu-story](https://vizzuhq.github.io/ipyvizzu-story/)** with which the
animated charts can be presented right from the notebooks. Since
`ipyvizzu-story`'s syntax is a bit different to `ipyvizzu`'s, we suggest you to
start from the [ipyvizzu-story repo](https://github.com/vizzuhq/ipyvizzu-story)
if you're interested in using animated charts to present your findings live or
to share your presentation as an HTML file.

Similarly to `Vizzu`, `ipyvizzu` utilizes a generic dataviz engine that
generates many types of charts and seamlessly animates between them. It is
designed for building animated data stories as it enables showing different
perspectives of the data that the viewers can easily follow.

Main features:

- Designed with animation in focus;
- Defaults based on data visualization guidelines;
- Works with `Pandas` dataframe, while also `JSON` and inline data input is
  available;
- Auto scrolling feature to keep the actual chart in position while executing
  multiple cells.

## Installation

```sh
pip install ipyvizzu
```

Visit [Installation chapter](https://ipyvizzu.vizzuhq.com/latest/installation/)
for more options and details.

## Usage

You can create the animation below with the following code snippet.

<p align="center">
  <img src="https://ipyvizzu.vizzuhq.com/latest/assets/ipyvizzu-promo.gif" alt="ipyvizzu" />
</p>

```python
import pandas as pd
from ipyvizzu import Chart, Data, Config

data_frame = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/latest/showcases/titanic/titanic.csv"
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

## Documentation

Visit our [Documentation site](https://ipyvizzu.vizzuhq.com/latest/) for more
details and a step-by-step tutorial into `ipyvizzu` or check out our
[Example gallery](https://ipyvizzu.vizzuhq.com/latest/examples/).

## Environments

`ipyvizzu` can be used in a wide variety of environments, visit
[Environments chapter](https://ipyvizzu.vizzuhq.com/latest/environments/) for
more details.

- Notebooks
  - [Jupyter Notebook](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/jupyternotebook/)
  - [Colab](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/colab/)
  - [Databricks](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/databricks/)
  - [DataCamp](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/datacamp/)
  - [Deepnote](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/deepnote/)
  - [JupyterLab](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/jupyterlab/)
  - [JupyterLite](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/jupyterlite/)
  - [Kaggle](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/kaggle/)
  - [Noteable](https://ipyvizzu.vizzuhq.com/latest/environments/notebook/noteable/)
- App platforms
  - [Streamlit](https://ipyvizzu.vizzuhq.com/latest/environments/platform/streamlit/)
  - [Flask](https://ipyvizzu.vizzuhq.com/latest/environments/platform/flask/)
  - [Panel](https://ipyvizzu.vizzuhq.com/latest/environments/platform/panel/)
  - [Mercury](https://ipyvizzu.vizzuhq.com/latest/environments/platform/mercury/)
  - [Voilà](https://ipyvizzu.vizzuhq.com/latest/environments/platform/voila/)
- BI tools
  - [Mode](https://ipyvizzu.vizzuhq.com/latest/environments/bi/mode/)
- IDEs
  - [PyCharm](https://ipyvizzu.vizzuhq.com/latest/environments/ide/pycharm/)
  - [VSCode Python](https://ipyvizzu.vizzuhq.com/latest/environments/ide/vscode/)

## Extensions

- [ipyvizzu-story](https://ipyvizzu-story.vizzuhq.com/) adds presentation
  controls to present data stories live or to share them as an interactive HTML
  file.

## Contributing

We welcome contributions to the project, visit our contributing
[guide](https://ipyvizzu.vizzuhq.com/latest/CONTRIBUTING/) for further info.

## Contact

- Join our Slack if you have any questions or comments:
  [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
- Drop us a line at hello@vizzuhq.com
- Follow us on Twitter: [VizzuHQ](https://twitter.com/VizzuHQ)

## License

Copyright © 2022-2023 [Vizzu Inc.](https://vizzuhq.com)

Released under the
[Apache 2.0 License](https://ipyvizzu.vizzuhq.com/latest/LICENSE/).
