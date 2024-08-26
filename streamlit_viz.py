import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Load the dataframe from the csv file with specified encoding
df = pd.read_csv('data/first.csv', encoding='latin1')

# Create a bar plot with the data
fig = go.Figure()

fig.add_trace(
    go.Bar(name="Price", x=df['name'], y=df['price'], offsetgroup=0)
)

fig.add_trace(
    go.Bar(name="Rating Average", x=df['name'], y=df['ratingAVG'], yaxis='y2', offsetgroup=1)
)

fig.update_layout(
    title="Top 10 best affordables Wines with best rating",
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

# Load and process the second dataframe
df1 = pd.read_csv('data/best_countries.csv')

countries = df1.groupby('country', as_index=False)[['price', 'rating', 'wine count']].median()
countries.sort_values('rating', ascending=False, inplace=True)
countries["median_price"] = countries['price'].mean()
countries["median_rating"] = countries['rating'].mean()

fig2 = go.Figure()

fig2.add_trace(
    go.Bar(name='price', x=countries['country'], y=countries['price'], offsetgroup=0)
)
fig2.add_trace(
    go.Bar(name='rating', x=countries['country'], y=countries['rating'], yaxis="y2", offsetgroup=1)
)
fig2.add_trace(
    go.Scatter(name="median_price", x=countries['country'], y=countries['median_price'], yaxis="y")
)
fig2.add_trace(
    go.Scatter(name="median_rating", x=countries['country'], y=countries['median_rating'], yaxis="y2")
)

fig2.update_layout(
    title="Median price and rating per country and wines count",
    yaxis=dict(
        title="Price (€)"
    ),
    yaxis2=dict(
        title="Rating",
        overlaying='y',
        side='right'
    ),
    barmode='group',
)

# Streamlit app layout
st.title("🍷 Vivino Project 🍷")
st.subheader("Top 10 best affordables Wines with best rating")

if st.button("Show plot", key='show_plot'):
    st.plotly_chart(fig)
if st.button("Show second plot", key='show_plot2'):
    st.subheader("Median price and rating per country")
    st.plotly_chart(fig2)
