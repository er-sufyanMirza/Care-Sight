import pandas as pd

from src.config import PROCESSED_DATA
from src.storage.postgres_loader import PostgreSQLLoader


loader = PostgreSQLLoader()

file_path = PROCESSED_DATA / "condition.csv"

df = pd.read_csv(file_path)

print("CSV rows:", len(df))

print()
print("CSV columns:")
print(df.columns.tolist())

print()
print("First 5 rows:")
print(df.head().to_string(index=False))

loader.load_dataframe(
    df,
    "fact_condition",
)

print()
print("Conditions loaded successfully.")