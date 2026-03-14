import matplotlib.pyplot as plt
import seaborn as sns


def plot_type_distribution(type_counts):

    plt.figure(figsize=(6,4))
    sns.barplot(x=type_counts.index, y=type_counts.values)

    plt.title("Movies vs TV Shows")
    plt.xlabel("Type")
    plt.ylabel("Count")

    plt.savefig("type_distribution.png")
    plt.show()


def plot_content_growth(df):

    year_counts = df['release_year'].value_counts().sort_index()

    plt.figure(figsize=(10,5))
    year_counts.plot()

    plt.title("Content Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")

    plt.savefig("content_growth.png")
    plt.show()


def plot_top_genres(top_genres):

    plt.figure(figsize=(10,6))

    sns.barplot(x=top_genres.values, y=top_genres.index)

    plt.title("Top 10 Genres")

    plt.savefig("top_genres.png")
    plt.show()