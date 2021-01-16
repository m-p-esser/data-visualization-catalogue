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
    mode = "number+gauge+delta", value = metric_cur_example,
    domain = {'x': [0.1, 1], 'y': [0, 1]},
    title = {'text' :"<b>Profit</b>"},
    delta = {'reference': metric_prev_example},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 15000]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': target_example},
        'steps': [
            {'range': [0, 6000], 'color': "lightgray"},
            {'range': [6000, 10000], 'color': "gray"}]}))
fig.update_layout(height = 250)
fig.show()
```