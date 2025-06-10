import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load analyzed reviews
df = pd.read_csv('analyzed_reviews.csv')

# 1. Sentiment trend over time (line plot)
df['date'] = pd.to_datetime(df['date'])
df['date_month'] = df['date'].dt.to_period('M')
plt.figure(figsize=(12,6))
for bank in df['bank'].unique():
    monthly_sentiment = df[df['bank'] == bank].groupby('date_month')['sentiment'].mean()
    plt.plot(monthly_sentiment.index.astype(str), monthly_sentiment.values, marker='o', label=bank)
plt.title('Sentiment Trend Over Time by Bank')
plt.xlabel('Month')
plt.ylabel('Average Sentiment')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sentiment_trend_over_time.png')
plt.close()

# 2. Rating distribution (histogram)
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='rating', hue='bank', multiple='dodge', bins=5, palette='Set2')
plt.title('Rating Distribution by Bank')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.savefig('rating_distribution_by_bank.png')
plt.close()

# 3. Bank comparison (violin plot for sentiment)
plt.figure(figsize=(10,6))
sns.violinplot(x='bank', y='sentiment', data=df, palette='Set1')
plt.title('Sentiment Comparison Across Banks')
plt.xlabel('Bank')
plt.ylabel('Sentiment Polarity')
plt.savefig('sentiment_comparison_violin.png')
plt.close()

print('Additional visualizations saved: sentiment_trend_over_time.png, rating_distribution_by_bank.png, sentiment_comparison_violin.png')
