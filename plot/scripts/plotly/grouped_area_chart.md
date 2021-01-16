```python
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")
df.head(5)

# Initialize variables
x, y, hue = "Date", "AveragePrice", "type"

# # Data Transformations
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
unique_categories = df[hue].unique()

# Draw Plot
fig = go.Figure()
for index, category in enumerate(unique_categories):
    filtered_df = df[df[hue] == category].head(5)
    if index == 0:
        fig.add_trace(
            go.Scatter(
                x=filtered_df.loc[:, x], y=filtered_df.loc[:, y], 
                name=category, fill='tozeroy')) # fill down to xaxis
    if index > 0:
        fig.add_trace(
            go.Scatter(
                x=filtered_df.loc[:, x], y=filtered_df.loc[:, y], 
                name=category, fill='tonexty')) # fill down to xaxis
fig.show()
