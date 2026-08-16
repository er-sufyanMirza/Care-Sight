from src.config import PROCESSED_DATA
from src.storage.postgres_loader import PostgreSQLLoader
import pandas as pd

loader = PostgreSQLLoader()

file_path = PROCESSED_DATA / "encounter.csv"

df = pd.read_csv(file_path)

print(f"CSV rows: {len(df)}")
print()
print("CSV columns:")
print(df.columns.tolist())

loader.load_dataframe(
    df,
    "fact_encounter",
)

print()
print("Encounters loaded successfully.")