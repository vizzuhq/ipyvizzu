```python
import pandas as pd
from ipyvizzu import Chart, Data, Config

df = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/xIPYVIZZU_MINOR_VERSIONx/assets/data/music_data.csv"
)
data = Data()
data.add_df(df)

chart = Chart()
```
