import sqlite3
import csv


conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

cursor.execute("""
SELECT name, price_euros, ratings_average, ratings_count
FROM vintages
WHERE ratings_average >= 4.5
ORDER BY price_euros ASC, ratings_count DESC
LIMIT 10;
""")

rows = cursor.fetchall()

with open('first.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['name', 'price', 'ratingAVG', 'ratingCOUNT'])
    csvwriter.writerows(rows)

conn.close()
