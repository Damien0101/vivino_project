import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to center the title and subheader
def center_text(text, header_type="title"):
    if header_type == "title":
        st.markdown(f"<h1 style='text-align: center;'>{text}</h1>", unsafe_allow_html=True)
    elif header_type == "subheader":
        st.markdown(f"<h3 style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)

def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{"https://img.getimg.ai/generated/img-AC5fvN41TJTfmXzn3uOjo.jpeg"}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
                /* General text color */
        .stMarkdown, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown li {{
            color: #FFFFFFF; /* Black text */
      
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image (replace 'your_image.jpg' with the actual path)
set_background('visual/vivino_background.jpg')


# Set the title of the app (centered)
center_text('🍷 Vivino Project 🍷', header_type="title")

# Sidebar for navigation
st.sidebar.title('Navigate through the analysis')
st.sidebar.subheader('Choose a section to explore')

# List of pages available for navigation in the sidebar
topic_names = [
    'Top 10 Wines 🔟',
    'Best affordable country 💸',
    'Best taste 👅',
    'Most used Grapes 🍇',
    'Country leaderboard for Vintages Wines 🏆',
    'Country leaderboard for Wines 🏆',
    'Top 5 recommendations for Cabernet Sauvignon 🎊',
    'Most expensive wine 🤑',
    'Best year for wine 🍾',
    'Best wine from 1998 🎉',
    'Global awards for wine by country 🏆',
    'Link between ratingAVG and url length 📏'
]

# Sidebar radio button for page selection
page = st.sidebar.radio('', topic_names)

# Page 1: Display the Top 10 Wines
if page == 'Top 10 Wines 🔟':
    top10 = pd.read_csv('data/top_ten.csv', encoding='latin1')
    top10.sort_values('ratingAVG', ascending=True, inplace=True)
    top10 = px.bar(top10, x='name', y='price', color='ratingAVG', color_continuous_scale='sunsetdark')
    center_text('Top 10 affordable wines with the best rating (< 65€)', header_type="subheader")
    st.plotly_chart(top10)

# Page 2: Best affordable country based on wine ratings and price
if page == 'Best affordable country 💸':
    df1 = pd.read_csv('data/best_countries.csv', encoding='latin1')
    countries = df1.groupby('country', as_index=False)[['price', 'rating', 'wine count']].median()
    countries["median_price"] = countries["price"].median()
    countries.sort_values('price', ascending=True, inplace=True)
    best_country = px.bar(countries, x='country', y=['price'], color='rating', color_continuous_scale='sunsetdark')
    best_country.add_trace(go.Scatter(x=countries['country'], y=countries['median_price'], mode='lines', name='Median price', line=dict(color='red', width=3)))
    center_text('💸 Best affordable country 💸', header_type="subheader")
    st.write("Based on this plot, we can tell that for our little budget we should go for Moldavia since it's cheap and has a rating average above the median.")
    st.plotly_chart(best_country)

# Page 3: Display the best tasting wines
if page == 'Best taste 👅':
    tastiest_wines = pd.read_csv('data/best_taste.csv', encoding='latin1')
    tastiest_wines.drop(columns=['taste', 'keyword_count'], inplace=True)
    tastiest_wines.set_index('wine', inplace=True)
    tastiest_wines.sort_values(['ratingAVG', 'ratingCOUNT'], ascending=False, inplace=True)
    center_text('👅 Best taste 👅', header_type="subheader")
    st.write("Here are all the wines with the specific taste you are looking for, along with their rating score and the number of ratings they received.")
    st.table(tastiest_wines)

# Page 4: Display the most used grapes and their top wines
if page == 'Most used Grapes 🍇':
    wines = pd.read_csv('data/wine_table.csv', encoding='latin1')
    wines = wines.drop(columns=['id','is_natural','region_id','winery_id','acidity','fizziness','intensity','sweetness','tannin','user_structure_count'])
    cabern_sauv_top5 = wines[wines['name'].str.contains('Cabernet Sauvignon')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    Chard_top5 = wines[wines['name'].str.contains('Chardonnay')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    pinot_top5 = wines[wines['name'].str.contains('Pinot Noir')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    center_text('🍇 Most used Grapes 🍇', header_type="subheader")
    st.write('Based on our research, here are the top 5 wines for the most used grapes, (Cabernet Sauvignon, Chardonnay, Pinot Noir)')
    center_text('Top 5 Cabernet Sauvignon wines by rating', header_type="subheader")
    st.table(cabern_sauv_top5)
    center_text('Top 5 Chardonnay wines by rating', header_type="subheader")
    st.table(Chard_top5)
    center_text('Top 5 Pinot Noir wines by rating', header_type="subheader")
    st.table(pinot_top5)

# Page 5: Country leaderboard for Vintages Wines
if page == 'Country leaderboard for Vintages Wines 🏆':
    df5 = pd.read_csv('data/priceAVG_per_country.csv', encoding='latin1')
    df5.sort_values('rantingAVG', ascending=False, inplace=True)
    fig4 = px.bar(df5, x='country', y='rantingAVG', title='Average rating of vintage wine per country', color='rantingAVG', color_continuous_scale='sunsetdark')
    center_text('🏆 Country leaderboard for Vintages Wines 🏆', header_type="subheader")
    st.plotly_chart(fig4)
    center_text('Here we can see that the best Vintage Wines are from Australia 🦘', header_type="subheader")

# Page 6: Country leaderboard for Wines
if page == 'Country leaderboard for Wines 🏆':
    wine_price_avg_per_country = pd.read_csv('data/wine_price_per_country.csv', encoding='latin1')
    wine_price_avg_per_country.sort_values('rantingAVG', ascending=False, inplace=True)
    fig5 = px.bar(wine_price_avg_per_country, x='country', y='rantingAVG', color='rantingAVG', color_continuous_scale='sunsetdark', title='Average price of wine per country')
    center_text('🏆 Country leaderboard for Wines 🏆', header_type="subheader")
    st.plotly_chart(fig5)
    st.write('Here we can see that the best wines are from Hungary 🍻')

# Page 7: Top 5 recommendations for Cabernet Sauvignon
if page == 'Top 5 recommendations for Cabernet Sauvignon 🎊':
    wines = pd.read_csv('data/wine_table.csv', encoding='latin1')
    wines = wines.drop(columns=['id','is_natural','region_id','winery_id','acidity','fizziness','intensity','sweetness','tannin','user_structure_count'])
    cabern_sauv_top5 = wines[wines['name'].str.contains('Cabernet Sauvignon')].sort_values(['ratings_average','ratings_count'], ascending=False).head(5)
    center_text("Top 5 Cabernet Sauvignon wines by rating for our VIP client", header_type="subheader")
    st.table(cabern_sauv_top5)
    st.write("Since it's the most used grape in the world, it's the same as previously")

# Page 8: Most expensive wine
if page == 'Most expensive wine 🤑':
    df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
    df6 = df6.drop(columns=['id','wine_id','price_discounted_from','price_discount_percentage','bottle_volume_ml'])
    most_expensive_wine = df6.sort_values('price_euros', ascending=False).head(3).reset_index()
    center_text('Here are the most expensive wines in our database', header_type="subheader")
    st.table(most_expensive_wine)

# Page 9: Best year for wine
if page == 'Best year for wine 🍾':
    df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
    best_year = df6.groupby('year', as_index=False)[['price_euros', 'ratings_average', 'ratings_count']].mean()
    fig = px.bar(best_year, x=best_year['year'], y=best_year['ratings_average'], color=best_year['ratings_count'], color_continuous_scale='sunsetdark', title='Best year for wine')
    st.plotly_chart(fig)
    center_text('Based on this plot, we can tell that the best year for wine is 1979 since it has the best rating average for years', header_type="subheader")

# Page 10: Best wine from 1998
if page == 'Best wine from 1998 🎉':
    df6 = pd.read_csv('data/vintage_table.csv', encoding='latin1')
    df6 = df6.drop(columns=['id','wine_id','price_discounted_from','price_discount_percentage','bottle_volume_ml'])
    best_wine_from1998 = df6.loc[df6['year'] == '1998'].sort_values(['ratings_average', 'ratings_count'], ascending=False).head(3).reset_index()
    center_text('Here are the best wines from 1998 (our beloved Coach’s birth year 🎂)', header_type="subheader")
    st.table(best_wine_from1998)

# Page 11: Global awards for wine by country
if page == 'Global awards for wine by country 🏆':
    df = pd.read_csv('data/global_awards_wine.csv')
    total_count = df['count'].sum()
    df['count'] = (df['count'] * 100) / total_count
    fig = px.pie(df, values='count', names='country', title='Count of global awards for wine by Country')
    fig.update_layout(title={'text': 'Count of Global Awards for Wine by Country', 'x': 0.5, 'xanchor': 'center'})
    st.plotly_chart(fig)


# Page 12: Link between ratingAVG and URL length
if page == 'Link between ratingAVG and url length 📏':
    df7 = pd.read_csv('data/wine_table.csv', encoding='latin1')
    df7['url'] = df7['url'].apply(len)
    df7 = df7.groupby('url', as_index=False)['ratings_average'].mean()
    fig = px.line(df7, x='url', y='ratings_average', title='Link between rating average and url length',color_discrete_sequence= ['purple'])
    center_text('Here is the link between rating average and url length', header_type="subheader")
    st.plotly_chart(fig)
