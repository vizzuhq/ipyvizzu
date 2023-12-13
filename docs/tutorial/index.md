# Tutorial

This is the tutorial of `ipyvizzu` - the `Python` integration of the free,
open-source `JavaScript`/`C++` library
[`Vizzu`](https://lib.vizzuhq.com/xLIB_MINOR_VERSIONx/). You can create animated
charts, data stories, interactive reports and dashboards with it in Jupyter and
similar notebooks and app building platforms.

This is an excellent starting point to get acquainted with `ipyvizzu`, as it
walks you through the installation of the library, introduces the logic it
employs and the different settings to control how your animated charts look and
behave.

The tutorial is organized into chapters that introduce the concept and the
details of `ipyvizzu` step-by-step. You can find the list of chapters at the end
of this page and in the menu.

## Basic logic of ipyvizzu

The foundation of an `ipyvizzu` chart is the animation. The animation contains
states describing the chart's configuration, such as the data series on the
chart, the coordinate system, labels, titles, etc. A static chart is the result
of a single animation state. When there are more states, `ipyvizzu`
automatically transitions between these. The animate method initiates the
animation into a new state by describing the new chart and how `ipyvizzu` should
transition to it.

![Vizzu](../assets/api-overview.svg){ class='image-center' }

The animate method has non-keyword and keyword arguments. The non-keyword
arguments sets the chart, and the (optional) keyword arguments determines how
`ipyvizzu` should animate to that state.

There are three types of non-keyword arguments:

- `data`: this is where you add the data that you want to visualize
- `config`: this is where you can add or remove series to the chart and set
  general settings like the chart title, the geometry, the alignment etc.
- `style`: this is where you can set how your chart looks

## Installation

```sh
pip install ipyvizzu
```

Visit [Installation chapter](../installation.md) for more options and details.

## Usage

!!! note
    `ipyvizzu` generates `JavaScript` code, then the `vizzu` calls are evaluated
    by the browser. Therefore if a blank space appears where the chart should
    be, check the console log of your browser. `vizzu` reports its errors there.
    If you get a `vizzu` error in your browser console that is not
    straightforward to understand, please clean your browser cache first,
    because it might be caused by an older version being stored in your browser.
