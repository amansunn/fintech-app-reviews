import pandas as pd
from google_play_scraper import reviews
from datetime import datetime

# Define the apps to scrape (replace with actual app IDs for the banks)
banks = [
    {"name": "CBE", "app_id": "com.combanketh.mobilebanking"},
    {"name": "BOA", "app_id": "com.boa.boaMobileBanking"},
    {"name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"}
]

all_reviews = []

for bank in banks:
    print(f"Scraping {bank['name']}...")
    result, _ = reviews(
        bank["app_id"],
        lang='en',
        country='us',
        count=450  # Fetch a bit more to allow for cleaning
    )
    for r in result:
        all_reviews.append({
            "review": r.get("content", ""),
            "rating": r.get("score", None),
            "date": r.get("at", None),
            "bank": bank["name"],
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Save raw scraped data for review
df.to_csv("raw_reviews.csv", index=False)
print("Scraping complete. Saved to raw_reviews.csv.")
