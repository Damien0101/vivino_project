import sqlite3
import pandas as pd

# count of global awards for wine by country

connection = sqlite3.connect('data/vivino.db')

cursor = connection.cursor()

sql_query = """
SELECT c.name AS country, COUNT(*) AS count
FROM vintage_toplists_rankings AS vi
JOIN toplists AS t ON vi.top_list_id = t.id
JOIN vintages AS v ON v.id = vi.vintage_id
JOIN wines AS w ON v.wine_id = w.id
JOIN regions AS r ON r.id = w.region_id
JOIN countries AS c ON c.code = r.country_code
WHERE t.country_code = 'global'
GROUP BY c.name;
"""

cursor.execute(sql_query)

results = cursor.fetchall()

# Get the column names from the cursor
column_names = [description[0] for description in cursor.description]

df = pd.DataFrame(results, columns=column_names)

df.to_csv('data/global_awards_wine.csv', index=False)

cursor.close()
connection.close()