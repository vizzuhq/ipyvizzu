# Data

## Data types

`ipyvizzu` currently supports two types of data series: dimensions and measures.
Dimensions slice the data cube `ipyvizzu` uses, whereas measures are values
within the cube.

Dimensions are categorical series that can contain strings and numbers, but both
will be treated as strings. Temporal data such as dates or timestamps should
also be added as dimensions. By default, `ipyvizzu` will draw the elements on
the chart in the order they are provided in the data set. Thus we suggest adding
temporal data in a sorted format from oldest to newest.

Measures at the moment can only be numerical.

## Adding data

There are multiple ways you can add data to `ipyvizzu`.

- Using pandas DataFrame
- Specify data by series - column after column if you think of a spreadsheet
- Specify data by records - row after row
- Using data cube form
- Using JSON

??? tip
    You should set the data in the first animate call.

    ```python
    chart.animate(data)
    ```

| Genres | Kinds        | Popularity |
| ------ | ------------ | ---------- |
| Pop    | Hard         | 114        |
| Rock   | Hard         | 96         |
| Jazz   | Hard         | 78         |
| Metal  | Hard         | 52         |
| Pop    | Smooth       | 56         |
| Rock   | Experimental | 36         |
| Jazz   | Smooth       | 174        |
| Metal  | Smooth       | 121        |
| Pop    | Experimental | 127        |
| Rock   | Experimental | 83         |
| Jazz   | Experimental | 94         |
| Metal  | Experimental | 58         |

### Using `pandas` DataFrame

Use
[`add_df`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data.add_df)
method for adding `pandas` DataFrame to
[`Data`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data).

```python
import pandas as pd
from ipyvizzu import Data


data = {
    "Genres": [
        "Pop",
        "Rock",
        "Jazz",
        "Metal",
        "Pop",
        "Rock",
        "Jazz",
        "Metal",
        "Pop",
        "Rock",
        "Jazz",
        "Metal",
    ],
    "Kinds": [
        "Hard",
        "Hard",
        "Hard",
        "Hard",
        "Smooth",
        "Experimental",
        "Smooth",
        "Smooth",
        "Experimental",
        "Experimental",
        "Experimental",
        "Experimental",
    ],
    "Popularity": [
        114,
        96,
        78,
        52,
        56,
        36,
        174,
        121,
        127,
        83,
        94,
        58,
    ],
}
df = pd.DataFrame(data)

data = Data()
data.add_df(df)
```

!!! info
    `ipyvizzu` makes a difference between two types of data, numeric (measure)
    and not numeric (dimension). A column's `dtype` specifies that the column is
    handled as a measure or as a dimension.

It is also possible to add the data frame's index as a series column while
adding the data frame

```python
import pandas as pd
from ipyvizzu import Data


df = pd.DataFrame(
    {"Popularity": [114, 96, 78]}, index=["x", "y", "z"]
)

data = Data()
data.add_df(df, include_index="IndexColumnName")
```

or later with the
[`add_df_index`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data.add_df_index)
method.

```python
import pandas as pd
from ipyvizzu import Data


df = pd.DataFrame(
    {"Popularity": [114, 96, 78]}, index=["x", "y", "z"]
)

data = Data()
data.add_df_index(df, column_name="IndexColumnName")
data.add_df(df)
```

!!! note
    If you want to work with `pandas` DataFrame and `ipyvizzu`, you need to
    install `pandas` or install it as an extra:

    ```sh
    pip install ipyvizzu[pandas]
    ```

#### Using csv

Download `music_data.csv` [here](../assets/data/music_data.csv).

```python
import pandas as pd
from ipyvizzu import Data


df = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.csv"
)

data = Data()
data.add_df(df)
```

#### Using Excel spreadsheet

Download `music_data.xlsx` [here](../assets/data/music_data.xlsx).

```python
import pandas as pd
from ipyvizzu import Data


df = pd.read_excel(
    "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.xlsx"
)

data = Data()
data.add_df(df)
```

#### Using Google Sheets

```python
import pandas as pd
from ipyvizzu import Data


google_sheet_id = "<Google Sheet id>"
worksheet_name = "<Worksheet name>"

df = pd.read_csv(
    f"https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet={worksheet_name}"
)

data = Data()
data.add_df(df)
```

