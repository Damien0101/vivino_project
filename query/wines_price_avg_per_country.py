import sqlite3
import csv

conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()


cursor.execute("""
    SELECT countries.name, wines.ratings_average
    FROM wines
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
    GROUP BY countries.name
""")

rows = cursor.fetchall()

with open('data/wine_price_per_country.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['country', 'rantingAVG']) 
    csvwriter.writerows(rows)  

conn.close()

