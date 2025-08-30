import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Preview
print(df.head())
print(df.info())

# 1. Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title("Count of Movies vs TV Shows on Netflix")
plt.show()

# 2. Content added per year
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='release_year', palette='coolwarm', order=sorted(df['release_year'].dropna().unique()))
plt.title("Content Release Year Trend")
plt.xticks(rotation=90)
plt.show()

# 3. Top 10 genres
df['listed_in'] = df['listed_in'].fillna('')
all_genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = all_genres.value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

# 4. Top 10 countries producing content
df['country'] = df['country'].fillna('')
all_countries = df['country'].str.split(',').explode().str.strip()
top_countries = all_countries.value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='mako')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Count")
plt.ylabel("Country")
plt.show()


