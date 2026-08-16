import pandas as pd
from src.config import PROCESSED_DATA
from src.storage.postgres_loader import PostgreSQLLoader

loader = PostgreSQLLoader()

file_path = PROCESSED_DATA  / "patient.csv"

df = pd.read_csv(file_path)

print("CSV rows:", len(df))

loader.load_dataframe(
    df,
    "dim_patient"
)

print("Patients loaded successfully")