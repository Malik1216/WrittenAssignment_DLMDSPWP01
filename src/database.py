import os
import pandas as pd
from sqlalchemy import create_engine, MetaData

os.makedirs("db", exist_ok=True)

DB_PATH = os.path.join("db", "data.db")

engine = create_engine(f"sqlite:///{DB_PATH}")
metadata = MetaData()

def save_dataframe(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Saved to table: {table_name}")

def save_all_to_db(train_df, ideal_df, test_df):
    save_dataframe(train_df, "training_data")
    save_dataframe(ideal_df, "ideal_functions")
    save_dataframe(test_df, "test_results")