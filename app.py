import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load the dataframe from the csv file with specified encoding
df = pd.read_csv('data/top_ten.csv', encoding='latin1')

# Create a bar plot with the data
fig = px.bar(df, x='name', y='price', color='ratingAVG', color_continuous_scale='Blues')

# Load and process the second dataframe
df1 = pd.read_csv('data/best_countries.csv', encoding='latin1')

countries = df1.groupby('country', as_index=False)[['price', 'rating', 'wine count']].median()
countries["median_price"] = countries["price"].median()
print(countries)
countries.sort_values('price', ascending=True, inplace=True)


fig2 = px.bar(countries, x='country', y=['price'], color='rating',color_continuous_scale='Blues')

fig2.add_trace(go.Scatter(x=countries['country'], y=countries['median_price'], mode='lines', name='Median price', line=dict(color='red', width=3)))



tastiest_wines = pd.read_csv('data/best_taste.csv', encoding='latin1')
tastiest_wines.drop(columns=['taste','keyword_count'], inplace=True)
tastiest_wines.set_index('wine', inplace=True)
tastiest_wines.sort_values('ratingAVG', ascending=False, inplace=True)




# Streamlit app layout
st.title("🍷 Vivino Project 🍷")
st.subheader("Top 10 best affordables Wines with best rating")

if st.button("Show plot", key='show_plot'):
    st.plotly_chart(fig)
st.subheader("Median price and rating per country")
if st.button("Show plot", key='show_plot2'):
    st.plotly_chart(fig2)
    st.write("Based on this plot, we can tell that for our little budget we should go for Moldavia since it's cheap and as a rating average above the median.")
st.subheader("Wines with the best taste")
if st.button("Show table"):
    st.table(tastiest_wines)
