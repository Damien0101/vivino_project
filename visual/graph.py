import plotly.express as px 
import plotly.graph_objects as go
import pandas as pd

# Load the dataframe from the csv file with specified encoding
df = pd.read_csv('data/first.csv', encoding='latin1')
df = df.drop(index=0)
df = df.drop(index=1)
print(df)
#create a bar plot with the data
fig = go.Figure(data=[
    go.Bar(name='Price', x=df['name'], y=df['price']),
    go.Line(name='Rating AVG', x=df['name'], y=df['ratingAVG'])
])
fig.show()

