import pandas as pd
import re

RAW_PATH = "data/raw/reviews_raw.csv"
CLEAN_PATH = "data/processed/reviews_clean.csv"

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def clean_reviews():
    df = pd.read_csv(RAW_PATH)
    df["clean_review"] = df["review"].apply(clean_text)
    df.to_csv(CLEAN_PATH, index=False)
    print("Cleaned dataset saved →", CLEAN_PATH)

if __name__ == "__main__":
    clean_reviews()
