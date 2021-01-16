```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x, y = "relationship", "percent"

# Data Transformation
freq_table = df[x].value_counts(normalize=True) \
    .mul(100).rename(y).reset_index().rename(columns={"index": x}) \
    .sort_values(by=y, ascending=False) \
    .round(1)

# Draw Plot
fig = freq_table.pipe(
    lambda df: px.bar(
        data_frame=df, x=x, y=y,
        template="seaborn", text=y)
        )
fig.show()
```