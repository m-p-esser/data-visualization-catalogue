```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables
x, y, hue = "relationship", "percent", "gender" 

# Data Transformation
group_count = df.groupby([hue, x]).count().iloc[:,0]
group_sum = df.groupby([x]).count().iloc[:,0]
group_percent = (group_count / group_sum) \
    .mul(100).rename("percent")
freq_table = group_percent.reset_index() \
    .sort_values(by=[hue, x], ascending=False) \
    .round(1)
freq_table

# Draw Plot
fig = freq_table.pipe(
    lambda df: px.bar(
        data_frame=df, x=y, y=x, color=hue, 
        barmode="group", template="seaborn", text=y)
        )
fig.show()
