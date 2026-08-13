from pathlib import Path
from src.ingestion.fhir_file_reader import FhirFileReader
from src.transformation.resource_extractor import ResourceExtractor
from src.transformation.medication_transformer import MedicationTransformer
from src.storage.csv_writer import CSVWriter

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

grouped = ResourceExtractor().group_by_type(resources)

medications = grouped["MedicationRequest"]

print(f"Medication RequestResources: {len(medications)}")

transformer = MedicationTransformer()

df = transformer.transform(medications)

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
    "medication_request.csv",
)