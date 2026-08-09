from __future__ import annotations
from pathlib import Path
from src.ingestion.fhir_file_reader import FhirFileReader
from src.storage.csv_writer import CSVWriter
from src.transformation.resource_extractor import ResourceExtractor
from src.transformation.condition_transformer import ConditionTransformer
import pandas as pd 

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

grouped = ResourceExtractor().group_by_type(resources)

conditions = grouped["Condition"]

print(f"condition resources {len(conditions)}")

transformer = ConditionTransformer()

df = transformer.transform(conditions)

print()
print("shape: ")
print(df.shape)

print()
print("columns: ")
print(df.columns.tolist())

print()
print("First 5 rows: ")
print(df.head())

print()
print("Missing values: ")
print(df.isna().sum())

print()
print("code system: ")
print(df["code_system"].value_counts(dropna=False))

CSVWriter.write(
    df,
    "condition.csv"
)