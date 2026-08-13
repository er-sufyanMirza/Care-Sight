from pathlib import Path

from src.ingestion.fhir_file_reader import FhirFileReader
from src.storage.csv_writer import CSVWriter
from src.transformation.procedure_transformer import (
    ProcedureTransformer,
)
from src.transformation.resource_extractor import (
    ResourceExtractor,
)


reader = FhirFileReader()

resources = reader.read_folder(
    Path(
        "synthea",
        "synthea",
        "output",
        "fhir",
    )
)

grouped = ResourceExtractor().group_by_type(
    resources
)

procedures = grouped["Procedure"]

print(
    f"Procedure Resources: {len(procedures)}"
)

transformer = ProcedureTransformer()

df = transformer.transform(procedures)

print()
print("Shape:")
print(df.shape)

print()
print("Columns:")
print(df.columns.tolist())

print()
print("First 5 rows:")
print(df.head())

print()
print("Missing values:")
print(df.isna().sum())

print()
print("Code systems:")
print(
    df["code_system"].value_counts(
        dropna=False
    )
)

CSVWriter.write(
    df,
    "procedure.csv",
)