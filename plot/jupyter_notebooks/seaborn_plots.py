# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: data_viz_with_seaborn
#     language: python
#     name: data_viz_with_seaborn
# ---

# %% [markdown]
# # Import packages

# %%
# %reload_ext autoreload
import seaborn as sns
import matplotlib.pyplot as plt
import squarify
import pandas as pd
import numpy as np
from plot import plot, plot_utils
import utils
# %matplotlib inline

# %% [markdown]
# # Settings

# %%
# Seaborn settings
plot.seaborn_settings()

# %% [markdown]
# # Global variables

# %%
vars_selection = {
    "cat_vars": ["race", "gender", "relationship", "income"],
    "num_vars": ["age", "hours-per-week", "capital-gain", "capital-loss"],
    "time_vars": [],
}

cues = ["x", "y", "hue", "size", "row", "col"]

# %% [markdown]
# # Load data

# %%
# Load data in memory
df = plot.load_data("6_adult.csv", sep=",")
df = plot.filter_data(df, vars_selection)
plot_taxanomy = plot.load_data("plot_taxanomy.csv")

# Create output dir
output_dir = plot_utils.create_output_dir("dataviz_gallery/static/img/seaborn")

# Clean folder
plot_utils.remove_files_in_dir("dataviz_gallery/static/img/seaborn")

# %% [markdown]
# # Glimpse at data

# %%
df.head(5)

# %% [markdown]
# # Define order of usage in plots

# %%
# Categorical vars
first_cat = "race"
second_cat = "gender"
third_cat = "relationship"
fourth_cat = "income"

# Numerical vars
first_num = "age"
second_num = "hours-per-week"
third_num = "capital-gain"
fourth_num = "capital-loss"

# %% [markdown]
# # Plots

# %% [markdown]
# ## 2D Density Plot

# %% [markdown]
# ## 3D Scatter Plot

# %% [markdown]
# ## Arc Diagramm

# %% [markdown]
# ## Area Chart

# %% [markdown]
# ## Bar Plot

# %% [markdown]
# ### Simple Bar Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x = "relationship"
file_path = output_dir / "simple_bar_plot.png"

# Data Transformation
freq_table = df[x].value_counts(normalize=True) \
    .mul(100).rename("percent").reset_index().rename(columns={"index": x}) \
    .sort_values("percent", ascending=False)

# Draw Plot
g = freq_table.pipe(lambda df: sns.catplot(data=df, x="percent", y=x, kind='bar', color=sns.color_palette()[0]))
g.set(xlim=(0, 100))

# Decoractions
ax = g.ax
for bar in ax.patches:
    value = format(bar.get_width(), '.1f')
    y_pos = bar.get_y() + bar.get_height()/2
    x_pos = bar.get_width()
    ax.text(s=value, x=x_pos, y=y_pos, horizontalalignment='left', verticalalignment='center')
    
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Grouped Bar Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, y = "gender", "relationship" 
file_path = output_dir / "grouped_bar_plot.png"

# Data Transformation
group_count = df.groupby([y, x]).count().iloc[:,0]
group_sum = df.groupby([y]).count().iloc[:,0]
group_percent = (group_count / group_sum).mul(100).rename("percent")
freq_table = group_percent.reset_index()

# Draw Plot
g = freq_table.pipe(lambda d: sns.catplot(data=d, y=y, x="percent", hue="gender", kind='bar'))
g.set(xlim=(0, 110))

# Decorations
ax = g.ax
for bar in ax.patches:
    value = format(bar.get_width(), '.0f')
    y_pos = bar.get_y() + bar.get_height()/2
    x_pos = bar.get_width()
    ax.text(s=value, x=x_pos, y=y_pos, horizontalalignment='left', verticalalignment='center')

plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Single Facetted Grouped Bar Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, y, col = "gender", "relationship", "race" 
file_path = output_dir / "single_facetted_grouped_bar_plot.png"

# Data Transformations
group_count = df.groupby([col, y, x]).count().iloc[:,0]
group_sum = df.groupby([col, y]).count().iloc[:,0]
group_percent = (group_count / group_sum).mul(100).rename("percent")
freq_table = group_percent.reset_index()

# Draw Plot
g = freq_table.pipe(lambda d: sns.catplot(data=d, y=x, x="percent", col=col, col_wrap=3, height=2, aspect=2, kind='bar', ci=None))
g.set_titles(col_template="{col_name}")
g.set(xlim=(0, 100))

