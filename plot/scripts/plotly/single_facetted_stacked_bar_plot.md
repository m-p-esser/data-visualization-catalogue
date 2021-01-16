```python
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/11_personality.csv")
df.head(5)

# Initialize variables
x, y, hue, col = "percent", "attribute", "score", "is_personalized"
attributes = ["openness", "agreeableness", "emotional_stability", "conscientiousness", "extraversion"]

# Data Transformation
df = df.melt(id_vars=["userid", col], value_vars=attributes,
var_name=y, value_name=hue)
df[hue] = df[hue].apply(lambda x: int(x) if x == round(x) else int(round(x)))
df[hue] = df[hue].astype("category")

group_count = df.groupby([y, hue, col]).count().iloc[:,0]
group_sum = df.groupby([y, col]).count().iloc[:,0]
group_percent = (group_count / group_sum) \
    .mul(100).rename(x)
freq_table = group_percent.reset_index() \
    .sort_values(by=[y, hue, col], ascending=False) \
    .round(0)
freq_table

# top3_table = freq_table[freq_table[hue].isin([5, 6, 7])] \
#     .groupby([y]).sum().reset_index().sort_values(by=[x], ascending=False)
# y_order = top3_table[y].tolist()

# Draw Plot
fig = freq_table.pipe(
    lambda df: px.bar(
        data_frame=df, x=x, y=y, color=hue, #category_orders={y: y_order},
        barmode="relative", template="seaborn", text=x,
        color_discrete_sequence=px.colors.diverging.Tealrose,
        facet_col=col, facet_col_spacing=0.1, facet_row_spacing=0.1, 
        facet_col_wrap =2
        ))
fig.show()
