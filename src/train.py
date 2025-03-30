import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path

# Sample training data (replace with your actual data loading)
data = pd.DataFrame({
    "text": ["Win money now", "Meeting tomorrow", "Claim your prize"],
    "label": [1, 0, 1]  # 1=SPAM, 0=NOT SPAM
})

# Train vectorizer and model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["text"])
y = data["label"]
model = LogisticRegression()
model.fit(X, y)

# Save artifacts
Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/model.joblib")
joblib.dump(vectorizer, "models/vectorizer.joblib")