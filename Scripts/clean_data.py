# clean_data.py
import pandas as pd

def load_data(path="data/diabetic_data.csv"):
    df = pd.read_csv(path)
    # Example cleaning step
    df = df.dropna(subset=["race"])
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