For example if the url is
`https://docs.google.com/spreadsheets/d/abcd1234/edit#gid=0` then
`google_sheet_id` here is `abcd1234`.

#### Using SQLite

```python
import pandas as pd
import sqlite3
from ipyvizzu import Data


# establish a connection to the SQLite database
conn = sqlite3.connect("mydatabase.db")
# read data from a SQLite table into a pandas DataFrame
df = pd.read_sql("SELECT * FROM mytable", conn)
# close the connection
conn.close()

data = Data()
data.add_df(df)
```

!!! note
    You'll need to adjust the SQL query and the database connection parameters
    to match your specific use case.

#### Using MySQL

```python
import pandas as pd
import mysql.connector
from ipyvizzu import Data


# establish a connection to the MySQL database
conn = mysql.connector.connect(
    user="myusername",
    password="mypassword",
    host="myhost",
    database="mydatabase",
)
# read data from a MySQL table into a pandas DataFrame
df = pd.read_sql("SELECT * FROM mytable", con=conn)
# close the connection
conn.close()

data = Data()
data.add_df(df)
```

!!! note
    You'll need to adjust the SQL query and the database connection parameters
    to match your specific use case.

#### Using PostgreSQL

```python
import pandas as pd
import psycopg2
from ipyvizzu import Data


# establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    user="myusername",
    password="mypassword",
    host="myhost",
    port="5432",
    database="mydatabase",
)
# read data from a PostgreSQL table into a pandas DataFrame
df = pd.read_sql("SELECT * FROM mytable", con=conn)
# close the connection
conn.close()

data = Data()
data.add_df(df)
```

!!! note
    You'll need to adjust the SQL query and the database connection parameters
    to match your specific use case.

#### Using Microsoft SQL Server

```python
import pandas as pd
import pyodbc
from ipyvizzu import Data


# establish a connection to the Microsoft SQL Server database
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=myserver;"
    "Database=mydatabase;"
    "UID=myusername;"
    "PWD=mypassword"
)
# read data from a SQL Server table into a pandas DataFrame
df = pd.read_sql("SELECT * FROM mytable", con=conn)
# close the connection
conn.close()

data = Data()
data.add_df(df)
```

!!! note
    You'll need to adjust the SQL query and the database connection parameters
    to match your specific use case.

### Using `pyspark` DataFrame

Use
[`add_spark_df`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data.add_spark_df)
method for adding `pyspark` DataFrame to
[`Data`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data).

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
)
from ipyvizzu import Data


spark = SparkSession.builder.appName("ipyvizzu").getOrCreate()
spark_schema = StructType(
    [
        StructField("Genres", StringType(), True),
        StructField("Kinds", StringType(), True),
        StructField("Popularity", IntegerType(), True),
    ]
)
spark_data = [
    ("Pop", "Hard", 114),
    ("Rock", "Hard", 96),
    ("Jazz", "Hard", 78),
    ("Metal", "Hard", 52),
    ("Pop", "Smooth", 56),
    ("Rock", "Experimental", 36),
    ("Jazz", "Smooth", 174),
    ("Metal", "Smooth", 121),
    ("Pop", "Experimental", 127),
    ("Rock", "Experimental", 83),
    ("Jazz", "Experimental", 94),
    ("Metal", "Experimental", 58),
]
df = spark.createDataFrame(spark_data, spark_schema)

data = Data()
data.add_spark_df(df)
```

!!! note
    If you want to work with `pyspark` DataFrame and `ipyvizzu`, you need to
    install `pyspark` or install it as an extra:

    ```sh
    pip install ipyvizzu[pyspark]
    ```

### Using `numpy` Array

Use
[`add_np_array`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data.add_np_array)
method for adding `numpy` Array to
[`Data`](../reference/ipyvizzu/animation.md#ipyvizzu.animation.Data).

```python
import numpy as np
from ipyvizzu import Data


numpy_array = np.array(
    [
        ["Pop", "Hard", 114],
        ["Rock", "Hard", 96],
        ["Jazz", "Hard", 78],
        ["Metal", "Hard", 52],
        ["Pop", "Smooth", 56],
        ["Rock", "Experimental", 36],
        ["Jazz", "Smooth", 174],
        ["Metal", "Smooth", 121],
        ["Pop", "Experimental", 127],
        ["Rock", "Experimental", 83],
        ["Jazz", "Experimental", 94],
        ["Metal", "Experimental", 58],
    ]
)

