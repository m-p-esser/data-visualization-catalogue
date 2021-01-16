```python
import plotly.graph_objects as go
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/13_indian_ecommerce_sales.csv", index_col=[0])

# Initialize variables
metric_cur, metric_prev, target = "Current Revenue", "Previous Revenue", "Current Target"

# Data Transformation
metric_cur_example = df.iloc[1].loc[metric_cur]
metric_prev_example = df.iloc[1].loc[metric_prev]
target_example = df.iloc[1].loc[target]

# Draw Plot
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = metric_cur_example,
    mode = "gauge+number+delta",
    title = {'text': "Revenue"},
    delta = {'reference': metric_prev_example},
    gauge = {'axis': {'range': [None, 15000]},
             'steps' : [
                 {'range': [0, 6000], 'color': "lightgray"},
                 {'range': [6000, 9000], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': target_example}}))

fig.show()
```