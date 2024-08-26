import sqlite3
import pandas as pd

# Open the file
f = open('tasty.csv', 'w')

# Create a connection and get a cursor
con = sqlite3.connect('db/vivino.db')
cur = con.cursor()

query_tasty = f'''
SELECT 
    keywords.name AS taste,
    keywords_wine.count AS keyword_count,
    wines.name AS wine,
    wines.ratings_average,
    wines.ratings_count
FROM 
    wines
JOIN 
    keywords_wine ON wines.id = keywords_wine.wine_id
JOIN 
    keywords ON keywords.id =keywords_wine.keyword_id
WHERE 
    keywords_wine.count > 10;
'''

# Execute the query
cur.execute(query_tasty)

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