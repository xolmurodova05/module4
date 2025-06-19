import pandas as pd

def ingest_data(filepath):
    df = pd.read_csv(filepath)
    # Add cleaning and transformation logic
    return df