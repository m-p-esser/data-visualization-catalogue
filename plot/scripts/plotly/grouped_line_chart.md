```python
import plotly.express as px
import pandas as pd
from datetime import datetime

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")

# Initialize variables
x1, x2, y, hue = "MonthName", "MonthNumber", "Total Volume", "type"

# Data Transformations
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["MonthName"] = df["Date"].apply(lambda x: x.month_name())
df["MonthNumber"] = df["Date"].apply(lambda x: x.month)
df = df[df["year"] == 2015]

mean_table = df.groupby([x1, hue])[x2, y].mean() \
    .reset_index().sort_values(by=[hue, x2]) \
    .round(0)

# Draw Plot
fig = mean_table.pipe(
    lambda df: px.line(
        data_frame=df, x=x1, y=y, color=hue,
        template="seaborn")
        )
fig.show()
```