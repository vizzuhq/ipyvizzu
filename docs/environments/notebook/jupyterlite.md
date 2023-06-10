# JupyterLite

## Features

The features of `ipyvizzu` that are available in `JupyterLite` are marked with a
green check.

- [x]  Change the url of `Vizzu` (`vizzu`)
- [x]  Change the width of the `Chart` (`width`)
- [x]  Change the height of the `Chart` (`height`)
- [x]  Use scroll into view (`scroll_into_view`=`True`)

Display features:

- [x]  Display all animations after `_repr_html_` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x]  Display all animations after `show` method called
  (`display`=`DisplayTarget.MANUAL`)
- [x]  Automatically display all animations after the first cell
  (`display`=`DisplayTarget.BEGIN`)
- [x]  Automatically display all animations after the currently running cell
  (`display`=`DisplayTarget.ACTUAL`)
- [x]  Automatically display all animations after the last running cell
  (`display`=`DisplayTarget.END`)
- [x]  Rerun any cell without rerun the first cell
  (`display`!=`DisplayTarget.MANUAL`)

Check [Chart settings chapter](../../tutorial/chart_settings.md) for more
details.

## Installation

Place the following code into a notebook cell in order to install `ipyvizzu`
(visit [Installation chapter](../../installation.md) for more options and
details).

```python
import micropip

await micropip.install("ipyvizzu")
```

## Sample

Try `ipyvizzu` in `JupyterLite` with the following sample.

```python
# import pandas, js, asyncio, StringIO and ipyvizzu

import pandas as pd
import js, asyncio
from io import StringIO
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


# initialize Chart

chart = Chart(
    width="640px", height="360px"
)  # or Chart(width="640px", height="360px", display=DisplayTarget.ACTUAL)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.BEGIN)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.END)
# chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)


# add data to Chart
# download data from
# "https://ipyvizzu.vizzuhq.com/latest/showcases/titanic/titanic.csv"
# and place it in your JupyterLite workspace

DB_NAME = "JupyterLite Storage"


async def get_contents(path):
    """use the IndexedDB API to acess JupyterLite's in-browser storage
    for documentation purposes, the full names of the JS API objects are used.
    see https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest
    """
    queue = asyncio.Queue(1)

    IDBOpenDBRequest = js.self.indexedDB.open(DB_NAME)
    IDBOpenDBRequest.onsuccess = (
        IDBOpenDBRequest.onerror
    ) = queue.put_nowait

    await queue.get()

    if IDBOpenDBRequest.result is None:
        return None

    IDBTransaction = IDBOpenDBRequest.result.transaction(
        "files", "readonly"
    )
    IDBObjectStore = IDBTransaction.objectStore("files")
    IDBRequest = IDBObjectStore.get(path, "key")
    IDBRequest.onsuccess = IDBRequest.onerror = queue.put_nowait

    await queue.get()

    return IDBRequest.result.to_py() if IDBRequest.result else None


data = Data()
data_csv = await get_contents("titanic.csv")
data_frame = pd.read_csv(StringIO(data_csv["content"]))
data.add_data_frame(data_frame)

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


# display Chart with show or _repr_html_ method (display=DisplayTarget.MANUAL)

# chart.show()
# chart
```

Check the [Tutorial](../../tutorial/index.md) for more info.
