```python
import plotly.graph_objects as go
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/11_personality.csv")
df.columns

# Initialize variables
hue = "enjoy_watching "
attributes = ["openness", "agreeableness", "emotional_stability", "conscientiousness", "extraversion"]

# Data Transformation
mean_table = df.groupby([hue])[attributes] \
    .mean().reset_index() \
    .round(1)

# Draw Plot
fig = go.Figure()
for index, row in mean_table.iterrows():
    mean_values = row[attributes].values.tolist()
    fig.add_trace(
        go.Scatterpolar(r=mean_values, theta=attributes, 
        fill='toself', name=row[hue])
    )

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
    )),
  showlegend=True
)
fig.show()
