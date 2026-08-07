from pathlib import Path

from src.ingestion.fhir_file_reader import FhirFileReader
from src.storage.csv_writer import CSVWriter
from src.transformation.resource_extractor import ResourceExtractor
from src.transformation.encounter_transformer import EncounterTransformer

reader = FhirFileReader()

resources = reader.read_folder(
    Path("synthea", "synthea", "output", "fhir")
)

grouped = ResourceExtractor().group_by_type(resources)

encounters = grouped["Encounter"]

print(f"Encounter Resources: {len(encounters)}")

transformer = EncounterTransformer()

df = transformer.transform(encounters)

print()
print(df.head())

print()
print(df.shape)

CSVWriter.write(
    df,
    "encounter.csv",
)