# Decorations
axes = g.axes
for ax in axes:
    for bar in ax.patches:
        value = format(bar.get_width(), '.0f')
        y_pos = bar.get_y() + bar.get_height()/2
        x_pos = bar.get_width()*0.95
        ax.text(s=value, x=x_pos, y=y_pos, horizontalalignment='right', verticalalignment='center')

plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Dual Facetted Grouped Bar Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, y, col, row = "gender", "relationship", "race", "income" 
file_path = output_dir / "dual_facetted_grouped_bar_plot.png"

# Data transformations
group_count = df.groupby([row, col, y, x]).count().iloc[:,0]
group_sum = df.groupby([row, col, y]).count().iloc[:,0]
group_percent = (group_count / group_sum).mul(100).rename("percent")
freq_table = group_percent.reset_index()

# Draw Plot
g = freq_table.pipe(lambda d: sns.catplot(data=d, x="percent", y=x, row=row, col=col, height=2, aspect=2, kind='bar', ci=None, margin_titles=True))
g.set_titles(col_template="{col_name}", row_template="{row_name}")
g.set(xlim=(0, 100))

plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Simple Stacked Bar Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, y = "gender", "race"
file_path = output_dir / "simple_stacked_bar_plot.png"

# Data transformations
group_count = df.groupby([y, x]).count().iloc[:,0]
group_sum = df.groupby([y]).count().iloc[:,0]
group_percent = (group_count / group_sum).mul(100).rename("percent")
freq_table = group_percent.reset_index()
pivot_table = freq_table.pivot(index=y, columns=x, values='percent')

# Decorations
colors = [sns.color_palette()[i] for i in range(len(pivot_table.index))]

# Draw Plot
pivot_table.plot.bar(stacked=True, color=colors, figsize=(10,7), )
plt.savefig(file_path, dpi=300)

# - Add title
# - Take ordinal variables and order by top1/top2/top3 (depending on scale) 

# %% [markdown]
# ## Box Plot

# %% [markdown]
# ### Simple Box Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "simple_box_plot.png"
x, y = "relationship", "age"

# Data transformations
order = df.groupby(by=[x])[y].median().sort_values(ascending=False).index

# Draw Plot
g = sns.catplot(data=df, x=x, y=y, kind="box", order=order)
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Grouped Box Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "grouped_boxplot.png"
x, y, hue = "relationship", "age", "gender"

# Data Transformations
# order = df.groupby(by=["relationship", "gender"])["age"].median()# .sort_values(ascending=False).index

# Draw Plot
g = sns.catplot(data=df, x=x, y=y, hue=hue, kind="box")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Single Facetted Box Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "single_facetted_box_plot.png"
y, col = "age", "relationship"

# Data transformations
order = df.groupby(by=[col])[y].median().sort_values(ascending=False).index

