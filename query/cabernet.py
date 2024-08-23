import sqlite3
import pandas as pd

# One of our VIP clients likes _Cabernet Sauvignon_ and would like our top 5 recommendations. 
# Which wines would you recommend to him?

connection = sqlite3.connect('data/vivino.db')

cursor = connection.cursor()


sql_query = """
SELECT w.name,
       w.ratings_average,
       v.year,
       v.price_euros,
       r.name AS region_name,
       c.name AS country_name
FROM wines AS w
JOIN regions AS r ON w.region_id = r.id
JOIN countries AS c ON c.code = r.country_code
JOIN vintages AS v ON v.wine_id = w.id
WHERE w.name = 'Cabernet Sauvignon'  
ORDER BY w.ratings_average DESC
LIMIT 5;
"""

cursor.execute(sql_query)


results = cursor.fetchall()


# Get the column names from the cursor
column_names = [description[0] for description in cursor.description]

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=column_names)

# Write the DataFrame to a CSV file
df.to_csv('data/cabernet_sauvignon_results.csv', index=False)


cursor.close()
connection.close()


