import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('data/top_ten.csv', encoding='latin1')
fig = px.bar(df, x='name', y='price', color='ratingAVG', color_continuous_scale='Blues')
df1 = pd.read_csv('data/best_countries.csv', encoding='latin1')

countries = df1.groupby('country', as_index=False)[['price', 'rating', 'wine count']].median()
countries["median_price"] = countries["price"].median()
countries.sort_values('price', ascending=True, inplace=True)

fig2 = px.bar(countries, x='country', y=['price'], color='rating',color_continuous_scale='Blues')
fig2.add_trace(go.Scatter(x=countries['country'], y=countries['median_price'], mode='lines', name='Median price', line=dict(color='red', width=3)))

tastiest_wines = pd.read_csv('data/best_taste.csv', encoding='latin1')
tastiest_wines.drop(columns=['taste','keyword_count'], inplace=True)
tastiest_wines.set_index('wine', inplace=True)
tastiest_wines.sort_values('ratingAVG', ascending=False, inplace=True)


st.set_page_config(
page_title="Vivino",
page_icon="knot",
)

source_link =  "Show link to source code repository"
repo_url = "https://github.com/servietsky0/vinivo_project"
info_hosting = f"Host your own Hangman interface using {repo_url}"

st.title("🍷 Vivino Project 🍷")

if st.sidebar.checkbox(source_link):
    st.info(info_hosting)

if st.sidebar.checkbox('Top 10 best affordables Wines with best rating'):
    st.subheader("Top 10 best affordables Wines with best rating")
    st.plotly_chart(fig)

if st.sidebar.checkbox("Median price and rating per country"):
    st.subheader('Median price and rating per country')
    st.plotly_chart(fig2)
    st.write("Based on this plot, we can tell that for our little budget we should go for Moldavia since it's cheap and as a rating average above the median.")

if st.sidebar.checkbox('Wines with the best taste'):
    st.subheader('Wines with the best taste')
    st.table(tastiest_wines)
    st.write('...')


