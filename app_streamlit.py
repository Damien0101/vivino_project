import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



st.title('🍷 Vivino Project 🍷')
st.sidebar.title('Navigate trought the analysis')
st.sidebar.subheader('Choose a section to explore')
start_names = ['Top 10 Wines 🔟',
                'Best affordable country 💸',
                  'Best taste 👅',
                    'Most used Grapes 🍇',
                    'Country leaderboard for Vintages Wines 🏆',
                    'Country leaderboard for Wines 🏆',
                    'Top 5 recomandation for Cabernet Sauvignon 🎊',
                    'Most expensive wine 🤑',
                    'Best year for wine 🍾',
                    'Best wine from 1998 🎉',
                    'Link between ratingAVG and url lenght 📏'
                    ]

page = st.sidebar.radio('', start_names)

if page == 'Top 10 Wines 🔟':
    top10 = pd.read_csv('data/top_ten.csv', encoding='latin1')
    top10.sort_values('ratingAVG', ascending=True, inplace=True)
    top10 = px.bar(top10, x='name', y='price', color='ratingAVG', color_continuous_scale='sunsetdark')
    st.subheader('Top 10 affordable wines with the best rating (< 65€)')
    st.plotly_chart(top10)

if page =='Best affordable country 💸':
    df1 = pd.read_csv('data/best_countries.csv', encoding='latin1')
    countries = df1.groupby('country', as_index=False)[['price', 'rating', 'wine count']].median()
    countries["median_price"] = countries["price"].median()
    countries.sort_values('price', ascending=True, inplace=True)
    best_country = px.bar(countries, x='country', y=['price'], color='rating',color_continuous_scale='sunsetdark')
    best_country.add_trace(go.Scatter(x=countries['country'], y=countries['median_price'], mode='lines', name='Median price', line=dict(color='red', width=3)))
    st.subheader("Based on this plot, we can tell that for our little budget we should go for Moldavia since it's cheap and as a rating average above the median.")
    st.plotly_chart(best_country)

if page == 'Best taste 👅':
    tastiest_wines = pd.read_csv('data/best_taste.csv', encoding='latin1')
    tastiest_wines.drop(columns=['taste','keyword_count'], inplace=True)
    tastiest_wines.set_index('wine', inplace=True)
    tastiest_wines.sort_values(['ratingAVG','ratingCOUNT'], ascending=False, inplace=True)
    st.subheader("Here are all the wine with the specific taste you are looking for, with their rating score and amout of rating they received.")
    st.table(tastiest_wines)

if page == 'Most used Grapes 🍇':
    wines = pd.read_csv('data/wine_table.csv', encoding='latin1')
    wines = wines.drop(columns=['id','is_natural','region_id','winery_id','acidity','fizziness','intensity','sweetness','tannin','user_structure_count'])
    cabern_sauv_top5 = wines[wines['name'].str.contains('Cabernet Sauvignon')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    Chard_top5 = wines[wines['name'].str.contains('Chardonnay')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    pinot_top5 = wines[wines['name'].str.contains('Pinot Noir')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    st.subheader('Based on our research, here are the top 5 wines for the most used grapes, (Cabernet Sauvignon, Chardonnay, Pinot Noir)')
    st.subheader('Top 5 Cabernet Sauvignon wines by rating')
    st.table(cabern_sauv_top5)
    st.subheader('Top 5 Chardonnay wines by rating')
    st.table(Chard_top5)
    st.subheader('Top 5 Pinot Noir wines by rating')
    st.table(pinot_top5)

if page == 'Country leaderboard for Vintages Wines 🏆':
    df5 = pd.read_csv('data/priceAVG_per_country.csv', encoding='latin1')
    df5.sort_values('rantingAVG', ascending=False, inplace=True)
    fig4 = px.bar(df5, x='country', y='rantingAVG', title='Average price of vintage wine per country', color='priceAVG', color_continuous_scale='sunsetdark')
    st.plotly_chart(fig4)
    st.subheader('Here we can see that the best Vintage Wines are from Australia 🦘')

if page == 'Country leaderboard for Wines 🏆':
    wine_price_avg_per_country = pd.read_csv('data/wine_price_per_country.csv', encoding='latin1')
    wine_price_avg_per_country.sort_values('rantingAVG', ascending=False, inplace=True)
    fig5 = px.bar(wine_price_avg_per_country, x='country', y='rantingAVG', color='rantingAVG', color_continuous_scale='sunsetdark', title='Average price of wine per country')
    st.plotly_chart(fig5)

if page == 'Top 5 recomandation for Cabernet Sauvignon 🎊':
    wines = pd.read_csv('data/wine_table.csv', encoding='latin1')
    cabern_sauv_top5 = wines[wines['name'].str.contains('Cabernet Sauvignon')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    st.subheader("Top 5 Cabernet Sauvignon wines by rating for our VIP client")
    st.table(cabern_sauv_top5)
    st.subheader("Since it's the most used grape in the world, it's the same as previously")

if page == 'Most expensive wine 🤑':
    df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
    df6 = df6.drop(columns=['id','wine_id','price_discounted_from','price_discount_percentage','bottle_volume_ml'])
    most_expensive_wine = df6.sort_values('price_euros', ascending=False).head(3).reset_index()
    st.subheader('Here are the most expensive wines in our database')
    st.table(most_expensive_wine)

if page == 'Best year for wine 🍾':
    df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
    best_year = df6.groupby('year', as_index=False)[['price_euros', 'ratings_average', 'ratings_count']].mean()
    best_year.sort_values('ratings_average', ascending=False, inplace=True)
    fig = px.bar(best_year, x=best_year['year'], y=best_year['ratings_average'], color=best_year['ratings_count'], color_continuous_scale='sunsetdark', title='Best year for wine')
    st.plotly_chart(fig)
if page == 'Best wine from 1998 🎉':
    df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
    df6 = df6.drop(columns=['id','wine_id','price_discounted_from','price_discount_percentage','bottle_volume_ml'])
    best_wine_from1998 = df6.loc[df6['year'] == '1998'].sort_values(['ratings_average', 'ratings_count'], ascending=False).head(3).reset_index()
    st.subheader('Here are the best wines from 1998')
    st.table(best_wine_from1998)

if page == 'Link between ratingAVG and url lenght 📏':
    df = pd.read_csv('data/wine_table.csv', encoding='latin1')
    df['lenght_url'] = df['url'].apply(len)
    funnny_df = df.groupby('lenght_url', as_index=False)['ratings_average'].mean()
    fig = px.line(funnny_df, x='lenght_url', y='ratings_average', color_discrete_sequence=['purple'], title='Funny graph')
    st.plotly_chart(fig)