```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x, hue, col = "age", "income", "native-country"

# Data Transformations
df["native-country"] = df["native-country"].apply(lambda x: "US" if x == "United-States" else "Non-US") 

# Draw Plot
fig = px.histogram(
    data_frame=df, x=x, color=hue, nbins=10, barmode='overlay',
    histnorm='probability density', template="seaborn",
    facet_col=col, facet_col_wrap=3, facet_col_spacing=0.07)
fig.show()
```