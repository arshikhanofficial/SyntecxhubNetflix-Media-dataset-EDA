import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):

    # Fill missing values
    df['director'] = df['director'].fillna("Unknown")
    df['cast'] = df['cast'].fillna("Unknown")
    df['country'] = df['country'].fillna("Unknown")

    # Fix date column
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

    # Extract year added
    df['year_added'] = df['date_added'].dt.year

    return df