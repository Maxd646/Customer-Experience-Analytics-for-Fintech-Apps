import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://play.google.com/store/apps/details?id=com.kifiya.leolla"
OUTPUT_PATH = "data/raw/reviews_raw.csv"

def extract_reviews():
    reviews = []
    for page in range(1, 6):
        print(f"Scraping page {page}...")
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        review_elements = soup.find_all("div", {"class": "RHo1pe"})

        for r in review_elements:
            text = r.text.strip()
            if len(text) > 0:
                reviews.append(text)

        time.sleep(1)

    df = pd.DataFrame({"review": reviews})
    df.to_csv(OUTPUT_PATH, index=False)
    print("Scraping complete →", OUTPUT_PATH)


if __name__ == "__main__":
    extract_reviews()
