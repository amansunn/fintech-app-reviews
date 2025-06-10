# Fintech App Reviews: Data Collection & Preprocessing

## Methodology

1. **Scraping**: Reviews, ratings, and dates are collected from the Google Play Store for three banks using `google-play-scraper`.
2. **Preprocessing**: Data is deduplicated, missing values are handled, and dates are normalized to `YYYY-MM-DD` format.
3. **Output**: Cleaned data is saved as a CSV with columns: `review`, `rating`, `date`, `bank`, `source`.

## Setup
- Python 3.8+
- Install dependencies: `pip install -r requirements.txt`

## Repo Structure
- `.gitignore`: Standard Python ignores + local env
- `requirements.txt`: Dependencies
- `scrape_reviews.py`: Scraping script (to be added)
- `preprocess_reviews.py`: Preprocessing script (to be added)
- `data/`: Folder for raw and processed CSVs

## Branching
- Work is done on the `task-1` branch with frequent, meaningful commits.
