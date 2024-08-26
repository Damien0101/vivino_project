import sqlite3
import csv


conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

cursor.execute("""
SELECT name, price_euros, ratings_average, ratings_count
FROM vintages
WHERE price_euros < 65
ORDER BY ratings_average DESC
LIMIT 10;
""")

rows = cursor.fetchall()

with open('data/first.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['name', 'price', 'ratingAVG', 'ratingCOUNT'])
    csvwriter.writerows(rows)

conn.close()
