import sqlite3
import pandas as pd

# Open the file
f = open('cabernet.csv', 'w')

# Create a connection and get a cursor
con = sqlite3.connect('db/vivino.db')
cur = con.cursor()

query_cabernet = f'''
SELECT
    vintages.name,
    vintages.ratings_average,
    vintages.ratings_count,
    vintages.year,
    vintages.price_euros
FROM 
    vintages
WHERE vintages.name LIKE '%Cabernet Sauvignon%' 
'''

# Execute the query
cur.execute(query_cabernet)

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