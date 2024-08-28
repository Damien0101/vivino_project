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

df4 = pd.read_csv('data/cabernet.csv', encoding='latin1')
df4.sort_values(['ratingAVG','ratingCOUNT'], ascending=False, inplace=True)
fig3 = px.bar(df4.head(5), x='name', y='ratingAVG', color='price', title='Top 5 Cabernet Sauvignon wines by rating')

df5 = pd.read_csv('data/priceAVG_per_country.csv', encoding='latin1')
df5.sort_values('rantingAVG', ascending=False, inplace=True)
fig4 = px.bar(df5, x='country', y='rantingAVG', color='priceAVG', title='Average price of wine per country')

df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
most_expensive_wine = df6.sort_values('price_euros', ascending=False).head(3).reset_index()

most_loved_wine = df6.sort_values(['ratings_average', 'ratings_count'], ascending=False).head(3).reset_index()

df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
best_year = df6.groupby('year', as_index=False)[['price_euros', 'ratings_average', 'ratings_count']].mean()
best_year.sort_values('ratings_average', ascending=False, inplace=True)
fig = px.bar(best_year, x=best_year['year'], y=best_year['ratings_average'], color=best_year['ratings_count'], title='Best year for wine')

best_wine_from1998 = df6.loc[df6['year'] == '1998'].sort_values(['ratings_average', 'ratings_count'], ascending=False).head(3).reset_index()
best_wine_from1998

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
st.subheader("Average price of wine per country")
if st.button("Show plot", key='show_plot4'):
    st.plotly_chart(fig4)
    st.write("Based on this plot we can tell that the best wine are from Australia, USA and Greece. We can also tell that French wines are not that expensive compared to their rating")
st.subheader("Top 5 Cabernet Sauvignon wines by rating")
if st.button("Show plot", key='show_plot3'):
    st.plotly_chart(fig3)
    st.write("Here's our top 5 recommandation for Cabernet Sauvignon wines based on their rating and price")