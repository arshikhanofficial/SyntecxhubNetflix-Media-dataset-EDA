def count_content_type(df):

    type_counts = df['type'].value_counts()

    print("\nMovies vs TV Shows")
    print(type_counts)

    return type_counts


def top_release_years(df):

    top_years = df['release_year'].value_counts().head(10)

    print("\nTop 10 Release Years")
    print(top_years)

    return top_years


def top_genres(df):

    genres = df['listed_in'].str.split(', ').explode()

    top_genres = genres.value_counts().head(10)

    print("\nTop 10 Genres")
    print(top_genres)

    return top_genres