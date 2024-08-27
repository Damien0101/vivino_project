import sqlite3
import csv

con = sqlite3.connect('data/vivino.db')
cur = con.cursor()

cur.execute('''
SELECT 
    keywords.name AS taste,
    keywords_wine.count AS keyword_count,
    wines.name AS wine,
    ROUND(AVG(wines.ratings_average),1) AS avg_by_taste,
    SUM(wines.ratings_count) AS total_ratings
FROM 
    wines
JOIN 
    keywords_wine ON wines.id = keywords_wine.wine_id
JOIN 
    keywords ON keywords.id =keywords_wine.keyword_id
WHERE 
    keywords_wine.count > 10
GROUP BY keywords.name
ORDER BY total_ratings DESC, avg_by_taste DESC;
''')

row = cur.fetchall()
with open('data/best_taste.csv', 'w', newline='') as file:
    csvfile = csv.writer(file)
    csvfile.writerow(['taste', 'keyword_count', 'wine', 'ratingAVG', 'ratingCOUNT'])
    csvfile.writerows(row)


"""
We detected that a big cluster of customers likes a specific combination of tastes.
We identified a few keywords that match these tastes: coffee, toast, green apple, cream,
and citrus (note that these keywords are case sensitive ⚠️). We would like you to find 
all the wines that are related to these keywords. Check that at least 10 users confirm those 
keywords, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.
"""

con.close()