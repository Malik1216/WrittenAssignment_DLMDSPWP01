import numpy as np
import pandas as pd

class Matcher:
    def __init__(self, train_df, ideal_df):
        self.train_df = train_df
        self.ideal_df = ideal_df
        self.matches = {}

    def find_best_ideal_matches(self):
        train_columns = [col for col in self.train_df.columns if col != 'x']
        ideal_columns = [col for col in self.ideal_df.columns if col != 'x']
        for train_col in train_columns:
            min_error = float('inf')
            best_match = None
            for ideal_col in ideal_columns:
                error = np.sum((self.train_df[train_col] - self.ideal_df[ideal_col]) ** 2)
                if error < min_error:
                    min_error = error
                    best_match = ideal_col
            self.matches[train_col] = best_match
        return self.matches

    def map_test_data(self, test_df):
        result_rows = []
        test_columns = [col for col in test_df.columns if col != 'x']
        for test_col in test_columns:
            for _, row in test_df.iterrows():
                x_val = row['x']
                y_val = row[test_col]
                mapped = False
                for train_y, ideal_y in self.matches.items():
                    ideal_row = self.ideal_df[self.ideal_df['x'] == x_val]
                    if ideal_row.empty:
                        continue
                    ideal_val = ideal_row[ideal_y].values[0]
                    max_dev = np.max(np.abs(self.train_df[train_y] - self.ideal_df[ideal_y]))
                    allowed_dev = max_dev * np.sqrt(2)
                    delta = abs(y_val - ideal_val)
                    if delta <= allowed_dev:
                        result_rows.append([x_val, y_val, delta, ideal_y, test_col])
                        mapped = True
                        break
                if not mapped:
                    result_rows.append([x_val, y_val, None, None, test_col])
        return pd.DataFrame(result_rows, columns=["x", "y", "delta_y", "ideal_function", "test_column"])

class TrainingMatcher(Matcher):
    def __init__(self, train_df, ideal_df):
        super().__init__(train_df, ideal_df)

    def get_training_match_summary(self):
        return f"Matched {len(self.matches)} training functions to ideal functions."