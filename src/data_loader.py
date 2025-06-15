import pandas as pd
import os

def load_training_data(file_path):
    df = pd.read_csv(file_path)
    return df

def load_ideal_functions(file_path):
    df = pd.read_csv(file_path)
    return df

def load_test_data(file_path):
    df = pd.read_csv(file_path)
    return df