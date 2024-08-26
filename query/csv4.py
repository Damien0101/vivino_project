import sqlite3
import csv

conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

cursor.execute("""     
    SELECT name FROM wines;
""")

# I want a csv with wineries with the most wines produced and best rating for the wines

rows = cursor.fetchall()

with open('data/fourth.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['winerie', 'wine name', 'wine rating']) 
    csvwriter.writerows(rows)  


