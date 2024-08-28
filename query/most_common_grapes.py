import sqlite3
import pandas as pd
import csv


con : sqlite3.Connection = sqlite3.connect('data/vivino.db')
cur : sqlite3.Cursor = con.cursor()

cur.execute('''
SELECT
        grapes.name,
        most_used_grapes_per_country.wines_count
    FROM
        grapes
    JOIN
        most_used_grapes_per_country ON grapes.id = most_used_grapes_per_country.grape_id
    GROUP BY
        grapes.id
''')

rows = cur.fetchall()

with open('data/most_comm.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow(['grape_name', 'wines_count'])
    csvfile.writerows(rows)

con.close()