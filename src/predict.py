import re
import joblib
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

class SpamClassifier:
    def __init__(self):
        try:
            # Load model and vectorizer from the correct path
            model_path = Path(__file__).parent.parent / "models" / "model.joblib"
            vectorizer_path = Path(__file__).parent.parent / "models" / "vectorizer.joblib"
            
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
        except Exception as e:
            raise RuntimeError(f"Model loading failed: {str(e)}")

    def preprocess(self, text):
        # Remove timestamps and clean text
        text = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+', '', text)
        return text.strip()

    def predict(self, text):
        cleaned_text = self.preprocess(text)
        features = self.vectorizer.transform([cleaned_text])
        return self.model.predict(features)[0]
        
