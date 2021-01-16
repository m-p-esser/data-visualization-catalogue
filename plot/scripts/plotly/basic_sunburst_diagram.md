```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/9_car_sales.csv")
df.head(5)

# # Initialize variables
size = "Sales_in_thousands"
path = ['Manufacturer', 'Model', 'Vehicle_type']

# # Draw Plot
fig = px.sunburst(
    data_frame=df, path=path, values=size,
    template="seaborn")
fig.show()
```