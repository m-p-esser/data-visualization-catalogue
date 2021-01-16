```python
import plotly.express as px
import pandas as pd
from datetime import datetime

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")

# Initialize variables
x1, x2, y, col = "MonthName", "MonthNumber", "Total Volume", "region"

# Data Transformations
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["MonthName"] = df["Date"].apply(lambda x: x.month_name())
df["MonthNumber"] = df["Date"].apply(lambda x: x.month)
df = df[df["year"] == 2015]
df = df[df["region"].isin(df["region"].unique()[7:16])]  # Pick random regions

mean_table = df.groupby([x1, col])[x2, y].mean() \
    .reset_index().sort_values(by=[col, x2]) \
    .round(0)

# Draw Plot
fig = mean_table.pipe(
    lambda df: px.line(
        data_frame=df, x=x1, y=y, template="seaborn",
        facet_col=col, facet_col_spacing=0.07, facet_col_wrap=3,
        labels={y: 'Volume', x1: ''}))

for annotation in fig.layout.annotations:
    annotation.text = annotation.text.split("=")[1]

fig.show()
```