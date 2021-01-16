```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/10_funnel_analysis.csv", index_col=[0])

# Initialize variables
cols = ['home_page', 'search_page', 'payment_page', 'payment_confirmation_page']
x, y = 'percent', 'page' 

# Data Transformation
freq_table = (df[cols].sum() / len(df)) * 100
freq_table = freq_table.reset_index() \
    .rename(columns={'index': 'page', 0: 'percent'}) \
    .sort_values(by='percent', ascending=False) \
    .round(1)

# Draw Plot
fig = px.funnel(
    data_frame=freq_table, x=x, y=y)
fig.show()
```