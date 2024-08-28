import pandas as pd
import plotly.express as px

# 
df = pd.read_csv('data/best_taste_country.csv')

# 
df = pd.DataFrame(df, columns=['taste', 'keyword_count','wine','ratingAVG','ratingCOUNT'])


if df.empty:
    print("The DataFrame is empty. Please check the CSV file.")
else:
     # Filter to get rows where 'ratingCOUNT' is greater than 4.5
    filtered_df = df[df['ratingCOUNT'] > 4.5]
    top_tastes = filtered_df.nlargest(10, 'ratingCOUNT')
    fig = px.bar(top_tastes, x='ratingCOUNT', y='taste', orientation='h', 
                 color='taste', title='Top 10 taste wine (count of ratings and rating > 4.5)',
                 color_discrete_sequence=px.colors.qualitative.Set2)  # Choose a color sequence
    
    # Center the title
    fig.update_layout(title_x=0.5)  # Center the title

    fig.show()