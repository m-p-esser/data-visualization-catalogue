```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x, hue = "age", "income"

# Draw Plot
fig = px.histogram(
    data_frame=df, x=x, color=hue, nbins=10, barmode='overlay',
    histnorm='probability density', template="seaborn")
fig.show()
```