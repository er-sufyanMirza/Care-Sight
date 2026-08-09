from pathlib import Path
from pprint import pprint
from src.ingestion.fhir_file_reader import FhirFileReader
from src.transformation.resource_extractor import ResourceExtractor

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

grouped = ResourceExtractor().group_by_type(resources)

#ptrkp

procedures = grouped["Procedure"]

print(f"Procedure count: {len(procedures)}")

print()

print("First procedure type")
print(type(procedures[0]))

print()

print("First procedure resourceType")
print(procedures[0].get("resourceType"))

print()

print("First procedure keys: ")
print(procedures[0].keys())

print()

print("First procedure: ")
print(procedures[0])