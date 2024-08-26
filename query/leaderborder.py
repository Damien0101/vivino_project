import sqlite3
import pandas as pd

connection = sqlite3.connect('data/vivino.db')

cursor = connection.cursor()

# We would like to create a country leaderboard. 
# Come up with a visual that shows the **average wine rating for each `country`**. 

sql_query = """
SELECT  c.name AS country_name,
       AVG(w.ratings_average) AS rating

  FROM wines AS w
       JOIN
       regions AS r ON w.region_id = r.id
       JOIN
       countries AS c ON c.code = r.country_code
GROUP BY country_name
ORDER BY rating DESC;
"""

cursor.execute(sql_query)

results = cursor.fetchall()

# Get the column names from the cursor
column_names = [description[0] for description in cursor.description]

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=column_names)

# Write the DataFrame to a CSV file
df.to_csv('data/leaders.csv', index=False)


cursor.close()
connection.close()