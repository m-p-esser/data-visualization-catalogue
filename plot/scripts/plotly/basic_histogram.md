```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x = "age"

# Draw Plot
fig = px.histogram(
    data_frame=df, x=x, nbins=10, 
    histnorm='probability density', template="seaborn")
fig.show()
```