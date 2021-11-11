import pandas as pd
import plotly.express as px

df = pd.read_csv('scatter.csv')
fig = px.scatter(df, x = 'Date', y = 'Cases', color = 'Country', size_max = 30, title = 'COVID Cases')
fig.show()