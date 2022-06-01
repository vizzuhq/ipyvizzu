# JupyterLite

You can use ipyvizzu in JupyterLite with the following restrictions:

| Function                                                                                   | Supported          |
| ------------------------------------------------------------------------------------------ | ------------------ |
| Rerun individual cells without rerun the chart initialization cell (if display!="manual")  | :white_check_mark: |
|                                                                                            |                    |
| Constructor arguments:                                                                     |                    |
| Change the url of vizzu (vizzu)                                                            | :white_check_mark: |
| Change the width of the chart (width)                                                      | :white_check_mark: |
| Change the height of the chart (height)                                                    | :white_check_mark: |
| Automatically display all animations after the constructor's cell (display="begin")        | :white_check_mark: |
| Automatically display animation after the currently running cell (display="actual")        | :white_check_mark: |
| Automatically display all animations after the last running cell (display="end")           | :white_check_mark: |
| Manually display all animations after `show()` method called (display="manual")            | :white_check_mark: |
| Manually display all animations after `_repr_html_()` method called (display="manual")     | :white_check_mark: |
|                                                                                            |                    |
| Properties:                                                                                |                    |
| Scroll into view (scroll_into_view=True)                                                   | :white_check_mark: |

Try ipyvizzu with this working example below (it is not necessary to put the code into different cells):

```python
# cell 1
# install jsonschema and ipyvizzu

import micropip
await micropip.install("jsonschema")
await micropip.install("ipyvizzu")
```

```python
# cell 2
# import pandas, js, asyncio, StringIO and ipyvizzu and initialize chart

import pandas as pd
import js, asyncio
from io import StringIO
from ipyvizzu import Chart, Data, Config, Style

chart = Chart(width="640px", height="360px")
# chart = Chart(width="640px", height="360px", display="begin")
# chart = Chart(width="640px", height="360px", display="actual")  # default
# chart = Chart(width="640px", height="360px", display="end")
# chart = Chart(width="640px", height="360px", display="manual")
```

```python
# add data
# download data from "https://github.com/vizzuhq/ipyvizzu/raw/main/docs/examples/stories/titanic/titanic.csv" and place it in your JupyterLite workspace

DB_NAME = 'JupyterLite Storage'

async def get_contents(path):
    """use the IndexedDB API to acess JupyterLite's in-browser storage
    for documentation purposes, the full names of the JS API objects are used.
    see https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest
    """
    queue = asyncio.Queue(1)
    
    IDBOpenDBRequest = js.self.indexedDB.open(DB_NAME)
    IDBOpenDBRequest.onsuccess = IDBOpenDBRequest.onerror = queue.put_nowait
    
    await queue.get()
    
    if IDBOpenDBRequest.result is None:
        return None
        
    IDBTransaction = IDBOpenDBRequest.result.transaction("files", "readonly")
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
```

```python
# cell 4
# add config

chart.animate(Config({"x": "Count", "y": "Sex", "label": "Count","title":"Passengers of the Titanic"}))
chart.animate(Config({"x": ["Count","Survived"], "label": ["Count","Survived"], "color": "Survived"}))
chart.animate(Config({"x": "Count", "y": ["Sex","Survived"]}))
```

```python
# cell 5
# add style

chart.animate(Style({"title": {"fontSize": 35}}))
```

```python
# cell 6
# display chart with show() or _repr_html_() method if display="manual"

# chart.show()
# chart
```
