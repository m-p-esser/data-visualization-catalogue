```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x, col, row = "age", "income", "native-country"

# Data Transformations
df["native-country"] = df["native-country"].apply(lambda x: "US" if x == "United-States" else "Non-US") 

# Draw Plot
fig = px.histogram(
    data_frame=df, x=x, color=col, nbins=10, barmode='overlay',
    histnorm='probability density', template="seaborn",
    facet_col=col, facet_col_spacing=0.07,
    facet_row=row, facet_row_spacing=0.1)
fig.show()
```