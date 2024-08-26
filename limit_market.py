import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('data/second.csv')


order = st.selectbox('Select the sorting order', options=["asc", "desc"])

if order == 'asc':
    df = df.sort_values(by='priceAVG')
elif order == 'desc':
    df = df.sort_values(by='priceAVG', ascending=False)

fig = px.bar(df, x='countries', y='priceAVG',
             title='Average Price by Country',
             labels={'priceAVG': 'Average Price (Euros)', 'countries': 'Countries'},
             color='priceAVG',
             text='priceAVG')



fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  
fig.update_layout(xaxis_tickangle=-45,
                  plot_bgcolor='rgba(0,0,0,0)',  
                  xaxis_title='Countries',
                  yaxis_title='Average Price (Euros)',
                  title_x=0.5)


st.plotly_chart(fig) 