import sqlite3
import pandas as pd

# Open the file
f = open('output.csv', 'w')

# Create a connection and get a cursor
con = sqlite3.connect('db/vivino.db')
cur = con.cursor()

query_grapes = f'''
SELECT 
    countries.name AS country,
    countries.wines_count AS wines_by_country,
    grapes.name AS grape,
    wines.name AS wine,
    wines.ratings_average,
    wines.ratings_count
FROM 
    countries
JOIN 
    most_used_grapes_per_country ON countries.code = most_used_grapes_per_country.country_code
JOIN 
    grapes ON most_used_grapes_per_country.grape_id = grapes.id
JOIN 
    regions ON countries.code = regions.country_code
JOIN
    wines ON regions.id = wines.region_id;
'''

# Execute the query
cur.execute(query_grapes)

# Get Header Names (without tuples)
colnames = [desc[0] for desc in cur.description]
# Get data in batches
while True:
    # Read the data
    df = pd.DataFrame(cur.fetchall())
    # We are done if there are no data
    if len(df) == 0:
        break
    # Let us write to the file
    else:
        df.to_csv(f, header=colnames)

# Clean up
f.close()
cur.close()
con.close()