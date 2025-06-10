import pandas as pd
from textblob import TextBlob
from collections import Counter
import re

# Load raw reviews
df = pd.read_csv('raw_reviews.csv')

# Remove duplicates based on review text and bank
df = df.drop_duplicates(subset=['review', 'bank'])

# Drop rows with missing review or rating
df = df.dropna(subset=['review', 'rating'])

# Normalize date to YYYY-MM-DD
# If 'date' is not already in datetime, convert it
if not pd.api.types.is_datetime64_any_dtype(df['date']):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# Drop rows with missing or invalid dates
df = df.dropna(subset=['date'])

# Sentiment analysis using TextBlob
def get_sentiment(text):
    if not isinstance(text, str) or not text.strip():
        return 0
    blob = TextBlob(text)
    return blob.sentiment.polarity

df['sentiment'] = df['review'].apply(get_sentiment)

def extract_keywords(text):
    # Simple keyword extraction: split, lowercase, remove short/common words
    if not isinstance(text, str):
        return []
    words = re.findall(r'\b\w{4,}\b', text.lower())
    stopwords = set(['this','that','with','have','from','they','will','your','just','about','what','when','which','their','there','would','could','should','because','very','more','some','than','like','only','also','been','were','them','then','into','over','such','most','other','after','even','back','still','being','where','those','these','does','did','has','had','for','and','the','you','but','not','are','was','all','can','out','get','use','one','app','bank'])
    return [w for w in words if w not in stopwords]

# Extract keywords for each review
df['keywords'] = df['review'].apply(extract_keywords)

# Aggregate top keywords (themes) per bank
top_themes = {}
for bank in df['bank'].unique():
    keywords = sum(df[df['bank'] == bank]['keywords'].tolist(), [])
    common = Counter(keywords).most_common(10)
    top_themes[bank] = common

# Save cleaned data
cleaned_path = 'clean_reviews.csv'
df.to_csv(cleaned_path, index=False)
print(f"Preprocessing complete. Saved to {cleaned_path}.")

# Save sentiment and themes
df.to_csv('analyzed_reviews.csv', index=False)

# Save top themes per bank to a text file
with open('bank_themes.txt', 'w', encoding='utf-8') as f:
    for bank, themes in top_themes.items():
        f.write(f"{bank} top themes:\n")
        for word, count in themes:
            f.write(f"  {word}: {count}\n")
        f.write("\n")

print("Sentiment analysis and theme extraction complete. Results saved to 'analyzed_reviews.csv' and 'bank_themes.txt'.")
