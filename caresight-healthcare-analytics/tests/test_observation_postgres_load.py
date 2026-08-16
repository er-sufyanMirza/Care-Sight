import pandas as pd

from src.config import PROCESSED_DATA
from src.storage.postgres_loader import PostgreSQLLoader


loader = PostgreSQLLoader()

file_path = PROCESSED_DATA / "observation.csv"

df = pd.read_csv(file_path)

print("Original rows:", len(df))

print()
print("Original columns:")
print(df.columns.tolist())

print()
print("Original value types:")
print(df["value"].map(type).value_counts())

print()
print("Sample values:")
print(df["value"].head(20).to_list())


# Use a copy for inspection
test_df = df.copy()

numeric_values = pd.to_numeric(
    test_df["value"],
    errors="coerce",
)

text_values = test_df["value"].where(
    numeric_values.isna()
)

test_df = test_df.assign(
    value=numeric_values,
    value_text=text_values,
)

print()
print("After conversion:")

print(
    test_df[
        [
            "observation_name",
            "value",
            "value_text",
            "unit",
        ]
    ].head(20).to_string(index=False)
)

print()
print(
    "Numeric values:",
    test_df["value"].notna().sum()
)

print(
    "Text values:",
    test_df["value_text"].notna().sum()
)

print()
print("Loading observations...")

loader.load_dataframe(
    df,
    "fact_observation",
)

print()
print("Observations loaded successfully.")