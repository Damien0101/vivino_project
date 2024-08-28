import sqlite3
import pandas as pd
import csv


con : sqlite3.Connection = sqlite3.connect('data/vivino.db')
cur : sqlite3.Cursor = con.cursor()

cur.execute('''
SELECT 
    DISTINCT keywords.name AS taste,
    keywords_wine.count AS keyword_count,
    wines.name AS wine,
    wines.ratings_average,
    wines.ratings_count
FROM 
    wines
JOIN 
    keywords_wine ON wines.id = keywords_wine.wine_id
JOIN 
    keywords ON keywords.id =keywords_wine.keyword_id
WHERE 
    keywords_wine.count > 10 AND 
    keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
GROUP BY
    wine
HAVING 
    COUNT(DISTINCT(taste)) = 5;             
''')

# row = cur.fetchall()

row : list[any] = cur.fetchall()



with open('data/best_taste.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow(['taste', 'keyword_count', 'wine', 'ratingAVG', 'ratingCOUNT'])
    csvfile.writerows(row)

con.close()