```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")
df.head(5)

# # Initialize variables
# x, y = "gender", "age"

# # Data Transformation
# order = list(df.groupby(by=[x])[y].median().sort_values(ascending=False).index)

# # Draw Plot
# fig = px.violin(
#     df, x=x, y=y, box=True,
#     category_orders={x: order}, template="seaborn")
# fig.show()

import plotly.graph_objects as go
from plotly.colors import n_colors
import numpy as np
np.random.seed(1)

# 12 sets of normal distributed random data, with increasing mean and standard deviation
data = (np.linspace(1, 2, 12)[:, np.newaxis] * np.random.randn(12, 200) +
            (np.arange(12) + 2 * np.random.random(12))[:, np.newaxis])

# colors = n_colors('rgb(5, 200, 200)', 'rgb(200, 10, 10)', 12, colortype='rgb')

# fig = go.Figure()
# for data_line, color in zip(data, colors):
#     fig.add_trace(go.Violin(x=data_line, line_color=color))

# fig.update_traces(orientation='h', side='positive', width=3, points=False)
# fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)
# fig.show()
```