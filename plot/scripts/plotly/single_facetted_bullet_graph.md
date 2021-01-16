```python
import plotly.graph_objects as go
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/13_indian_ecommerce_sales.csv", index_col=[0])

# Initialize variables and parameters
metric_cur, metric_prev, target, row = "Current Revenue", "Previous Revenue", "Current Target", "Category"
start_domain_y = 0.1
end_domain_y = 0.9
space_between_graphs_y = 0.15
space_available_y = end_domain_y - start_domain_y - (space_between_graphs_y * (len(categories)-1))
space_per_graph_y = space_available_y / len(categories)

# Data Transformation
df = df[df["Month of Order Date"] == "2018-05"]
categories = df["Category"].unique()

# Draw Plot
fig = go.Figure()

categories = df["Category"].unique()
for index, category in enumerate(categories):
    plot_number = index+1
    print(plot_number)

    # Each filtered dataframe contains only one row
    filtered_df = df[df["Category"] == category]
    metric_cur_example = filtered_df.iloc[0].loc[metric_cur]
    metric_prev_example = filtered_df.iloc[0].loc[metric_prev]
    target_example = filtered_df.iloc[0].loc[target]

    # Position of Graph on Y-Axis
    if plot_number == 1:  # First Plot
            domain = {'x': [0.15, 1], 'y': [0.1, start_domain_y + space_per_graph_y]}

    elif plot_number == len(categories):  # Last Plot
        domain = {'x': [0.15, 1], 'y': [
            start_domain_y + ((plot_number-1)*space_per_graph_y) + ((plot_number-1)*space_between_graphs_y),
            end_domain_y
            ]}

    else: # Every Plot in between
        domain = {'x': [0.15, 1], 'y': [
            start_domain_y + ((plot_number-1)*space_per_graph_y) + space_between_graphs_y,
            start_domain_y + ((plot_number-1)*space_per_graph_y) + ((plot_number-1)*space_between_graphs_y) + space_per_graph_y,
            ]}

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = metric_cur_example,
        domain = domain,
        title = {'text' :f"<b>{category}</b>"},
        delta = {'reference': metric_prev_example},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 15000]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': target_example},
            'steps': [
                {'range': [0, 6000], 'color': "lightgray"},
                {'range': [6000, 10000], 'color': "gray"}]}))
fig.show()
```