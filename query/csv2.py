import sqlite3
import csv


conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT wineries.name, AVG(wines.ratings_average) as ratingAVG
    FROM wineries
    JOIN wines ON wineries.id = wines.winery_id
    GROUP BY wineries.name
    ORDER BY ratingAVG DESC
    LIMIT 3;
""")

rows = cursor.fetchall()

with open('data/second.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['winery_name', 'ratingAVG']) 
    csvwriter.writerows(rows)  

conn.close()
