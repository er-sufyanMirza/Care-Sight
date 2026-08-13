from pathlib import Path
from pprint import pprint
from src.transformation.resource_extractor import ResourceExtractor
from src.ingestion.fhir_file_reader import FhirFileReader

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

grouped = ResourceExtractor().group_by_type(resources)

medications = grouped["MedicationRequest"]

print(f"MedicationRequest count: {len(medications)}")

print()

print("First MedicationRequest type:")
print(type(medications))

print()
print("First MedicationRequest resourcceType:")
print(medications[0].get("resourceType"))

print()
print("First MedicationRequest keys:")
print(medications[0].keys())

print()
print("First MedicationRequest:")
print(medications[0])

