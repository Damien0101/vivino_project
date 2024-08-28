import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/global_awards_wine.csv')

if 'country' in df.columns and 'count' in df.columns:

    total_count = df['count'].sum()

    df['count'] = (df['count'] * 100) / total_count
    
    fig = px.pie(df, values='count', names='country', title='Count of global awards for wine by Country')
    fig.update_layout(title={'text': 'Count of Global Awards for Wine by Country', 'x': 0.5, 'xanchor': 'center'})
    
    fig.show()
else:
    print("The required columns 'country' and 'count' are not present in the CSV file.")