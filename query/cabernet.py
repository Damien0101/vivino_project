import sqlite3
import pandas as pd
import csv

# Create a connection and get a cursor
con : sqlite3.Connection = sqlite3.connect('data/vivino.db')
cur : sqlite3.Cursor = con.cursor()

cur.execute('''
SELECT
    vintages.name,
    vintages.ratings_average,
    vintages.ratings_count,
    vintages.year,
    vintages.price_euros
FROM 
    vintages
WHERE vintages.name LIKE '%Cabernet Sauvignon%' 
''')

row : list[any]= cur.fetchall()

with open('data/cabernet.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow(['name', 'ratingAVG', 'ratingCOUNT', 'year', 'price'])
    csvfile.writerows(row)

con.close()