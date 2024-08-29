#  Vivino Project 🍷🍷

## 📜 Project Description
#### The Vivino project is designed to answer key questions about the wine market using data from Vivino. Utilizing SQL for querying, Plotly for interactive visualizations, and Streamlit for a web-based interface, this project provides valuable insights into wine trends, prices, and market dynamics. It aims to help Vivino users and industry professionals better understand the wine market and identify growth opportunities thanks to the data.. ####

[![N|Solid](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP._myDh4nle6wYFGPGxAfzcgHaDn%26pid%3DApi&f=1&ipt=95eb30229bd8d514c3605abbe01b169acfd9521a071089801c66b7d26caf85e0&ipo=images "easter egg")](loveUantoine.png)

***click on the image to analize the graphs...***

## 👀 Project Overview 

- #### data: Contains raw data files (CSV) and a database (vivino.db) with comprehensive wine-related data used for analysis.

- #### query: Includes Python scripts that utilize SQL queries to analyze various aspects of the wine market, such as identifying top wine-producing countries, analyzing wine prices, and understanding grape varieties. 

- #### visual: Houses visualization files created with Plotly to provide interactive and insightful representations of the data.

- #### app.py: The main application script that deploys a Streamlit web interface, allowing users to explore data and visualizations in an interactive format.. 

- #### requirements.txt: Lists all Python dependencies required to run the project, ensuring a smooth setup process.



## 🤖 Sample Code 
```python
cursor.execute("""
SELECT name, price_euros, ratings_average, ratings_count
FROM vintages
WHERE price_euros < 65
ORDER BY ratings_average DESC
LIMIT 10;
""")

rows = cursor.fetchall()

with open('data/top_ten.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([i[0] for i in cursor.description])
    csvwriter.writerows(rows)
```

## ⏱️ Project Timeline 

### 1. Project Setup and Exploration

Set up the environment, repository, and explore the database to understand data structure.

### 2.  Querying the Database

Develop and execute SQL queries to extract relevant insights from the wine data.

### 3. Making Visualizations

Create interactive visualizations using Plotly to illustrate key findings.

### 4. Creation of the App

Build a Streamlit app for interactive exploration of data and visualizations.

## ⛓️ Project Directory Structure 

```plaintext
VINIVO_PROJECT
│
├── data
│   ├── <csv files>
|   └── vivino.db
│
├── query
│   └── <query files>
|
├── visual
│   └── <visualization files>
│
├── app.py
├── README.md
└── requirements.txt
```
   

## 🔧  Installation

### To run the app locally, follow these steps :

1. #### Clone the repository :

    
    ```sh
    git clone https://github.com/servietsky0/vinivo_project
    ```
    

2. #### Navigate into the cloned repository :

    
    ```sh
    cd ../Vivino_project 
    ```


3. #### Install the necessary dependencies using pip :

    
    ```sh
    pip install -r requirements.txt
    ```
    

4. #### Once you did all the these steps, type this commande in the terminal :

   ```sh
   streamlit run app.py
   ```
      
    #### Or visit :
    [vivino deployed app](https://vinivoproject-v7jiussdmfd2tavvkxcycp.streamlit.app/) 

## 🎉 Have Fun!

#### *I trust you'll find joy in using my app, just as much joy as I had in developing it! Every graph is a step towards a more comprehensible view of the wine market.*  🚀