import pandas as pd
import oracledb
from datetime import datetime

# Oracle connection details
username = 'bank_reviews'
password = 'P@ssw0rd'  # Change to your actual password
host = 'localhost'
port = 1521
service = 'XEPDB1'  # Use the default pluggable database for Oracle XE 21c+

dsn = oracledb.makedsn(host, port, service_name=service)

# Read cleaned data
reviews_df = pd.read_csv('analyzed_reviews.csv')

# Connect to Oracle
conn = oracledb.connect(user=username, password=password, dsn=dsn)
cursor = conn.cursor()

# Get bank_id mapping
def get_bank_id(bank_name):
    cursor.execute("SELECT bank_id FROM banks WHERE bank_name = :name", {"name": bank_name})
    result = cursor.fetchone()
    return result[0] if result else None

# Insert reviews
def insert_reviews():
    for _, row in reviews_df.iterrows():
        bank_id = get_bank_id(row['bank'])
        if not bank_id:
            continue
        # Convert date string to datetime.date
        try:
            review_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
        except Exception:
            review_date = None
        cursor.execute(
            """
            INSERT INTO reviews (review, rating, review_date, sentiment, bank_id)
            VALUES (:review, :rating, :review_date, :sentiment, :bank_id)
            """,
            {
                'review': row['review'],
                'rating': row['rating'],
                'review_date': review_date,
                'sentiment': row['sentiment'],
                'bank_id': bank_id
            }
        )
    conn.commit()
    print('Inserted reviews into Oracle DB.')

if __name__ == "__main__":
    insert_reviews()
    cursor.close()
    conn.close()
