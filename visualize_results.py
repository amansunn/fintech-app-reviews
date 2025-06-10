import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load analyzed reviews
df = pd.read_csv('analyzed_reviews.csv')

# 1. Sentiment distribution per bank
plt.figure(figsize=(10,6))
sns.boxplot(x='bank', y='sentiment', data=df)
plt.title('Sentiment Distribution per Bank')
plt.ylabel('Sentiment Polarity')
plt.xlabel('Bank')
plt.savefig('sentiment_distribution_per_bank.png')
plt.close()

# 2. Bar chart of top 10 keywords per bank
for bank in df['bank'].unique():
    keywords = sum(df[df['bank'] == bank]['keywords'].apply(eval).tolist(), [])
    freq = pd.Series(keywords).value_counts().head(10)
    plt.figure(figsize=(8,4))
    sns.barplot(x=freq.values, y=freq.index, palette='viridis')
    plt.title(f'Top 10 Themes for {bank}')
    plt.xlabel('Frequency')
    plt.ylabel('Theme')
    plt.tight_layout()
    plt.savefig(f'top_themes_{bank}.png')
    plt.close()

# 3. Word cloud per bank
for bank in df['bank'].unique():
    keywords = sum(df[df['bank'] == bank]['keywords'].apply(eval).tolist(), [])
    text = ' '.join(keywords)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {bank}')
    plt.savefig(f'wordcloud_{bank}.png')
    plt.close()

print('Visualizations saved: sentiment_distribution_per_bank.png, top_themes_<bank>.png, wordcloud_<bank>.png')
