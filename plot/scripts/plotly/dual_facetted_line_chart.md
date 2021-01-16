```python
import plotly.express as px
import pandas as pd
from datetime import datetime

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")

# Initialize variables
x1, x2, y, col, row = "MonthName", "MonthNumber", "Total Volume", "year", "type"

# Data Transformations
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["MonthName"] = df["Date"].apply(lambda x: x.month_name())
df["MonthNumber"] = df["Date"].apply(lambda x: x.month)


mean_table = df.groupby([x1, col, row])[x2, y].mean() \
    .reset_index().sort_values(by=[col, row, x2]) \
    .round(0)

# Draw Plot
fig = mean_table.pipe(
    lambda df: px.line(
        data_frame=df, x=x1, y=y, facet_col=col, facet_row=row,
        color=row, template="seaborn")
        )
fig.update_yaxes(matches=None)
fig.show()
```