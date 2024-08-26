import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/priceAVG_per_country.csv')

# User selects the sorting order
type_plot = st.selectbox('Select type of plot', options=["Average price", "Rating"])
order = st.selectbox('Select the sorting order', options=["asc", "desc"])

# Determine the plot based on user selection
if type_plot == 'Average price':
    x1 = 'country'
    y1 = 'priceAVG'
    title1 = 'Average Price by Country'
    labels1 = {'priceAVG': 'Average Price (Euros)', 'country': 'Countries'}
    color1 = 'priceAVG'
    text1 = 'priceAVG'
    xaxis_title1 = 'Countries'
    yaxis_title1 = 'Average Price (Euros)'
elif type_plot == 'Rating':
    x1 = 'country'
    y1 = 'rantingAVG'
    title1 = 'Average Rating by Country'
    labels1 = {'rantingAVG': 'Average Rating', 'country': 'Countries'}
    color1 = 'rantingAVG'  # Removed comma
    text1 = 'rantingAVG'
    xaxis_title1 = 'Countries'
    yaxis_title1 = 'Average Rating'

# Sort the DataFrame based on user selection
if order == 'asc' and type_plot == 'Average price':
    df = df.sort_values(by='priceAVG')
elif order == 'desc'and type_plot == 'Average price':
    df = df.sort_values(by='priceAVG', ascending=False)
elif order == 'asc' and type_plot == 'Rating':
    df = df.sort_values(by='rantingAVG')
elif order == 'desc'and type_plot == 'Rating':
    df = df.sort_values(by='rantingAVG', ascending=False)



# Create the bar chart
fig = px.bar(df, x=x1, y=y1,
             title=title1,
             labels=labels1,
             color=color1,
             text=text1)

# Update the figure's aesthetics
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  
fig.update_layout(xaxis_tickangle=-45,
                  plot_bgcolor='rgba(0,0,0,0)',  
                  xaxis_title=xaxis_title1,
                  yaxis_title=yaxis_title1,
                  title_x=0.5)

# Display the plotly chart in Streamlit
st.plotly_chart(fig)