# Draw Plot
g = sns.catplot(data=df, y=y, col=col, col_wrap=3, height=4, aspect=1, kind="box", col_order=order)
g.set_titles(col_template="{col_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Single Facetted Grouped Box Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "single_facetted_grouped_box_plot.png"
x, y, hue, col = "age", "relationship", "gender", "income"

# Data transformations
# order = df.groupby(by=["relationship"])["age"].median().sort_values(ascending=False).index

# Draw Plot
g = sns.catplot(data=df, x=x, y=y, hue=hue, col=col, col_wrap=3, height=6, aspect=1, kind="box")
g.set_titles(col_template="{col_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Dual Facetted Box Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "dual_facetted_box_plot.png"
x, y, row, col = "age", "relationship", "gender", "income"

# Data transformations
# order = df.groupby(by=["relationship"])["age"].median().sort_values(ascending=False).index

# Draw Plot
g = sns.catplot(data=df, x=x, y=y, row=row, col=col, height=4, aspect=1, kind="box", margin_titles=True)
g.set_titles(col_template="Income {col_name}", row_template="{row_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Dual Facetted Box Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "dual_facetted_grouped_box_plot.png"
x, y, hue, row, col = "age", "relationship", "gender", "income", "race"

# Data transformations
# order = df.groupby(by=["relationship"])["age"].median().sort_values(ascending=False).index

# Draw Plot
g = sns.catplot(data=df, x=x, y=y, hue=hue, col=col, row=row, height=4, aspect=1, kind="box", margin_titles=True)
g.set_titles(col_template="{col_name}", row_template="Income {row_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ## Bubble Map

# %% [markdown]
# ## Bubble Plot

# %% [markdown]
# ## Bullet Graph

# %% [markdown]
# - References: https://pbpython.com/bullet-graph.html

# %% [markdown]
# ## Bump Chart

# %% [markdown]
# ## Candlestick Chart

# %% [markdown]
# ## Cartogram

# %% [markdown]
# ## Chord Diagram

# %% [markdown]
# ## Connection Map

# %% [markdown]
# ## Contour Plot

# %% [markdown]
# ## Correlogram

# %% [markdown]
# ## Dendrogram

# %% [markdown]
# ## Density Plot

# %% [markdown]
# ## Donut Chart

# %% [markdown]
# ### Simple Donut Chart

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
hue = "gender" 
file_path = output_dir / "simple_donut_chart.png"

# Data transformations
freq_table = df[hue].value_counts(normalize=True) \
    .mul(100).rename('percent').reset_index() \
    .sort_values('percent', ascending=True).rename(columns={"index": hue})
# labels = freq_table.apply(lambda x: str(x[0]) + "\n" + str(round(x[1],1)) + "%", axis=1).tolist()
labels = freq_table[hue].unique()

# Draw Plot
circle = plt.Circle( (0,0), 0.7, color='white')
fig, ax = plt.subplots(figsize=(10,10))
plt.pie(x=freq_table["percent"].values, startangle=90, autopct='%1.1f%%', pctdistance=0.85, labels=labels,
        wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
ax.axis('equal')
p = plt.gcf()
p.gca().add_artist(circle)
plt.savefig(file_path, dpi=300)

# References
# https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html
# https://matplotlib.org/3.3.3/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py
# https://python-graph-gallery.com/160-basic-donut-plot/
# https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.pie.html
# https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f

# %% [markdown]
# ## Dumbbell Plot

# %% [markdown]
# ## Fan Chart

# %% [markdown]
# ## Gauge Chart

# %% [markdown]
# ## Donut Chart

# %% [markdown]
# ## Heat Map

# %% [markdown]
# ### Simple Heat Map

# %%
import seaborn as sns
import matplotlib.pyplot as plt
from string import ascii_letters

file_path = output_dir / "simple_histogram.png"
sns.set_theme(style="white")

# Generate a large random dataset
rs = np.random.RandomState(33)
df = pd.DataFrame(data=rs.normal(size=(100, 26)),
                 columns=list(ascii_letters[26:]))

# Data Transformations
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

# Draw Plot
f, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(corr, mask=mask, cmap="viridis", vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.savefig(file_path, dpi=300)

# %% [markdown]
# ## Hexbin Map

# %% [markdown]
# ## Histogram

# %% [markdown]
# ### Simple Histogram

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x = "age"
file_path = output_dir / "simple_histogram.png"

# Draw Plot
g = sns.displot(data=df, x=x, bins=10, kind="hist")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Grouped Histogram

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, hue = "age", "gender"
file_path = output_dir / "grouped_histogram.png"

# Draw Plot
p = sns.displot(data=df, x=x, hue=hue, kind="hist", bins=10)
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Single Facetted Histogram

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "single_facetted_histogram.png"
x, col = "age", "gender"

# Draw Plot
g = sns.displot(data=df, x=x, col=col, col_wrap=3, height=4, aspect=1, kind="hist", bins=10)
g.set_axis_labels(x="age")
g.set_titles("{col_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Single Facetted Grouped Histogram

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "single_facetted_grouped_histogram.png"
x, hue, col = "age", "gender", "race"

g = sns.displot(data=df, x=x, hue=hue, col=col, col_wrap=3, height=4, aspect=1, kind="hist", bins=10)
g.set_axis_labels(x=x)
g.set_titles("{col_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Dual Facetted Histogram

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "dual_facetted_histogram.png"
x, row, col = "age", "gender", "race"

g = sns.displot(data=df, x=x, row=row, col=col, height=4, aspect=1, kind="hist", bins=10)
g.set_titles(col_template="{col_name}", row_template="{row_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ### Dual Facetted Grouped Histogram

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
file_path = output_dir / "dual_facetted_grouped_histogram.png"
x, hue, row, col = "age", "gender", "income", "race"

g = sns.displot(data=df, x=x, hue=hue, row=row, col=col, height=4, aspect=1, kind="hist", bins=10)
g.set_titles(col_template="{col_name}", row_template="Income {row_name}")
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ## Line Chart

# %% [markdown]
# ### Simple Line Chart

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")

# Initialize variables and output path
file_path = output_dir / "simple_line_chart.png"
x, y = "Date", "AveragePrice"

# # Data Transformations
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# Draw Plot 
g = sns.relplot(data=df, x=x, y=y, kind="line", height=4, aspect=4)

# %% [markdown]
# ### Grouped Line Chart

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/8_avocado.csv")

# Initialize variables and output path
file_path = output_dir / "grouped_line_chart.png"
x, y, hue = "Date", "AveragePrice", "type"

# # Data Transformations
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# Draw Plot 
g = sns.relplot(data=df, x=x, y=y, hue="type", kind="line", height=4, aspect=4)

# %% [markdown]
# ## Lollipop Chart

# %% [markdown]
# ## Marimekko Chart

# %% [markdown]
# ## Non ribbon Chord Diagram

# %% [markdown]
# ## Parallel Coordinate Plot

# %% [markdown]
# ### Simple Parallel Coordinate Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x = "gender"
file_path = output_dir / "simple_parallel_coordinate_plot.png"

# Data transformations
cols = [x] + ["age", "hours-per-week", "capital-gain", "capital-loss"]
df = df[cols]

# Decorations
labels = df[x].unique()
colors = [sns.color_palette()[i] for i in range(len(labels))]

# Draw Plot
pd.plotting.parallel_coordinates(
    df, x, color=colors
)
plt.savefig(file_path, dpi=300)

# - Smaller Dataset with numerical variables on a similar scale, survey

# %% [markdown]
# ## Parallel Sets

# %% [markdown]
# ## Pareto Chart

# %% [markdown]
# ## Pie Chart

# %% [markdown]
# ### Simple Pie Chart

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
hue = "gender" 
file_path = output_dir / "simple_pie_chart.png"

# Data transformations
freq_table = df[hue].value_counts(normalize=True) \
    .mul(100).rename('percent').reset_index() \
    .sort_values('percent', ascending=False).set_index("index")

# Draw Plot
p = freq_table.pipe(lambda d: d.plot(kind='pie', y="percent", autopct='%1.1f%%'))
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ## Point Map

# %% [markdown]
# ## Population Pyramid

# %% [markdown]
# ### Simple Population Pyramid

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, y = "gender", "age_categories" 
file_path = output_dir / "simple_population_pyramid.png"

# Data transformations
cut_labels = ["0 to 19 years", "20 to 29 year", "30 to 39 years", "40 to 49 years", "50 to 59 years", "60 to 69 years", "70 to 79 years", "80 to 89 years", "90 or more years"]
cut_bins = [0, 19, 29, 39, 49, 59, 69, 79, 89, 120]
df[y] = pd.cut(df["age"], bins=cut_bins, labels=cut_labels)

groups = df[x].unique()
colors = [sns.color_palette()[i] for i in range(len(groups))]
bar_order = cut_labels

group_count = df.groupby([y, x]).count().iloc[:,0]
group_sum = df.groupby([y]).count().iloc[:,0]
group_percent = (group_count / group_sum).mul(100).rename("percent")
freq_table = group_percent.reset_index()
freq_table["percent"] = freq_table.apply(lambda x: x[2] * -1 if x[1] == groups[0] else x[2], axis=1)  # 

# Draw Plot
plt.figure(figsize=(10,6), dpi= 80)
for c, g in zip(colors, groups):
    sns.barplot(x="percent", y=y, data=freq_table.loc[freq_table[x]==g, :], order=bar_order, color=c, label=g)

# Decorations
plt.xlim((-100,100))
plt.ylabel("Stage of Purchase")
plt.yticks(fontsize=12)
plt.title("Population Pyramid", fontsize=22)
plt.legend()
plt.savefig(file_path, dpi=300)

# %% [markdown]
# ## Ridgeline Plot

# %% [markdown]
# ### Simple Ridgeline Plot

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = output_dir / "simple_ridgeline_plot.png"

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="race", hue="gender", aspect=14, height=.5, palette=pal)

# Draw the densities in a few steps
g.map(sns.kdeplot, "age", bw_adjust=.5, clip_on=False, fill=True, alpha=1, linewidth=1.5)
#g.map(sns.kdeplot, "age", clip_on=False, color="w", lw=2, bw_adjust=.5)
#g.map(plt.axhline, y=0, lw=2, clip_on=False)

# # Define and use a simple function to label the plot in axes coordinates
# def label(x, color, label):
#     ax = plt.gca()
#     ax.text(0, .2, label, fontweight="bold", color=color,
#             ha="left", va="center", transform=ax.transAxes)


# g.map(label, "x")

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.25)

# # Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)

# %%
df.head(5)

# %% [markdown]
# ## Sankey Diagram

# %% [markdown]
# ## Scatter Plot

# %% [markdown]
# ### Simple Scatter Plot

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x, y = "age", "hours-per-week" 
file_path = output_dir / "simple_scatter_plot.png"

g = sns.lmplot(data=df, x=x, y=y)
# Find a better dataset

# %% [markdown]
# ## Slope Chart

# %% [markdown]
# ## Small Multiples

# %% [markdown]
# ## Spider Chart

# %% [markdown]
# ### Simple Spider Chart

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = "gender"
# num_vars = ["age", "hours-per-week", "capital-gain", "capital-loss"]
file_path = output_dir / "simple_spider_chart.png"
group_mean = df.groupby([x]).mean().apply(np.log)  # log for better comparison
mean_table = group_mean.reset_index()
group1 = mean_table[mean_table[x] == "Male"].iloc[:,1:]

# labels = ["age", "hours-per-week", "capital-gain", "capital-loss"]
# angles = np.linspace(0, 2*np.pi, len(labels))
# angles = np.append(angles, [0])

# fig = plt.figure()
# ax = fig.add_subplot(111, polar=True)
# # ax.set_theta_offset(pi / 2)
# # ax.set_theta_direction(-1)
# plt.xticks(angles[0:4], labels)

# Ressources: https://python-graph-gallery.com/391-radar-chart-with-several-individuals/
# https://medium.com/python-in-plain-english/radar-chart-basics-with-pythons-matplotlib-ba9e002ddbcd
# https://www.kaggle.com/typewind/draw-a-radar-chart-with-python-in-a-simple-way
# Find a better dataset, survey probably good, because of similar scaling

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
x = "gender"
file_path = output_dir / "simple_spider_chart.png"

# Data Transformation
labels = ["age", "hours-per-week", "capital-gain", "capital-loss"]
labels_and_groups = [x] + labels
mean_table = df.groupby([x]).mean().apply(np.log).reset_index().loc[:, labels_and_groups]
male_values = mean_table[mean_table[x]=="Male"].loc[:, labels].values.tolist()[0]
female_values = mean_table[mean_table[x]=="Female"].loc[:, labels].values.tolist()[0]

# # Department Names in the Organisation
# Depts = ["COGS","IT","Payroll","R & D", "Sales & Marketing"]

# # rp is the planned spend for each of the departments respectively for a given year. 
# # ra is the actual spend. 
# # Since it is a circular spider web, we need to connect the last point to first point, 
# # so that circle gets completed. 
# # In order to achieve this, we need to repeat first department data at the end of the list again. 
# # Hence, 30 and 32 first entry in each of the lists are repeated at the end again.
# rp = [30, 15, 25, 10, 20, 30]
# ra = [32, 20, 23, 11, 14, 32]

# Initialise the spider plot by setting figure size and polar projection
plt.figure(figsize=(10,6))
plt.subplot(polar=True)

# Split 2 pie radians(360 degrees) into number of departments equally. matplotlib.pyplot 
# accepts in radians only.
# To convert radians to degrees use np.degrees(theta)
theta = np.linspace(0, 2 * np.pi, len(labels))

# Arrange the grid into number of departments equal parts in degrees(NOT in radians here, 
# but degrees)
(lines, labels) = plt.thetagrids(range(0,360, int(360/len(labels))), (labels))

# Plot planned spend graph, which is a line plot on polar co-ordiantes
plt.plot(theta, male_values)
# Fill the area under the line plot
plt.fill(theta, male_values, 'b', alpha=0.1)

# Plot actual spend graph, which is a line plot on polar co-ordiantes
plt.plot(theta, female_values)

# Add legend and title for the plot
plt.legend(labels=('Plan','Actual'),loc=1)
plt.title("Plan vs Actual spend by Department")

# Dsiplay the plot on the screen
plt.show();

# %% [markdown]
# ## Stepped Line Graph

# %% [markdown]
# ## Stream Graph

# %% [markdown]
# ## Tornado Chart

# %% [markdown]
# ## Tree Map

# %% [markdown]
# ### Simple Tree Map

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/6_adult.csv")

# Initialize variables and output path
size = "relationship"
file_path = output_dir / "simple_tree_map.png"

# Data Transformations
freq_table = df[size].value_counts().rename('count').reset_index() \
    .sort_values("count", ascending=False).rename(columns={"index": hue})
sizes = freq_table["count"].values.tolist()
labels = freq_table.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
colors = [sns.color_palette()[i] for i in range(len(labels))]

# Draw Plot
plt.figure(figsize=(10,6), dpi=100)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
plt.axis('off')
plt.savefig(file_path, dpi=300)

# Further documentation: https://github.com/laserson/squarify

# %% [markdown]
# ## Violin Plot

# %% [markdown]
# ## Waterfall Chart
