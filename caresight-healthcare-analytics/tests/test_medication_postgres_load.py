import pandas as pd 
from src.storage.postgres_loader import PostgreSQLLoader
from src.config import PROCESSED_DATA

loader = PostgreSQLLoader()

file_path = PROCESSED_DATA / "medication_request.csv"

df = pd.read_csv(file_path)

print("CSV rows:", len(df))

print()
print("CSV columns:")
print(df.columns.to_list())

print()
print("First 5 rows:")
print(df.head().to_string(index= False))

loader.load_dataframe(
    df,
    "fact_medication"
)

print()
print("Medication loaded Successfully")