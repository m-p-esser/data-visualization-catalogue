```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x = "relationship"

# Data Transformation
freq_table = df[x].value_counts() \
    .rename("count").reset_index().rename(columns={"index": x}) \
    .sort_values("count", ascending=False)

# Draw Plot
fig = freq_table.pipe(
    lambda df: px.pie(
        data_frame=df, values='count', names=x,  
        hole=0.5, template="seaborn")
        )
fig.show()
