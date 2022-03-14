<p align="center">
  <a href="https://github.com/vizzuhq/vizzu-lib">
    <img src="https://github.com/vizzuhq/vizzu-lib-doc/blob/main/docs/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>ipyvizzu</b> - Jupyter notebook integration for Vizzu.</p>
  <p align="center">
    <a href="https://vizzuhq.github.io/ipyvizzu/index.html">Tutorial & Examples</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu">Repository</a>
  </p>
</p>

[![CI check](https://github.com/vizzuhq/ipyvizzu/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu/actions/workflows/ci.yml)

# About The Project

ipyvizzu provides Jupyter Notebook integration for [Vizzu](https://github.com/vizzuhq/vizzu-lib).

# Installation

ipyvizzu requires only `IPython` package.
However you can use it only in Jupyter Notebook therefore `notebook` project has to be installed.

```sh
pip install ipyvizzu
pip install notebook
```

ipyvizzu downloads Vizzu from [jsDelivr](https://www.jsdelivr.com/package/npm/vizzu?version=~0.4.0) CDN by default,
but a local copy of it can be used.

Install a local copy of Vizzu.

```sh
npm install vizzu@~0.4.0
```

Change Vizzu's url in the constructor of the Chart class.

```python
from ipyvizzu import Chart

chart = Chart(vizzu="./node_modules/vizzu/dist/vizzu.min.js")
```

# Usage

ipyvizzu only works in Jupiter Notebook environment.
A notebook cell may contain the following code snippet.

```python
from ipyvizzu import Chart, Data, Config

data = Data()
data.add_series("Foo", ['Alice', 'Bob', 'Ted'])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 2, 2])

chart = Chart()
chart.animate(data)

chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
chart.animate(Config({"geometry": "circle"}))
chart.animate(Config({"x": "Foo", "y": "Baz", "color": "Foo"}))
chart.animate(Config({"geometry": "rectangle"}))
```

Visit our [documentation](https://vizzuhq.github.io/ipyvizzu/index.html) site for more tutorials and examples.

# Contributing

We welcome contributions to the project, visit our [contributing guide](https://github.com/vizzuhq/ipyvizzu/blob/main/CONTRIBUTING.md) for further info.

# Contact

* Join our Slack: [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
* Drop us a line at hello@vizzuhq.com
* Follow us on twitter: [https://twitter.com/VizzuHQ](https://twitter.com/VizzuHQ)

# License

Copyright © 2022 [Vizzu Kft.](https://vizzuhq.com).

Released under the [Apache 2.0 License](https://github.com/vizzuhq/ipyvizzu/blob/main/LICENSE).
