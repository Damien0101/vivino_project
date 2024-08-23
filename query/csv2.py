import sqlite3
import csv


conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

# avg wine price per country

cursor.execute("""
    SELECT round(avg(vintages.price_euros)), countries.name
    FROM vintages
    JOIN wines ON vintages.wine_id = wines.id
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
    GROUP BY countries.name
""")

rows = cursor.fetchall()

with open('data/second.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['priceAVG', 'countries']) 
    csvwriter.writerows(rows)  

conn.close()
