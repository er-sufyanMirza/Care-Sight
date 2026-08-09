from pathlib import Path

from src.ingestion.fhir_file_reader import FhirFileReader
from src.storage.csv_writer import CSVWriter
from src.transformation.observation_transformer import (
    ObservationTransformer,
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

observations = grouped["Observation"]

print(
    f"Observation Resources: {len(observations)}"
)

transformer = ObservationTransformer()

df = transformer.transform(observations)

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

CSVWriter.write(
    df,
    "observation.csv",
)