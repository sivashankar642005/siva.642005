import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")
#data cleaning
df.info()
df.isnull().sum()
# Drop rows where title is missing
df = df.dropna(subset=['title'])
df['release_year'] = df['release_year'].astype('int')
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
df = df.drop_duplicates()




# Set style for plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Content Type Distribution
type_counts = df['type'].value_counts()

# 2. Growth in content over the years
content_growth = df['date_added'].value_counts().sort_index()

# 3. Country-wise content count (splitting multiple countries)
country_series = df['country'].str.split(', ', expand=True).stack()
country_counts = country_series.value_counts()

# 4. Top 10 countries with most content
top_countries = country_counts.head(10)

# Plotting
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Plot 1: Content type distribution
sns.barplot(x=type_counts.index, y=type_counts.values, ax=axes[0], palette='Set2')
axes[0].set_title("Content Type Distribution on Netflix")
axes[0].set_ylabel("Count")
axes[0].set_xlabel("Content Type")

# Plot 2: Growth of content over the years
sns.lineplot(x=content_growth.index, y=content_growth.values, marker='o', ax=axes[1])
axes[1].set_title("Growth of Netflix Content Over the Years")
axes[1].set_ylabel("Number of Titles Added")
axes[1].set_xlabel("Year Added")

# Plot 3: Top 10 countries by number of titles
sns.barplot(x=top_countries.values, y=top_countries.index, ax=axes[2], palette='coolwarm')
axes[2].set_title("Top 10 Countries with Most Netflix Content")
axes[2].set_xlabel("Number of Titles")
axes[2].set_ylabel("Country")

plt.tight_layout()
plt.show()
