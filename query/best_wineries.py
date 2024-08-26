import sqlite3
import csv

conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

cursor.execute("""     
    SELECT wines.name, ratings_count, avg(ratings_average)
    FROM wines
    GROUP BY name.ratings_average
    ORDER BY ratings_count DESC
    LIMIT 3;
""")

# I want a csv with wineries with the most wines produced and best rating for the wines

rows = cursor.fetchall()

with open('data/best_wineries.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['wine name', 'rating count', 'wine rating']) 
    csvwriter.writerows(rows)  


