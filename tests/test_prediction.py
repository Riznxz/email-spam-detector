import unittest
from src.predict import SpamClassifier
from src.config import PATHS
import os

class TestSpamClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not all(os.path.exists(p) for p in [PATHS['model'], PATHS['vectorizer']]):
            raise FileNotFoundError("Train model first!")
        cls.classifier = SpamClassifier()

    def test_spam(self):
        samples = [
            ("WIN FREE PRIZE", 'spam'),
            ("Claim your reward", 'spam')
        ]
        for text, expected in samples:
            with self.subTest(text=text):
                res = self.classifier.predict(text)
                self.assertEqual(res['prediction'], expected)
                self.assertGreater(res['confidence'], 0.8)

    def test_edge_cases(self):
        res = self.classifier.predict("")
        self.assertIsNotNone(res['error'])

if __name__ == "__main__":
    unittest.main()