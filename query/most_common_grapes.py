import sqlite3
import pandas as pd
import csv


con : sqlite3.Connection = sqlite3.connect('data/vivino.db')
cur : sqlite3.Cursor = con.cursor()

cur.execute('''
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
''')

rows = cur.fetchall()

with open('data/most_comm.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow(['country', 'wine_per_country', 'grape', 'wine', 'ratingAVG', 'ratingCOUNT'])
    csvfile.writerows(rows)

con.close()