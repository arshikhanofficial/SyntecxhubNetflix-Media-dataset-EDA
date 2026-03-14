from src.datacleaning import load_data, clean_data
from src.analysis import count_content_type, top_release_years, top_genres
from src.visualization import plot_type_distribution, plot_content_growth, plot_top_genres


def main():

    # Load dataset
    df = load_data("data/netflix_titles.csv")

    # Clean dataset
    df = clean_data(df)

    # Analysis
    type_counts = count_content_type(df)

    top_years = top_release_years(df)

    genres = top_genres(df)

    # Visualizations
    plot_type_distribution(type_counts)

    plot_content_growth(df)

    plot_top_genres(genres)


if __name__ == "__main__":
    main()