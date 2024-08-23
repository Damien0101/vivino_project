import pandas as pd
# One of our VIP clients likes _Cabernet Sauvignon_ and would like our top 5 recommendations. 
# Which wines would you recommend to him?

# Read the CSV file into a DataFrame
df = pd.read_csv('data/cabernet_sauvignon_results.csv')

# Convert the list of tuples to a DataFrame
advise = pd.DataFrame(df, columns=['Wine', 'Average Rating', 'Year', 'Price (€)', 'Region', 'Country'])

print("The best wine Cabernet Sauvignon")
print(df)