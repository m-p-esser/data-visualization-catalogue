```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
hue, y, col, row = "gender", "relationship", "native-country", "income" 

# Data Transformations
df["native-country"] = df["native-country"].apply(lambda x: "US" if x == "United-States" else "Non-US") 
group_count = df.groupby([row, col, y, hue]).count().iloc[:,0]
group_sum = df.groupby([row, col, y]).count().iloc[:,0]
group_percent = (group_count / group_sum).mul(100).rename("percent")
freq_table = group_percent.reset_index() \
    .round(1)

# Draw Plot
fig = freq_table.pipe(
    lambda df: px.bar(
        data_frame=df, x=y, y="percent", color=hue, barmode="group",
             facet_col=col, facet_row=row, template="seaborn",
             facet_col_spacing=0.07, facet_row_spacing=0.1))
fig.show()
```