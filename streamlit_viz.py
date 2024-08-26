import streamlit as st

import plotly.express as px 
import plotly.graph_objects as go
import pandas as pd




# Load the dataframe from the csv file with specified encoding
df = pd.read_csv('data/first.csv', encoding='latin1')
print(df)
#create a bar plot with the data
fig = go.Figure()

fig.add_trace(
    go.Bar(name="Price", x=df['name'], y=df['price'], offsetgroup=0)
)

fig.add_trace(
    go.Bar(name="Rating Average", x=df['name'], y=df['ratingAVG'], yaxis='y2', offsetgroup=1)
)

fig.update_layout(
    title = "Top 10 best affordables Wines with best rating",
    yaxis=dict(
        title="Price (€)",
    ),

    yaxis2=dict(
        title="Rating Average",
        overlaying='y',
        side='right',
    ),
    xaxis=dict(
        title="name",
    ),
    barmode='group',
    )



st.title("🍷 Vivino Project 🍷")
st.subheader("Top 10 best affordables Wines with best rating")


if st.button("Show plot"):
    st.plotly_chart(fig)
    