from matcher import TrainingMatcher
from data_loader import load_training_data, load_ideal_functions, load_test_data
from visualizer import plot_training_vs_ideal, plot_test_data_mapping
from database import save_all_to_db

class FunctionMatcherApp:
    def __init__(self, train_path, ideal_path, test_path):
        self.train_df = load_training_data(train_path)
        self.ideal_df = load_ideal_functions(ideal_path)
        self.test_df = load_test_data(test_path)
        self.matcher = TrainingMatcher(self.train_df, self.ideal_df)
        self.matches = None
        self.mapped_df = None

    def process_matching(self):
        self.matches = self.matcher.find_best_ideal_matches()

    def process_mapping(self):
        self.mapped_df = self.matcher.map_test_data(self.test_df)

    def visualize(self):
        plot_training_vs_ideal(self.train_df, self.ideal_df, self.matches)
        plot_test_data_mapping(self.mapped_df)

    def save_to_database(self):
        save_all_to_db(self.train_df, self.ideal_df, self.mapped_df)

    def run(self):
        self.process_matching()
        self.process_mapping()
        self.visualize()
        self.save_to_database()

if __name__ == "__main__":
    app = FunctionMatcherApp(
        "data/training_data.csv",
        "data/ideal_functions.csv",
        "data/test_data.csv"
    )
    app.run()