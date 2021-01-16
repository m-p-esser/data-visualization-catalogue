```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")

# Initialize variables
x, y = "Total Bags", "Total Volume"

# Draw Plot
fig = px.scatter(
    df, x=x, y=y, opacity=0.7, 
    template="seaborn")
fig.show()
```