import unittest
import pandas as pd
from src.matcher import TrainingMatcher

class TestTrainingMatcher(unittest.TestCase):
    def test_training_matches_count(self):
        train_df = pd.read_csv("data/training_data.csv")
        ideal_df = pd.read_csv("data/ideal_functions.csv")
        matcher = TrainingMatcher(train_df, ideal_df)
        matches = matcher.find_best_ideal_matches()
        self.assertEqual(len(matches), 4)

if __name__ == "__main__":
    unittest.main()