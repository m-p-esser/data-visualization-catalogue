```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/10_funnel_analysis.csv", index_col=[0])

# Initialize variables
cols = ['home_page', 'search_page', 'payment_page', 'payment_confirmation_page']
x, y, hue = 'percent', 'page', 'sex'

# Data Transformation
group_count = df.groupby([hue])[cols].sum() # works because True = 1, False = 0
group_sum = df.groupby([hue])[cols].count()
group_count, group_sum
group_percent = (group_count / group_sum).mul(100)
freq_table = group_percent.reset_index() \
    .melt(id_vars=hue, value_vars=cols, var_name=y, value_name=x) \
    .round(1)

# Draw Plot
fig = px.funnel(data_frame=freq_table, x=x, y=y, color=hue)
fig.show()
```