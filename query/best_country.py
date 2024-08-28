import sqlite3
import csv

conn : sqlite3.Connection = sqlite3.connect('data/vivino.db')
cursor : sqlite3.Cursor = conn.cursor()

cursor.execute("""
    SELECT wines.name, vintages.price_euros, countries.name, wines.ratings_average, countries.wines_count
    FROM wines
    JOIN vintages ON wines.id = vintages.wine_id
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
""")

rows : list[any] = cursor.fetchall()

with open('data/best_countries.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['wine', 'price', 'country', 'rating', 'wine count']) 
    csvwriter.writerows(rows)  

# cursor = conn.cursor()
