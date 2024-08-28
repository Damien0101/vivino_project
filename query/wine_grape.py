import sqlite3
import csv

connect = sqlite3.connect('data/vivino.db')
cur = connect.cursor()

cur.execute(
    """
SELECT grapes.name AS grape_name, wines.name AS wine_name, wines.ratings_average, vintages.price_euros, wines.ratings_count
FROM grapes
JOIN most_used_grapes_per_country ON grapes.id = most_used_grapes_per_country.grape_id
JOIN regions ON most_used_grapes_per_country.country_code = regions.country_code
JOIN wines ON regions.id = wines.region_id
JOIN vintages ON wines.id = vintages.wine_id
WHERE grapes.name IS NOT NULL 
""")

row = cur.fetchall()

with open('data/wine_grape.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow(['grape_name', 'wine_name', 'wine_ratingAVG', 'wine_price', 'wine_ratingCOUNT'])
    csvfile.writerows(row)