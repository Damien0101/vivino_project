import sqlite3
import csv

conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()


cursor.execute("""
    SELECT countries.name, round(avg(vintages.price_euros)), vintages.ratings_average
    FROM vintages
    JOIN wines ON vintages.wine_id = wines.id
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
    GROUP BY countries.name
""")

rows = cursor.fetchall()

with open('data/priceAVG_per_country.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['country', 'priceAVG', 'rantingAVG']) 
    csvwriter.writerows(rows)  

conn.close()

