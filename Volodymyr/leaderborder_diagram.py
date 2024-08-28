import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# We would like to create a country leaderboard. 
# Come up with a visual that shows the **average wine rating for each `country`**.

# Read the CSV file into a DataFrame
df = pd.read_csv('data/leaders.csv')

df = pd.DataFrame(df, columns=['country_name', 'rating'])

plt.figure(figsize=(10, 6))  # Set the figure size
sns.barplot(x='country_name', y='rating', data=df, palette='viridis')

# Add titles and labels
plt.title('The Average Rating of countries', fontsize=16)

plt.ylabel('rating', fontsize=14)
plt.xlabel('country_name', fontsize=14)
# Rotate x-tick labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()  # Adjusts plot to ensure everything fits without overlapping
plt.show()