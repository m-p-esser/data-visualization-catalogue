```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/11_personality.csv")

# # Initialize variables
x, y, hue = "percent", "attribute", "score"
attributes = ["openness", "agreeableness", "emotional_stability", "conscientiousness", "extraversion"]

# Data Transformation
df = df.melt(id_vars="userid", value_vars=attributes,
var_name=y, value_name=hue)
df[hue] = df[hue].apply(lambda x: int(x) if x == round(x) else int(round(x)))
df[hue] = df[hue].astype("category")

group_count = df.groupby([y, hue]).count().iloc[:,0]
group_sum = df.groupby([y]).count().iloc[:,0]
group_percent = (group_count / group_sum) \
    .mul(100).rename(x)
freq_table = group_percent.reset_index() \
    .sort_values(by=[y, hue], ascending=False) \
    .round(0)

top3_table = freq_table[freq_table[hue].isin([5, 6, 7])] \
    .groupby([y]).sum().reset_index().sort_values(by=[x], ascending=False)
y_order = top3_table[y].tolist()

# Draw Plot
fig = freq_table.pipe(
    lambda df: px.bar(
        data_frame=df, x=x, y=y, color=hue, category_orders={y: y_order},
        barmode="relative", template="seaborn", text=x,
        color_discrete_sequence=px.colors.diverging.Tealrose
        ))
fig.show()
```