# Chart settings

You can change the behaviour of the chart with chart properties and constructor
arguments.

## Constructor arguments

### Size of Chart

The size of the chart can be changed with `width` and `height`
[constructor](../reference/ipyvizzu/chart.md#ipyvizzu.chart.Chart.__init__)
arguments.

!!! info
    `width` and `height` constructor arguments are optional and the default
    values are `800px` and `480px`, but you can change them to any valid cssText
    value.

```python
from ipyvizzu import Chart


chart = Chart(width="100%", height="500px")
```

### Display behavior of Chart

The chart can be displayed in several ways and this behavior can be changed with
the `display`
[constructor](../reference/ipyvizzu/chart.md#ipyvizzu.chart.Chart.__init__)
argument.

!!! info
    `display` constructor argument is optional and the default value is
    [DisplayTarget.ACTUAL](../reference/ipyvizzu/template.md#ipyvizzu.template.DisplayTarget).

!!! note
    Not all of the options below work in all environments, before you choose,
    please also check the [Environments chapter](../environments/index.md).

The main advantage of using `ACTUAL`, `BEGIN` or `END`
[DisplayTarget](../reference/ipyvizzu/template.md#ipyvizzu.template.DisplayTarget)
is that once you have played the whole notebook, you can replay any intermediate
cell without running the entire notebook again.

#### Actual

By default or if `display` is set to `DisplayTarget.ACTUAL`, the chart is
relocated and displayed after the cell that is actually running.

```python
from ipyvizzu import Chart, DisplayTarget


chart = Chart(display=DisplayTarget.ACTUAL)
```

#### Begin

if `display` is set to `DisplayTarget.BEGIN`, the chart is displayed after the
cell of the constructor.

```python
from ipyvizzu import Chart, DisplayTarget


chart = Chart(display=DisplayTarget.BEGIN)
```

#### End

if `display` is set to `DisplayTarget.END`, the chart is displayed after the
last running cell.

!!! note
    If you rerun an intermediate cell it becomes the last running cell.

```python
from ipyvizzu import Chart, DisplayTarget


chart = Chart(display=DisplayTarget.END)
```

#### Manual

If `display` is set to `DisplayTarget.MANUAL`, the chart is not displayed until
a display function is called.

One of the display functions is the `_repr_html_` method which is supported in
most environments.

```python
from ipyvizzu import Chart, DisplayTarget


chart = Chart(display=DisplayTarget.MANUAL)

# ...

chart
```

The other display function is the `show` method, which uses
`IPython.display.display_javascript` function, like the `ACTUAL`, `BEGIN` and
`END` targets, except it doesn't relocate the chart.

```python
from ipyvizzu import Chart, DisplayTarget


chart = Chart(display=DisplayTarget.MANUAL)

# ...

chart.show()
```

!!! note
    Against better compatibility, the disadvantage of using `MANUAL`
    [DisplayTarget](../reference/ipyvizzu/template.md#ipyvizzu.template.DisplayTarget)
    is that the chart cannot be modified after calling one of the display
    functions, so intermediate cells cannot be rerun.

### Vizzu

`ipyvizzu` requires and downloads the [Vizzu](https://lib.vizzuhq.com/)
JavaScript/C++ library from
[jsDelivr CDN](https://www.jsdelivr.com/package/npm/vizzu), but you can also use
a self-hosted version of `Vizzu`.

After download `Vizzu`, you can store and host it on your server.

```sh
npm install vizzu
```

```python
from ipyvizzu import Chart


chart = Chart(vizzu="<url>/vizzu.min.js")
```

## Properties

### Scroll into view

When the scroll into view feature is turned on, ipyvizzu is able to
automatically follow and scroll to the currently running animation.

!!! info
    If manual scrolling is detected, ipyvizzu will not scroll automatically
    until the notebook is replayed again.

!!! note
    Scroll into view feature does not work in all environments, before you
    choose, please also check the
    [Environments chapter](../environments/index.md).

You can enable this feature, if set
[scroll_into_view](../reference/ipyvizzu/chart.md#ipyvizzu.chart.Chart.scroll_into_view)
property to `True` (which is `False` by default).

```python
from ipyvizzu import Chart


chart = Chart()
chart.scroll_into_view = True
```
