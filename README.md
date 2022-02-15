[![Makefile CI](https://github.com/nyirog/ipyvizzu/actions/workflows/makefile.yml/badge.svg?branch=main)](https://github.com/nyirog/ipyvizzu/actions/workflows/makefile.yml)

# ipyvizzu

Jupyter notebook integration for vizzu.

ipyvizzu only works in jupiter notebook environment. A notebook cell may
contain the following code snippet.

```python
from ipyvizzu import Chart, Data, Config

data = Data()
data.add_serie("Foo", ["Alice", "Bob", "Ted"])
data.add_serie("Bar", [15, 32, 12])
data.add_serie("Baz", [5, 2, 2])

chart = Chart()
chart.animate(data)

chart.animate(x="Foo", y="Bar", color="Foo")
chart.animate(geometry="circle")
chart.animate(x="Foo", y="Baz", color="Foo")
chart.animate(geometry="rectangle")

chart.show()
```

## Installation

ipyvizzu requires only `IPython` package, but you can use it only in jupyter
notebook therefore `notebook` project has to be installed.

```sh
pip install ipyvizzu
pip install notebook
```

## Documentation

Documentation can be build with the `doc` make target.

```sh
make doc
```

Online version can be read at [vizzuhq.github.io/ipyvizzu](https://vizzuhq.github.io/ipyvizzu/index.html).

## CI check

The `check` make target collects the targets which are run by the CI server.

```sh
make check
```

### Testing

The unit tests can be run with the `test` make target. As part of the unit
tests the notebooks under the `docs/examples` are executed, too.

```sh
make test
```

### Formatting

The ipyvizzu project is formatted with `black`. The CI check invokes the
`check-format` target to ensure that the python files are formatted with
`black`.

```sh
make check-format
```

`black` can be run with the `format` make target.

```sh
make format
```
