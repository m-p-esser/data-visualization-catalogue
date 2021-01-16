```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x, y, hue = "relationship", "age", "gender"

# Data Transformation
order = list(df.groupby(by=[x])[y].median().sort_values(ascending=False).index)

# Draw Plot
fig = px.box(df, x=x, y=y, color=hue, category_orders={x: order}, template="seaborn")
fig.show()
```