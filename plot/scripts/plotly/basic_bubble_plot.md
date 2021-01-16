```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")
df.head(5)

# Initialize variables
x, y, size = "Total Bags", "Total Volume", "Large Bags"

# # Draw Plot
fig = px.scatter(
    df, x=x, y=y, size=size,
    opacity=0.5, template="seaborn")
fig.show()
```