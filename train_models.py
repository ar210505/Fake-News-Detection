"""
Quick model training script to regenerate pickle files.
Uses sample data from fake.csv and true.csv
"""

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

print("Loading datasets...")
fake_df = pd.read_csv('fake.csv')
true_df = pd.read_csv('true.csv')

# Prepare data
fake_df['label'] = 0  # Fake = 0
true_df['label'] = 1  # Real = 1

df = pd.concat([fake_df, true_df], ignore_index=True)
df['text'] = df['text'].fillna('') + ' ' + df['title'].fillna('')

print(f"Total samples: {len(df)}")
print(f"Fake samples: {(df['label'] == 0).sum()}")
print(f"Real samples: {(df['label'] == 1).sum()}")

# Vectorize
print("\nVectorizing text...")
vectorizer = TfidfVectorizer(max_features=15000, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['text'])
y = df['label']

print(f"Vector shape: {X.shape}")

# Train model
print("\nTraining Logistic Regression...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X, y)

# Save models
print("\nSaving models...")
joblib.dump(model, 'fake_news_master_model.pkl')
joblib.dump(vectorizer, 'tfidf_master_vectorizer.pkl')

print("✓ Models saved successfully!")
print(f"  - Model: {os.path.getsize('fake_news_master_model.pkl')} bytes")
print(f"  - Vectorizer: {os.path.getsize('tfidf_master_vectorizer.pkl')} bytes")

# Test
print("\nTesting model...")
test_text = "Breaking news: Scientists discover new cure"
test_vec = vectorizer.transform([test_text])
pred = model.predict(test_vec)[0]
proba = model.predict_proba(test_vec)[0]
print(f"  Test: '{test_text}'")
print(f"  Prediction: {'REAL' if pred == 1 else 'FAKE'}")
print(f"  Confidence: {max(proba)*100:.1f}%")
