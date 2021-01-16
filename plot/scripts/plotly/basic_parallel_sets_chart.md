```python
import plotly.graph_objects as go
import pandas as pd

# Load Data
df = pd.read_csv("https://raw.githubusercontent.com/m-p-esser/dataviz-with-seaborn/master/data/example_datasets/12_titanic.csv")

# Initialize variables
cols = ["Pclass", "SexualMaturity", "Sex", "Survived"]
hue = "Pclass"

# Data Transformation
df['SexualMaturity'] = df['Age'].apply(lambda x: "adult" if x > 17 else "child")
dimensions = []
for col in cols:
    if col == hue:
        dim = go.parcats.Dimension(values=df[col], label=col, categoryorder='category descending')
    else:
        dim = go.parcats.Dimension(values=df[col], label=col)
    dimensions.append(dim)

# Draw Plot
fig = go.Figure(data = [go.Parcats(dimensions=dimensions,
        line={'color': df[hue], 'colorscale': "haline"},
        hoveron='color', hoverinfo='count+probability',
        arrangement='freeform')])
fig.show()
```