data = Data()
data.add_np_array(
    numpy_array,
    column_name={0: "Genres", 1: "Kinds", 2: "Popularity"},
    column_dtype={2: int},
)
```

!!! info
    - Arrays with dimensions higher than 2 are not supported.
    - If `column_name` dictionary is not added, column indices will be used as
      names.
    - If `column_dtype` dictionary is not added, every column will use
      `numpy_array.dtype`.

!!! note
    If you want to work with `numpy` Array and `ipyvizzu`, you need to install
    `numpy` or install it as an extra:

    ```sh
    pip install ipyvizzu[numpy]
    ```

### Specify data by series

When you specify the data by series or by records, it has to be in first normal
form. Here is an example of that:

```python
from ipyvizzu import Data


data = Data()
data.add_series(
    "Genres",
    [
        "Pop",
        "Rock",
        "Jazz",
        "Metal",
        "Pop",
        "Rock",
        "Jazz",
        "Metal",
        "Pop",
        "Rock",
        "Jazz",
        "Metal",
    ],
    type="dimension",
)
data.add_series(
    "Kinds",
    [
        "Hard",
        "Hard",
        "Hard",
        "Hard",
        "Smooth",
        "Experimental",
        "Smooth",
        "Smooth",
        "Experimental",
        "Experimental",
        "Experimental",
        "Experimental",
    ],
    type="dimension",
)
data.add_series(
    "Popularity",
    [114, 96, 78, 52, 56, 36, 174, 121, 127, 83, 94, 58],
    type="measure",
)
```

### Specify data by records

```python
from ipyvizzu import Data


data = Data()

data.add_series("Genres", type="dimension")
data.add_series("Kinds", type="dimension")
data.add_series("Popularity", type="measure")

record = ["Pop", "Hard", 114]

data.add_record(record)

records = [
    ["Rock", "Hard", 96],
    ["Jazz", "Hard", 78],
    ["Metal", "Hard", 52],
    ["Pop", "Smooth", 56],
    ["Rock", "Experimental", 36],
    ["Jazz", "Smooth", 174],
    ["Metal", "Smooth", 121],
    ["Pop", "Experimental", 127],
    ["Rock", "Experimental", 83],
    ["Jazz", "Experimental", 94],
    ["Metal", "Experimental", 58],
]

data.add_records(records)
```

Where records can be lists as shown above or dictionaries:

```python
records = [
    {
        "Genres": "Pop",
        "Kinds": "Hard",
        "Popularity": 114,
    },
    {
        "Genres": "Rock",
        "Kinds": "Hard",
        "Popularity": 96,
    },
    # ...
]
```

### Using data cube form

!!! note
    In the example below, the record `Rock,Experimental,36` has been replaced
    with `Rock,Smooth,36` in order to illustrate that only data with same
    dimensions can be used in the data cube form.

<table>
  <tbody><tr><th colspan="2" rowspan="2"></th><th colspan="4" style="text-align:center">Genres</th></tr>
  <tr>
      <td>Pop</td><td>Rock</td><td>Jazz</td><td>Metal</td>
  </tr>
  <tr><th rowspan="3" style="text-align:center">Kinds</th>
      <td style="text-align:center">Hard</td>
      <td>114</td><td>96</td><td>78</td><td>52</td>
  </tr>
  <tr><td style="text-align:center">Smooth</td>
      <td>56</td><td>36</td><td>74</td><td>121</td>
  </tr>
  <tr>
      <td style="text-align:center">Experimental</td>
      <td>127</td><td>83</td><td>94</td><td>58</td>
  </tr>
  <tr><td colspan="2"></td><th colspan="4" style="text-align:center">Popularity</th></tr>
</tbody></table>

```python
from ipyvizzu import Data


data = Data()

data.add_dimension("Genres", ["Pop", "Rock", "Jazz", "Metal"])
data.add_dimension("Kinds", ["Hard", "Smooth", "Experimental"])

data.add_measure(
    "Popularity",
    [
        [114, 96, 78, 52],
        [56, 36, 174, 121],
        [127, 83, 94, 58],
    ],
)
```

### Using JSON

Download `music_data.json` [here](../assets/data/music_data.json) (in this
example the data stored in the data cube form).

```python
from ipyvizzu import Data


data = Data.from_json("../assets/data/music_data.json")
```
