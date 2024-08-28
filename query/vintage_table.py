import sqlite3
import csv

con = sqlite3.connect('data/vivino.db')
cur = con.cursor()

cur.execute(
    '''
    SELECT * FROM vintages
'''
)

row = cur.fetchall()

with open('data/vintage_table.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow([i[0] for i in cur.description])
    csvfile.writerows(row)

con.close()